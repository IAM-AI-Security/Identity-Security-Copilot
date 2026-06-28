# NIST SP 800-207: Zero Trust Architecture

**Document ID:** FWK-ZTA-001  
**Version:** 2.0  
**Last Updated:** 2026-06-26  
**Source:** NIST Special Publication 800-207, August 2020  
**Authors:** Scott Rose, Oliver Borchert (NIST), Stu Mitchell (Stu2Labs), Sean Connelly (CISA/DHS)  
**Classification:** Framework Summary -- Internal Knowledge Base  
**Official URL:** https://doi.org/10.6028/NIST.SP.800-207

---

## 1. Purpose and Scope

NIST SP 800-207 defines Zero Trust Architecture (ZTA) as an enterprise cybersecurity strategy designed to prevent data breaches and limit internal lateral movement. It is not a single product or technology but a set of guiding principles for workflow design, system architecture, and operational policy.

This document summarizes the key concepts, logical components, deployment models, threats, and migration guidance from NIST SP 800-207 and maps them to enterprise identity governance practice. It is intended to ground the Identity Governance RAG Assistant's responses on zero trust questions in authoritative NIST guidance.

---

## 2. Core Definition

**Zero Trust (ZT)** provides a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions in information systems and services in the face of a network viewed as compromised.

**Zero Trust Architecture (ZTA)** is an enterprise's cybersecurity plan that utilizes zero trust concepts and encompasses component relationships, workflow planning, and access policies.

**Zero Trust Enterprise** is the network infrastructure (physical and virtual) and operational policies that are in place for an enterprise as a product of a zero trust architecture plan.

The core shift: ZTA moves defenses from static, network-based perimeters to focus on users, assets, and resources. Network location alone no longer implies trust. Authentication and authorization are discrete functions performed before every session.

---

## 3. Zero Trust Tenets (Section 2.1)

NIST SP 800-207 defines seven foundational tenets. All seven must be addressed in a ZTA deployment:

**Tenet 1 -- All data sources and computing services are considered resources.**
A network is composed of multiple device classes. SaaS systems, IoT devices, storage, and compute are all resources. An enterprise may classify personally owned devices as resources if they access enterprise-owned resources.

**Tenet 2 -- All communication is secured regardless of network location.**
Network location alone does not imply trust. Access requests from assets on enterprise-owned infrastructure must meet the same security requirements as requests from any nonenterprise network. All communication must protect confidentiality, integrity, and provide source authentication.

**Tenet 3 -- Access to individual enterprise resources is granted on a per-session basis.**
Trust is evaluated before access is granted and applies only to that session. Authentication and authorization to one resource does not automatically grant access to a different resource. Least privilege applies at the session level.

**Tenet 4 -- Access is determined by dynamic policy.**
Policy evaluates the observable state of client identity, application or service, and requesting asset. This includes device characteristics, software versions, network location, time and date, previously observed behavior, and installed credentials. Behavioral and environmental attributes are incorporated. Least privilege principles restrict both visibility and accessibility.

**Tenet 5 -- The enterprise monitors and measures the integrity and security posture of all owned and associated assets.**
No asset is inherently trusted. A continuous diagnostics and mitigation (CDM) system or equivalent monitors device and application state. Assets discovered to be subverted, have known vulnerabilities, or are not managed by the enterprise may be denied access entirely.

**Tenet 6 -- All resource authentication and authorization are dynamic and strictly enforced before access is allowed.**
This is a constant cycle: obtain access, scan and assess threats, adapt, continually reevaluate trust. Multifactor authentication (MFA) is required for access to enterprise resources. Continual monitoring with possible reauthentication and reauthorization occurs throughout user transactions as defined by policy.

**Tenet 7 -- The enterprise collects as much information as possible about asset state, network infrastructure, and communications and uses it to improve security posture.**
Data about asset security posture, network traffic, and access requests is processed and used to refine policies and warn of possible attacks.

---

## 4. Zero Trust Network Assumptions (Section 2.2)

An enterprise implementing ZTA operates under these assumptions:

1. The entire enterprise private network is not an implicit trust zone. Assets must behave as if an attacker is present on the network at all times.
2. Devices on the network may not be owned or configurable by the enterprise (BYOD, contractors, visitors).
3. No resource is inherently trusted. Every asset's security posture must be evaluated via a Policy Enforcement Point before a request is granted.
4. Not all enterprise resources are on enterprise-owned infrastructure. Cloud services and remote resources are in scope.
5. Remote enterprise subjects and assets cannot fully trust their local network connection. All connections should be authenticated and authorized, all communications done in the most secure manner available.
6. Assets and workflows moving between enterprise and nonenterprise infrastructure must retain a consistent security policy and posture.

---

## 5. Logical Components of ZTA (Section 3)

### 5.1 Core Components

**Policy Engine (PE)**
The PE is responsible for the ultimate decision to grant access to a resource for a given subject. It uses enterprise policy and input from external sources (CDM systems, threat intelligence) as input to a trust algorithm to grant, deny, or revoke access. The PE makes and logs the decision; the Policy Administrator executes it.

**Policy Administrator (PA)**
The PA establishes and/or shuts down the communication path between a subject and a resource via commands to Policy Enforcement Points. It generates session-specific authentication tokens or credentials used by a client to access an enterprise resource. If the session is authorized, the PA configures the PEP to allow the session. If denied or revoked, the PA signals the PEP to shut down the connection.

**Policy Enforcement Point (PEP)**
The PEP enables, monitors, and eventually terminates connections between a subject and an enterprise resource. It communicates with the PA to forward requests and receive policy updates. The PEP may be a single logical component or two components: a client-side agent and a resource-side gateway.

Together the PE and PA form the Policy Decision Point (PDP). The ZTA logical components use a separate control plane to communicate while application data moves on a data plane.

### 5.2 Supporting Data Sources

The Policy Engine draws input from these sources when making access decisions:

| Data Source | Function |
| :--- | :--- |
| Continuous Diagnostics and Mitigation (CDM) system | Gathers enterprise asset state, software versions, patch level, and configuration compliance |
| Industry compliance system | Ensures the enterprise remains compliant with regulatory requirements (FISMA, HIPAA, PCI, SOX) |
| Threat intelligence feeds | Provides information about newly discovered attacks, malware, and vulnerabilities from internal or external sources |
| Network and system activity logs | Aggregates asset logs, network traffic, resource access actions, and events for real-time security posture feedback |
| Data access policies | Attributes, rules, and policies governing access to enterprise resources; the starting point for authorization |
| Enterprise PKI | Generates and logs certificates issued to resources, subjects, services, and applications |
| ID management system | Creates, stores, and manages enterprise user accounts and identity records including attributes, roles, and assigned assets |
| SIEM system | Collects security-centric information for analysis, policy refinement, and attack warning |

---

## 6. ZTA Deployment Approaches (Section 3.1)

NIST SP 800-207 identifies three primary ZTA implementation approaches. A full ZT solution includes elements of all three.

### 6.1 ZTA Using Enhanced Identity Governance

Identity is the key component of policy creation. Enterprise resource access policies are based on identity and assigned attributes. The primary requirement for resource access is based on access privileges granted to the subject. Other factors (device status, environmental context) may modify the confidence level.

This approach works well with cloud-based applications and SaaS offerings where the enterprise cannot deploy ZT security components. The enterprise uses subject identity to form and enforce policy on these platforms.

**Identity governance connection:** This is the approach most relevant to enterprise IAM programs. Identity governance standards, access certification campaigns, and NHI ownership requirements all feed the identity-driven policy model.

### 6.2 ZTA Using Micro-Segmentation

The enterprise places individual resources or resource groups on unique network segments protected by gateway security components (intelligent switches, next-generation firewalls, or special purpose gateways acting as PEPs). Each PEP dynamically grants access to individual requests.

This approach requires an identity governance program to function fully. The gateway PEP shields resources from unauthorized access and discovery.

### 6.3 ZTA Using Network Infrastructure and Software Defined Perimeters

Uses overlay network infrastructure to implement ZTA. The PA acts as a network controller that sets up and reconfigures the network based on PE decisions. Clients continue to request access via PEPs managed by the PA. Often implemented as an agent/gateway deployment at the application layer.

---

## 7. Deployed Architecture Variations (Section 3.2)

### 7.1 Device Agent/Gateway-Based Deployment

Each enterprise asset has an installed device agent. Each resource has a gateway placed directly in front acting as a proxy. The agent directs traffic to the appropriate PEP; the gateway communicates with the PA and allows only approved communication paths.

Flow: Subject requests resource → local agent captures request → forwarded to PA → PA forwards to PE for evaluation → if authorized, PA configures communication channel between agent and gateway via control plane → encrypted session begins → session terminated on completion or security event.

### 7.2 Enclave-Based Deployment

Gateway components reside at the boundary of a resource enclave (on-premises data center) rather than in front of individual resources. Useful for enterprises with legacy applications that cannot support individual gateways. The gateway protects a collection of resources and may not protect each resource individually.

### 7.3 Resource Portal-Based Deployment

The PEP is a single gateway portal for subject requests. No software component needs to be installed on client devices. More flexible for BYOD policies and inter-organizational collaboration. Limitation: limited continuous monitoring of assets between portal sessions.

### 7.4 Device Application Sandboxing

Vetted applications run compartmentalized on assets (virtual machines, containers). The goal is to protect applications from a possibly compromised host. The PEP refuses requests from applications not running in an approved sandbox. Enterprises must maintain sandboxed applications for all assets and ensure each sandboxed application is individually secured.

---

## 8. Trust Algorithm (Section 3.3)

The Trust Algorithm (TA) is the process used by the Policy Engine to grant or deny access to a resource. The PE takes input from five categories:

1. **Access request** -- the resource requested, requester information, OS version, software in use, patch level
2. **Subject database** -- who is requesting (human or process identity, attributes, roles, historical behavior)
3. **Asset database and observable status** -- known state of enterprise assets compared to the observed state at request time
4. **Resource requirements** -- minimum requirements for access, including authenticator assurance level, network location, data sensitivity
5. **Threat intelligence** -- external feeds and internal scans about active threats, malware, and attack signatures

### 8.1 Trust Algorithm Variations

**Criteria-based vs. Score-based:**
- Criteria-based: A set of qualified attributes that must all be met before access is granted. Binary per criterion.
- Score-based: Computes a confidence level from weighted data source values. Access granted if score exceeds a configured threshold. Allows partial access grants.

**Singular vs. Contextual:**
- Singular: Each request is evaluated independently. Faster but may miss attacks that stay within a subject's allowed role.
- Contextual: Takes subject or network agent's recent history into account. More likely to detect an attacker using subverted credentials exhibiting atypical access patterns. Requires the PE to maintain state on subjects.

A contextual, score-based TA provides the most dynamic and granular access control. This is the target model for mature ZTA deployments. Examples:
- An HR employee normally accesses 20-30 records per day. A contextual TA alerts if access suddenly exceeds 100 records per day.
- An accountant normally accesses financial systems during business hours. Attempting access from an unrecognized location at midnight triggers an alert and stricter authentication requirements.

---

## 9. Threats to ZTA (Section 5)

### 9.1 Subversion of ZTA Decision Process

The PE and PA are the most critical components. Any administrator with configuration access to PE rules can make unapproved changes or mistakes that disrupt operations. A compromised PA could allow access to resources that would otherwise be denied. Mitigation: PE and PA components must be properly configured, monitored, and all configuration changes must be logged and subject to audit.

### 9.2 Denial-of-Service or Network Disruption

If an attacker disrupts access to PEPs or the PE/PA (DoS or route hijack), enterprise operations are impacted. Mitigation: Host policy enforcement in a properly secured cloud environment or replicate across multiple locations for resiliency.

### 9.3 Stolen Credentials and Insider Threats

Even a properly implemented ZTA cannot prevent a compromised account or malicious insider from accessing resources the account is authorized to access. However, ZTA prevents lateral movement beyond the compromised account's authorized scope. A contextual trust algorithm can detect access patterns outside normal behavior and deny or limit access. Mitigation: MFA reduces risk; contextual TA detects anomalous behavior; JIT access limits standing privilege.

### 9.4 Visibility on the Network

Encrypted traffic may be opaque to layer 3 analysis tools. The enterprise can collect metadata (source and destination addresses, timing, device identity) about encrypted traffic and use machine learning to categorize traffic as valid or potentially malicious.

### 9.5 Storage of System and Network Information

Log data, network traffic metadata, and policy management tools become targets for attackers because they reveal access patterns and identify valuable accounts. These resources must be protected with the most restrictive access policies, accessible only from designated administrator accounts.

### 9.6 Reliance on Proprietary Data Formats or Solutions

ZTA relies on multiple data sources making access decisions. Proprietary APIs between components create vendor lock-in. If one provider has a security issue, migration may require extreme cost or long transition programs. Mitigation: Evaluate service providers on vendor security controls, switching costs, and supply chain risk in addition to performance.

### 9.7 Non-Person Entities (NPEs) in ZTA Administration

**This is the NHI and AI agent threat.** AI systems and automated software agents are being deployed to manage security on enterprise networks and must interact with ZTA management components (PE, PA). Two primary risks:

**False positives and false negatives:** Automated systems may mistakenly classify innocuous actions as attacks (false positive) or miss actual attacks (false negative). Mitigation: Regular retuning to correct mistaken decisions and improve decision quality.

**Attacker coercion of NPEs:** An attacker may be able to induce or coerce an NPE to perform a task the attacker is not privileged to perform. Software agents may have a lower authentication bar (API key versus MFA) than human users. If an attacker can interact with the agent, they could trick the agent into granting greater access or performing unauthorized tasks. An attacker gaining access to a software agent's credentials can impersonate the agent entirely.

**Governance implication:** This threat is why the enterprise AI agent governance standard requires:
- Conjur JWT authentication (not API keys) for all AI agents
- Dedicated, scoped execution roles per agent
- Deterministic execution gates that prevent agents from taking actions autonomously
- Human approval required for high-risk actions
- Mutual governance pattern where agents cannot modify each other's IAM permissions

---

## 10. ZTA Identity Governance Connection

ZTA's enhanced identity governance approach (Section 3.1.1) places identity as the primary policy driver. This directly requires mature identity governance programs. Specifically:

| ZTA Requirement | Identity Governance Control |
| :--- | :--- |
| Precise subject provisioning | IGA platform (SailPoint, Okta) managing joiner/mover/leaver |
| Subject attributes and access privileges | Role-based and attribute-based access models; access certification |
| Service account identification | NHI lifecycle standard; NHI inventory |
| MFA for resource access | Entra ID or Okta Conditional Access policies |
| Session-based access | JIT access via CyberArk Secure Cloud Access or PIM |
| Continuous monitoring | IAM Privilege Drift Agent; IAM Access Analyzer |
| AI agent identity | Conjur JWT authentication; dedicated execution roles; boundary SCPs |
| Audit logging | CloudTrail; CyberArk session recording; SIEM integration |

---

## 11. ZTA for Non-Human Identities

NIST SP 800-207 Section 5.7 explicitly addresses Non-Person Entities (NPEs) as both ZTA participants and a threat vector. Key governance requirements that flow from this section:

- NPEs (service accounts, workload identities, AI agents) must be uniquely identified and authenticated; shared or anonymous NPE credentials violate ZTA tenets
- NPE authentication should use the strongest available mechanism for the platform context (Kubernetes OIDC tokens, AWS IAM roles, Conjur JWT)
- NPE access must be scoped to the minimum required per-session, not standing broad permission
- NPE behavior must be monitored continuously; contextual anomalies (calls to APIs not previously accessed, unexpected volumes) trigger policy evaluation
- AI agents and automation with access to PE or PA management interfaces represent the highest-risk NPE category; human approval gates are required for any action that modifies access policy

---

## 12. Migrating to ZTA (Section 7)

ZTA migration is a journey, not a replacement. Most enterprises operate in a hybrid ZTA/perimeter-based mode for an indefinite period. The migration cycle follows the NIST Risk Management Framework steps.

### 12.1 Prerequisites Before ZTA Deployment

- Complete asset inventory (physical and virtual)
- Complete subject inventory (human and NPE, including service accounts)
- Business process review and data flow mapping
- Identity governance maturity (strong provisioning, access policies, ID management system)
- CDM or continuous monitoring capability

### 12.2 Migration Steps (Section 7.3)

**Step 1 -- Identify Actors on the Enterprise**
Catalog all human users and NPEs including service accounts. Users with special privileges (developers, administrators) require additional scrutiny. In legacy architectures these accounts often have blanket access; ZTA restricts them to least privilege with full audit logging.

**Step 2 -- Identify Assets Owned by the Enterprise**
Catalog hardware, software, digital certificates, user accounts, and cloud resources. Include configuration management and continuous monitoring capability. Shadow IT presents a particular risk: unknown enterprise-owned resources may not be included in network access policies.

**Step 3 -- Identify Key Processes and Evaluate Risks**
Rank business processes and data flows by mission importance. Start ZTA migration with lower-risk processes to gain experience before moving to critical ones. Cloud-based and remote-worker processes are often the best first candidates.

**Step 4 -- Formulate Policies for the ZTA Candidate**
For each candidate workflow, identify all upstream resources (ID management, databases, microservices), downstream resources (logging, monitoring), and all subjects and service accounts involved. Develop criteria-based or score-based trust algorithm configuration for each resource.

**Step 5 -- Identify Candidate Solutions**
Evaluate whether solutions require client-side agents, how they handle cloud vs. on-premises resources, logging capability, protocol breadth, and impact on user behavior.

**Step 6 -- Initial Deployment and Monitoring**
Begin in reporting-only or observation mode. Collect baseline access patterns. Enforce basic policies (MFA failures, known malicious IPs) immediately but allow more lenient access initially to gather behavioral data. Tune policies before strict enforcement.

**Step 7 -- Expanding the ZTA**
Once the initial workflow reaches steady operational state, plan the next candidate. Any significant change (new devices, major software updates, organizational shifts) requires reevaluation of ZTA policies for affected workflows.

---

## 13. ZTA and Related Federal Frameworks

| Framework | Relationship to ZTA |
| :--- | :--- |
| NIST Risk Management Framework (SP 800-37) | ZTA planning maps to RMF steps; ZTA deployment cycle aligns to Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor |
| NIST Privacy Framework | ZTA traffic inspection and logging must address privacy risks; informed consent and data minimization required |
| Federal ICAM Architecture | ZTA is heavily dependent on precise identity management; ICAM policy must be integrated with ZTA; aligns to OMB M-19-17 |
| Trusted Internet Connections 3.0 | TIC 3.0 updated to accommodate cloud and ZTA; TIC 3.0 PEP security capabilities directly support ZTA enforcement points |
| DHS CDM Program | CDM asset and user inventory programs are foundational prerequisites for ZTA deployment |
| NIST SP 800-53 Rev. 5 | ZTA controls map to AC-2, AC-6, IA-2, IA-3, IA-5, AU-2, AU-12, CA-7, SI-4, and the broader Access Control and Identification and Authentication control families |

---

## 14. Key ZTA Terms for Identity Governance RAG Retrieval

| Term | Definition per NIST SP 800-207 |
| :--- | :--- |
| Zero Trust (ZT) | Cybersecurity paradigm focused on resource protection where trust is never implicitly granted but must be continually evaluated |
| Zero Trust Architecture (ZTA) | Enterprise cybersecurity plan using ZT concepts encompassing component relationships, workflow planning, and access policies |
| Policy Engine (PE) | Component responsible for the ultimate access grant or deny decision for a given subject |
| Policy Administrator (PA) | Component that establishes or shuts down communication paths between subjects and resources by commanding PEPs |
| Policy Enforcement Point (PEP) | Component that enables, monitors, and terminates connections between subjects and enterprise resources |
| Policy Decision Point (PDP) | The combination of PE and PA that makes and executes access decisions |
| Trust Algorithm (TA) | The process used by the PE to grant or deny access based on multiple input sources |
| Non-Person Entity (NPE) | Any non-human subject that interacts with enterprise resources; includes service accounts, workload identities, AI agents |
| Implicit Trust Zone | Area where entities are trusted to at least the level of the last PDP/PEP gateway; ZTA minimizes this zone |
| Control Plane | Network used by PE, PA, and PEPs to communicate and manage access; logically separate from data plane |
| Data Plane | Network used for actual application and service communication between subjects and resources |
| Contextual Trust Algorithm | TA variant that considers subject's recent historical behavior in addition to the current request |
| Zero Standing Privilege (ZSP) | Target state where no identity holds persistent privileged access; all elevated access is per-session JIT |
| CDM | Continuous Diagnostics and Mitigation; provides real-time asset state to the PE for access decisions |

---

## 15. Example Questions This Document Answers

The following governance questions are answerable from this document for RAG retrieval:

- What is zero trust architecture?
- What are the seven tenets of zero trust per NIST?
- What is the difference between the Policy Engine and the Policy Administrator?
- What is a Policy Enforcement Point?
- How does zero trust handle non-human identities and AI agents?
- What are the risks of using automated agents in a ZTA environment?
- What is a contextual trust algorithm and why does it matter?
- What are the deployment models for ZTA?
- How does ZTA relate to least privilege?
- What are the threats to a ZTA deployment?
- How do you migrate an enterprise to zero trust?
- How does ZTA connect to NIST 800-53?
- What is the role of identity governance in zero trust?
- Why does ZTA require continuous monitoring?
- What is Zero Standing Privilege (ZSP)?

---

## 16. Source Citation

NIST Special Publication 800-207, "Zero Trust Architecture," Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly. National Institute of Standards and Technology, U.S. Department of Commerce. August 2020. Available free of charge at: https://doi.org/10.6028/NIST.SP.800-207

This document is not subject to copyright in the United States. Attribution to NIST is appreciated.

---

*This document is part of the Go Cloud Architects Identity Governance RAG Assistant knowledge base. It is a summary of NIST SP 800-207 (public domain) grounded in the full original text. See SOURCE_INDEX.md for the authoritative source citation and official URL.*
