# Compliance Evidence Requirements (SOX, PCI-DSS, NIST)

This document outlines the standard evidence artifacts required by internal and external auditors to demonstrate compliance with identity and access governance controls.

## 1. Joiner, Mover, Leaver (JML) Evidence
- **Control:** Access is granted, modified, and revoked in a timely manner based on authoritative HR data.
- **Evidence Required:**
  - System-generated report of all new hires, transfers, and terminations for the audit period.
  - Timestamped logs from the IGA platform (e.g., SailPoint/Okta) showing provisioning/deprovisioning actions corresponding to the HR events.
  - For leavers: Proof that access was revoked within the SLA (typically 24 hours).

## 2. Periodic Access Review (Certification) Evidence
- **Control:** User access is reviewed periodically by management to ensure least privilege.
- **Evidence Required:**
  - System-generated report of the access certification campaign.
  - List of all reviewers and the date they completed the review.
  - Evidence of remediation: Timestamped logs showing that access marked for revocation during the review was actually removed from the target systems.

## 3. Privileged Access Management (PAM) Evidence
- **Control:** Privileged access is restricted, logged, and monitored.
- **Evidence Required:**
  - List of all active privileged accounts (from CyberArk or AWS IAM).
  - Proof of approval for a sample of users granted privileged access during the audit period.
  - Evidence of password rotation policies (e.g., CyberArk CPM configuration screenshots).
  - Audit logs showing who accessed the privileged accounts and when.

## 4. Authentication and Password Policy Evidence
- **Control:** Strong authentication mechanisms are enforced.
- **Evidence Required:**
  - Configuration screenshots from the IdP (Entra ID/Okta) showing MFA is enforced for all users.
  - Configuration screenshots showing password complexity, length, and expiration settings align with corporate policy.

## 5. Non-Human Identity (Service Account) Evidence
- **Control:** Service accounts are governed and their credentials are secured.
- **Evidence Required:**
  - Inventory of all service accounts with their assigned business owners.
  - Evidence that service account passwords/keys are rotated periodically (e.g., AWS Secrets Manager rotation configuration).
  - Proof that hardcoded secrets are not used (e.g., static code analysis reports or CyberArk Conjur configuration).
