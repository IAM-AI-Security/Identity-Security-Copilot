# Example Questions and Expected Answers

## 1. Overview
This document provides a test set of questions to validate the RAG Assistant's retrieval accuracy and policy enforcement.

## 2. Test Questions

**Q1: Can a contractor receive AdministratorAccess?**
*Expected Answer:* No. Broad administrative permission sets like `AdministratorAccess` must not be permanently assigned. Access must follow least privilege and be granted via Just-In-Time (JIT) provisioning.

**Q2: What evidence is required for a SOX privileged access review?**
*Expected Answer:* Three pillars of evidence are required: 
1. Population Completeness (raw extract and query parameters).
2. Review Execution (reviewer mapping and approval logs).
3. Revocation Fulfillment (tickets proving access was removed within 72 hours).

**Q3: Should service accounts have permanent secrets?**
*Expected Answer:* No. The Non-Human Identity Standard dictates a "Secretless First" approach using workload identities (e.g., AWS IAM Roles, Azure Managed Identities). If static secrets are unavoidable, they must be stored in a secrets manager (like CyberArk Conjur) and rotated automatically.

**Q4: What is the maximum session duration for cloud admins?**
*Expected Answer:* According to the Numeric Thresholds, the maximum session duration for Administrator/Global Admin access is 4 hours.

**Q5: Which NIST controls map to privileged access reviews?**
*Expected Answer:* NIST SP 800-53 control AC-2 (Account Management) and AC-6 (Least Privilege) require the periodic review and adjustment of system accounts and privileges.

**Q6: How should stale service accounts be handled?**
*Expected Answer:* Service accounts that have been dormant for 180 days must be automatically disabled.

**Q7: What should happen when an NHI owner cannot be identified?**
*Expected Answer:* The NHI must be flagged for quarantine, disabled (after a brief grace period to monitor for business impact), and subsequently deleted if no owner claims it.
