# Enterprise Privileged Access Standard

## Section 1 -- Scope
Applies to all privileged accounts including human administrators, service accounts, and AI agent execution roles across AWS, Azure, GCP, and on-premises environments.

## Section 2 -- Eligibility
- **Full-time employees:** Eligible with manager and security team approval.
- **Contractors:** Eligible for temporary Just-In-Time (JIT) access only; no permanent privileged access permitted.
- **Service accounts:** Eligible with a documented owner and quarterly review.
- **AI agents:** Eligible for scoped execution roles only; Conjur JWT authentication required; no stored credentials permitted.

## Section 3 -- Session Duration Limits
- **Administrator:** 4 hours maximum
- **Security Audit:** 8 hours maximum
- **Read Only:** 12 hours maximum
- **Developer:** 8 hours maximum
- **Break Glass:** 1 hour maximum, dual approval required

## Section 4 -- Review Requirements
- **Privileged accounts:** Quarterly certification
- **Break glass accounts:** Monthly review
- **Service accounts:** Semi-annual review
- **AI agent execution roles:** Continuous automated monitoring via IAM Privilege Drift Detection Agent

## Section 5 -- Approval Requirements
- **Standard privileged access:** Manager + security team approval
- **AdministratorAccess:** CISO approval required
- **Break glass:** Dual approval, automatic revocation after 1 hour
- **Contractor privileged access:** Prohibited for permanent access; JIT only with manager and security approval

## Section 6 -- Prohibited Configurations
- AdministratorAccess attached to service accounts: PROHIBITED
- Permanent privileged access for contractors: PROHIBITED
- Privileged access without MFA: PROHIBITED
- Shared privileged accounts: PROHIBITED
- Hardcoded credentials in code or configuration: PROHIBITED
