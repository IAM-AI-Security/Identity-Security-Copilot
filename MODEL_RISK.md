# Model Risk Management

## 1. Overview
This document applies model risk management principles to the Identity Governance RAG Assistant.

Scope note. Federal Reserve SR 26-02, which superseded SR 11-7 effective April 17, 2026, places generative and agentic AI models outside its scope at footnote 3, while directing that an organization's own risk management practices should determine appropriate governance for systems the guidance does not cover. This system is generative, so SR 26-02 does not apply to it by its own terms. The controls below apply the guidance's principles to a system it explicitly excludes, alongside NIST AI RMF, because the absence of prescriptive guidance is not an absence of model risk.

## 2. Core Principles

### A. Human-in-the-Loop (Human Approval)
The LLM is strictly an advisory tool. It does not possess the capability or authorization to execute access grants, revocations, or workflow approvals. A human reviewer MUST make the final determination based on the cited evidence.

### B. Confidence Thresholds and Fallback
- The retrieval system utilizes semantic search thresholds. If the vector search cannot find relevant context above the defined similarity threshold, the LLM is instructed to trigger a fallback response.
- **Fallback Response:** "I cannot find a specific policy addressing this question in the current knowledge base. Please consult the Identity Security team."

### C. Audit Logging
Every interaction with the RAG Assistant is logged for audit and model-tuning purposes. Logs include:
- The user's original query.
- The specific document chunks retrieved by the vector database.
- The generated response.
- User feedback (thumbs up/down) on the accuracy of the response.

### D. Versioning and Document Freshness
- **Knowledge Base Versioning:** All policy documents are version-controlled in Git.
- **Vector Sync:** The vector database is automatically synchronized with the `main` branch. The system tracks the commit hash of the ingested documents to ensure the LLM is referencing the current state.

## 3. Ongoing Governance
The performance of the RAG Assistant is reviewed quarterly by the Identity Security team to identify hallucination trends, missing policies, or required prompt tuning.
