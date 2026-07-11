# SOC 2 Trust Services Criteria -- Identity and Access Control Requirements
## AICPA Trust Services Criteria (2017 with 2022 updates)

**Source:** AICPA Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (TSC)

---

## 1. Overview

SOC 2 (System and Organization Controls 2) is an auditing standard developed by the American Institute of Certified Public Accountants (AICPA). It evaluates service organizations based on five Trust Services Criteria:

1. **Security** (Common Criteria -- required for all SOC 2 reports)
2. **Availability**
3. **Processing Integrity**
4. **Confidentiality**
5. **Privacy**

Most SOC 2 audits focus on Security (Common Criteria) plus one or more additional criteria selected based on the organization's services.

**SOC 2 Type I:** Point-in-time assessment of whether controls are suitably designed
**SOC 2 Type II:** Assessment of whether controls operated effectively over a period (typically 6-12 months) -- the gold standard for enterprise trust

---

## 2. Common Criteria -- Security (CC Series)

### CC1 -- Control Environment

**CC1.1** -- The entity demonstrates a commitment to integrity and ethical values
**CC1.2** -- The board of directors demonstrates independence and exercises oversight
**CC1.3** -- Management establishes structure, reporting lines, and authorities
**CC1.4** -- The entity demonstrates commitment to attract, develop, and retain competent individuals
**CC1.5** -- The entity holds individuals accountable for their responsibilities

**IAM relevance:** Documented security policies, security awareness training, role-based accountability for access decisions

---

### CC2 -- Communication and Information

**CC2.1** -- The entity obtains or generates and uses relevant, quality information to support control objectives
**CC2.2** -- The entity communicates information internally to support control objectives
**CC2.3** -- The entity communicates externally with parties affecting the achievement of control objectives

**IAM relevance:** Security policies communicated to workforce, access request and approval workflows documented

---

### CC3 -- Risk Assessment

**CC3.1** -- The entity specifies objectives with sufficient clarity to enable identification and assessment of risks
**CC3.2** -- The entity identifies risks to the achievement of its objectives and analyzes those risks
**CC3.3** -- The entity considers the potential for fraud
**CC3.4** -- The entity identifies and assesses significant changes that could impact the system of internal control

**IAM relevance:** Access risk assessments, privileged access risk scoring, identity risk matrix

---

### CC4 -- Monitoring Activities

**CC4.1** -- The entity selects, develops, and performs ongoing and separate evaluations to ascertain whether the components of internal control are present and functioning
**CC4.2** -- The entity evaluates and communicates internal control deficiencies

**IAM relevance:** Continuous access monitoring, periodic access reviews, audit findings remediation tracking

---

### CC5 -- Control Activities

**CC5.1** -- The entity selects and develops control activities that contribute to the mitigation of risks
**CC5.2** -- The entity selects and develops general control activities over technology
**CC5.3** -- The entity deploys control activities through policies and procedures

**IAM relevance:** Access control policies, technical controls implementation, separation of duties enforcement

---

### CC6 -- Logical and Physical Access Controls (Most Critical for IAM)

**CC6.1 -- Logical Access Security Measures**
The entity implements logical access security software, infrastructure, and architectures over protected information assets to protect them from security events to meet the entity's objectives.

Key points of focus:
- Identification and authentication of users
- Identification and authentication of systems and devices
- Restriction of access based on authorization
- Identification and authentication requirements to access specific assets
- Management of encryption keys
- New data processing and computing needs
- Vulnerabilities and threats to systems

**Evidence required:**
- Access control policies and procedures
- User provisioning and deprovisioning records
- Authentication configuration (MFA enforcement)
- Privileged access inventory and controls
- Encryption key management documentation

**CC6.2 -- Prior to Issuing System Credentials**
Prior to issuing system credentials and granting system access, the entity registers and authorizes new internal and external users whose access is administered by the entity.

Key points of focus:
- New internal and external users are registered
- Credentials and authentication methods are authorized and issued

**Evidence required:**
- Access request and approval workflow documentation
- New user onboarding records showing authorization before access granted
- Contractor and third-party access authorization records

**CC6.3 -- Role of the Entity's Processes to Remove Access**
The entity authorizes, modifies, or removes access to data, software, functions, and other protected information assets based on roles, responsibilities, or the system design and changes, giving consideration to the concepts of least privilege and segregation of duties.

Key points of focus:
- Role-based access is aligned with responsibilities
- Access is modified based on role changes
- User access is removed when no longer required
- Access reviews are performed

**Evidence required:**
- Role-based access control documentation
- Access modification records for role changes (movers)
- Deprovisioning records for terminated users (leavers) with timestamps
- Access review campaign results showing reviews completed
- Evidence of access removed based on review findings

**CC6.4 -- Physical Access**
The entity restricts physical access to facilities and protected information assets to authorized personnel to meet the entity's objectives.

**CC6.5 -- Logical Access to Information Assets**
The entity discontinues logical access to protected information assets when access is no longer authorized.

Key points of focus:
- Access is removed when employment or engagement ends
- Access is removed when responsibilities change
- Periodic access reviews result in access removal

**Evidence required:**
- Automated deprovisioning logs showing access removed within SLA
- Role change access modification records
- Periodic access certification completion records

**CC6.6 -- Security Threats from Outside the System Boundaries**
The entity implements controls to prevent or detect and act upon the introduction of unauthorized or malicious software to meet the entity's objectives.

**CC6.7 -- Transmission and Movement of Information**
The entity restricts the transmission, movement, and removal of information to authorized internal and external users and processes and protects it during transmission.

**Evidence required:**
- Encryption in transit configuration
- Data loss prevention controls
- Secure file transfer documentation

**CC6.8 -- Prevents or Detects Unauthorized or Malicious Software**
The entity implements controls to prevent or detect and act upon the introduction of unauthorized or malicious software to meet the entity's objectives.

---

### CC7 -- System Operations

**CC7.1** -- Detection and Monitoring Procedures
The entity uses detection and monitoring procedures to identify changes to configurations or the introduction of new components.

**CC7.2** -- Monitoring of System Components
The entity monitors system components and the operation of those components for anomalies that are indicative of malicious acts, natural disasters, and errors affecting the entity's ability to meet its objectives.

**Evidence required:**
- SIEM/logging configuration and coverage
- Security monitoring alerts and response records
- Anomaly detection procedures

**CC7.3** -- Evaluation of Security Events
The entity evaluates security events to determine whether they could or have resulted in a failure of the entity to meet its objectives.

**CC7.4** -- Incident Response
The entity responds to identified security incidents by executing a defined incident response program to understand, contain, remediate, and communicate security events.

**CC7.5** -- Remediation of Identified Security Vulnerabilities
The entity removes security vulnerabilities from systems and infrastructure to meet the entity's objectives.

---

### CC8 -- Change Management

**CC8.1** -- The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures.

**IAM relevance:** Access control changes go through change management, privileged access required for production changes

---

### CC9 -- Risk Mitigation

**CC9.1** -- Risk Mitigation Activities
**CC9.2** -- Third Party and Vendor Risk Management

**IAM relevance:** Third-party access controls, vendor access reviews, business associate/vendor risk assessments

---

## 3. SOC 2 Access Review Evidence Requirements

For CC6.3 and CC6.5, auditors typically require:

### Joiner Evidence
- Access request tickets with manager approval
- Provisioning logs showing access granted after approval
- User account creation timestamps matching onboarding dates

### Mover Evidence
- HR system role change records
- Access modification tickets aligned to role changes
- Removed access records for previous role entitlements

### Leaver Evidence
- Termination records from HR
- Deprovisioning logs showing account disabled/access removed
- SLA compliance evidence (typically same-day or within 24 hours for standard users, immediate for privileged users)
- Confirmation of privileged account removal

### Periodic Access Review Evidence
- Access certification campaign launch records
- Reviewer completion records with timestamps
- Access removals resulting from review findings
- Management sign-off on review completion

---

## 4. Privileged Access Requirements for SOC 2

SOC 2 auditors scrutinize privileged access heavily under CC6.1 and CC6.3:

- **Inventory:** Complete list of all privileged accounts and their owners
- **Justification:** Business justification documented for each privileged account
- **Approval:** Management approval documented for privileged access grants
- **Review frequency:** Privileged access reviews conducted more frequently than standard access (typically quarterly)
- **Session monitoring:** Privileged sessions logged and monitored
- **Just-in-time access:** Privileged access granted only when needed, revoked after use (preferred model)
- **Separation of duties:** Privileged accounts separated from standard accounts

---

## 5. SOC 2 and CyberArk Alignment

CyberArk Privilege Cloud directly addresses SOC 2 CC6.1 and CC6.3 requirements:

| SOC 2 Control | CyberArk Capability |
|---|---|
| CC6.1 -- Logical access security | Safe-based access control, dual control |
| CC6.1 -- Authentication | MFA enforcement, session isolation |
| CC6.2 -- Authorization before access | Approval workflows, access request process |
| CC6.3 -- Least privilege | Just-in-time access, time-limited sessions |
| CC6.3 -- Access reviews | Privileged access review reports |
| CC6.5 -- Access removal | Automated session termination, account deactivation |
| CC7.2 -- System monitoring | Session recording, keystroke logging |
| CC8.1 -- Change management | Dual control for sensitive operations |

---

## 6. SOC 2 vs Other Frameworks

| Aspect | SOC 2 | SOX ITGC | HIPAA | PCI DSS |
|---|---|---|---|---|
| Who it applies to | Service organizations | Public companies | Healthcare entities | Card data processors |
| Report type | Third-party audit report | Internal control assessment | Regulatory compliance | QSA assessment |
| Access review frequency | Defined by entity (annual minimum) | Typically annual | Periodic (quarterly recommended) | Every 6 months |
| Privileged access review | Quarterly recommended | Annual minimum | Periodic | Every 6 months |
| Audit trail retention | Per entity policy | 7 years | 6 years | 1 year minimum |

---

## 7. Common SOC 2 Deficiencies Related to Identity

Most common access control findings in SOC 2 audits:

1. **Untimely deprovisioning** -- terminated users retained access beyond SLA
2. **Incomplete access reviews** -- reviews not completed within required timeframe or missing evidence of action taken
3. **Excessive privileged access** -- users with admin rights without documented business justification
4. **Shared accounts** -- multiple users sharing a single account making audit trails unreliable
5. **Missing MFA** -- administrative or remote access without multi-factor authentication
6. **Orphaned accounts** -- accounts with no associated active user
7. **Missing joiner approval** -- access granted before documented manager approval
8. **Inadequate audit logging** -- insufficient log coverage or retention for privileged account activity
