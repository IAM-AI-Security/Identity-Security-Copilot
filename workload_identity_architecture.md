# Workload Identity Reference Architecture

## 1. Overview
Workload Identity provides a secure, secretless method for applications, scripts, and cloud resources to authenticate to other services. This architecture eliminates the need to manage and rotate static credentials.

## 2. Core Mechanisms

### A. Cloud-Native Workload Identity
- **AWS IAM Roles:** EC2 instances, Lambda functions, and ECS tasks assume IAM roles via the AWS instance metadata service. No permanent access keys are stored on the compute resource.
- **Azure Managed Identities:** Azure resources (VMs, App Services) are assigned system-assigned or user-assigned managed identities, which Azure AD automatically authenticates.

### B. Kubernetes Workload Identity
- **OIDC Federation:** Kubernetes service accounts are linked to cloud IAM roles (e.g., AWS IAM Roles for Service Accounts - IRSA). The pod exchanges its Kubernetes service account token for temporary cloud credentials via an OIDC provider.

### C. SPIFFE/SPIRE (Cross-Platform)
- For hybrid or multi-cloud workloads, SPIFFE (Secure Production Identity Framework for Everyone) provides a standard for issuing cryptographic identities (SVIDs) to workloads based on node attestation, enabling mutual TLS (mTLS) authentication between services without shared secrets.

## 3. Security Benefits
- **Zero Static Secrets:** Eliminates the risk of hardcoded credentials in source code or configuration files.
- **Short-Lived Credentials:** Workloads receive temporary, automatically rotating tokens.
- **Strong Identity:** Authentication is cryptographically tied to the compute resource itself.

## 4. Governance Application
When asked how to secure application-to-application communication or database access, the RAG Assistant MUST recommend Workload Identity (Managed Identities, IAM Roles, or SPIFFE) over static service accounts and passwords.
