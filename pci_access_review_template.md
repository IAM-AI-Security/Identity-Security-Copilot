# PCI DSS v4.0 Access Review Template

## 1. Overview
This template outlines the evidence required to demonstrate compliance with Payment Card Industry Data Security Standard (PCI DSS) v4.0 Requirement 7 (Restrict Access to System Components and Cardholder Data by Business Need to Know).

## 2. Key PCI DSS Requirements
- **Requirement 7.2.4:** User access to system components and cardholder data is reviewed at least once every six months.
- **Requirement 7.2.5:** All application and system accounts and related access privileges are reviewed at least once every six months.
- **Requirement 7.2.6:** Management acknowledges that access remains appropriate.

## 3. Required Evidence Artifacts

### A. Scope Definition
- **CDE Boundary Definition:** Documentation defining the current Cardholder Data Environment (CDE).
- **In-Scope Systems List:** A verified list of all systems, applications, and databases within the CDE boundary subject to the review.

### B. Review Execution (Bi-Annual)
- **Review Campaign Logs:** System reports proving the review was initiated and completed within the six-month timeframe.
- **Management Sign-Off:** Explicit, timestamped approvals from management confirming that the access privileges for each user are still required for their job function.
- **Application/System Accounts:** Specific evidence showing that non-human/service accounts were reviewed by their designated technical owners.

### C. Revocation Evidence
- **Access Removal Logs:** Evidence that access deemed unnecessary was revoked immediately upon discovery.

## 4. Governance Application
The RAG Assistant MUST enforce the strict six-month review frequency for PCI environments and highlight the explicit requirement to review application/system accounts, not just human users.
