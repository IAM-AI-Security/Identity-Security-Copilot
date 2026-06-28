# 🛡️ Identity Security Copilot

> AI-assisted identity governance platform for enterprise IAM, PAM, and non-human identity teams. Answers governance questions, enforces policy guardrails, and provides architecture guidance grounded strictly in approved enterprise standards and never inventing policy.

---

## Demo

🎥 **[Watch the Demo Video](#)** ← add YouTube link after recording

![Identity Security Copilot](screenshots/demo.png)

---

## What This Is

Most RAG demos are "upload PDFs, ask questions." This is different.

The Identity Security Copilot is a domain-specific governance assistant built for identity security teams at financial services organizations. It answers questions the way a Principal Identity Security Architect would with citations, rationale, and business impact while enforcing the rule that AI assists and humans decide.

**It handles four types of questions:**

| Question Type | Example | Response Style |
|---|---|---|
| Policy & Governance | Can a contractor receive AdministratorAccess? | Recommendation + Why + Standards + Business Impact |
| Architecture & Design | How does HTML5 Gateway fit into CyberArk? | Component flow + trade-offs + migration considerations |
| Troubleshooting | CPM rotation is failing on a Windows domain account | Senior engineer diagnostic steps |
| Compliance & Audit | What evidence is needed for a SOX privileged access review? | Audit artifact checklist with citations |

---

## The Policy Violation Scenario

The strongest demonstration of the tool is what happens when a request violates policy:

> **"Melissa is a contractor customer service manager at Meridian Financial Group requesting permanent AdministratorAccess to the production AWS account. Is this allowed?"**

The assistant:
1. Cites Meridian's internal policy (MFG-IAM-001 §3.2) prohibiting contractor Tier 1 access
2. Cites NIST SP 800-53 AC-6 (Least Privilege) as the authoritative control
3. Explains the Zero Standing Privilege violation
4. Redirects to the authorized human reviewer
5. Never makes the access decision itself

This is governance AI done correctly.

---

## Architecture
**Key architectural decisions:**

- **Local embeddings** (sentence-transformers) no data leaves the machine during indexing
- **Bedrock Mantle** for LLM inference data stays within AWS, satisfies FFIEC data residency requirements for financial services
- **Conversation memory** sliding window of last 6 turns passed to the model; follow-up questions resolve naturally without re-querying
- **Query rewriting** before retrieval, a fast LLM call rewrites follow-up queries into standalone queries using conversation history (coreference resolution)
- **Strict grounding** the model is instructed to return a fallback message when the knowledge base has no relevant content; it never generates policy from training data

---

## Knowledge Base

44 documents · 326 indexed chunks · Last updated June 2026

### Meridian Financial Group (Mock Client Policies)
Fictional financial services company used as a demo client persona. Written in authentic corporate policy voice with real document IDs, approval chains, and regulatory cross-references.

| Document | Policy ID | Coverage |
|---|---|---|
| Privileged Access Management Policy | MFG-IAM-001 v3.2 | Contractor prohibitions, ZSP requirement, approval tiers, dormancy thresholds |
| Cloud Access Policy | MFG-CLD-001 v2.1 | AWS account inventory, JIT provisioning, SCP guardrails, CloudTrail requirements |
| Non-Human Identity Policy | MFG-NHI-001 v1.4 | NHI lifecycle, AI agent governance, mutual oversight pattern, owner departure SLAs |
| Identity Security Incident Response | MFG-INC-001 v2.0 | P1-P4 classification, hardcoded credential playbook, AI agent incident response |

### Enterprise Standards
Privileged Access Standard · Identity Governance Standard · Non-Human Identity Standard · Cloud Access Standard · Break-Glass Standard · Agent Security Standard

### Reference Architectures
PAM Reference Architecture · Enterprise IAM Reference Architecture · Zero Trust Identity Architecture · NHI Lifecycle Architecture · Workload Identity Architecture

### Regulatory Frameworks
NIST SP 800-53 Rev. 5 · NIST SP 800-207 (Zero Trust) · NIST AI RMF · SR 26-02 (Model Risk) · OWASP LLM Top 10 2025

### Vendor Documentation
CyberArk Privilege Cloud · CyberArk Conjur · AWS IAM Identity Center · Okta Lifecycle · Microsoft Entra ID Governance

### Audit Templates
SOX Evidence Template · PCI Access Review Template · Privileged Access Review Checklist · NHI Owner Attestation · Break-Glass Review Form

---

## Persona Modes

The assistant adapts its response format based on who is asking:

| Persona | Response Style | Best For |
|---|---|---|
| 🏛️ Architect | Architecture diagrams, component flows, trade-offs, migration considerations | Design reviews, solution architecture |
| ⚙️ Engineer | CLI commands, configuration steps, troubleshooting diagnostics | Implementation, operations |
| 📋 Auditor | Evidence checklists, control citations, compliance mappings | Audit preparation, evidence collection |
| 👔 Executive | One-paragraph summary, risk level, business impact, affected teams | CISO briefings, board reporting |

---

## AI Safety and Governance

This project is governed as an enterprise AI system, not a demo:

- **Answers grounded only in the knowledge base** the model cannot use training data to answer governance questions
- **AI assists, humans decide** the assistant never approves, denies, or grants access
- **Fallback enforcement** when no relevant policy exists, a standard fallback message is returned
- **Feedback logging** thumbs up/down feedback is logged to `feedback_log.jsonl` for model risk monitoring
- **Threat model** documented in `THREAT_MODEL.md` against OWASP LLM Top 10 and NIST AI RMF
- **Model risk** aligned to Federal Reserve SR 26-02 (effective April 17, 2026), documented in `MODEL_RISK.md`

---

## Technology Stack

| Layer | Technology | Rationale |
|---|---|---|
| Frontend | Streamlit | Rapid enterprise UI; supports multi-page apps |
| Embeddings | sentence-transformers all-MiniLM-L6-v2 | Local execution; no data egress during indexing |
| Vector Store | FAISS IndexFlatIP | Cosine similarity; deterministic; no external dependency |
| LLM | Mistral Large 3 (675B) | Via AWS Bedrock Mantle; data stays within AWS |
| Auth | AWS Secrets Manager + Bearer token | API key stored in Secrets Manager; never hardcoded |
| Infrastructure | AWS (us-east-1) | Satisfies FFIEC data residency for financial services |

---

## Governance Documentation

| Document | Purpose |
|---|---|
| `THREAT_MODEL.md` | Threats and mitigations mapped to OWASP LLM Top 10 and NIST AI RMF |
| `MODEL_RISK.md` | Model risk management aligned to SR 26-02 |
| `COMPLIANCE.md` | Control mapping across NIST 800-53, SOX, PCI DSS, OWASP |
| `BUSINESS_CASE.md` | Business case and value narrative |
| `SOURCE_INDEX.md` | Authoritative source index with official URLs |

---

## Roadmap

The following capabilities are planned for v2:

- **IAM Policy Analyzer** paste a JSON IAM policy, receive findings against least-privilege standards and a remediated version
- **Audit Evidence Generator** generate a ready-to-use SOX or PCI evidence package from a natural language request
- **Access Request Evaluator** submit an access request, receive a governance assessment against loaded policies
- **Semantic Chunking** section-boundary chunking for more consistent citations
- **Architecture Generator** generate full CyberArk or AWS IAM architecture specifications from a natural language prompt
- **Hybrid Search** BM25 keyword search combined with vector similarity for improved retrieval of exact policy terms

---

## Portfolio Context

This project is the governance layer for a three-part identity security AI portfolio:

| Project | Purpose |
|---|---|
| **Identity Security Copilot** (this repo) | Governance assistant and policy enforcement |
| **NHI Lifecycle Automation Agent** | Automated non-human identity lifecycle management |
| **IAM Privilege Drift Detection Agent** | Continuous detection and remediation of IAM privilege drift |

All three projects use AWS Bedrock Mantle for LLM inference and follow the same architectural pattern: deterministic gate, human-in-the-loop for high-risk actions, and audit logging to ServiceNow.

---

## About

**Go Cloud Architects**

📧 curtis@igasecurityconsulting.com
