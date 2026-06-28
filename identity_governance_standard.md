# Enterprise Identity Governance Standard

## Section 1 -- Scope
This standard applies to all enterprise identities (employees, contractors, vendors, partners) requiring access to corporate systems, applications, and infrastructure.

## Section 2 -- Joiner, Mover, Leaver (JML) Lifecycle
### 2.1 Joiner (Onboarding)
- **Birthright Access:** Basic access (email, intranet, standard productivity tools) is provisioned automatically based on the authoritative HR source system (e.g., Workday) via Okta or Entra ID lifecycle workflows.
- **Requestable Access:** Access beyond birthright must be requested through the central identity governance platform (IGA) and requires business justification.

### 2.2 Mover (Role Change)
- **Access Revocation:** Access granted for a previous role must be revoked within 24 hours of the effective role change date unless a temporary extension is approved by both the old and new managers.
- **Access Provisioning:** New access is provisioned according to the joiner process for the new role.

### 2.3 Leaver (Offboarding)
- **Immediate Revocation:** All access must be disabled immediately upon termination (involuntary) or at the end of the last working day (voluntary).
- **Data Retention:** User data (email, OneDrive) is retained for 30 days post-termination before deletion, subject to legal hold holds.

## Section 3 -- Access Request and Approval
- **Least Privilege:** Access requests must be scoped to the minimum permissions necessary to perform job duties.
- **Approval Chain:** 
  - Standard access requires manager approval.
  - Sensitive or privileged access requires manager approval plus resource owner or security team approval.
- **Justification:** All access requests must include a clear, documented business justification.

## Section 4 -- Contractor and Vendor Access
- **Sponsorship:** All contractor and vendor identities must be sponsored by a full-time employee (FTE).
- **Time-Bound Access:** Access must be provisioned with a hard expiration date not exceeding the contract end date or 6 months, whichever is shorter.
- **Renewals:** Access extensions require explicit sponsor re-approval prior to expiration.

## Section 5 -- Authentication Requirements
- **MFA:** Multi-Factor Authentication (MFA) is required for all access to corporate resources from any location.
- **SSO:** Applications must integrate with the enterprise Single Sign-On (SSO) provider (Okta/Entra ID) using SAML or OIDC where technically feasible.

## Section 6 -- Emergency Access (Break-Glass)
- **Scope:** Break-glass accounts are reserved for critical system recovery when standard authentication mechanisms fail.
- **Controls:** Break-glass accounts must be heavily monitored, require dual approval for checkout, and trigger immediate alerts to the Security Operations Center (SOC) upon use.
