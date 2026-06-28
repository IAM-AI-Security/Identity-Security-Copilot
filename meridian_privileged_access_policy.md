# Meridian Financial Group
## Privileged Access Management Policy
**Policy ID:** MFG-IAM-001  
**Version:** 3.2  
**Effective Date:** January 1, 2026  
**Next Review:** January 1, 2027  
**Policy Owner:** Chief Information Security Officer  
**Maintained By:** Identity Security Architecture  
**Classification:** Internal — Restricted  
**Regulatory Alignment:** SOX ITGC, FFIEC IT Examination Handbook, PCI DSS v4.0, NIST SP 800-53 Rev. 5

---

## 1. Purpose and Scope

This policy establishes Meridian Financial Group's requirements for the provisioning, use, monitoring, and review of privileged access to information systems, infrastructure, and data. Privileged access includes any access that exceeds standard user permissions and could be used to modify security controls, access regulated data, or impact system availability.

This policy applies to all Meridian employees, contractors, consultants, and third-party vendors who hold or request privileged access to Meridian systems, regardless of location or employment type.

---

## 2. Privileged Access Tiers

Meridian classifies privileged access into three tiers based on risk:

| Tier | Description | Examples | Review Frequency |
| :--- | :--- | :--- | :--- |
| Tier 1 — Critical | Access that could affect regulated data, financial systems, or security controls enterprise-wide | AWS AdministratorAccess, Global Administrator (Entra ID), CyberArk Master Policy Account, Core Banking System DBA | Quarterly |
| Tier 2 — Elevated | Access to production systems with write capability; limited blast radius | PowerUserAccess (AWS), Contributor (Azure), Active Directory Domain Admin, Database Owner | Quarterly |
| Tier 3 — Standard Privileged | Read-only privileged access; operational access with no write to regulated data | SecurityAudit (AWS), Security Reader (Azure), Read-only DBA | Semi-annual |

---

## 3. Eligibility Requirements -- Contractor Access Rules and Prohibitions

### 3.1 Full-Time Employees
Full-time Meridian employees may be eligible for Tier 1, 2, or 3 privileged access subject to:
- Documented business justification approved by the employee's direct manager
- Role-appropriate background verification on file with Human Resources
- Completion of Meridian's annual Privileged Access Security Training within the preceding 12 months
- Approval per Section 5 of this policy

### 3.2 Contractors and Consultants
Contractors and consultants engaged through Meridian's approved vendor program are subject to the following restrictions:
- **Tier 1 access is prohibited for all contractors under all circumstances.** No exception process exists for contractor Tier 1 access.
- Tier 2 access requires CISO approval in addition to standard approvals, is limited to a maximum duration of 90 days per engagement, and requires weekly review by the Identity Security team.
- Tier 3 access requires manager and Cloud Security team approval, is limited to 180 days, and requires quarterly certification.
- All contractor privileged access is provisioned as Just-In-Time only via CyberArk Secure Cloud Access. No standing privileged roles are permitted.

### 3.3 Third-Party Vendors
Third-party vendors (e.g., software support, managed services) may receive time-limited, scoped privileged access only:
- Access is provisioned via CyberArk Vendor Privileged Access Management (VPAM)
- Sessions are recorded by PSM for all vendor connections
- Maximum session duration: 4 hours per session, 30-day total engagement limit without renewal
- Vendor access is revoked immediately upon completion of the engagement

---

## 4. Zero Standing Privilege (ZSP) Requirement -- No Standing Privileged Access

Meridian's target architecture state is Zero Standing Privilege (ZSP). No Meridian employee or contractor shall hold persistent Tier 1 or Tier 2 privileged access outside of an active, approved Just-In-Time session.

**Implementation:**
- All Tier 1 AWS access is provisioned via CyberArk Secure Cloud Access (SCA) with a maximum 4-hour session duration
- All Tier 1 Azure access is provisioned via Entra ID Privileged Identity Management (PIM) with a maximum 4-hour activation window
- Tier 2 AWS and Azure access is provisioned via SCA or PIM with an 8-hour maximum session duration
- Standing privileged roles are reserved exclusively for Meridian's designated break-glass accounts (see MFG-BG-001)

---

## 5. Approval Requirements

All privileged access requests are submitted through ServiceNow. Approvals are required before provisioning.

| Access Level | Approver 1 | Approver 2 | Approver 3 |
| :--- | :--- | :--- | :--- |
| Tier 3 — Standard Privileged | Direct Manager | — | — |
| Tier 2 — Elevated | Direct Manager | Cloud Security Team Lead | — |
| Tier 1 — Critical | Direct Manager | VP of Information Security | CISO |
| Contractor Tier 2 | Direct Manager | Cloud Security Team Lead | CISO |
| Break-Glass Checkout | CISO | VP Infrastructure | — |
| Exception to ZSP Policy | CISO | Chief Risk Officer | — |

Approvals are logged in ServiceNow and retained for 7 years as SOX ITGC evidence.

---

## 6. Session Duration Limits

| Access Level | AWS | Azure | Maximum Duration |
| :--- | :--- | :--- | :--- |
| Tier 1 — Critical | AdministratorAccess | Owner / Global Admin | 4 hours |
| Tier 2 — Elevated | PowerUserAccess | Contributor | 8 hours |
| Tier 3 — Standard | SecurityAudit | Security Reader | 12 hours |
| Break-Glass | Root / Global Admin | Global Administrator | 4 hours |
| Vendor Access | Custom scoped role | Custom scoped role | 4 hours |

Session duration limits are enforced by CyberArk SCA and Entra ID PIM. They cannot be extended without a new approval request.

---

## 7. Prohibited Configurations

The following configurations are prohibited and constitute a critical finding if discovered:

- AdministratorAccess or Owner role assigned permanently to any human identity
- Privileged access assigned directly to a user without going through CyberArk SCA or PIM
- Shared privileged accounts (multiple individuals using the same privileged credential)
- AdministratorAccess or equivalent assigned to any service account or automation identity
- Hardcoded privileged credentials in source code, configuration files, or pipeline variables
- Privileged access assigned to a contractor in Tier 1
- Active privileged access for a departed employee or contractor (access-after-termination)

Critical findings require same-business-day remediation. Unresolved critical findings are escalated to the CISO at end of business day.

---

## 8. Access Review and Certification

### 8.1 Quarterly Certification
All Meridian employees holding Tier 1 or Tier 2 privileged access are subject to quarterly access certification. Certification campaigns run in January, April, July, and October. Certifications must be completed by the 15th of the month following quarter end.

Certification is conducted in SailPoint IdentityNow. Managers receive automated notification and must approve or revoke each privilege assigned to their direct reports.

Failure to certify within the grace period (15th of the month) triggers:
- Day 16: Automated suspension of uncertified access
- Day 20: Escalation to the manager's director
- Day 30: Permanent revocation pending re-request and full approval workflow

### 8.2 Dormancy-Based Disablement
The following dormancy thresholds apply regardless of certification status:

| Account Type | Dormancy Threshold | Action |
| :--- | :--- | :--- |
| Tier 1 Privileged Account | 30 days unused | Automatic suspension; owner notified |
| Tier 2 Privileged Account | 45 days unused | Automatic suspension; manager notified |
| Contractor Privileged Account | 14 days unused | Automatic revocation |
| Standard Employee Account | 90 days unused | Automatic suspension; manager notified |

### 8.3 Separation-of-Duties Reviews
The Identity Security Architecture team conducts semi-annual SoD reviews to identify conflicting role combinations. Users holding conflicting roles receive a 30-day remediation window before automatic revocation of the lower-risk role.

---

## 9. Monitoring and Alerting

All privileged access sessions are monitored in real time. The following events generate immediate alerts to the Security Operations Center (SOC):

- Privileged session initiated outside standard business hours (8 AM–8 PM Eastern) without prior approval
- Privileged session from an IP address not associated with Meridian corporate infrastructure or approved VPN
- More than 3 failed privileged session attempts in a 10-minute window
- Privileged access to production financial systems outside of a change management window
- Any break-glass account authentication event
- Privileged access by a user whose access certification is overdue

All privileged session activity is forwarded to Meridian's Splunk SIEM within 60 seconds of the event. PSM session recordings are retained for 12 months online and 7 years archived.

---

## 10. Violations and Enforcement

| Violation | Classification | Response |
| :--- | :--- | :--- |
| Tier 1 access granted to contractor | Critical | Immediate revocation; CISO notification; disciplinary review |
| Standing privileged role assigned outside SCA/PIM | Critical | Immediate revocation; incident investigation |
| Shared privileged account discovered | Critical | Immediate revocation; forensic review |
| Access-after-termination discovered | Critical | Immediate revocation; HR and Legal notification |
| Certification not completed by grace period | High | Automatic suspension per Section 8.1 |
| Dormancy threshold exceeded | High | Automatic suspension per Section 8.2 |
| Session duration limit exceeded | Medium | Session terminated; manager notified |
| Privileged access request without proper approval | High | Access revoked; re-request required |

---

## 11. Related Policies and Standards

- **MFG-BG-001** — Break-Glass Emergency Access Policy
- **MFG-NHI-001** — Non-Human Identity and Machine Identity Policy  
- **MFG-CLD-001** — Cloud Access Policy
- **MFG-INC-001** — Identity Security Incident Response Procedure
- CyberArk Privilege Cloud (primary PAM platform — see Identity Security Architecture runbooks)
- NIST SP 800-53 Rev. 5 (AC-2, AC-5, AC-6, AU-2, IA-5)
- FFIEC IT Examination Handbook — Access Controls section
- SOX ITGC CC5.2, CC6.1, CC7.2
- PCI DSS v4.0 Requirements 7, 8, 10

---

## 12. Document History

| Version | Date | Author | Change Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | March 2022 | Identity Security Architecture | Initial policy — on-premises PAM only |
| 2.0 | January 2024 | Identity Security Architecture | Added ZSP requirement; expanded cloud access controls |
| 3.0 | June 2025 | Identity Security Architecture | Added contractor Tier 1 prohibition; AI agent controls |
| 3.2 | January 2026 | Identity Security Architecture | Updated dormancy thresholds; added SoD review requirements |

---

*Meridian Financial Group — Internal Policy Document. Not for external distribution. Questions: identity-security@meridianfinancial.com*
