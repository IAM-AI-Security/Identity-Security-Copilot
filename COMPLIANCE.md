# Compliance Mapping

## 1. Overview
The Identity Governance RAG Assistant is designed to enforce and map to major cybersecurity and compliance frameworks.

## 2. Framework Mapping

### NIST 800-53 Rev. 5
- **AC-2 (Account Management):** Enforced via the Identity Governance Standard and JML lifecycle rules.
- **AC-6 (Least Privilege):** Enforced via the Privileged Access Standard and Numeric Thresholds (JIT, JEA).

### NIST 800-207 (Zero Trust Architecture)
- The architecture reference documents (Zero Trust Identity, PAM, Workload Identity) explicitly define the PDP and PEP components required to enforce continuous verification.

### NIST AI RMF
- **Govern:** The system is governed by the MODEL_RISK.md guidelines.
- **Map/Measure/Manage:** The THREAT_MODEL.md identifies and mitigates LLM-specific risks (prompt injection, hallucinations).

### Sarbanes-Oxley (SOX)
- The `sox_evidence_template.md` defines the strict requirements for population completeness, review execution, and revocation fulfillment necessary for ITGC compliance.

### Payment Card Industry Data Security Standard (PCI DSS) v4.0
- The `pci_access_review_template.md` enforces Requirement 7 (Restrict Access by Business Need to Know) and the mandatory six-month review frequency.

### OWASP Top 10 for LLM Applications 2025
- The system architecture mitigates LLM01 (Prompt Injection), LLM03 (Data Poisoning), and LLM09 (Model Misuse/Over-Reliance) through strict RAG grounding, read-only LLM access, and RBAC on the knowledge base.

### MITRE ATLAS
- Access to the underlying vector database and AWS Bedrock APIs is governed by the Cloud Access Standard, mitigating ATLAS credential access and execution threats.
