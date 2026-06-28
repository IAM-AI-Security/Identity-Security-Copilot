# Meridian Financial Group
## Non-Human Identity and Machine Identity Policy
**Policy ID:** MFG-NHI-001  
**Version:** 1.4  
**Effective Date:** January 1, 2026  
**Next Review:** January 1, 2027  
**Policy Owner:** Chief Information Security Officer  
**Maintained By:** Identity Security Architecture  
**Classification:** Internal — Restricted  
**Regulatory Alignment:** SOX ITGC, FFIEC, PCI DSS v4.0, NIST SP 800-53, SR 26-02

---

## 1. Purpose and Scope

This policy governs the lifecycle of all non-human identities (NHIs) at Meridian Financial Group. NHIs include service accounts, application identities, API keys, OAuth clients, certificates, AI agent execution roles, and any other programmatic identity used by automated systems to authenticate and access Meridian resources.

NHIs now outnumber human identities at Meridian by approximately 85 to 1. This policy ensures every NHI is owned, scoped, monitored, and lifecycle-managed with the same rigor applied to human privileged access.

---

## 2. NHI Classification

| Tier | Type | Examples | Credential Standard |
| :--- | :--- | :--- | :--- |
| Tier 1 — Critical | NHIs with access to regulated data, financial systems, or security controls | Core banking API service account, Payment processing identity, SIEM integration account | Conjur dynamic secrets; zero static credentials |
| Tier 2 — Elevated | NHIs with production write access; limited scope | Application deployment service accounts, CI/CD pipeline identities | Conjur JWT or IRSA; 90-day rotation maximum |
| Tier 3 — Standard | NHIs with read-only or non-production access | Monitoring integrations, dev/test service accounts | Conjur or Secrets Manager; 90-day rotation |
| AI Agent | Autonomous AI execution roles | NHI Lifecycle Agent, IAM Drift Detection Agent, RAG Assistant | Conjur JWT; dedicated execution role; mutual governance |

---

## 3. Ownership Requirements

Every NHI at Meridian must have:
- A named human owner (a current Meridian employee, not a contractor)
- A designated backup owner
- A documented business purpose
- A provisioned-by record (which team and which change ticket)
- An expected decommission date or review date

NHIs without a named owner are classified as orphans. Orphan NHIs are disabled within 7 days of discovery and decommissioned within 30 days unless a new owner is assigned through the standard provisioning process.

**Owner departure:** When an NHI owner departs Meridian:
- Day 1: Identity Security team receives automated notification from HR system
- Day 7: NHI must be reassigned to the departing owner's manager or a designated successor
- Day 7 (if no reassignment): NHI is automatically disabled
- Day 30 (if still unresolved): NHI is decommissioned and credentials permanently invalidated

---

## 4. Credential Requirements

### 4.1 Approved Credential Types (in order of preference)

| Tier | Preferred Method | Acceptable Alternative | Prohibited |
| :--- | :--- | :--- | :--- |
| AWS workloads | IAM execution role (IRSA, Lambda role, ECS task role) | Conjur JWT | Static access keys |
| Azure workloads | Managed Identity | Conjur JWT | Client secret in config |
| Kubernetes | IRSA + service account token | Conjur Secrets Provider | Kubernetes Secrets (unencrypted) |
| CI/CD pipelines | OIDC JWT (GitHub Actions, GitLab) | Conjur JWT | Repository secrets (static) |
| AI agents | Conjur JWT via platform authenticator | — | Any static credential |
| On-premises | Conjur JWT | CyberArk CPM-managed password | Hardcoded password |

### 4.2 Rotation Requirements

| Credential Type | Maximum Rotation Interval | Method |
| :--- | :--- | :--- |
| Service account passwords | 90 days | CyberArk CPM automated |
| API keys (internal) | 90 days | Conjur rotation policy |
| OAuth client secrets | 90 days | Automated via identity platform |
| TLS/mTLS certificates | 1 year (renew at 30 days prior) | CyberArk Certificate Manager |
| Dynamic Conjur secrets | Per TTL at issuance (max 24 hours) | Automatic at TTL expiry |
| AI agent JWTs | Per execution (TTL ≤ 1 hour) | Automatic per Conjur authn-jwt |

**Hardcoded credentials** (passwords, API keys, tokens in source code, container images, or environment variables) are prohibited and constitute a Critical finding. Discovery triggers immediate revocation, incident investigation, and mandatory code remediation within the same business day.

---

## 5. AI Agent Identity Requirements

AI agents deployed at Meridian are subject to all NHI requirements plus the following additional controls:

### 5.1 Execution Role Design
- Every AI agent has a dedicated named execution role: `agt-<agent-name>-<environment>`
- Execution roles are scoped to the minimum API operations required for the agent's documented function
- AdministratorAccess or equivalent is prohibited for all agent execution roles
- A permission boundary SCP enforces the maximum permissions the role can ever hold

### 5.2 Mutual Governance
Meridian's AI agent architecture implements mutual governance:
- The NHI Lifecycle Automation Agent monitors the IAM Privilege Drift Detection Agent's execution role
- The IAM Privilege Drift Detection Agent monitors the NHI Lifecycle Automation Agent's execution role
- Neither agent holds write permissions on its own execution role
- Changes to either agent's execution role require human approval through the standard IAM change process

### 5.3 Deterministic Gate Requirement
AI agents that perform remediation actions must implement a deterministic execution gate:
- The language model classifies findings and recommends actions
- Deterministic Python code validates the recommendation against the agent's authorized action set
- HIGH and CRITICAL actions route to human approval in ServiceNow before execution
- The LLM does not call cloud APIs directly

### 5.4 Human-in-the-Loop Requirements
The following agent actions always require human approval regardless of severity:
- Disabling or deleting any IAM identity
- Revoking privileged access
- Any action in a production account that was not explicitly pre-approved
- Any action that modifies IAM policies, trust relationships, or permission boundaries

---

## 6. Lifecycle Management

### 6.1 Provisioning
NHI provisioning requires:
1. ServiceNow request with business justification, owner, expected lifetime, and data classification
2. Manager approval
3. Identity Security Architecture review for Tier 1 NHIs
4. CISO approval for AI agent production deployment
5. Conjur policy entry or IAM role creation per approved request
6. NHI registered in Meridian's NHI inventory (maintained in DynamoDB by the NHI Lifecycle Automation Agent)

### 6.2 Ongoing Monitoring
- NHI Lifecycle Automation Agent scans all AWS IAM service accounts and Azure service principals daily
- Findings classified by risk level using Mistral Large 3 via AWS Bedrock Mantle with compliance context injected per inference
- CRITICAL findings (unused >180 days, AdministratorAccess, key age >365 days) auto-remediate: access key disabled, ServiceNow P1 ticket created
- HIGH and MEDIUM findings generate ServiceNow tickets for human review

### 6.3 Dormancy Thresholds

| NHI Type | Dormancy Threshold | Action |
| :--- | :--- | :--- |
| Tier 1 NHI | 90 days no activity | Automatic disable; P1 ServiceNow ticket |
| Tier 2 NHI | 180 days no activity | Automatic disable; P2 ServiceNow ticket |
| AI agent execution role | 30 days no execution | Flag for owner review; P3 ticket |
| CI/CD pipeline identity | 90 days no pipeline run | Automatic disable |
| OAuth client | 90 days no token issuance | Notification to owner; disable at 120 days |

### 6.4 Decommissioning
When an NHI is decommissioned:
1. All associated credentials are revoked and deleted
2. IAM role or service account is deleted (not just disabled)
3. Conjur policy entries are removed
4. NHI inventory record is closed with decommission date and requestor
5. Audit logs retained per MFG retention schedule (7 years for regulated systems)

---

## 7. Access Review

NHI access reviews are conducted on the following schedule:

| NHI Tier | Review Frequency | Reviewer | Evidence Required |
| :--- | :--- | :--- | :--- |
| Tier 1 | Quarterly | NHI owner + Identity Security team | Owner attestation + last-used data |
| Tier 2 | Semi-annual | NHI owner | Owner attestation |
| AI Agents | Quarterly | Agent owner + Identity Security Architecture | Execution role review + authorized tool set review |
| All NHIs | Annual | Identity Security Architecture | Full inventory reconciliation |

Review evidence is retained in ServiceNow for 7 years.

---

## 8. Compliance Mapping

| Control | SOX ITGC | NIST SP 800-53 | PCI DSS v4.0 | SR 26-02 |
| :--- | :--- | :--- | :--- | :--- |
| NHI inventory and ownership | CC6.1 | AC-2, IA-9 | Req 8.6.1 | Model inventory |
| Credential rotation | CC6.1 | IA-5(1) | Req 8.3.9 | — |
| Orphan detection | CC6.1 | AC-2(3) | Req 8.2.6 | — |
| AI agent deterministic gate | CC5.2 | AC-3, AC-6 | — | Section III governance |
| Human-in-the-loop for remediation | CC7.3 | AC-5, AU-6 | — | Section V human oversight |
| Mutual governance pattern | CC5.2 | AC-5, AC-6(9) | — | Section VI SoD |
| NHI access review | CC5.2 | AC-2(7) | Req 8.6.3 | Section V ongoing monitoring |

---

*Meridian Financial Group — Internal Policy Document. Not for external distribution. Questions: identity-security@meridianfinancial.com*
