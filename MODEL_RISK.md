# Model Risk Management

## 1. Overview
This document outlines the governance and risk management framework for the Identity Governance RAG Assistant, aligning with the principles of the Federal Reserve's SR 26-02 (formerly SR 11-7) guidance on Model Risk Management.

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
