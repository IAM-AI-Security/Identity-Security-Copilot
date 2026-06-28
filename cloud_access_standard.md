# Cloud Access Standard

## 1. Purpose
This standard defines the requirements for managing and securing identity and access within cloud environments (AWS, Azure, GCP). It establishes rules for privileged roles, permission sets, conditional access, and multi-factor authentication (MFA).

## 2. Scope
Applies to all human and non-human identities accessing cloud service provider (CSP) consoles, APIs, and CLI tools.

## 3. General Requirements
- **Centralized Identity:** Cloud access MUST be federated through the enterprise Identity Provider (IdP) using SAML 2.0 or OIDC. Local IAM users are prohibited except for emergency break-glass accounts.
- **MFA:** Multi-Factor Authentication is REQUIRED for all human access to cloud environments, enforced at the IdP level.
- **Least Privilege:** Access MUST be granted based on the principle of least privilege, utilizing role-based access control (RBAC) or attribute-based access control (ABAC).

## 4. AWS IAM Identity Center Requirements
- **Permission Sets:** MUST be mapped to specific job functions. Broad administrative permission sets (e.g., `AdministratorAccess`) MUST NOT be permanently assigned to standard users.
- **Service Control Policies (SCPs):** MUST be used at the AWS Organization level to establish guardrails (e.g., restricting regions, preventing CloudTrail disablement) regardless of individual IAM permissions.
- **Access Analyzer:** MUST be enabled to continuously monitor for unintended external or cross-account access.

## 5. Microsoft Entra ID (Azure) Requirements
- **Privileged Identity Management (PIM):** All Azure AD roles with administrative capabilities (e.g., Global Administrator, Privileged Role Administrator) MUST be managed via PIM.
- **Conditional Access:** Policies MUST be enforced to require MFA and evaluate sign-in risk (e.g., block legacy authentication, require compliant devices for privileged roles).
- **Just-In-Time (JIT):** Privileged roles MUST require activation via PIM with a maximum duration of 8 hours, requiring justification and, where applicable, secondary approval.

## 6. Just-in-Time (JIT) and Just-Enough-Access (JEA)
- Standing privileged access is prohibited. All administrative access MUST be requested and granted dynamically (JIT) and scoped only to the required permissions (JEA).
- Sessions MUST automatically terminate upon expiration.

## 7. Review and Audit
- Cloud access entitlements MUST be reviewed quarterly.
- All cloud access events MUST be logged to a centralized SIEM.
