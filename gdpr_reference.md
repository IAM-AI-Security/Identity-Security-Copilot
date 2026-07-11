# GDPR Reference -- Identity and Access Control Requirements
## General Data Protection Regulation (EU) 2016/679

**Source:** Regulation (EU) 2016/679 of the European Parliament and of the Council (April 27, 2016)

---

## 1. Overview

The General Data Protection Regulation (GDPR) applies to organizations that process personal data of individuals in the European Union, regardless of where the organization is located. It establishes rights for data subjects and obligations for controllers and processors.

**Key definitions:**
- **Personal data:** Any information relating to an identified or identifiable natural person
- **Processing:** Any operation performed on personal data
- **Controller:** Entity that determines the purposes and means of processing personal data
- **Processor:** Entity that processes personal data on behalf of a controller
- **Data subject:** The natural person whose personal data is being processed

---

## 2. Core Principles (Article 5)

Personal data must be:
1. **Lawfulness, fairness, transparency** -- processed lawfully, fairly, and transparently
2. **Purpose limitation** -- collected for specified, explicit, and legitimate purposes
3. **Data minimization** -- adequate, relevant, and limited to what is necessary
4. **Accuracy** -- accurate and kept up to date
5. **Storage limitation** -- kept no longer than necessary for the purpose
6. **Integrity and confidentiality** -- processed with appropriate security including protection against unauthorized access, loss, or destruction
7. **Accountability** -- controller is responsible for and must demonstrate compliance

---

## 3. Lawful Basis for Processing (Article 6)

Processing is lawful only if at least one of the following applies:
- Consent of the data subject
- Necessary for performance of a contract
- Necessary for compliance with a legal obligation
- Necessary to protect vital interests
- Necessary for a task carried out in the public interest
- Necessary for legitimate interests pursued by the controller or third party

---

## 4. Data Subject Rights

### Right of Access (Article 15)
- Data subjects have the right to obtain confirmation of whether personal data is being processed
- Right to receive a copy of personal data being processed
- Must be provided within one month of request

### Right to Rectification (Article 16)
- Data subjects have the right to have inaccurate personal data corrected without undue delay

### Right to Erasure / Right to be Forgotten (Article 17)
- Data subjects have the right to have personal data erased when:
  - Data is no longer necessary for the purpose it was collected
  - Consent is withdrawn and no other legal basis exists
  - Data subject objects and no overriding legitimate grounds exist
  - Data has been unlawfully processed
- **IAM implication:** Systems must support deprovisioning and data deletion workflows

### Right to Restriction of Processing (Article 18)
- Data subjects can request restriction of processing in certain circumstances

### Right to Data Portability (Article 20)
- Data subjects have the right to receive their personal data in a structured, commonly used, machine-readable format

### Right to Object (Article 21)
- Data subjects have the right to object to processing based on legitimate interests or for direct marketing

---

## 5. Controller and Processor Obligations

### Records of Processing Activities (Article 30)
Controllers must maintain records of processing activities including:
- Name and contact details of the controller
- Purposes of processing
- Categories of data subjects and personal data
- Categories of recipients
- Transfers to third countries
- Envisaged time limits for erasure
- Description of technical and organizational security measures

**IAM implication:** Identity lifecycle events -- provisioning, access changes, deprovisioning -- must be logged and retained as records of processing.

### Data Protection by Design and Default (Article 25)
- Implement appropriate technical and organizational measures to implement data protection principles effectively
- By default, only personal data necessary for each specific purpose is processed
- **IAM implication:** Least privilege access models and role-based access control directly satisfy this requirement

### Security of Processing (Article 32)
Controllers and processors must implement appropriate technical and organizational measures including:
- Pseudonymization and encryption of personal data
- Ability to ensure ongoing confidentiality, integrity, availability, and resilience of processing systems
- Ability to restore availability and access to personal data in a timely manner after an incident
- Process for regularly testing, assessing, and evaluating effectiveness of technical and organizational measures

**IAM controls that satisfy Article 32:**
- Encryption of personal data at rest and in transit
- Multi-factor authentication for access to personal data systems
- Role-based access control limiting access to personal data by job function
- Audit logging of all access to personal data
- Regular access reviews and certifications
- Automated deprovisioning when employment ends
- Privileged access management for administrative access to personal data systems

---

## 6. Breach Notification Requirements

### Notification to Supervisory Authority (Article 33)
- Controllers must notify the competent supervisory authority of a personal data breach without undue delay and where feasible within **72 hours** of becoming aware
- Notification must include: nature of the breach, categories and approximate number of data subjects, categories and approximate number of records, likely consequences, measures taken or proposed
- If notification is not made within 72 hours, reasons for delay must be provided

### Notification to Data Subjects (Article 34)
- When a breach is likely to result in high risk to rights and freedoms, the controller must communicate the breach to affected data subjects without undue delay
- Communication is not required if: data was encrypted, controller has taken measures ensuring high risk is unlikely to materialize, communication would involve disproportionate effort

---

## 7. International Data Transfers

### Transfers to Third Countries (Chapter V)
- Personal data may only be transferred outside the EU/EEA if adequate protection is ensured
- Adequacy decisions: transfers to countries the European Commission has determined provide adequate protection
- Appropriate safeguards: Standard Contractual Clauses (SCCs), Binding Corporate Rules
- **IAM implication:** Cloud providers processing EU personal data must have appropriate transfer mechanisms in place

---

## 8. Data Protection Officer (DPO) (Articles 37-39)

Organizations must appoint a DPO when:
- Processing is carried out by a public authority
- Core activities require large-scale regular and systematic monitoring of data subjects
- Core activities consist of large-scale processing of special categories of data

DPO responsibilities include:
- Informing and advising the controller/processor of GDPR obligations
- Monitoring compliance
- Acting as contact point for supervisory authority
- Cooperating with supervisory authority

---

## 9. GDPR and Identity Governance Alignment

| GDPR Requirement | IAM Control |
|---|---|
| Data minimization (Art. 5(1)(c)) | Least privilege access, attribute-based access control |
| Integrity and confidentiality (Art. 5(1)(f)) | Encryption, access controls, audit logging |
| Data protection by design (Art. 25) | Privacy-by-design in IAM architecture |
| Access control (Art. 32) | RBAC, MFA, privileged access management |
| Right of access (Art. 15) | Identity data inventory and reporting |
| Right to erasure (Art. 17) | Automated deprovisioning workflows |
| Records of processing (Art. 30) | Identity lifecycle audit trails |
| Breach notification 72hr (Art. 33) | Incident response with identity impact assessment |
| Data portability (Art. 20) | Exportable identity and access records |

---

## 10. Special Categories of Personal Data (Article 9)

Processing of the following categories is prohibited unless specific conditions are met:
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Biometric data for uniquely identifying natural persons
- Health data
- Sex life or sexual orientation data

**IAM implication:** Systems storing or processing special category data require enhanced access controls, strict least privilege, enhanced audit logging, and explicit lawful basis documentation.

---

## 11. Penalties for Non-Compliance (Article 83)

| Violation Type | Maximum Fine |
|---|---|
| Less severe violations | Up to EUR 10 million or 2% of global annual turnover |
| More severe violations | Up to EUR 20 million or 4% of global annual turnover |

More severe violations include violations of basic principles, data subject rights, transfers to third countries, and non-compliance with supervisory authority orders.

---

## 12. Key Differences from US Privacy Frameworks

| Aspect | GDPR | US Frameworks (HIPAA, CCPA) |
|---|---|---|
| Scope | Any organization processing EU resident data | Sector-specific or state-specific |
| Lawful basis | Required for all processing | Varies by framework |
| Data subject rights | Comprehensive including right to erasure | Limited, sector-specific |
| Breach notification | 72 hours to authority | 60 days (HIPAA), expedient (CCPA) |
| Penalties | Up to 4% global revenue | Fixed caps per violation |
| DPO requirement | Mandatory in certain cases | Not required |
