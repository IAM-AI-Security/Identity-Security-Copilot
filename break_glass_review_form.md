# Break-Glass Account Review Form

## 1. Purpose
Break-glass accounts are highly privileged, emergency-only accounts designed to bypass normal authentication mechanisms (e.g., IdP failure). Because of their risk, their existence and usage must be strictly governed.

## 2. Monthly Review Requirements

### A. Account Inventory
- [ ] Verify the list of all approved break-glass accounts across critical platforms (e.g., AWS root, Entra ID emergency access accounts, CyberArk Master).
- [ ] Confirm no unauthorized break-glass accounts have been created.

### B. Usage Audit
- [ ] Review SIEM logs for the past 30 days for any login events associated with break-glass accounts.
- [ ] If usage occurred:
  - [ ] Was an emergency incident ticket opened?
  - [ ] Was the usage approved by the designated security authority?
  - [ ] Did the usage align with the scope of the emergency?

### C. Credential Rotation
- [ ] If a break-glass account was used, confirm its password/credentials were rotated immediately after the incident was resolved.
- [ ] If not used, confirm credentials are rotated according to the maximum age policy (typically 90-180 days, depending on the system capability to store them securely offline).

### D. Monitoring Verification
- [ ] Trigger a test alert for a break-glass account login.
- [ ] Verify the SOC receives the high-priority alert within the expected SLA (e.g., < 5 minutes).

## 3. Governance Application
The RAG Assistant MUST state that break-glass accounts are for emergencies only, must trigger immediate SOC alerts upon use, and must be reviewed monthly.
