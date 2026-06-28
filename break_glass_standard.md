# Emergency Access (Break-Glass) Standard

**Document ID:** STD-BG-001  
**Version:** 2.0  
**Last Updated:** 2026-06-26  
**Owner:** Identity Security Architecture  
**Classification:** Internal — Governance  
**Review Cycle:** Annual  
**Supersedes:** STD-BG-001 v1.0 (stub)

---

## 1. Purpose

This standard defines the requirements for provisioning, protecting, monitoring, and reviewing emergency access accounts, commonly referred to as break-glass accounts. Break-glass accounts are pre-provisioned, highly privileged accounts held in reserve for scenarios where normal administrative access mechanisms are unavailable -- such as identity provider outages, MFA system failures, federated authentication disruptions, or catastrophic infrastructure events.

Break-glass accounts are the last resort. Their existence creates standing privileged access that bypasses standard security controls. Without rigorous governance, break-glass accounts become the highest-risk credential in the enterprise. This standard ensures they remain available when genuinely needed while minimizing the risk of unauthorized use.

---

## 2. Scope

This standard applies to all break-glass and emergency access accounts across:

- Microsoft Entra ID (cloud-only emergency administrator accounts)
- AWS (root account and break-glass IAM users where applicable)
- CyberArk Privilege Cloud (master policy account and vault emergency accounts)
- On-premises Active Directory (dedicated emergency domain admin accounts)
- Network infrastructure and firewall platforms with local emergency credentials
- SaaS platforms where federated SSO is the primary access method and a local emergency account is required as fallback

This standard applies to both human emergency access accounts and emergency service credentials (e.g., emergency database accounts, emergency network device credentials).

---

## 3. Definitions

| Term | Definition |
| :--- | :--- |
| Break-Glass Account | A pre-provisioned, highly privileged account held in reserve exclusively for emergency scenarios where normal access mechanisms are unavailable |
| Emergency Scenario | A condition in which standard authentication, federation, or administrative access is unavailable due to outage, failure, or disaster -- not a situation where a user has forgotten their password or lost their device |
| Dual Approval | A requirement that two separate, named approvers must independently authorize break-glass checkout before credentials are released |
| Checkout | The act of retrieving break-glass credentials from the vault for active use |
| Check-in | The act of returning break-glass credentials to the vault after use, triggering immediate password rotation |
| SOC Alert | A critical-priority alert sent to the Security Operations Center within 5 minutes of any break-glass authentication event |
| Post-Use Review | A mandatory review conducted within 24 hours of break-glass use to document the incident, validate the emergency justification, and confirm no unauthorized actions were taken |

---

## 4. Guiding Principles

**4.1 Break-Glass Is the Last Resort**
Break-glass accounts must never be used as a convenience mechanism, a workaround for forgotten credentials, or a substitute for JIT access. Every use must be preceded by documented evidence that normal access mechanisms were unavailable or insufficient for the emergency at hand.

**4.2 Separation from Standard Identity Infrastructure**
Break-glass accounts must be isolated from the identity systems they are designed to back up. An Entra ID break-glass account must not depend on the Entra ID federation service to authenticate. An AWS break-glass account must not depend on IAM Identity Center. If the system being recovered is also the system authenticating the break-glass account, recovery becomes impossible.

**4.3 Every Use Is a Security Event**
Use of a break-glass account is never routine. Every checkout triggers a critical SOC alert, generates a mandatory incident ticket, and requires a post-use review within 24 hours. There are no exceptions.

**4.4 Dual Control at All Times**
No single individual may both approve and use a break-glass account. The approver and the user must be different people. For the most sensitive break-glass accounts (Entra ID Global Admin, AWS root, CyberArk Master Policy), two approvers are required.

**4.5 Zero Standing Knowledge**
No individual should know the break-glass password outside of an active, approved emergency scenario. Credentials are stored in the vault and released only upon dual approval. Immediately after use, credentials are rotated so the previous password is permanently invalidated.

---

## 5. Account Types and Inventory

### 5.1 Required Break-Glass Accounts

The following break-glass accounts must be maintained at all times:

| Account Type | Platform | Minimum Count | Storage Location | Approval Requirement |
| :--- | :--- | :--- | :--- | :--- |
| Cloud Emergency Admin | Microsoft Entra ID | 2 | CyberArk Vault (dedicated safe) | Dual approval: CISO + VP Infrastructure |
| AWS Root Account | AWS | 1 per AWS account | CyberArk Vault (dedicated safe) | Dual approval: CISO + Cloud Security Lead |
| CyberArk Master Policy Account | CyberArk Privilege Cloud | 1 | Hardware-secured offline storage | Dual approval: CISO + Identity Security Director |
| Emergency Domain Admin | Active Directory | 2 | CyberArk Vault (dedicated safe) | Dual approval: CISO + Infrastructure Lead |
| Emergency Network Admin | Core network infrastructure | 1 per platform | CyberArk Vault (dedicated safe) | Dual approval: CISO + Network Lead |

### 5.2 Account Naming Convention

Break-glass accounts must follow a consistent naming convention to distinguish them from standard administrative accounts and facilitate monitoring:

- Entra ID: `bg-cloud-admin-01@tenant.onmicrosoft.com`, `bg-cloud-admin-02@tenant.onmicrosoft.com`
- AWS: Tagged with `Purpose: BreakGlass`, `Owner: CISO`
- Active Directory: `BG-DomainAdmin-01`, `BG-DomainAdmin-02`

### 5.3 Redundancy Requirement

A minimum of two break-glass accounts must be maintained for each critical platform. If one account becomes unavailable (locked, credential expired, vault unreachable), the second provides continuity. The two accounts must use different hardware security keys and be stored in separate vault safes to prevent a single vault failure from blocking both.

---

## 6. Account Configuration Requirements

### 6.1 Microsoft Entra ID Break-Glass Accounts

- **Cloud-only accounts:** Must use the `.onmicrosoft.com` domain. Must not be synchronized from on-premises Active Directory or federated through any external IdP. If the federation service fails, a federated break-glass account is inaccessible -- defeating its purpose.
- **Authentication method:** Must use FIDO2 hardware security keys (e.g., YubiKey 5 series). Must not use the same authentication method as standard administrators. If standard admins use Microsoft Authenticator, break-glass accounts must use hardware keys.
- **Role assignment:** Assigned the Global Administrator role permanently (this is the exception to the JIT rule -- JIT is unavailable when the IdP is down).
- **Conditional Access exclusions:** Must be excluded from all Conditional Access policies that could block sign-in, including device compliance policies, location-based restrictions, and risk-based policies. Must be placed in a dedicated `EmergencyAccess` security group used exclusively for CA exclusion management.
- **License:** Must not depend on licensed features (e.g., Entra ID P2 PIM) that may be unavailable during an outage.
- **Password:** Minimum 64-character random password stored exclusively in CyberArk Vault.

### 6.2 AWS Root Account

- **MFA:** Hardware MFA device (physical TOTP token or FIDO2 key) required. Must not use a virtual MFA app that could be unavailable.
- **Access keys:** No programmatic access keys attached to the root account under any circumstances.
- **Usage restriction:** Root account used only for tasks that explicitly require root -- not for general administration.
- **Contact email:** Dedicated security team distribution list, not an individual's email address.
- **Storage:** Root account password and MFA device stored separately in the vault. MFA device stored in a physically secured location (safe or lockbox) in addition to vault documentation.

### 6.3 CyberArk Master Policy Account

- **Offline storage:** The Master Policy Account credentials are stored in a physically secured offline document in addition to the vault (since the vault itself may be the system being recovered).
- **Sealed envelope procedure:** Credentials are printed, placed in a tamper-evident sealed envelope, and stored in a physical safe. The envelope seal is inspected quarterly. Any evidence of tampering triggers an immediate credential rotation and security investigation.
- **Dual-custody:** Two separate individuals (CISO and Identity Security Director) must both be present to open the physical storage.

### 6.4 Active Directory Emergency Domain Admin

- **Dedicated OU:** Placed in a dedicated Organizational Unit with restricted Group Policy application.
- **Interactive logon restriction:** Configured to allow logon only from designated jump servers or the PAM console.
- **Password:** Managed by CyberArk CPM; minimum 40-character random password rotated after every use.
- **No email or mailbox:** Break-glass AD accounts must not have associated Exchange mailboxes, reducing the attack surface.

---

## 7. Vault Storage and Access Controls

All break-glass credentials (except the CyberArk Master Policy Account offline copy) must be stored in CyberArk Privilege Cloud in dedicated break-glass safes.

### 7.1 Safe Design

| Safe | Contents | Safe Members | Dual Control |
| :--- | :--- | :--- | :--- |
| `BG-EntraID-Emergency` | Entra ID break-glass accounts | CISO, VP Infrastructure, Identity Security Director | Yes -- 2 approvers required for checkout |
| `BG-AWS-Root` | AWS root account credentials per account | CISO, Cloud Security Lead, Identity Security Director | Yes -- 2 approvers required |
| `BG-AD-Emergency` | AD emergency domain admin accounts | CISO, Infrastructure Lead, Identity Security Director | Yes -- 2 approvers required |
| `BG-Network-Emergency` | Network platform emergency credentials | CISO, Network Lead, Identity Security Director | Yes -- 2 approvers required |

### 7.2 Dual Control Enforcement

CyberArk Dual Control is enabled on all break-glass safes. Dual Control requires that a configurable number of authorized approvers confirm the checkout request before the password is released. For break-glass safes, the required approver count is set to 2.

The requester submits a checkout request in PVWA with:
- Documented reason for emergency access
- Incident ticket number (auto-generated if one does not exist)
- Estimated duration of use

Two approvers from the safe's approval group independently review the request and approve. The checkout window is set to 4 hours maximum. After 4 hours, the credential is automatically checked in and rotated.

### 7.3 Post-Checkout Rotation

Immediately upon check-in (or automatically at checkout window expiration), the CyberArk CPM rotates the break-glass credential. The previous password is permanently invalidated. This ensures that anyone who observed the password during use cannot retain working knowledge of it.

---

## 8. Approval and Checkout Process

### 8.1 Standard Checkout Flow

```
Emergency condition identified
        ↓
Requestor confirms normal access is unavailable (documented in incident ticket)
        ↓
Requestor submits break-glass checkout request in CyberArk PVWA
  - Reason: [specific emergency description]
  - Incident ticket: [auto-generated or existing]
  - Duration: [estimated hours, max 4]
        ↓
SOC alert fires immediately (within 5 minutes of request submission)
        ↓
Approver 1 (e.g., CISO) reviews and approves in PVWA
        ↓
Approver 2 (e.g., VP Infrastructure) reviews and approves in PVWA
        ↓
Credential released to requestor via PVWA one-time view or PSM session
        ↓
Requestor uses credential to address emergency
        ↓
Requestor checks in credential upon completion
        ↓
CPM immediately rotates credential
        ↓
Post-use review conducted within 24 hours
```

### 8.2 Approver Unavailability

If a primary approver is unavailable, the request escalates to their designated backup approver. Each approver role must have a documented backup. Backup approver assignments are reviewed quarterly and updated when organizational changes occur.

If both the primary and backup approvers for a required role are unavailable simultaneously, this itself constitutes an emergency requiring CISO escalation. The CISO may authorize a single-approver exception for that specific checkout, which is documented and reviewed within 24 hours.

### 8.3 Prohibited Checkout Scenarios

Break-glass checkout is prohibited in the following scenarios:

- The requestor's standard credentials are unavailable due to forgotten password or lost MFA device (this is a self-service password reset scenario, not an emergency)
- JIT access was not requested before a deadline (planning failure, not an emergency)
- The break-glass account is more convenient than going through standard JIT approval
- The requestor wants to avoid leaving an audit trail in the standard access system

Requests that do not meet the emergency criteria are rejected by the approvers and the incident is documented.

---

## 9. Monitoring and Alerting

### 9.1 Real-Time Alerts

The following events must generate a critical-priority SOC alert within 5 minutes:

| Event | Alert Severity | Notification Recipients |
| :--- | :--- | :--- |
| Break-glass checkout requested | High | SOC, CISO, Identity Security team |
| Break-glass checkout approved | Critical | SOC, CISO, Identity Security team, Audit team |
| Break-glass account sign-in | Critical | SOC, CISO, Identity Security team, Audit team, Board notification if Global Admin |
| Break-glass account sign-in from unexpected location | Critical | SOC, CISO -- immediate incident response engagement |
| Break-glass credential rotation failure | High | SOC, Identity Security team |
| Break-glass account used outside checkout window | Critical | SOC, CISO -- immediate investigation |
| Checkout request rejected | Medium | CISO, Identity Security team |

### 9.2 SIEM Integration

All break-glass authentication events, PVWA checkout events, CPM rotation events, and Conditional Access exclusion changes must be forwarded to the enterprise SIEM. Dedicated detection rules must alert on:

- Any sign-in by an account in the `EmergencyAccess` group (Entra ID)
- Any API call by the AWS root account
- Any PVWA checkout from break-glass safes
- Any change to Conditional Access policy exclusions for break-glass accounts
- Any change to break-glass safe membership in CyberArk

### 9.3 Anomaly Detection

The following patterns must trigger an immediate security investigation:

- Break-glass account sign-in from an IP address not associated with corporate infrastructure
- Break-glass account sign-in outside of the approved checkout window
- Multiple break-glass checkout requests in a short period (possible probing)
- Break-glass account used to access resources beyond the stated emergency scope
- Checkout approval by an individual not on the authorized approver list

---

## 10. Post-Use Review

Within 24 hours of any break-glass checkout, the Identity Security team must conduct a post-use review. The review is documented using the `break_glass_review_form.md` template and includes:

1. Confirmation that a genuine emergency existed and normal access was unavailable
2. Timeline of events: when the emergency occurred, when checkout was requested, when access was obtained, when check-in occurred
3. Actions taken during the emergency session (from PSM recording or PVWA audit log)
4. Confirmation that no unauthorized actions were taken
5. Root cause of the emergency and remediation to prevent recurrence
6. Confirmation that the break-glass credential was rotated after use
7. Sign-off by the CISO and Identity Security Director

The post-use review report is retained for 7 years as a compliance artifact.

If the post-use review reveals that the emergency was not genuine, or that the break-glass account was used for non-emergency purposes, this constitutes a critical policy violation and is escalated as a security incident.

---

## 11. Testing and Validation

Break-glass accounts and the processes surrounding them must be tested on the following schedule to ensure they function when genuinely needed.

| Test Type | Frequency | Scope | Owner |
| :--- | :--- | :--- | :--- |
| Credential validity test | Monthly | Verify break-glass credentials in vault are current and retrievable | Identity Security Operations |
| Authentication test | Quarterly | Perform a controlled test sign-in with break-glass account in a test environment | Identity Security Architecture |
| Conditional Access exclusion test | Quarterly | Verify break-glass accounts can bypass CA policies as configured | Identity Security Architecture |
| Dual approval workflow test | Semi-annual | Full end-to-end test of checkout, dual approval, use, and check-in | Identity Security team + CISO |
| Physical storage inspection | Quarterly | Inspect tamper-evident seals on offline CyberArk Master Policy Account storage | CISO + Identity Security Director |
| Alert validation | Quarterly | Confirm SOC alerts fire within 5 minutes of test checkout event | SOC + Identity Security Operations |
| Recovery drill | Annual | Full break-glass scenario exercise simulating IdP outage | CISO + all stakeholders |

Test results are documented and retained. Failed tests trigger immediate remediation before the next business day.

---

## 12. Access Review and Certification

Break-glass accounts are reviewed on the following schedule:

| Review Type | Frequency | Reviewer | Action on Finding |
| :--- | :--- | :--- | :--- |
| Account existence and configuration | Monthly | Identity Security Operations | Remediate within 48 hours |
| Approver roster validity | Quarterly | Identity Security Director | Update immediately if approver has departed |
| Safe membership audit | Quarterly | Identity Security Architecture | Remove unauthorized members immediately |
| Full break-glass program review | Annual | CISO + Internal Audit | Update standard as required |

Break-glass accounts are explicitly excluded from standard access certification campaigns. They are governed exclusively by this standard and its dedicated review schedule.

---

## 13. Compliance Mapping

| Control | SOX ITGC | NIST SP 800-53 Rev. 5 | PCI DSS v4.0 | FFIEC |
| :--- | :--- | :--- | :--- | :--- |
| Emergency account provisioning and configuration | CC6.1 | AC-2(2), AC-2(4) | Req 8.2.2 | Access Controls |
| Dual approval for checkout | CC5.2 | AC-5, AC-2(12) | Req 8.2.4 | Separation of Duties |
| Real-time alerting on use | CC7.2 | AU-2, AU-6, IR-4 | Req 10.2.1 | Security Monitoring |
| Post-use review and documentation | CC7.3 | IR-4, AU-12 | Req 10.3 | Incident Response |
| Credential rotation after use | CC6.1 | IA-5(1) | Req 8.3.9 | Authentication Management |
| Testing and validation | CC7.3 | CP-4, CA-7 | Req 12.3 | Business Continuity |
| Conditional Access exclusion management | CC6.1 | AC-2, AC-17 | Req 8.4 | Access Controls |
| Audit log retention | CC7.2 | AU-11 | Req 10.7 | Audit Trail Retention |
| Physical security of offline credentials | CC6.4 | PE-3, MP-4 | Req 9.4 | Physical Security |

**NIST SP 800-53 AC-2(2) -- Automated Temporary and Emergency Account Management:**
Organizations must automatically remove or disable temporary and emergency accounts after a defined time period. This standard implements this control through: automatic checkout window expiration (4 hours), automatic credential rotation upon check-in, and monthly account validity reviews.

---

## 14. Violations and Enforcement

| Violation | Classification | Response |
| :--- | :--- | :--- |
| Break-glass account used without dual approval | Critical | Immediate investigation; CISO notification; potential disciplinary action |
| Break-glass account used for non-emergency purpose | Critical | Security incident; disciplinary review; post-incident remediation |
| Break-glass credential shared with unauthorized individual | Critical | Immediate rotation; security incident; CISO notification |
| Checkout approval by unauthorized approver | Critical | Immediate investigation; access revoked; safe membership audited |
| Post-use review not completed within 24 hours | High | Escalate to CISO; complete within 48 hours or escalate to audit |
| Credential not rotated after use | Critical | Immediate manual rotation; investigation of CPM failure |
| Break-glass account sign-in without active checkout | Critical | Immediate incident response; forensic review; CISO notification |
| Testing schedule missed | High | Complete overdue test within 5 business days; document reason for delay |
| Physical storage seal broken without documented procedure | Critical | Immediate credential rotation; security investigation |

---

## 15. Related Documents

- `break_glass_review_form.md` -- Post-use review template
- `STD-PAM-001` -- Privileged Access Standard
- `pam_reference_architecture.md` -- CyberArk PAM architecture including vault safe design
- `access_approval_matrix.md` -- Approval chains including break-glass dual approval
- `numeric_thresholds.md` -- Session duration limits, alerting SLAs
- `compliance_evidence_requirements.md` -- SOX and PCI audit evidence guide
- `cyberark_privilege_cloud.md` -- CyberArk Privilege Cloud capability summary

---

## 16. Document History

| Version | Date | Author | Change Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-06-26 | Identity Security Architecture | Initial stub -- basic Entra ID emergency account requirements |
| 2.0 | 2026-06-26 | Identity Security Architecture | Full rebuild -- all platforms, dual control, vault design, checkout flow, monitoring, testing, compliance mapping, violations |

---

*This document is part of the Go Cloud Architects Identity Governance RAG Assistant knowledge base. It is an original governance document grounded in NIST SP 800-53 Rev. 5 (AC-2(2), AC-5, AU-2, IR-4, IA-5(1), CP-4), PCI DSS v4.0 (Requirements 8, 10, 12), SOX ITGC control objectives (CC5.2, CC6.1, CC7.2, CC7.3), FFIEC IT Examination Handbook, and CyberArk Privilege Cloud Dual Control documentation. See SOURCE_INDEX.md for authoritative source citations.*
