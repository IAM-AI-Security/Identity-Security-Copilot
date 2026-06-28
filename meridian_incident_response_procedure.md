# Meridian Financial Group
## Identity Security Incident Response Procedure
**Policy ID:** MFG-INC-001  
**Version:** 2.0  
**Effective Date:** January 1, 2026  
**Next Review:** January 1, 2027  
**Policy Owner:** Chief Information Security Officer  
**Maintained By:** Identity Security Architecture + SOC  
**Classification:** Internal — Restricted  
**Regulatory Alignment:** FFIEC IT Examination Handbook, NIST SP 800-61, SOX ITGC

---

## 1. Purpose and Scope

This procedure defines Meridian Financial Group's response to identity security incidents -- events involving the compromise, misuse, or unauthorized use of human or machine identities. Identity incidents represent Meridian's highest-risk event category given our regulated data environment and reliance on federated, cloud-native identity infrastructure.

This procedure applies to all identity-related security events including compromised credentials, unauthorized privileged access, AI agent anomalies, and NHI credential exposure.

---

## 2. Incident Classification

| Severity | Definition | Examples | Response SLA |
| :--- | :--- | :--- | :--- |
| P1 — Critical | Active compromise of a privileged identity or regulated system | Compromised Global Admin, Root account usage, Break-glass misuse, Confirmed credential theft | Immediate — 15 minutes to first response |
| P2 — High | Suspected compromise or policy violation with potential data access | Unusual privileged session from unknown IP, Access-after-termination discovered, AI agent taking unauthorized action | 1 hour to first response |
| P3 — Medium | Policy violation without confirmed data access | Hardcoded credential discovered in code, Dormant privileged account accessed, Contractor accessing Tier 1 resources | 4 hours to first response |
| P4 — Low | Policy anomaly; no confirmed risk | Certification overdue, Orphaned NHI discovered, Session duration limit exceeded | Next business day |

---

## 3. Identity Incident Response Team

| Role | Responsibility | Contact |
| :--- | :--- | :--- |
| SOC Analyst (On-call) | Initial triage and P1/P2 escalation | SOC hotline — 24/7 |
| Identity Security Architect | Technical containment lead | On-call rotation |
| CISO | Executive decision authority; regulatory notification | Direct line |
| Cloud Security Lead | AWS/Azure containment actions | On-call rotation |
| Legal / Compliance | Regulatory notification assessment | Business hours; CISO escalates after-hours |
| HR | Employee-involved incidents | Business hours |

---

## 4. Response Procedures by Incident Type

### 4.1 Compromised Human Privileged Account

**Indicators:** Unusual login time/location, impossible travel, MFA fatigue attack, user reports credential theft.

**Immediate Actions (within 15 minutes for P1):**
1. SOC disables the affected user account in Okta (suspends all sessions)
2. Revoke all active CyberArk SCA sessions for the affected user
3. Revoke all active Entra ID PIM role activations
4. Force-rotate any credentials the affected user may have viewed or retrieved via CyberArk PVWA in the preceding 24 hours
5. Preserve all Splunk and CloudTrail logs for forensic review -- do not delete or modify
6. Open P1 ServiceNow incident; notify CISO immediately

**Investigation (within 1 hour):**
- Pull CloudTrail logs for all API calls made by or on behalf of the affected identity in the preceding 72 hours
- Pull CyberArk PSM session recordings for any privileged sessions in the same window
- Identify all resources accessed and any configuration changes made
- Determine if lateral movement occurred (other accounts accessed using the compromised identity)

**Recovery:**
- Re-provision user account only after confirmed containment and CISO approval
- Force new MFA device registration
- Require re-enrollment in Meridian's Privileged Access Security Training before access restoration

---

### 4.2 Hardcoded Credential Discovered

**Indicators:** GitHub Advanced Security alert, code review finding, developer self-report, external researcher report.

**Immediate Actions (same business day):**
1. Identify the credential type (API key, password, certificate, OAuth secret)
2. Revoke the credential immediately -- do not wait to assess impact
3. Determine the credential's scope of access and which systems it could have reached
4. Pull access logs for the credential from point of first commit to revocation
5. Identify when the credential was first committed to source control (git log)
6. Assess whether the repository is or was ever public

**If Repository Was Public:**
- Treat as confirmed compromise -- assume credential was observed by external parties
- Escalate to P1; notify CISO and Legal immediately
- If credential had access to regulated data: assess regulatory notification requirement (FFIEC breach notification, PCI incident reporting)
- Engage forensics to determine if credential was used by unauthorized parties

**Remediation:**
- Remove the hardcoded credential from all branches and tags (git history rewrite if necessary)
- Replace with Conjur JWT authentication or approved secrets management pattern
- Conduct code audit for additional hardcoded credentials in the same repository
- Developer mandatory remediation training

---

### 4.3 AI Agent Unauthorized Action

**Indicators:** AI agent takes an action outside its authorized tool set, rate limit breached, agent modifies its own execution role, agent bypasses deterministic gate.

**Immediate Actions:**
1. Suspend the agent's execution role (remove all permissions via IAM policy deny)
2. Preserve CloudTrail and CloudWatch logs for the agent's execution role ARN
3. Review all actions taken by the agent in the preceding 24 hours
4. Assess whether any unauthorized IAM changes, data access, or system modifications occurred
5. Open P1 or P2 incident depending on impact scope; notify Identity Security Architecture

**Investigation:**
- Review the agent's system prompt and tool configuration for potential prompt injection vectors
- Review CloudTrail for any API calls outside the agent's authorized action set
- Determine if the agent's execution role was modified by the agent itself (automatic P1 escalation)
- Review Conjur audit logs for any secrets retrieved outside the agent's authorized policy

**Recovery:**
- Agent is not reinstated until: root cause identified, deterministic gate validated, authorized tool set reviewed, and Identity Security Architecture signs off
- Mandatory adversarial testing (minimum 20 prompt injection test cases) before production reinstatement
- CISO sign-off required for any P1 AI agent incident before reinstatement

---

### 4.4 Break-Glass Account Misuse

**Indicators:** Break-glass used outside of documented emergency, break-glass used without dual approval, post-use review reveals non-emergency use.

**Immediate Actions:**
1. Rotate break-glass credential immediately (if not already done post-checkout)
2. Preserve all session recordings and PVWA audit logs
3. Open P1 incident; notify CISO and Legal
4. Identify all actions taken during the break-glass session

**Investigation:**
- Confirm whether a genuine emergency existed at the time of use
- Review approver identity -- confirm both approvers were authorized
- Review PSM session recording for all commands executed
- Determine if any unauthorized actions were taken

**Disciplinary:**
- Break-glass misuse is a terminable offense under Meridian's Code of Conduct
- HR and Legal are engaged for all confirmed break-glass misuse incidents
- Regulatory notification assessed by Legal based on actions taken during the session

---

## 5. Regulatory Notification Requirements

The following identity incidents may trigger regulatory notification obligations. Legal and Compliance assess within 24 hours of P1 incident confirmation:

| Incident Type | Potential Notification | Timeframe |
| :--- | :--- | :--- |
| Compromised credential with access to cardholder data | PCI DSS — card brand and acquiring bank | Immediately upon confirmation |
| Unauthorized access to customer financial data | FFIEC — primary federal regulator | As soon as possible |
| Breach affecting >500 customers | State breach notification laws | Varies by state — typically 30-72 hours |
| Material cybersecurity incident | SEC Rule 10-K/8-K disclosure | 4 business days if material |
| Ransomware or destructive attack | CISA reporting | 72 hours |

CISO is the decision authority for regulatory notification. Legal drafts all external communications.

---

## 6. Post-Incident Review

All P1 and P2 incidents require a post-incident review (PIR) within 5 business days of containment:

**PIR Content:**
- Incident timeline from detection to containment to recovery
- Root cause analysis (5-why or fishbone)
- Evidence that the incident is fully contained
- Regulatory notification status
- Lessons learned
- Control improvements implemented or planned
- Owner and target date for each improvement

PIR report is reviewed by the CISO and retained for 7 years as regulatory evidence.

---

## 7. Evidence Preservation

All identity incident evidence is preserved as follows:
- CloudTrail logs: exported to immutable S3 in MFG-AWS-Prod-Security account immediately upon incident declaration
- PSM session recordings: flagged for legal hold; not subject to standard retention deletion
- Okta audit logs: exported to Splunk immediately
- Conjur audit logs: exported and preserved
- ServiceNow incident record: complete with all notes, approvals, and attachments

Evidence must not be modified, deleted, or overwritten after incident declaration. Evidence preservation requests are logged in the ServiceNow incident record.

---

*Meridian Financial Group — Internal Policy Document. Not for external distribution. Questions: soc@meridianfinancial.com | identity-security@meridianfinancial.com*
