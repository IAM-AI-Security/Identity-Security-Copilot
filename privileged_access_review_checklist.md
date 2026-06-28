# Privileged Access Review Checklist

## 1. Overview
This checklist defines the mandatory steps for conducting quarterly reviews of privileged access (e.g., Domain Admins, AWS Administrators, CyberArk Safe Owners).

## 2. Review Checklist

### Phase 1: Preparation
- [ ] **Define Scope:** Identify all target systems, cloud platforms, and PAM vaults in scope for the quarterly review.
- [ ] **Extract Population:** Generate raw extracts of all privileged entitlements and vault memberships.
- [ ] **Identify Reviewers:** Map each privileged entitlement to the appropriate reviewer (must be a manager or asset owner, NOT the user themselves).

### Phase 2: Execution
- [ ] **Launch Campaign:** Initiate the review campaign in the IGA platform (e.g., SailPoint).
- [ ] **Validate Justification:** Reviewers MUST verify the business need for the privileged access. "They had it before" is not a valid justification.
- [ ] **Check Dormancy:** Flag any privileged accounts that have not been used in the last 45 days for potential revocation.
- [ ] **Review MFA Status:** Confirm that all human privileged accounts have hardware or strong MFA enforced.

### Phase 3: Remediation
- [ ] **Revoke Unjustified Access:** Automatically generate tickets to remove access that was denied during the review.
- [ ] **Verify Removal:** Confirm that all revocation tickets are closed and access is physically removed from the target systems within 72 hours.
- [ ] **Handle Non-Responders:** Any access not explicitly approved by the campaign deadline MUST be revoked.

## 3. Governance Application
The RAG Assistant MUST enforce that privileged access is reviewed quarterly (more frequently than standard access) and that non-responses result in automatic revocation.
