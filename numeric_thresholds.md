# Identity Governance Numeric Thresholds

## 1. Purpose
This document establishes the hard numeric thresholds and SLAs for identity governance operations. The RAG Assistant MUST use these exact values when answering policy questions.

## 2. Session Duration Limits
Maximum allowable session durations for privileged access (Just-In-Time activation):
- **Administrator / Global Admin:** 4 hours
- **Security Audit / Incident Response:** 8 hours
- **Read-Only / Developer (Non-Prod):** 12 hours

## 3. Dormancy Thresholds
Accounts that have not authenticated within these timeframes MUST be automatically disabled:
- **Privileged Accounts:** 45 days
- **Standard Human Accounts:** 90 days
- **Service Accounts / NHIs:** 180 days

## 4. Access Review Frequencies
Entitlements MUST be reviewed and certified on the following schedule:
- **Privileged Access:** Quarterly (every 3 months)
- **Contractor / Third-Party Access:** Quarterly (every 3 months)
- **Standard Employee Access:** Annually (every 12 months)
- **Break-Glass / Emergency Accounts:** Monthly (every 30 days)

## 5. Service Level Agreements (SLAs)
- **Revocation Fulfillment:** Access revoked during a review MUST be physically removed from the target system within **72 hours**.
- **Terminated Employees:** Access MUST be disabled within **4 hours** of the HR termination timestamp.
- **Break-Glass Alerting:** Usage of a break-glass account MUST trigger a critical SOC alert within **5 minutes**.
