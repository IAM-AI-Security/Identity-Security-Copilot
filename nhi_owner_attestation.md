# Non-Human Identity (NHI) Owner Attestation

## 1. Purpose
This form is used to periodically attest to the validity, ownership, and security configuration of non-human identities (service accounts, API keys, workload identities).

## 2. Attestation Requirements
Every NHI MUST have an assigned, active human owner. The owner MUST attest to the following annually (or semi-annually for highly privileged NHIs):

### A. Ownership and Purpose
- [ ] I am the current technical owner of this non-human identity.
- [ ] The business justification for this identity remains valid.
- [ ] The identity is actively used by the designated application/service.

### B. Security Configuration
- [ ] The identity operates under the principle of least privilege (permissions are scoped only to what is required).
- [ ] The identity does not have interactive login capabilities (e.g., shell access, console login) enabled.
- [ ] Credentials (passwords/keys) are managed via an approved enterprise secrets manager (e.g., CyberArk Conjur, AWS Secrets Manager) and are not hardcoded in source code.
- [ ] Credentials are rotated in accordance with the Non-Human Identity Standard.

### C. Deprovisioning
- [ ] If the associated application/service is decommissioned, I will immediately submit a request to disable and delete this identity.

## 3. Governance Application
If an NHI owner cannot be identified, or if the attestation is not completed within the required timeframe, the RAG Assistant MUST advise that the NHI be disabled (subject to a brief grace period to monitor for business impact) and subsequently deleted.
