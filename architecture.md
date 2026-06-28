# System Architecture

## 1. Overview
The Identity Governance RAG Assistant is built on a serverless AWS architecture, utilizing AWS Bedrock for LLM inference and a vector database for semantic retrieval.

## 2. Component Architecture

### A. Frontend (Streamlit)
- A Python-based Streamlit application provides the chat interface for identity engineers.
- It captures user queries and displays the LLM's response alongside the retrieved source citations.

### B. Inference (AWS Bedrock)
- **Model:** Amazon Titan or Anthropic Claude (via Bedrock).
- **Function:** Receives the user prompt augmented with the retrieved context chunks. It synthesizes the final answer strictly based on the provided context.

### C. Retrieval (Vector Database)
- **Database:** FAISS (local for development) or Amazon OpenSearch Serverless (production).
- **Function:** Stores the embedded chunks of the knowledge base Markdown files. Performs semantic similarity search against the user's query.

### D. Ingestion Pipeline
- A Python script (`ingest.py`) reads the `knowledge_base/` directory.
- It splits the Markdown files into semantic chunks.
- It generates embeddings using Amazon Titan Embeddings via Bedrock.
- It loads the embeddings and metadata (source filename) into the vector database.

## 3. Deployment (Terraform)
The infrastructure is defined as code using Terraform, provisioning:
- IAM Roles for the Streamlit app to access Bedrock.
- S3 buckets for document storage (optional, if moving away from local files).
- Bedrock model invocation permissions.
