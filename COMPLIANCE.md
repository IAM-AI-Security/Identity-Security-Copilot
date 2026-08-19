# Compliance Mapping

## 1. Overview
The Identity Governance RAG Assistant is designed to map to and cite major cybersecurity and compliance frameworks.

## 2. Framework Mapping

### NIST 800-53 Rev. 5
- **AC-2 (Account Management):** Maps to the Identity Governance Standard and JML lifecycle rules.
- **AC-6 (Least Privilege):** Maps to the Privileged Access Standard and Numeric Thresholds (JIT, JEA).

### NIST 800-207 (Zero Trust Architecture)
- The architecture reference documents (Zero Trust Identity, PAM, Workload Identity) explicitly define the PDP and PEP components required to enforce continuous verification.

### NIST AI RMF
- **Govern:** The system is governed by the MODEL_RISK.md guidelines.
- **Map/Measure/Manage:** LLM-specific risks including prompt injection, data poisoning, and over-reliance are addressed through retrieval grounding, mandatory source citation, a fallback response when no relevant policy is retrieved, and the human decision gate described in MODEL_RISK.md.

### Sarbanes-Oxley (SOX)
- SOX ITGC access reviews require population completeness, documented review execution, and evidence of revocation fulfillment. The assistant returns these requirements with citations when asked what a SOX access review needs.

### Payment Card Industry Data Security Standard (PCI DSS) v4.0
- PCI DSS Requirement 7 (Restrict Access by Business Need to Know) and its mandatory six-month access review frequency are covered in the knowledge base and returned with citations.

### OWASP Top 10 for LLM Applications 2025
- The system architecture addresses LLM01 (Prompt Injection), LLM03 (Data Poisoning), and LLM09 (Model Misuse/Over-Reliance) through strict RAG grounding, read-only LLM access, and RBAC on the knowledge base.

### MITRE ATLAS
- Access to the underlying vector database and AWS Bedrock APIs is subject to the Cloud Access Standard, addressing ATLAS credential access and execution threats.
