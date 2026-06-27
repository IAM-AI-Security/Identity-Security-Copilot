"""
Ingestion Pipeline for the Identity Governance RAG Assistant.
Reads all .md files from the project root, chunks them, embeds via
AWS Bedrock Titan, and builds a FAISS index for retrieval.

Usage:
    python3 ingest.py
"""

import os
import json
import glob
import pickle
from typing import List, Dict

import boto3
import numpy as np
import faiss

KNOWLEDGE_BASE_DIR = os.path.dirname(__file__)
EMBEDDINGS_DIR = os.path.join(os.path.dirname(__file__), "embeddings")
INDEX_PATH = os.path.join(EMBEDDINGS_DIR, "faiss.index")
METADATA_PATH = os.path.join(EMBEDDINGS_DIR, "metadata.pkl")

EMBED_MODEL_ID = os.environ.get("BEDROCK_EMBED_MODEL", "amazon.titan-embed-text-v2:0")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

SKIP_FILES = {"README.md", "SCREENSHOTS.md", "SOURCE_INDEX.md"}

def get_bedrock_client():
    return boto3.client("bedrock-runtime", region_name=AWS_REGION)

def embed_text(client, text: str) -> List[float]:
    body = json.dumps({"inputText": text})
    response = client.invoke_model(
        modelId=EMBED_MODEL_ID,
        body=body,
        accept="application/json",
        contentType="application/json",
    )
    result = json.loads(response["body"].read())
    return result["embedding"]

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: List[str] = []
    current = ""
    for para in paragraphs:
        if len(current) + len(para) + 2 <= chunk_size:
            current += (para + "\n\n")
        else:
            if current:
                chunks.append(current.strip())
            if len(para) > chunk_size:
                start = 0
                while start < len(para):
                    chunks.append(para[start:start + chunk_size].strip())
                    start += chunk_size - overlap
                current = ""
            else:
                current = para + "\n\n"
    if current:
        chunks.append(current.strip())
    return chunks

def load_documents() -> List[Dict]:
    docs: List[Dict] = []
    pattern = os.path.join(KNOWLEDGE_BASE_DIR, "*.md")
    for path in glob.glob(pattern):
        filename = os.path.basename(path)
        if filename in SKIP_FILES:
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            continue
        docs.append({"source": filename, "content": content})
    return docs

def main():
    os.makedirs(EMBEDDINGS_DIR, exist_ok=True)
    client = get_bedrock_client()

    documents = load_documents()
    print(f"Loaded {len(documents)} documents from knowledge base.")

    all_vectors: List[List[float]] = []
    metadata: List[Dict] = []

    for doc in documents:
        chunks = chunk_text(doc["content"])
        for i, chunk in enumerate(chunks):
            try:
                vector = embed_text(client, chunk)
            except Exception as e:
                print(f"  ! Failed to embed chunk {i} of {doc['source']}: {e}")
                continue
            all_vectors.append(vector)
            metadata.append({
                "source": doc["source"],
                "chunk_index": i,
                "text": chunk,
            })
        print(f"  - {doc['source']}: {len(chunks)} chunks")

    if not all_vectors:
        print("No vectors generated. Check Bedrock access and credentials.")
        return

    matrix = np.array(all_vectors, dtype="float32")
    dimension = matrix.shape[1]
    faiss.normalize_L2(matrix)
    index = faiss.IndexFlatIP(dimension)
    index.add(matrix)

    faiss.write_index(index, INDEX_PATH)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print(f"\nIngestion complete. {len(all_vectors)} chunks indexed.")
    print(f"Index: {INDEX_PATH}")
    print(f"Metadata: {METADATA_PATH}")

if __name__ == "__main__":
    main()
