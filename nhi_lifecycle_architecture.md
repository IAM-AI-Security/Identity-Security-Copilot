# Non-Human Identity (NHI) Lifecycle Architecture

## 1. Overview
This document defines the architectural flow for managing the lifecycle of Non-Human Identities (NHIs)—such as service accounts, API keys, and workload identities—from creation to decommissioning.

## 2. Lifecycle Phases

### A. Discovery and Onboarding
- **Continuous Discovery:** Tools (e.g., cloud posture management, IAM analyzers) continuously scan AWS/Azure environments for newly created NHIs.
- **Ownership Assignment:** Every discovered NHI MUST be mapped to a human owner or a specific application team in the identity registry. Unowned NHIs are flagged for quarantine.

### B. Authentication and Secrets Management
- **Secretless First:** Workloads MUST use native cloud identity (e.g., AWS IAM Roles for EC2, Azure Managed Identities) or certificate-based authentication (SPIFFE/mTLS) wherever possible.
- **Vaulting:** If static secrets (API keys, passwords) are unavoidable, they MUST be generated and stored in an approved secrets manager (e.g., CyberArk Conjur, AWS Secrets Manager) and injected at runtime.

### C. Governance and Monitoring
- **Least Privilege:** NHI permissions MUST be scoped tightly to the required API actions.
- **Anomaly Detection:** SIEM/UEBA tools monitor NHI behavior. Deviations from baseline (e.g., an API key used from a new IP address or calling a new service) trigger high-priority alerts.

### D. Rotation and Deprovisioning
- **Automated Rotation:** Secrets MUST be rotated automatically by the secrets manager without human intervention.
- **Deprovisioning:** When the owning application is decommissioned, the CI/CD pipeline MUST trigger the revocation and deletion of the associated NHIs.

## 3. Governance Application
The RAG Assistant MUST prioritize secretless authentication and strict human ownership when advising on non-human identity management.
