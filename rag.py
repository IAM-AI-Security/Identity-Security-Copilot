"""
RAG core for the Identity Governance RAG Assistant.
Handles semantic retrieval against the FAISS index and answer generation
via AWS Bedrock, with strict grounding and mandatory citations.
"""

import os
import json
import pickle
from typing import List, Dict, Tuple

import boto3
import numpy as np
import faiss

EMBEDDINGS_DIR = os.path.join(os.path.dirname(__file__), "embeddings")
INDEX_PATH = os.path.join(EMBEDDINGS_DIR, "faiss.index")
METADATA_PATH = os.path.join(EMBEDDINGS_DIR, "metadata.pkl")

EMBED_MODEL_ID = os.environ.get("BEDROCK_EMBED_MODEL", "amazon.titan-embed-text-v2:0")
LLM_MODEL_ID = os.environ.get("BEDROCK_LLM_MODEL", "anthropic.claude-haiku-4-5-20251001-v1:0")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

SIMILARITY_THRESHOLD = float(os.environ.get("RAG_SIMILARITY_THRESHOLD", "0.35"))
TOP_K = int(os.environ.get("RAG_TOP_K", "7"))

SYSTEM_PROMPT = """You are an Identity Governance Assistant for an enterprise security team.

You help identity architects, IAM engineers, and compliance teams make faster, more consistent, and more defensible governance decisions. You retrieve answers from an approved knowledge base of enterprise identity standards, NIST controls, CyberArk documentation, and audit templates.

STRICT RULES:
1. Answer ONLY using the provided CONTEXT from approved governance documents. Never use outside knowledge.
2. Never make access decisions. You inform; the human decides.
3. Never invent thresholds, control numbers, timeframes, or policy language. If the exact value is not in the CONTEXT, say so.
4. If the CONTEXT does not contain sufficient information, respond exactly:
   "I cannot find a specific policy addressing this question in the current knowledge base. Please consult the Identity Security team."

RESPONSE FORMAT - always use this four-part structure:

**Recommendation**
State the direct answer or required action clearly and concisely.

**Why**
Explain the security and governance rationale. What risk does this control address? What happens without it?

**Supporting Standards**
Cite the specific document and section from the CONTEXT that grounds this answer. Use this format: [document_name.md Section]. List every relevant citation.

**Business Impact**
Explain how following this recommendation reduces risk, satisfies compliance requirements, or simplifies audit evidence production.

---

If the question asks for a checklist or list of controls, produce a structured list and still cite sources for every item.

If the question is a simple factual lookup, answer directly with the value and its citation - no need for the full four-part format.
"""


class RAGEngine:
    def __init__(self):
        self.client = boto3.client("bedrock-runtime", region_name=AWS_REGION)
        self.index = faiss.read_index(INDEX_PATH)
        with open(METADATA_PATH, "rb") as f:
            self.metadata: List[Dict] = pickle.load(f)

    def embed_query(self, query: str) -> np.ndarray:
        body = json.dumps({"inputText": query})
        response = self.client.invoke_model(
            modelId=EMBED_MODEL_ID,
            body=body,
            accept="application/json",
            contentType="application/json",
        )
        result = json.loads(response["body"].read())
        vec = np.array([result["embedding"]], dtype="float32")
        faiss.normalize_L2(vec)
        return vec

    def retrieve(self, query: str) -> List[Tuple[Dict, float]]:
        vec = self.embed_query(query)
        scores, idxs = self.index.search(vec, TOP_K)
        results: List[Tuple[Dict, float]] = []
        for score, idx in zip(scores[0], idxs[0]):
            if idx == -1:
                continue
            if score >= SIMILARITY_THRESHOLD:
                results.append((self.metadata[idx], float(score)))
        return results

    def build_context(self, results: List[Tuple[Dict, float]]) -> str:
        blocks = []
        for meta, score in results:
            blocks.append(f"[SOURCE: {meta['source']}]\n{meta['text']}")
        return "\n\n---\n\n".join(blocks)

    def generate(self, query: str) -> Dict:
        results = self.retrieve(query)

        if not results:
            return {
                "answer": (
                    "I cannot find a specific policy addressing this question in the "
                    "current knowledge base. Please consult the Identity Security team."
                ),
                "sources": [],
            }

        context = self.build_context(results)
        user_message = f"CONTEXT:\n{context}\n\nQUESTION: {query}"

        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2048,
            "system": SYSTEM_PROMPT,
            "messages": [
                {"role": "user", "content": user_message}
            ],
        })

        response = self.client.invoke_model(
            modelId=LLM_MODEL_ID,
            body=body,
            accept="application/json",
            contentType="application/json",
        )
        result = json.loads(response["body"].read())
        answer = result["content"][0]["text"]

        sources = sorted({meta["source"] for meta, _ in results})
        return {"answer": answer, "sources": sources}
