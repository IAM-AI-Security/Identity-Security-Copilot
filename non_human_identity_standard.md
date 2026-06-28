# Non-Human Identity (NHI) Standard

## Section 1 -- Scope
This standard defines the governance, lifecycle, and security requirements for all non-human identities, including service accounts, API keys, OAuth tokens, Kubernetes service accounts, and AI agent execution roles.

## Section 2 -- NHI Ownership and Lifecycle
- **Ownership:** Every NHI must have an assigned, active human owner (FTE) responsible for its lifecycle.
- **Orphaned NHIs:** If an owner departs, the NHI must be reassigned to their manager within 7 days; otherwise, the NHI will be automatically disabled.
- **Expiration:** All API keys, tokens, and service account credentials must have a defined expiration date not exceeding 90 days.
- **Rotation:** Credentials must be rotated automatically before expiration. Manual rotation is prohibited for production systems.

## Section 3 -- Authentication and Secrets Management
- **Vaulting:** Hardcoded secrets in source code, configuration files, or environment variables are strictly prohibited.
- **Dynamic Secrets:** Applications and CI/CD pipelines must retrieve secrets dynamically at runtime using CyberArk Conjur or AWS Secrets Manager.
- **Workload Identity:** Where supported (e.g., AWS IAM Roles for Service Accounts, Azure Managed Identities, Kubernetes workload identities), credential-less authentication must be used instead of static keys.

## Section 4 -- Privilege Assignment
- **Least Privilege:** NHIs must be granted only the specific permissions required to execute their function. Wildcard permissions (e.g., `s3:*`) are prohibited.
- **Scope Restriction:** Access must be restricted by resource, IP address, and time of day where feasible.
- **Drift Detection:** NHI permissions must be continuously monitored against actual usage. Unused permissions must be automatically revoked after 30 days of inactivity.

## Section 5 -- AI Agent Specific Requirements
- **Execution Roles:** AI agents must operate under dedicated, scoped execution roles.
- **Token Authentication:** Agents must authenticate using short-lived JWTs via CyberArk Conjur; static credentials are not permitted.
- **Boundary Controls:** Agent roles must include boundary policies (e.g., AWS Service Control Policies) to prevent privilege escalation.
