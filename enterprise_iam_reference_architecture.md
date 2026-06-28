# Enterprise IAM Reference Architecture

This document describes the high-level reference architecture for the enterprise Identity and Access Management (IAM) ecosystem.

## 1. Identity Providers (IdP) and Directory Services
- **Authoritative Source:** Workday (HRIS) acts as the single source of truth for human identities.
- **Primary Directory:** Active Directory (AD) for legacy on-premises systems; Microsoft Entra ID for cloud and modern applications.
- **Single Sign-On (SSO):** Okta or Entra ID serves as the central SSO federation hub, utilizing SAML 2.0 and OIDC protocols.

## 2. Identity Governance and Administration (IGA)
- **Platform:** SailPoint IdentityNow or Entra ID Governance.
- **Function:** Connects the HR source to the directories and downstream applications.
- **Capabilities:** Automates Joiner, Mover, Leaver (JML) provisioning via SCIM, manages access request workflows, and orchestrates periodic access certification campaigns.

## 3. Privileged Access Management (PAM)
- **Human PAM:** CyberArk Privilege Cloud secures administrator access to Windows/Linux servers, databases, and network devices. Enforces session isolation (PSM) and password rotation (CPM).
- **Cloud PAM:** AWS IAM Identity Center provides federated, role-based access to AWS accounts. CyberArk Secure Cloud Access provides Just-In-Time (JIT) elevation for cloud consoles.
- **Machine PAM (Secrets Management):** CyberArk Conjur and AWS Secrets Manager provide dynamic secrets to CI/CD pipelines, Kubernetes clusters, and AI agents, eliminating hardcoded credentials.

## 4. Zero Trust and Access Enforcement
- **Conditional Access:** Entra ID Conditional Access policies evaluate user risk, device compliance (via Intune/MDM), and location before granting access to applications.
- **Multi-Factor Authentication (MFA):** Enforced globally via Okta Verify or Microsoft Authenticator. FIDO2/WebAuthn hardware keys are required for highly privileged administrators.

## 5. Continuous Monitoring and Drift Detection
- **Cloud Entitlements:** AWS IAM Access Analyzer continuously monitors cloud permissions to identify unused access and external sharing.
- **SIEM Integration:** All identity platforms (Okta, Entra, CyberArk, SailPoint) forward authentication and audit logs to the central SIEM (e.g., Splunk or Sentinel) for threat detection and incident response.
