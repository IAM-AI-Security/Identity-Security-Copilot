# Sample Questions and Grounded Answers

**Document ID:** REF-QA-001  
**Version:** 2.0  
**Last Updated:** 2026-06-26  
**Purpose:** Validated Q&A set for RAG engine testing and governance quick reference. Every answer is grounded in a specific knowledge base document. This document also demonstrates the "Why Mode" response format -- Recommendation, Why, Supporting Standards, Business Impact -- used by the Identity Governance RAG Assistant.

---

## Privileged Access

### Q1: Can a contractor receive permanent AdministratorAccess in AWS?

**Recommendation:** No. Permanent AdministratorAccess for contractors is prohibited under any circumstances.

**Why:** Contractors are not full-time employees and do not have the same accountability, background verification, or ongoing employment relationship. Granting permanent administrative access creates standing privilege that persists beyond the contractor's engagement and cannot be automatically revoked when the contract ends. This violates Zero Standing Privilege principles and least privilege requirements.

**Supporting Standards:** Enterprise Privileged Access Standard §2 (Eligibility) -- contractors are eligible for JIT access only, never permanent privileged access. NIST SP 800-53 AC-6 (Least Privilege). SOX ITGC CC6.1.

**Business Impact:** Contractor accounts with standing AdminAccess are a leading cause of access-after-termination findings in SOX audits. JIT access eliminates this risk by revoking access automatically at session expiry.

---

### Q2: How should human administrators access production AWS environments?

**Recommendation:** All human access to production AWS must use Just-In-Time (JIT) elevation via CyberArk Secure Cloud Access. No standing IAM roles with privileged permissions are permitted for human users.

**Why:** Standing privileged access creates a permanent attack surface. If the user's credential is compromised, the attacker inherits all permissions immediately. JIT access limits the window of exposure to the duration of a single approved session. When the session expires, there is nothing to steal.

**Supporting Standards:** Enterprise Privileged Access Standard §4.2 (Zero Standing Privilege). Cloud Access Standard §6 (JIT and JEA). PAM Reference Architecture Layer 3 (Secure Cloud Access). NIST SP 800-53 AC-2(7), AC-6.

**Business Impact:** Eliminates the #1 cloud access risk -- standing admin credentials. Reduces audit finding exposure and produces a per-session approval and CloudTrail trail that satisfies SOX and PCI evidence requirements.

---

### Q3: What is the maximum session duration for a cloud administrator?

**Recommendation:** 4 hours maximum for Administrator-level access. 8 hours for Security Audit. 12 hours for Read Only.

**Why:** Shorter session durations limit the window of opportunity for credential misuse while still allowing engineers to complete multi-hour tasks. Unlimited session durations defeat the purpose of JIT access -- a credential that is valid indefinitely is effectively a standing credential.

**Supporting Standards:** Numeric Thresholds document §2 (Session Duration Limits). Enterprise Privileged Access Standard §3 (Session Duration Limits). Cloud Access Standard §5 (Azure PIM -- 8 hours for Azure Admin).

**Business Impact:** Enforcing session limits reduces the blast radius of compromised admin sessions and is directly auditable via CloudTrail and SCA session logs.

---

### Q4: What approval is required for AdministratorAccess in AWS?

**Recommendation:** Manager approval plus Cloud Security team approval. For break-glass root account access, dual approval from CISO and VP Infrastructure is required.

**Why:** AdministratorAccess grants unrestricted control over an AWS account. The risk of misconfiguration, data destruction, or security control modification is severe. A single approver is insufficient -- Cloud Security must validate the business justification and confirm no least-privilege alternative exists.

**Supporting Standards:** Access Approval Decision Matrix (Privileged Cloud row). Enterprise Privileged Access Standard §5 (Approval Requirements). PAM Reference Architecture §5.4 (Permission Level Matrix).

**Business Impact:** Two-person approval creates a separation of duties control that satisfies SOX CC5.2 and provides an audit trail showing that every administrative access event was reviewed by an independent security team member.

---

### Q5: What is required before granting break-glass privileged access?

**Recommendation:** Two things must happen before break-glass credentials are released: (1) documentation that normal access is unavailable, and (2) dual approval from CISO and VP Infrastructure in the CyberArk vault portal.

**Why:** Break-glass accounts bypass all standard security controls including MFA federation, Conditional Access policies, and JIT workflows. They must be protected by the strictest possible approval requirements. A single approver could be coerced or compromised. Dual approval requires attacker compromise of two independent senior executives simultaneously.

**Supporting Standards:** Break-Glass Standard §7.2 (Dual Control Enforcement), §8 (Approval and Checkout Process). NIST SP 800-53 AC-5 (Separation of Duties), AC-2(2). SOX ITGC CC5.2.

**Business Impact:** Dual control is a direct SOX and PCI separation of duties control. Every break-glass use produces a dual-approval audit trail with the approvers' identities and timestamps -- exactly what an examiner requests during an incident investigation.

---

## Non-Human Identities

### Q6: Should service accounts have permanent secrets or rotating credentials?

**Recommendation:** Credentials must rotate automatically on a maximum 90-day schedule. Manual rotation is prohibited for production systems. Dynamic secrets via CyberArk Conjur are the preferred approach -- no stored credential at all.

**Why:** Static, long-lived credentials are the most common source of credential compromise in enterprise environments. Every day a credential is unchanged is another day an attacker who obtained it has unrestricted access. Automated rotation limits exposure to the rotation window. Dynamic secrets eliminate the credential entirely -- a new one is generated per-execution.

**Supporting Standards:** Non-Human Identity Standard §7.3 (Rotation Requirements). Enterprise Privileged Access Standard §5.2 (Service Accounts). NHI Standard Tier 2 (credential hierarchy -- dynamic preferred over static). NIST SP 800-53 IA-5(1).

**Business Impact:** Automated credential rotation is a PCI DSS Requirement 8.3.9 control. Manual rotation is a SOX finding risk because evidence of rotation timing is harder to produce. Automated rotation via CPM generates a rotation compliance report that is ready-made audit evidence.

---

### Q7: What happens when a non-human identity owner departs the organization?

**Recommendation:** The NHI must be reassigned to the departing owner's manager within 7 days. If no reassignment is confirmed by day 7, the NHI is automatically disabled. If still unresolved at day 30, the NHI is decommissioned.

**Why:** Every NHI must have an active human owner accountable for its permissions and behavior. An NHI with no owner is an orphan -- it cannot be certified during access reviews, cannot receive anomaly alerts, and represents uncontrolled machine access with no responsible party.

**Supporting Standards:** Non-Human Identity Standard §6.2 (Owner Departure). Enterprise Privileged Access Standard §8 (Access Review -- Orphan account scan monthly). Numeric Thresholds document §5 (SLAs).

**Business Impact:** Orphaned NHIs are a frequent SOX and PCI audit finding. Automated orphan detection and the 7-day reassignment SLA produce evidence that machine identity governance is continuous and not dependent on manual discovery.

---

### Q8: What credential type should a Kubernetes workload use to access AWS services?

**Recommendation:** AWS IAM Roles for Service Accounts (IRSA) -- workload identity federation. No static AWS access keys.

**Why:** IRSA allows EKS pods to authenticate to AWS services using a Kubernetes service account token, which is projected by the cluster's OIDC provider and validated by AWS STS. No credential is stored anywhere. Static access keys embedded in pods or Kubernetes Secrets are a critical finding because they can be extracted from the pod environment.

**Supporting Standards:** NHI Standard §7.4 (Workload Identity Implementation -- AWS IRSA). NHI Standard §5.1 (Credential Hierarchy Tier 1). Agent Security Standard §5.2 (Tier 1 -- AWS IAM role via IRSA).

**Business Impact:** IRSA eliminates the #1 Kubernetes security risk -- credential sprawl. It also satisfies PCI Requirement 8.6.2 (system and application account credentials must be managed). No static key means no static key to rotate, audit, or accidentally expose.

---

### Q9: Can an AI agent use a hardcoded API key?

**Recommendation:** No. Hardcoded credentials in agent code, configuration files, container images, or environment variables are prohibited. This is a critical-severity finding if discovered.

**Why:** Hardcoded credentials are exposed in source code repositories, build artifacts, container image layers, and deployment logs. They cannot be rotated without a code change and deployment. They are frequently discovered in public GitHub repositories by automated scanning tools.

**Supporting Standards:** Agent Security Standard §5.4 (Credential Prohibition). NHI Standard §7.1 (Credential Hierarchy -- Tier 4 Prohibited). Enterprise Privileged Access Standard §6 (Prohibited Configurations). OWASP LLM06 (Excessive Agency -- excessive permissions).

**Business Impact:** A single hardcoded API key in a public repository can result in complete account compromise within minutes. Secret scanning tools (GitHub Advanced Security, truffleHog) detect these automatically -- a CI/CD pipeline failure on a hardcoded credential is an immediate critical remediation ticket.

---

## Zero Trust and Architecture

### Q10: What is Zero Standing Privilege and why does it matter?

**Recommendation:** Zero Standing Privilege (ZSP) is the target architecture state in which no identity holds persistent privileged access. All elevated access is Just-In-Time, time-bounded, and automatically revoked. It matters because standing privilege is the most exploited access pattern in enterprise breaches.

**Why:** Every standing privileged account is a target that exists 24/7 regardless of whether the business needs it. An attacker who compromises standing admin credentials has immediate, unrestricted access to production systems. JIT access limits this window to a single approved session -- the credential that doesn't exist cannot be stolen.

**Supporting Standards:** Enterprise Privileged Access Standard §4.2 (ZSP Target State). NIST SP 800-207 (Zero Trust Architecture) Tenets 3 and 4. Cloud Access Standard §6 (JIT and JEA requirements).

**Business Impact:** ZSP is the most effective architectural control for reducing the impact of credential compromise. It is increasingly required by cyber insurance underwriters and is a positive signal to SOX and PCI auditors that the organization has moved beyond compliance-minimum controls.

---

### Q11: What NIST controls apply to privileged access reviews?

**Recommendation:** The primary controls are AC-2(7) (Privileged User Accounts -- review privileges), AC-6(9) (Log use of privileged functions), and AC-5 (Separation of Duties). Supporting controls include PS-7 (External Personnel Security) for contractor reviews and CA-7 (Continuous Monitoring).

**Why:** NIST SP 800-53 AC-2 requires organizations to review accounts for compliance with account management requirements. AC-2(7) specifically requires review of privileges assigned to privileged users and reassignment or removal of privileges when no longer needed. This maps directly to quarterly privileged access certification campaigns.

**Supporting Standards:** NIST SP 800-53 Access Control Summary (AC-2, AC-5, AC-6). Enterprise Privileged Access Standard §8 (Access Review and Certification). Compliance Evidence Requirements §3 (PAM Evidence).

**Business Impact:** Mapping access certification campaigns to specific NIST control numbers allows audit evidence packages to cite the authoritative standard. When an examiner asks "what controls govern your privileged access reviews?" the answer cites AC-2(7) and AC-6(9) with the evidence artifacts from CyberArk's compliance reports.

---

### Q12: How does Zero Trust apply to identity governance?

**Recommendation:** Zero Trust's enhanced identity governance approach (NIST SP 800-207 Section 3.1.1) makes identity the primary policy driver. Every access decision -- human or machine -- is evaluated against the subject's identity, current attributes, device posture, and behavioral context. Trust is never implicit; it is continuously verified.

**Why:** Traditional perimeter-based security assumed that anything inside the network could be trusted. Modern enterprise environments have no meaningful perimeter -- cloud, remote workers, SaaS, and contractors make the network perimeter irrelevant. Identity is the only consistent boundary that can be enforced everywhere.

**Supporting Standards:** NIST SP 800-207 §2.1 (Seven Tenets of Zero Trust). NIST SP 800-207 §3.1.1 (ZTA Using Enhanced Identity Governance). Zero Trust Identity Architecture standard. Enterprise Privileged Access Standard §4.2.

**Business Impact:** Identity-centric Zero Trust reduces lateral movement risk -- the #1 technique used in ransomware and APT attacks. An attacker who compromises one identity cannot move to other systems without re-authenticating through the Policy Enforcement Point.

---

## AI Agent Security

### Q13: How do you prevent AI agents from taking unauthorized actions?

**Recommendation:** The deterministic execution gate pattern. The LLM classifies findings and recommends actions. A separate Python enforcement layer validates the classification against the agent's authorized action set, checks severity against the approval matrix, and routes HIGH/CRITICAL actions to human review before any execution occurs.

**Why:** LLMs can hallucinate, be manipulated via prompt injection, or produce unexpected outputs. If the LLM directly executed API calls based on its own outputs, a single adversarial input could trigger a destructive action. The deterministic gate separates reasoning (LLM) from execution (deterministic code) -- the LLM cannot execute anything directly.

**Supporting Standards:** Agent Security Standard §7 (Deterministic Execution Gate Pattern). OWASP LLM06:2025 (Excessive Agency -- excessive autonomy). NIST SP 800-207 §5.7 (Non-Person Entities in ZTA). SR 26-02 (human oversight for AI-assisted decisions).

**Business Impact:** The deterministic gate is the governance control that makes AI agents safe for production use. Without it, agents represent an uncontrolled privileged principal. With it, every agent action is bounded, auditable, and human-reviewed for high-risk operations -- satisfying SR 26-02 model risk requirements for AI-assisted decision-making.

---

### Q14: What is Excessive Agency in AI and how do we prevent it?

**Recommendation:** Excessive Agency (OWASP LLM06:2025) is the vulnerability where an AI agent is granted more functionality, permissions, or autonomy than required. Prevention requires three controls: minimize tools (only authorized tools in the agent's documented tool set), minimize permissions (execution role scoped to minimum required API operations), and minimize autonomy (human approval required for high-risk actions).

**Why:** An agent with excessive functionality can call tools it was not designed to use. An agent with excessive permissions can access data beyond its intended scope. An agent with excessive autonomy can take destructive or irreversible actions without human review. All three contribute to the same outcome: an agent that does things its designer did not intend.

**Supporting Standards:** Agent Security Standard §6 (Least Privilege and Tool Governance), §9.2 (LLM06 Prevention). OWASP Top 10 for LLM Applications 2025 (LLM06). NHI Standard §8.1 (Prohibited Permission Patterns).

**Business Impact:** Excessive Agency is the identity security equivalent of over-privileged service accounts -- the same risk pattern, amplified by the agent's ability to act autonomously. Scoped execution roles and authorized tool sets are the machine identity governance controls applied to the AI context.

---

## Compliance and Audit

### Q15: What evidence is required for a SOX privileged access review?

**Recommendation:** Four artifacts are required: (1) a system-generated list of all active privileged accounts with their assigned owners, (2) proof of approval for a sample of users granted privileged access during the audit period, (3) evidence of password rotation policies including CPM configuration, and (4) audit logs showing who accessed privileged accounts and when.

**Why:** SOX ITGC CC6.1 requires that access to systems is restricted to authorized users. Auditors test this by sampling privileged accounts and tracing each one back to an approval, an active employee, and a rotation event. Without system-generated evidence, examiners cannot confirm that controls operated effectively throughout the period.

**Supporting Standards:** Compliance Evidence Requirements §3 (PAM Evidence). SOX Evidence Template. CyberArk Privilege Cloud Compliance Reports (account inventory, rotation compliance, access certification history).

**Business Impact:** CyberArk's built-in compliance reports produce most of this evidence automatically. The quarterly certification campaign in SailPoint or Entra ID Governance produces the remainder. Together they reduce SOX audit preparation time from days to hours.

---

### Q16: Which NIST controls map to non-human identity governance?

**Recommendation:** Primary controls: IA-2 (Identification and Authentication -- organizational users and processes), IA-3 (Device Identification and Authentication), IA-5 (Authenticator Management), IA-9 (Service Identification and Authentication), and AC-2 (Account Management). Supporting: AC-6 (Least Privilege), AU-2 (Audit Events), CA-7 (Continuous Monitoring).

**Why:** NIST SP 800-53 IA-9 specifically requires that services and applications uniquely identify and authenticate themselves before establishing communications. This is the control that mandates machine identity authentication -- JWT, OIDC, mutual TLS -- rather than shared or anonymous credentials.

**Supporting Standards:** NIST SP 800-53 Access Control Summary. NHI Standard §12 (Compliance Mapping). Privileged Access Standard §9 (Compliance Mapping -- NHI row).

**Business Impact:** Mapping NHI controls to NIST IA-9 and IA-3 gives the identity program a defensible framework citation for machine identity governance. When a PCI QSA asks about Requirement 8.6 (system and application account management), the NIST control mapping is the bridge to your internal standard.

---

### Q17: What dormancy thresholds trigger account disablement?

**Recommendation:** Privileged accounts: 45 days. Standard human accounts: 90 days. Service accounts and NHIs: 180 days.

**Why:** Dormant accounts represent access that is no longer actively needed. They accumulate over time due to role changes, project completions, and organizational restructuring. An attacker who obtains credentials for a dormant privileged account may go undetected for extended periods because there is no baseline activity to deviate from.

**Supporting Standards:** Numeric Thresholds document §3 (Dormancy Thresholds). NHI Standard §6 (Lifecycle -- orphan detection). Enterprise Privileged Access Standard §8 (NHI inventory reconciliation monthly). NIST SP 800-53 AC-2(3) (Disable Inactive Accounts).

**Business Impact:** Automated dormancy detection and disablement reduces the standing attack surface continuously. The 45-day threshold for privileged accounts satisfies PCI DSS Requirement 8.2.6 (remove or disable inactive user accounts within 90 days -- the enterprise standard is stricter at 45 days for privileged accounts).

---

## CyberArk Operations

### Q18: What causes a CyberArk CPM rotation failure and how is it resolved?

**Recommendation:** CPM rotation failures most commonly result from three root causes: (1) network connectivity between CPM and the target system, (2) the reconcile account lacking sufficient permissions on the target, or (3) the target account being locked in Active Directory. Resolution follows: verify network path, check reconcile account permissions, unlock the target account, and verify CPM platform configuration.

**Why:** The CPM uses a reconcile account to reset the target account's password. If the reconcile account cannot authenticate to the target system -- due to network issues, permission problems, or account lockout -- the rotation fails and the vault credential becomes out of sync with the target. An out-of-sync credential means the next PSM session will fail, blocking administrative access.

**Supporting Standards:** CyberArk Troubleshooting Guide (CPM errors). PAM Reference Architecture §3.2 (CPM component description). Enterprise Privileged Access Standard (rotation failure escalation -- 24 hours to application owner, 14 days to disable).

**Business Impact:** Unresolved rotation failures are a compliance risk -- PCI DSS requires credentials to rotate on schedule. CyberArk's failed rotation report is audit evidence. A rotation failure that persists beyond 14 days without resolution is escalated as a potential credential compromise.

---

### Q19: How does CyberArk Conjur authenticate a Kubernetes workload without storing credentials in the pod?

**Recommendation:** The authn-jwt/k8s authenticator. The pod presents its Kubernetes-issued service account JWT to the Conjur authentication endpoint. Conjur validates the JWT against the cluster's OIDC JWKS endpoint, issues a short-lived Conjur access token (8-minute TTL), and the pod uses that token to retrieve the specific secret it needs. No credential is stored in the pod at any point.

**Why:** Kubernetes Secrets objects are only base64-encoded by default -- not encrypted at rest. Any principal with `get secret` permission on a namespace can read them in plaintext. Conjur eliminates the Kubernetes Secret entirely -- secrets are retrieved at runtime and never written to disk or stored in the pod's environment.

**Supporting Standards:** CyberArk Conjur overview. PAM Reference Architecture §4.3 (Kubernetes Integration Pattern). NHI Standard §7.4 (Workload Identity -- Kubernetes). Agent Security Standard §5.3 (Conjur JWT Authentication Flow).

**Business Impact:** Eliminating Kubernetes Secrets for sensitive credentials removes the most common cloud-native credential exposure path. It also satisfies PCI DSS Requirement 8.3.1 (credentials must be secured against misuse and disclosure) for containerized workloads.

---

### Q20: What SOX evidence does CyberArk Privilege Cloud produce automatically?

**Recommendation:** Six reports are available directly from the Privilege Cloud compliance dashboard: account inventory with owner assignments, CPM rotation compliance report, safe membership change log, PSM session recording coverage report, access certification history, and failed rotation report. These are exported quarterly and retained for 7 years.

**Why:** SOX ITGC testing requires auditors to sample privileged accounts and confirm that access is appropriately restricted, monitored, and reviewed. System-generated reports are more reliable audit evidence than manually compiled spreadsheets -- they cannot be retroactively edited and carry a system timestamp that confirms when the data was captured.

**Supporting Standards:** PAM Reference Architecture §6.2 (Compliance Reporting). Compliance Evidence Requirements §3 (PAM Evidence). Privileged Access Standard §10.6 (Privilege Cloud Reporting).

**Business Impact:** Automated compliance reports reduce SOX audit preparation time significantly. The account inventory report satisfies CC6.1 evidence requirements. The rotation compliance report satisfies CC6.1 and PCI Req 8.3.9. The session recording coverage report satisfies CC7.2 and PCI Req 10.2. Together they cover the majority of privileged access ITGC evidence in a single export.

---

## Document Notes

This Q&A set uses the "Why Mode" response format throughout:
- **Recommendation** -- the direct answer
- **Why** -- the security and governance rationale
- **Supporting Standards** -- specific document and section citations from this knowledge base
- **Business Impact** -- how the recommendation reduces risk, improves compliance, or simplifies operations

This format is the target output structure for the Identity Governance RAG Assistant. Every response should follow this pattern when answering governance questions.

---

*This document is part of the Go Cloud Architects Identity Governance RAG Assistant knowledge base. All answers are grounded in the governance standards, architecture documents, vendor summaries, and framework references in this knowledge base. See SOURCE_INDEX.md for authoritative source citations.*
