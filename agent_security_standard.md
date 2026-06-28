# AI Agent Identity Security Standard

**Document ID:** STD-AGT-001  
**Version:** 1.0  
**Last Updated:** 2026-06-26  
**Owner:** Identity Security Architecture  
**Classification:** Internal — Governance  
**Review Cycle:** Annual  

---

## 1. Purpose

This standard defines the minimum security requirements for all AI agents operating within the enterprise. AI agents -- including LLM-orchestrated agents, robotic process automation (RPA), agentic workflows, and multi-agent systems -- represent a new and rapidly growing identity class that introduces unique risks not fully addressed by traditional identity governance standards.

Unlike human users or conventional service accounts, AI agents operate autonomously, make dynamic decisions, invoke tools and APIs without direct human interaction at execution time, and can take sequences of actions with compounding effects. A misconfigured or compromised AI agent with broad permissions can cause damage at a scale and speed that no human attacker can match.

This standard closes the governance gap by applying identity security principles -- least privilege, credential hygiene, human oversight, and continuous monitoring -- specifically to the AI agent execution context.

---

## 2. Scope

This standard applies to all AI agents owned, operated, or deployed by the enterprise, including:

- LLM-orchestrated agents (LangChain, Semantic Kernel, CrewAI, AWS Strands, custom frameworks)
- Robotic Process Automation (RPA) bots that invoke APIs or access enterprise systems
- Autonomous AI workflows triggered by events, schedules, or other agents
- Multi-agent systems where one agent orchestrates or delegates to other agents
- AI agents integrated with Model Context Protocol (MCP) servers
- AI agents accessing AWS Bedrock, Azure OpenAI, or other cloud AI services
- The NHI Lifecycle Automation Agent and IAM Privilege Drift Detection Agent in this portfolio

This standard applies regardless of the agent framework, deployment platform (Lambda, ECS, Kubernetes, EC2), or AI model provider.

This standard does not apply to static automation scripts, deterministic rule-based processes, or scheduled batch jobs that do not use a language model for decision-making.

---

## 3. Definitions

| Term | Definition |
| :--- | :--- |
| AI Agent | An autonomous or semi-autonomous software system that uses a language model to perceive inputs, reason, make decisions, and take actions via tool calls or API invocations |
| Agentic Workflow | A sequence of AI agent actions, potentially involving multiple tool calls, API requests, and decision branches executed without continuous human interaction |
| Execution Role | The IAM role, service account, or identity credential used by an agent at runtime to authenticate and authorize its actions against enterprise systems |
| Tool | A function, API endpoint, or capability that an agent is authorized to invoke (e.g., read S3 bucket, query database, create ServiceNow ticket) |
| Deterministic Gate | A hardcoded, non-AI enforcement control that bounds the actions an agent may take, regardless of the LLM's output |
| Human-in-the-Loop | A required human review and approval step before an agent executes a high-risk or irreversible action |
| Prompt Injection | An attack in which malicious content in the agent's input or tool output manipulates the LLM into taking unauthorized actions |
| Excessive Agency | The OWASP LLM06 vulnerability class where an agent is granted more functionality, permissions, or autonomy than required for its documented purpose |
| Mutual Governance | An architecture pattern where agent A governs agent B's execution role and agent B governs agent A's execution role; neither can unilaterally escalate its own privilege |
| ZSP | Zero Standing Privilege -- an architecture posture where agents hold no persistent credentials between task executions |
| MCP | Model Context Protocol -- an open protocol that standardizes how AI agents connect to tools and data sources |

---

## 4. Guiding Principles

**4.1 Agents Are NHIs and Must Be Governed as Such**
Every AI agent is a non-human identity. It must have a named human owner, a documented purpose, a scoped execution role, and a credential that rotates or expires. The NHI Lifecycle Standard (STD-NHI-001) applies to all agents. This standard adds agent-specific requirements on top of that foundation.

**4.2 LLMs Classify -- They Do Not Execute**
The language model's role is to reason and classify findings. Execution of actions against enterprise systems must occur through deterministic Python or infrastructure code that the LLM informs but does not directly control. This is the deterministic gate pattern. An LLM output saying "delete this IAM role" does not delete the role -- the Python execution layer validates the classification, checks it against allowed actions, and decides whether to proceed.

**4.3 Least Privilege at the Tool Level**
Agent execution roles are scoped to the exact API operations and resource paths required to perform the agent's documented function. An agent that reads IAM findings has read-only IAM permissions. An agent that creates ServiceNow tickets has ServiceNow create-ticket permissions only. Wildcard permissions and administrative roles are prohibited.

**4.4 Zero Stored Credentials Between Executions**
Agents must not cache, store, or persist credentials between task executions. Every execution begins with a fresh authentication event. Static API keys or passwords in agent code, environment variables, or configuration files are prohibited.

**4.5 Human Oversight Is Non-Negotiable for High-Risk Actions**
Agents may classify, recommend, and prepare actions. For actions classified as HIGH or CRITICAL severity, a human must review and approve before execution. Agents do not self-authorize destructive, irreversible, or privileged actions.

**4.6 Every Agent Action Is Auditable**
Every tool call, API invocation, classification decision, and remediation action taken by an agent must be logged with the agent's identity, timestamp, input context, and output. This audit trail is a compliance requirement, not an option.

**4.7 Agents Cannot Govern Themselves**
No agent may hold permissions to modify its own execution role, its own IAM policy, or its own Conjur secrets policy. Self-governance creates an uncontrolled privilege escalation path. The mutual governance pattern enforces this at the architecture level.

---

## 5. Agent Identity and Credential Requirements

### 5.1 Execution Role

Every agent must operate under a dedicated, named execution role. Role naming convention: `agt-<agent-name>-<environment>` (e.g., `agt-nhi-scanner-prod`, `agt-drift-detector-prod`).

| Requirement | Standard |
| :--- | :--- |
| Dedicated role | One execution role per agent type; shared roles across functionally different agents are prohibited |
| Naming convention | `agt-<name>-<env>` for all agent roles |
| Least privilege | Role grants only the specific API actions required; wildcard permissions prohibited |
| Permission boundary | AWS Service Control Policy (SCP) or Azure Policy defines the maximum permissions the role can ever assume, even if the role policy is later misconfigured |
| No standing admin | Administrator, Owner, or equivalent roles are prohibited for any agent execution role |
| Cross-account access | Read-only unless explicitly approved; write access across accounts requires documented exception |

### 5.2 Authentication -- Preferred to Prohibited

| Tier | Method | Requirement |
| :--- | :--- | :--- |
| Tier 1 -- Preferred | AWS IAM role via IRSA / Lambda execution role / ECS task role | Use wherever the agent runs on AWS-native compute; no credential storage required |
| Tier 1 -- Preferred | CyberArk Conjur JWT (authn-jwt authenticator) | Required for agents that need to retrieve secrets for downstream tool calls; short-lived JWT, TTL ≤ 1 hour |
| Tier 2 -- Acceptable | Azure Managed Identity | For agents running on Azure compute |
| Tier 2 -- Acceptable | Kubernetes OIDC / workload identity | For agents running as Kubernetes pods |
| Tier 3 -- Exception | Static secret in AWS Secrets Manager with rotation | Requires documented exception; 90-day rotation enforced |
| Tier 4 -- Prohibited | Hardcoded API key, password, or token in code or environment variables | Never permitted; critical finding if discovered |

### 5.3 Conjur JWT Authentication Flow for Agents

When an agent requires secrets to call downstream APIs, it authenticates to CyberArk Conjur as follows:

1. The agent runtime platform (Lambda, Kubernetes, EC2) provides a platform-issued JWT as the agent's identity proof
2. The agent calls the Conjur `authn-jwt` endpoint, presenting the platform JWT
3. Conjur validates the JWT signature against the configured JWKS endpoint
4. Conjur evaluates the policy to determine which secrets the authenticated agent identity may retrieve
5. Conjur issues a short-lived Conjur access token (TTL ≤ 8 minutes)
6. The agent uses the Conjur token to retrieve the specific secret needed for the current task
7. The Conjur token expires; the agent must re-authenticate for subsequent tasks

No static credential is ever present in the agent runtime environment. Every secret retrieval is individually logged.

### 5.4 Credential Prohibition

The following are prohibited for all agents in all environments:

- Hardcoded API keys, passwords, or tokens in source code
- Secrets in environment variables passed to agent containers or Lambda functions
- Secrets in agent system prompts or LLM context windows
- Credentials stored between executions in agent memory, cache, or state
- Shared credentials used by multiple agent instances or agent types
- Long-lived access keys (AWS IAM access keys) for agent execution

---

## 6. Least Privilege and Tool Governance

### 6.1 Authorized Tool Set

Every agent must have a documented authorized tool set -- the explicit list of APIs, functions, databases, and external services the agent is permitted to call. Tools not on the authorized list must not be available to the agent at runtime.

The authorized tool set is defined at agent provisioning time, reviewed quarterly, and updated only through the standard change management process. Addition of new tools requires owner approval and Identity Security team review.

**Per OWASP LLM06 (Excessive Agency):** Excessive functionality is a root cause of Excessive Agency. Agents must be configured with only the minimum extensions and tools needed. An agent that needs to read emails must not be given an extension that also sends emails. Tool scope is enforced at the integration layer, not by trusting the LLM to self-restrict.

### 6.2 Permission Scope per Tool

For each tool in the authorized set, permissions must be scoped to the minimum required operation:

| Tool Type | Permitted Scope | Prohibited |
| :--- | :--- | :--- |
| AWS IAM read | `iam:Get*`, `iam:List*` on specific accounts | `iam:*`, `iam:CreateRole`, `iam:AttachPolicy` |
| S3 access | `s3:GetObject` on specific bucket ARN | `s3:*`, `s3:DeleteObject`, `s3:PutBucketPolicy` |
| ServiceNow | Create incident, update incident | Delete record, modify user, change RBAC |
| Database | SELECT on specific tables | INSERT, UPDATE, DELETE, DROP |
| Secrets retrieval | Specific Conjur variable paths | Conjur policy modification |
| Cloud console | Read-only role for specific services | Any write or administrative role |

### 6.3 Rate Limiting

All agent tool invocations are subject to rate limits to contain runaway or compromised agent behavior. Rate limits are enforced at the API gateway or tool integration layer, not trusted to the agent to self-enforce.

Default rate limits (configurable per agent):
- Maximum 100 API calls per minute per agent instance
- Maximum 10 write operations per minute per agent instance
- Maximum 5 cross-account operations per hour per agent instance

Breaching rate limits triggers an automated alert to the Identity Security team and the agent owner.

---

## 7. Deterministic Execution Gate Pattern

The deterministic gate is the most important architectural control for AI agent security. It is mandatory for all agents that take remediation or write actions.

### 7.1 How It Works

```
Input Event (e.g., IAM finding, NHI scan result)
        ↓
Agent receives input and formats context
        ↓
LLM classifies the finding:
  - Severity: CRITICAL / HIGH / MEDIUM / LOW
  - Finding type: dormant account / excessive permission / orphan NHI / etc.
  - Recommended action: disable / revoke / notify / escalate
        ↓
DETERMINISTIC GATE (Python code -- not LLM):
  - Validates LLM output is within expected classification schema
  - Checks severity against action permission matrix
  - Checks action against agent's authorized tool set
  - Checks rate limits
  - For CRITICAL/HIGH: routes to human approval queue (ServiceNow ticket)
  - For AUTO-REMEDIATE: executes only if severity and action both match pre-approved rules
        ↓
Human reviews ticket (CRITICAL/HIGH) OR
Auto-remediation executes (approved LOW/MEDIUM patterns only)
        ↓
All outcomes logged to CloudTrail + SIEM with agent identity context
```

### 7.2 What the LLM May and May Not Do

| LLM May | LLM May Not |
| :--- | :--- |
| Classify a finding by severity | Execute API calls directly |
| Recommend an action | Approve its own recommended actions |
| Generate a ticket description | Modify its own execution role or permissions |
| Summarize governance context from RAG | Access secrets outside its authorized Conjur policy |
| Identify which standard section applies | Bypass the deterministic gate |
| Determine if a finding needs human review | Determine that human review is not needed for a HIGH finding |

### 7.3 Auto-Remediation Approved Patterns

Only the following patterns may be auto-remediated without human approval. All other actions require human review:

| Finding | Auto-Remediation Action | Condition |
| :--- | :--- | :--- |
| Unused IAM access key > 180 days | Disable access key | Severity CRITICAL per remediation rules |
| Unused IAM access key 90-180 days | Send notification to owner | Severity HIGH, notify only |
| NHI with no activity > 90 days | Add tag for human review; open ServiceNow P3 | Severity MEDIUM |
| Missing required resource tag | Apply standard tag | LOW, no access impact |

Any action not in this table requires human approval via ServiceNow before execution.

---

## 8. Human-in-the-Loop Requirements

Human oversight is required before agent execution for the following action categories. This requirement is non-negotiable and cannot be overridden by agent configuration or LLM output.

| Action Category | Approval Required | Approver |
| :--- | :--- | :--- |
| Disable or delete any IAM identity | Human review | Agent owner + Identity Security team |
| Revoke privileged access | Human review | Agent owner + CISO notification |
| Modify IAM policies or permission boundaries | Human review | Identity Security Architecture |
| Delete or decommission any NHI | Human review | NHI owner + Identity Security team |
| Execute in production environment for first time | Human sign-off | Agent owner + Identity Security team |
| Any action on break-glass or emergency accounts | Human review | CISO dual approval |
| Cross-account write operations | Human review | Cloud Security team |
| Actions involving financial systems or regulated data | Human review | Compliance team |

**Per SR 26-02 / SR 11-7 model risk principles:** AI-assisted decisions that affect access to regulated systems require a human decision-maker who is accountable for the outcome. The agent's classification informs the human; it does not replace the human.

**Per NIST AI RMF MAP 3.5:** Processes for human oversight are defined, assessed, and documented in accordance with organizational policies.

---

## 9. OWASP LLM Top 10 Controls

The following controls address the OWASP Top 10 for LLM Applications 2025 risks most relevant to enterprise AI agents. All controls are mandatory.

### 9.1 LLM01 -- Prompt Injection Prevention

Prompt injection occurs when malicious content in agent inputs or tool outputs manipulates the LLM into taking unauthorized actions.

**Controls:**
- All external inputs to agents (API responses, file contents, database records, user-provided text) are treated as untrusted data and sanitized before inclusion in LLM context
- Agent system prompts are stored in version-controlled configuration, not constructed dynamically from user input
- Indirect injection from tool outputs is mitigated by the deterministic gate -- even if the LLM is manipulated into recommending a harmful action, the gate prevents execution
- Adversarial testing (red team prompt injection attempts) is required before production deployment of any new agent or tool integration
- Agent inputs and outputs are logged to SIEM; anomalous patterns (unexpected tool calls, unusual action sequences) trigger alerts

**MITRE ATLAS reference:** AML.T0051.000 (Direct Prompt Injection), AML.T0051.001 (Indirect Prompt Injection)

### 9.2 LLM06 -- Excessive Agency Prevention

Excessive Agency is the primary identity security risk for AI agents. It occurs when an agent has more functionality, permissions, or autonomy than required.

**Root causes per OWASP:**
- Excessive functionality: agent has access to tools it does not need
- Excessive permissions: agent's execution role grants more than minimum required
- Excessive autonomy: agent can take actions without human approval

**Controls:**
- Authorized tool set documented and enforced at integration layer (Section 6.1)
- Execution role scoped to minimum required permissions (Section 5.1)
- Deterministic gate enforces action boundaries (Section 7)
- Human-in-the-loop required for high-risk actions (Section 8)
- Rate limits prevent runaway tool invocation (Section 6.3)
- Multiple agents with separate scoped roles used when different permission levels are required within a workflow; a single agent must not hold permissions for all phases of a workflow

### 9.3 LLM07 -- Insecure Plugin / Tool Design Prevention

Tools and plugins invoked by agents must enforce authorization independently. They must not implicitly trust that the agent has the right to call them.

**Controls:**
- Every tool endpoint enforces authentication -- it validates the agent's execution role before executing the requested operation
- Tools do not trust the LLM's claimed context or identity; they validate the calling identity against IAM policy
- Tool responses that contain sensitive data are scoped to the minimum required for the agent's task; tools do not return more data than the agent needs
- Third-party MCP servers and external plugins are reviewed by Identity Security before integration; they must support standard authentication (OAuth, IAM, JWT) and not require static API keys embedded in agent configuration

### 9.4 LLM08 -- System Prompt Leakage Prevention

Agent system prompts may contain sensitive information about internal architecture, tool configurations, or security controls.

**Controls:**
- System prompts do not contain secrets, credentials, internal IP addresses, or architecture details that would provide an attacker meaningful uplift if leaked
- System prompts are stored in version-controlled configuration and treated as sensitive internal documentation
- Agents are instructed not to reveal their system prompt contents if asked; this instruction is supplemented by output filtering
- System prompt contents are reviewed during agent security review before production deployment

### 9.5 LLM04 -- Model Denial of Service Prevention

Agents with unrestricted tool access can be manipulated into consuming excessive resources.

**Controls:**
- Rate limits on all tool invocations (Section 6.3)
- Token limits enforced on LLM context window per agent execution
- Lambda function timeouts and ECS task resource limits defined per agent
- Anomalous resource consumption (unusually high API call volume, unusually long execution duration) triggers automated alert

---

## 10. Mutual Governance Pattern

The mutual governance pattern prevents any single agent from holding unchecked power over its own identity controls. It is required for all agents that perform identity-related actions.

### 10.1 Architecture

```
NHI Lifecycle Agent                    IAM Privilege Drift Agent
        |                                        |
        | Monitors execution role of             | Monitors execution role of
        |-------------------------------->       |<--------------------------------
        |   Drift Agent                          |   NHI Agent
        |                                        |
        | Cannot modify own role                 | Cannot modify own role
        | Cannot modify Drift Agent's            | Cannot modify NHI Agent's
        |   role (read-only monitoring only)     |   role (read-only monitoring only)
```

### 10.2 Requirements

- Agent A holds read-only monitoring permissions on Agent B's execution role (for drift detection)
- Agent A holds no write permissions on Agent B's execution role
- Agent A holds no permissions on its own execution role
- IAM Access Analyzer continuously evaluates both execution roles for unused permissions and external access
- Any change to either agent's execution role requires human approval through the standard IAM change process
- Both agents are monitored by the IAM Privilege Drift Detection Agent -- the agents govern each other

### 10.3 Why This Matters

Without mutual governance, a compromised agent could modify its own permissions to escalate privilege. The mutual governance pattern ensures that no single agent can expand its own access scope, and that any unauthorized change to agent permissions is detected by the sibling agent's continuous monitoring.

---

## 11. Audit Logging Requirements

Every agent execution must produce an immutable audit trail. Logging is not optional and cannot be disabled by agent configuration.

**Required log fields per agent action:**

| Field | Description |
| :--- | :--- |
| Timestamp | UTC timestamp of the action |
| Agent identity | Execution role ARN or Conjur host identity |
| Agent name and version | Identifies which agent and which version took the action |
| Input context | Summary of the finding or event that triggered the action (not full LLM context -- PII minimized) |
| LLM classification | Severity and finding type returned by the LLM |
| Action taken | Specific tool call or API invocation executed |
| Action outcome | Success, failure, or human review required |
| Human approver | If human approved, the approver's identity and timestamp |
| Ticket reference | ServiceNow ticket ID associated with the action |

Logs are forwarded to the enterprise SIEM within 60 seconds of the action. Log retention minimum: 7 years for actions on regulated systems, 1 year for all other agent actions.

CloudTrail must be enabled for all AWS accounts where agents operate. CloudTrail log integrity validation must be enabled to ensure log immutability.

**Per SR 26-02:** All AI-assisted decisions that affect financial or regulated systems must have a complete audit trail traceable to a specific authenticated identity and timestamp.

---

## 12. Agent Lifecycle Governance

### 12.1 Pre-Production Requirements

Before any agent is deployed to a non-development environment:

1. Agent security review completed by Identity Security Architecture
2. Authorized tool set documented and approved by agent owner
3. Execution role reviewed against least privilege requirement
4. Deterministic gate logic reviewed and tested
5. Prompt injection testing completed (minimum 10 adversarial test cases)
6. Conjur or IAM authentication flow validated end-to-end
7. Rate limits configured and tested
8. Audit logging verified in SIEM
9. ServiceNow integration tested for human approval workflow
10. Agent inventory record created with all required attributes

### 12.2 Quarterly Review

All production agents are subject to quarterly review covering:

- Authorized tool set still matches actual usage (unused tool access revoked)
- Execution role permissions still match actual API calls made (drift detection)
- Human owner still active; reassign if owner has departed
- Rate limit thresholds still appropriate
- No prompt injection incidents in prior quarter; if any, remediation documented
- Agent version current; deprecated model versions flagged for upgrade

### 12.3 Agent Decommissioning

When an agent is retired:

1. Agent execution is stopped
2. Execution role is detached from all compute and deleted
3. Conjur policy entries for the agent are removed
4. Agent record closed in NHI inventory with decommission date
5. Audit logs retained per retention schedule

---

## 13. Risk Classification for AI Agents

Agents are classified by risk level at provisioning. Risk level determines review frequency, approval requirements, and monitoring intensity.

| Risk Level | Criteria | Review Frequency | Auto-Remediation Permitted |
| :--- | :--- | :--- | :--- |
| Critical | Accesses financial systems, regulated data, or identity infrastructure; can disable or delete identities | Monthly | No -- all actions require human approval |
| High | Accesses production cloud accounts; can create or modify IAM entities or NHIs | Quarterly | Limited -- notify-only actions only |
| Medium | Accesses production read-only; routes findings to humans only | Quarterly | Notify and tag actions only |
| Low | Development or non-production only; no access to regulated systems | Annual | Permitted per approved patterns |

The NHI Lifecycle Agent and IAM Privilege Drift Detection Agent are classified as **High**.

---

## 14. Compliance Mapping

| Control Domain | OWASP LLM Top 10 2025 | NIST AI RMF 1.0 | NIST SP 800-53 Rev. 5 | NIST SP 800-207 | SR 26-02 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Agent execution role least privilege | LLM06 Excessive Agency | GOVERN 1.1, MAP 3.5 | AC-6, AC-6(1) | Section 5.7 NPE | Section III model governance |
| No hardcoded credentials | LLM06, LLM08 | GOVERN 2.2 | IA-5, SA-15 | Section 5.7 | Section VI controls |
| Prompt injection prevention | LLM01 Prompt Injection | MEASURE 2.6 | SI-10, SI-4 | Section 5.1 | Section V validation |
| Deterministic execution gate | LLM06 Excessive Agency | GOVERN 1.7, MAP 3.5 | AC-3, AC-6 | Section 3.3 Trust Algorithm | Section III |
| Human-in-the-loop for high-risk | LLM06, LLM09 | MAP 3.5, MANAGE 4.1 | AC-5, AU-6 | Section 5.1 | Section V human oversight |
| Audit logging every action | LLM02 Insecure Output | GOVERN 1.4, MEASURE 2.9 | AU-2, AU-3, AU-12 | Section 3.4 | Section VI audit trail |
| Mutual governance pattern | LLM06 | GOVERN 1.2 | AC-5, AC-6(9) | Section 5.7 | Section VI SOD |
| Tool authorization enforcement | LLM07 Insecure Plugin | MAP 4.2, MANAGE 2.2 | AC-3, IA-9 | Section 3.1.1 | Section III |
| Rate limiting | LLM04 Model DoS | MANAGE 2.4 | SC-5, SI-4 | Section 5.2 | Section V |
| System prompt protection | LLM08 Prompt Leakage | GOVERN 2.2 | SC-28, AC-3 | Section 5.5 | Section VI |
| Quarterly agent review | LLM06 | GOVERN 1.7, MEASURE 4.2 | AC-2(7), CA-7 | Section 7.3.7 | Section V ongoing monitoring |
| Agent decommissioning | LLM06 | MANAGE 4.2 | AC-2(3), PS-4 | Section 7.3.7 | Section VI |

---

## 15. Violations and Enforcement

| Violation | Classification | Response |
| :--- | :--- | :--- |
| Hardcoded credential discovered in agent code | Critical | Immediate revocation; agent suspended; incident review |
| Agent bypasses deterministic gate | Critical | Agent execution suspended immediately; incident response |
| Agent modifies own execution role | Critical | Immediate revocation; forensic review; CISO notification |
| Agent takes HIGH action without human approval | Critical | Action reversed if possible; incident review; agent suspended |
| Agent uses tool not in authorized tool set | High | Alert to owner and Identity Security team; audit of prior executions |
| Agent execution role with wildcard permissions | High | Remediate within 14 days; CISO notified at 30 days |
| Prompt injection attempt detected | High | Security incident opened; agent inputs reviewed; adversarial test coverage expanded |
| Agent not in NHI inventory | High | Investigate within 5 business days; register or decommission |
| Quarterly review overdue | Medium | Escalate to agent owner manager; suspend agent at 30 days overdue |
| Missing audit log for agent action | High | Investigate gap; restore logging before resuming execution |

---

## 16. Related Documents

- `STD-NHI-001` -- Non-Human Identity Lifecycle Standard (NHI governance foundation)
- `STD-PAM-001` -- Privileged Access Standard (execution role provisioning)
- `access_approval_matrix.md` -- Approval chains for agent provisioning and tool additions
- `nist_800_207_zero_trust.md` -- NIST SP 800-207 Zero Trust, Section 5.7 NPE threats
- `nist_ai_rmf.md` -- NIST AI RMF 1.0 Govern, Map, Measure, Manage functions
- `owasp_llm_top_10.md` -- OWASP Top 10 for LLM Applications 2025
- `sr_11_7_model_risk.md` -- SR 26-02 Model Risk Management guidance
- `cyberark_conjur.md` -- Conjur JWT authentication for agent credentials
- `compliance_evidence_requirements.md` -- Audit evidence requirements

---

## 17. Document History

| Version | Date | Author | Change Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-06-26 | Identity Security Architecture | Initial release -- full agent security standard covering identity, credentials, deterministic gate, OWASP LLM Top 10 controls, mutual governance, audit logging, lifecycle, and compliance mapping |

---

*This document is part of the Go Cloud Architects Identity Governance RAG Assistant knowledge base. It is an original governance document grounded in OWASP Top 10 for LLM Applications 2025 (LLM01, LLM06, LLM07, LLM08), NIST AI RMF 1.0 (GOVERN, MAP, MEASURE, MANAGE functions), NIST SP 800-207 Section 5.7 (Non-Person Entities in ZTA), NIST SP 800-53 Rev. 5 (AC-6, IA-5, AU-2, SI-4), and Federal Reserve SR 26-02 Model Risk Management guidance. See SOURCE_INDEX.md for authoritative source citations.*
