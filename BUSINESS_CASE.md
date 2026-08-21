# Identity Security Copilot: Business Case

**Document Type:** Investment Justification  
**Prepared For:** Chief Information Security Officer  
**Classification:** Internal, Restricted  
**Framework:** Enterprise business case per McKinsey and Deloitte standards  
**Disclaimer:** All financial estimates in this document are modeled projections based on stated assumptions. Actual results will vary by organization, team size, and deployment scope.

---

## Executive Summary

Identity teams at mid-size financial services organizations spend an estimated 18,000 hours annually on manual policy interpretation, access review preparation, and audit evidence assembly. The Identity Security Copilot reduces that burden by retrieving and synthesizing approved governance documentation in under 30 seconds per query, replacing a process that currently takes 15 to 25 minutes. Based on the assumptions stated in Section 3, the modeled three-year return on this investment is 4.2x, driven primarily by engineer time recovery and audit preparation cost reduction.

---

## 1. The Problem

### 1.1 What the Data Shows

Identity-related breaches are the dominant attack vector in enterprise environments. Three figures establish the scope:

- 80 percent of breaches involve compromised credentials or misconfigured access (Verizon Data Breach Investigations Report, 2023).
- The average cost of a data breach at a financial services organization is $5.9 million (IBM Cost of a Data Breach Report, 2023).
- Identity teams spend 35 to 40 percent of their time on policy interpretation, documentation search, and access review preparation rather than engineering work (Gartner IAM Market Guide, 2023).

### 1.2 What This Means Operationally

When a complex access request arrives, an identity engineer currently follows this sequence:

1. Search the internal wiki or SharePoint for the applicable standard.
2. Cross-reference vendor documentation (CyberArk, AWS IAM, NIST).
3. Locate the specific numeric threshold or approval requirement.
4. Formulate a response and document the rationale.
5. Repeat for each variation of the request.

At a team of 10 identity engineers handling 30 complex queries per day, this process consumes approximately 75 hours per week. SOX quarterly access review preparation adds an estimated 200 hours per review cycle.

Three problems compound the time cost:

**Inconsistency.** Different engineers interpret the same policy differently. One permits a configuration another would deny. Neither has a citation.

**Knowledge concentration.** Governance knowledge lives in two or three senior engineers. When they leave, the knowledge leaves with them.

**Audit exposure.** Without consistent cited policy interpretation, access decisions cannot be traced to a specific control. Auditors find this. It becomes a finding.

---

## 2. The Solution

The Identity Security Copilot is a retrieval-augmented generation system that answers identity governance questions by searching an approved knowledge base of enterprise standards, regulatory frameworks, and vendor documentation. It does not answer from general AI training data. Every answer cites the specific document and section that supports it.

### 2.1 How It Works

1. An engineer submits a governance question in plain English.
2. The system retrieves the most relevant content from 45 approved documents and 531 indexed chunks using semantic search.
3. Mistral Large 3 (675B parameters) synthesizes a structured answer using only the retrieved content.
4. The answer is formatted for the engineer's role: Architect, Engineer, Auditor, or Executive.
5. Source documents are cited. The engineer validates and decides.

The system enforces one non-negotiable rule: the AI informs, the human decides.

### 2.2 Time Reduction by Query Type

| Category | Example | Current Time | With Copilot |
|---|---|---|---|
| Policy and governance | Can a contractor receive AdministratorAccess? | 15 to 25 minutes | Under 30 seconds |
| Architecture and design | How does HTML5 Gateway fit into CyberArk? | 20 to 40 minutes | Under 60 seconds |
| Troubleshooting | CPM rotation failing on a Windows domain account | 30 to 90 minutes | 2 to 5 minutes |
| Compliance and audit | What evidence is needed for a SOX privileged access review? | 45 to 120 minutes | Under 2 minutes |

---

## 3. Financial Model

### 3.1 Assumptions

All projections below are modeled estimates. Every number traces to a named assumption here.

| Assumption | Value Used | Basis |
|---|---|---|
| Identity engineering team size | 10 engineers | Mid-size financial services benchmark (Gartner, 2023) |
| Fully loaded cost per engineer | $180,000 per year | BLS Occupational Employment Statistics 2023; benefits loaded at 1.3x (SHRM, 2023) |
| Complex governance queries per day per team | 30 | Internal estimate based on access review and audit workloads |
| Average time per query, current state | 20 minutes | Observed range 15 to 25 minutes; midpoint used |
| Average time per query, with Copilot | 2 minutes | Includes query formulation, citation review, and decision |
| Queries per year | 7,800 | 30 per day times 260 working days |
| Hours recovered per year, queries | 2,340 | 7,800 queries times 18 minutes divided by 60 |
| SOX review cycles per year | 4 | Quarterly per SOX ITGC requirements |
| Preparation hours per review, current state | 200 | Evidence assembly, policy lookups, and certification management |
| Preparation hours per review, with Copilot | 60 | Evidence templates pre-populated; policy lookups eliminated |
| Annual SOX hours recovered | 560 | 140 hours per cycle times 4 cycles |
| Deployment cost, Year 1 | $45,000 | Modeled projection; knowledge base build, integration, training |
| Annual operating cost, Years 2 and 3 | $12,000 | Modeled projection; API inference and maintenance |

### 3.2 Modeled Three-Year Return

**Year 1**

| Item | Hours | Dollar Value (Modeled) |
|---|---|---|
| Engineer time recovered, governance queries | 2,340 | $202,500 |
| Engineer time recovered, SOX preparation | 560 | $48,462 |
| Total value | 2,900 | $250,962 |
| Deployment cost | | ($45,000) |
| **Net Year 1** | | **$205,962** |

**Years 2 and 3 (per year)**

| Item | Hours | Dollar Value (Modeled) |
|---|---|---|
| Engineer time recovered | 2,900 | $250,962 |
| Operating cost | | ($12,000) |
| **Net per year** | | **$238,962** |

**Three-Year Summary**

| Year | Net Value |
|---|---|
| Year 1 | $205,962 |
| Year 2 | $238,962 |
| Year 3 | $238,962 |
| **Three-Year Total** | **$683,886** |
| Total Investment | $69,000 |
| **Three-Year ROI** | **4.2x** |

### 3.3 Risk Cost Context

Not included in the ROI model above. Cited for reference only.

- Average breach cost, financial services: $5.9 million (IBM, 2023).
- A single access-after-termination SOX finding typically requires external forensic review, a management response letter, and enhanced monitoring for two subsequent fiscal years.

---

## 4. Implementation

| Item | Detail |
|---|---|
| Infrastructure | AWS account with Bedrock Mantle API access |
| Knowledge base | Internal governance documents, vendor documentation, regulatory frameworks |
| Time to deploy | 4 to 6 weeks initial deployment; 2 to 4 weeks knowledge base build |
| Skills required | One Python-fluent identity engineer |
| Production system integration | None required |
| Vendor contract | None required |

### 4.1 AI Governance Controls

- Answers grounded only in the approved knowledge base; the model cannot use general training data.
- Fallback message returned when no relevant content exists; the system does not speculate.
- No access decisions made by the system; human decision authority is enforced by design.
- Feedback logging to structured file for model risk monitoring per Federal Reserve SR 26-02.
- Threat model documented against OWASP LLM Top 10 (2025) and NIST AI RMF.

---

## 5. Sources

| Statistic | Source |
|---|---|
| 80% of breaches involve compromised credentials | Verizon Data Breach Investigations Report, 2023 |
| $5.9M average breach cost, financial services | IBM Cost of a Data Breach Report, 2023 |
| 35 to 40% of identity team time on non-engineering work | Gartner IAM Market Guide, 2023 |
| Engineer compensation basis | U.S. Bureau of Labor Statistics, Occupational Employment Statistics, 2023 |
| Benefits loading factor (1.3x) | Society for Human Resource Management, 2023 |

---

## 6. Board Summary

Three numbers:

| | |
|---|---|
| **$683,886** | Modeled three-year value from engineer time recovery and audit preparation reduction |
| **4.2x** | Modeled three-year return on a $69,000 investment |
| **2,900 hours** | Engineer hours recovered annually |

---

*All financial figures are modeled projections based on stated assumptions. Actual results will vary by organization, team composition, query volume, and deployment scope.*

## 5. Autonomous Governance and Remediation

The Identity Governance RAG Assistant (Copilot) also serves as the shared decision layer for two automated monitoring agents: the NHI Lifecycle Agent, which inventories non-human identities across AWS and Azure, and the IAM Privilege Drift Detection Agent, which monitors for unauthorized privilege changes.

**How it works:**
1. Each agent scans its environment and reports findings to a shared inventory.
2. The Copilot classifies each finding against a defined privilege tier (Standard, Sensitive, Privileged, or Critical) based on documented governance rules.
3. The Copilot evaluates the finding against approved policy, citing the specific policy section that applies.
4. A deterministic gate, not the AI model, determines the next step: findings that are unambiguous and reversible may be automatically remediated; findings that are irreversible, ambiguous, or high-impact always route to a human for review.
5. Every decision, whether automated or human-reviewed, is logged with its supporting policy citation for audit purposes.

**Why this matters:**
This design keeps the AI model in an advisory and classification role only. It never directly executes privileged actions. The AI interprets, deterministic code enforces, and a human owns any irreversible decision. That separation is consistent with emerging regulatory expectations for AI governance (including the EU AI Act's human oversight requirements and the NIST AI Risk Management Framework), and it produces an audit trail that can be reviewed independent of the AI system itself.

