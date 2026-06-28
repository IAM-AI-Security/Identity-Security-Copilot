# SOX Access Review Evidence Template

## 1. Overview
This template defines the mandatory evidence required to prove the effective execution of periodic access reviews for systems in scope for the Sarbanes-Oxley Act (SOX).

## 2. Required Evidence Artifacts

### A. Population Completeness (The "System Generated Data" Test)
To prove the review covered all users, the following MUST be provided:
- **Raw User Extract:** The original, unfiltered export of all active accounts from the target system.
- **Extraction Parameters:** Screenshot or system log proving the date, time, and query parameters used to generate the extract.
- **Reconciliation Proof:** Evidence that the raw extract was successfully loaded into the identity governance tool (e.g., SailPoint) without data loss.

### B. Review Execution
To prove the review was performed by authorized personnel:
- **Reviewer Mapping:** Documentation showing how reviewers (usually direct managers or application owners) were assigned to specific users/entitlements.
- **Approval/Revocation Logs:** System-generated logs showing the exact timestamp, reviewer identity, and decision (Approve/Revoke) for every entitlement.
- **Review Completion:** A system report confirming 100% of the population was reviewed before the campaign deadline.

### C. Revocation Fulfillment
To prove that revoked access was actually removed:
- **Fulfillment Tickets:** Ticket numbers (e.g., ServiceNow) automatically generated for every revoked entitlement.
- **Closure Evidence:** Logs showing the tickets were closed and the access was removed from the target system within the SLA (typically 72 hours).

## 3. Governance Application
If an auditor or user asks what is required for a SOX review, the RAG Assistant MUST list the three pillars: Population Completeness, Review Execution, and Revocation Fulfillment.
