# HIPAA Security Rule Reference
## Identity and Access Control Requirements

**Source:** NIST SP 800-66 Rev. 2 -- Implementing the HIPAA Security Rule (February 2024) and 45 CFR Part 164

---

## 1. Overview

The HIPAA Security Rule (45 CFR Part 164) establishes national standards to protect electronic protected health information (ePHI). It applies to covered entities (health plans, healthcare clearinghouses, healthcare providers) and their business associates.

The rule requires regulated entities to implement administrative, physical, and technical safeguards to ensure the confidentiality, integrity, and availability of ePHI.

---

## 2. Administrative Safeguards (45 CFR 164.308)

### Security Management Process (164.308(a)(1))
- Conduct accurate and thorough risk analysis of potential risks and vulnerabilities to ePHI
- Implement security measures to reduce risks to a reasonable and appropriate level
- Apply sanctions against workforce members who violate security policies
- Implement procedures to regularly review information system activity records

### Assigned Security Responsibility (164.308(a)(2))
- Designate a security official responsible for developing and implementing security policies and procedures

### Workforce Security (164.308(a)(3))
- Implement authorization and supervision procedures for workforce members who work with ePHI
- Implement procedures to determine access authorization
- Establish clearance procedures for workforce members requiring access to ePHI
- Implement procedures for terminating access when employment ends

### Information Access Management (164.308(a)(4))
- Implement policies for authorizing access to ePHI appropriate to the user's role
- Establish access establishment and modification procedures
- For covered entities using a healthcare clearinghouse: isolate clearinghouse functions from the larger organization

### Security Awareness and Training (164.308(a)(5))
- Train all workforce members on security policies and procedures
- Implement protection from malicious software procedures
- Implement login monitoring procedures
- Implement password management procedures

### Security Incident Procedures (164.308(a)(6))
- Implement procedures to identify and respond to suspected or known security incidents
- Mitigate harmful effects of security incidents to the extent practicable
- Document security incidents and their outcomes

### Contingency Plan (164.308(a)(7))
- Establish data backup plan to create retrievable exact copies of ePHI
- Establish disaster recovery plan
- Establish emergency mode operation plan
- Implement testing and revision procedures
- Assess relative criticality of specific applications and data

### Evaluation (164.308(a)(8))
- Perform periodic technical and non-technical evaluation of security policies and procedures

### Business Associate Contracts (164.308(b))
- Before permitting business associates to create, receive, maintain, or transmit ePHI, obtain satisfactory assurances they will appropriately safeguard the information
- Business associate agreements must require compliance with the Security Rule

---

## 3. Physical Safeguards (45 CFR 164.310)

### Facility Access Controls (164.310(a))
- Implement policies to limit physical access to electronic information systems
- Allow only authorized physical access
- Establish contingency operations procedures
- Implement facility security plans
- Implement access control and validation procedures
- Maintain maintenance records

### Workstation Use (164.310(b))
- Implement policies specifying proper functions for workstations accessing ePHI
- Define physical attributes of workstation surroundings

### Workstation Security (164.310(c))
- Implement physical safeguards for workstations that access ePHI

### Device and Media Controls (164.310(d))
- Implement policies governing receipt and removal of hardware and electronic media containing ePHI
- Implement procedures for disposal of ePHI and hardware
- Implement procedures for removal of ePHI from media before reuse
- Maintain accountability records for hardware and media movement
- Create retrievable exact copies of ePHI before equipment is moved

---

## 4. Technical Safeguards (45 CFR 164.312)

### Access Control (164.312(a)) -- REQUIRED
- **Unique User Identification (Required):** Assign unique name or number to each user for identifying and tracking user identity
- **Emergency Access Procedure (Required):** Establish procedures for obtaining necessary ePHI during emergencies
- **Automatic Logoff (Addressable):** Implement electronic procedures that terminate sessions after a predetermined period of inactivity
- **Encryption and Decryption (Addressable):** Implement mechanism to encrypt and decrypt ePHI

### Audit Controls (164.312(b)) -- REQUIRED
- Implement hardware, software, and procedural mechanisms that record and examine activity in information systems containing ePHI
- Audit logs must capture: login and logout events, access to ePHI, modifications to ePHI, failed access attempts

### Integrity (164.312(c))
- Implement policies and procedures to protect ePHI from improper alteration or destruction
- **Addressable:** Implement electronic mechanisms to corroborate that ePHI has not been altered or destroyed in an unauthorized manner

### Person or Entity Authentication (164.312(d)) -- REQUIRED
- Implement procedures to verify that a person or entity seeking access to ePHI is who they claim to be
- Authentication methods include: passwords, PINs, biometrics, smart cards, tokens

### Transmission Security (164.312(e))
- Implement technical security measures to guard against unauthorized access to ePHI transmitted over an electronic communications network
- **Addressable -- Encryption:** Implement a mechanism to encrypt ePHI in transit

---

## 5. Identity and Access Management Requirements Mapped to HIPAA

### User Provisioning
- Access must be authorized based on job function (minimum necessary standard)
- Access authorization must be documented
- Supervisory approval required before access is granted
- Workforce clearance procedures must be documented

### Access Reviews
- Periodic review of workforce access to ePHI is required
- Access must be terminated promptly when employment ends or role changes
- NIST SP 800-66r2 recommends quarterly access reviews for privileged accounts

### Privileged Access
- Privileged users must be individually identified with unique credentials
- Privileged access must be logged and audited
- Emergency access accounts (break glass) must have documented procedures
- All privileged access to ePHI must generate audit trails

### Authentication Requirements
- Unique user IDs required for all workforce members -- shared accounts are prohibited
- Strong authentication recommended for access to ePHI systems
- Multi-factor authentication strongly recommended for remote access and privileged accounts
- Automatic session timeouts required for unattended workstations

### Audit Logging
- All access to ePHI must be logged
- Audit logs must be protected from modification
- Log retention: minimum 6 years (45 CFR 164.316(b)(2)(i))
- Regular review of audit logs required as part of security management process

---

## 6. Breach Notification Requirements (45 CFR Part 164, Subpart D)

### Definition of Breach
A breach is an impermissible use or disclosure of unsecured ePHI that compromises the security or privacy of the information.

### Notification Timelines
- **Individuals:** Must be notified without unreasonable delay and within 60 days of discovery
- **HHS Secretary:** Must be notified within 60 days of end of calendar year for breaches affecting fewer than 500 individuals; within 60 days of discovery for breaches affecting 500 or more individuals
- **Media:** Prominent media notice required for breaches affecting more than 500 residents of a state or jurisdiction

### Business Associate Notification
- Business associates must notify covered entities without unreasonable delay and within 60 days of discovery of a breach

---

## 7. Business Associate Requirements

A business associate is any person or entity that performs functions or activities on behalf of or provides services to a covered entity involving the use or disclosure of ePHI.

### Required Business Associate Agreement Provisions
- Describe permitted uses and disclosures of ePHI
- Require business associate to implement appropriate safeguards
- Require business associate to report security incidents and breaches
- Require business associate to ensure subcontractors also comply
- Authorize covered entity to terminate contract if business associate violates material terms

### Cloud Service Providers
Cloud service providers that create, receive, maintain, or transmit ePHI on behalf of a covered entity are business associates and must execute a business associate agreement.

---

## 8. HIPAA and Identity Governance Alignment

| HIPAA Requirement | IAM Control |
|---|---|
| Unique user identification (164.312(a)(2)(i)) | Unique user accounts, no shared credentials |
| Access authorization (164.308(a)(4)) | Role-based access control, least privilege |
| Workforce clearance (164.308(a)(3)(ii)(B)) | Background checks, access request approval |
| Access termination (164.308(a)(3)(ii)(C)) | Automated deprovisioning on termination |
| Audit controls (164.312(b)) | SIEM logging, audit trail preservation |
| Person authentication (164.312(d)) | MFA, strong password policies |
| Automatic logoff (164.312(a)(2)(iii)) | Session timeout policies |
| Security awareness (164.308(a)(5)) | Security training programs |

---

## 9. NIST SP 800-66r2 Key Recommendations for Access Control

From the February 2024 NIST cybersecurity resource guide for implementing the HIPAA Security Rule:

- Implement role-based access control (RBAC) aligned to job functions
- Enforce least privilege -- users should have minimum access necessary
- Implement privileged access management for administrative accounts
- Use multi-factor authentication for all remote access to ePHI systems
- Conduct access reviews at minimum annually; quarterly for privileged accounts
- Automate deprovisioning to ensure access is removed within 24 hours of termination
- Maintain audit logs for minimum 6 years
- Encrypt ePHI at rest and in transit
- Implement data loss prevention controls for ePHI

---

## 10. Penalties for Non-Compliance

| Violation Category | Annual Penalty Cap |
|---|---|
| Did not know | $25,000 |
| Reasonable cause | $100,000 |
| Willful neglect, corrected | $250,000 |
| Willful neglect, not corrected | $1,500,000 |

Criminal penalties apply for intentional violations: up to $250,000 fine and 10 years imprisonment for offenses committed with intent to sell or use ePHI for commercial advantage.
