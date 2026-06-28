# Privileged Access Management (PAM) Reference Architecture

**Document ID:** ARCH-PAM-001  
**Version:** 2.0  
**Last Updated:** 2026-06-26  
**Owner:** Identity Security Architecture  
**Classification:** Internal — Architecture  
**Review Cycle:** Annual  
**Supersedes:** ARCH-PAM-001 v1.0 (stub — Core PAS only)

---

## 1. Purpose

This document defines the enterprise reference architecture for Privileged Access Management (PAM). It covers the full CyberArk platform stack including Privilege Cloud (SaaS), CyberArk Conjur (secrets management), and CyberArk Secure Cloud Access (JIT cloud privilege), as well as the integration patterns that connect them to enterprise identity infrastructure, cloud environments, and AI agent workloads.

This architecture serves as the design standard for all PAM deployments and the authoritative reference for audit questions about how privileged access is secured, monitored, and governed.

---

## 2. Architecture Overview

The enterprise PAM architecture is organized into four functional layers:

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 4 -- Governance and Compliance                           │
│  Access reviews, compliance reports, audit evidence, SIEM       │
├─────────────────────────────────────────────────────────────────┤
│  Layer 3 -- Just-In-Time Cloud Access                           │
│  CyberArk Secure Cloud Access -- JIT cloud console/CLI roles    │
├─────────────────────────────────────────────────────────────────┤
│  Layer 2 -- Non-Human Identity and Secrets                      │
│  CyberArk Conjur -- workload identity, dynamic secrets,         │
│  CI/CD pipelines, Kubernetes, AI agents                         │
├─────────────────────────────────────────────────────────────────┤
│  Layer 1 -- Human Privileged Access                             │
│  CyberArk Privilege Cloud -- vault, CPM, PSM, portal            │
└─────────────────────────────────────────────────────────────────┘
```

Each layer is independent but integrated. A human administrator accessing a production server flows through Layer 1. A Kubernetes pod retrieving a database password flows through Layer 2. A cloud engineer requesting temporary AWS console access flows through Layer 3. All layers feed into Layer 4 for audit and compliance evidence.

---

## 3. Layer 1 -- Human Privileged Access: CyberArk Privilege Cloud

### 3.1 Platform Overview

CyberArk Privilege Cloud is a SaaS-delivered PAM platform. The Digital Vault (credential store) is hosted and managed by CyberArk in their cloud infrastructure. Customer-side components (CPM, PSM) are deployed in the customer's environment or cloud to communicate with on-premises and cloud target systems.

This hybrid architecture means:
- The vault and portal are available without customer infrastructure maintenance
- CPM and PSM can reach internal target systems that CyberArk's cloud cannot directly access
- Customers retain control over session routing and credential rotation logic

### 3.2 Core Components

**Digital Vault**
The encrypted credential repository. Stores passwords, SSH keys, certificates, and secret references. Access to vault contents is governed by Safe membership and permission rules -- no component or user has direct database access to the vault. All access is through authenticated API calls logged to the vault audit log.

The vault uses proprietary encryption with AES-256 at rest. In Privilege Cloud, the vault is operated by CyberArk with SOC 2 Type II attestation.

**Privilege Cloud Portal (PVWA)**
The web interface for all user interactions with the PAM system. Administrators use the portal to:
- Request and retrieve credentials
- Launch PSM-proxied sessions to target systems
- Manage safes, policies, and platform configurations
- Review audit reports and compliance dashboards
- Manage break-glass checkout requests and dual control approvals

**Central Policy Manager (CPM)**
Deployed in the customer environment. Connects to target systems over the network to automatically rotate credentials according to platform policies. The CPM never exposes the new password to any human -- it sets the password on the target system and updates the vault simultaneously.

CPM platform policies define:
- Rotation frequency (e.g., every 30 days, or after every use)
- Password complexity requirements
- Reconcile account behavior (what account CPM uses to change the password)
- Verification behavior (whether CPM confirms the new password works after rotation)

CPM rotation failure generates an immediate alert. Unresolved failures escalate to the application owner within 24 hours and to the CISO if unresolved at 14 days.

**Privileged Session Manager (PSM)**
Deployed in the customer environment. Acts as a session proxy between the requesting user and the target system. The PSM:
- Retrieves the credential from the vault on behalf of the user
- Establishes the privileged session to the target system
- Records all session activity (full video and keystroke logging)
- Presents the user with a proxied session -- the user never sees or handles the actual password
- Terminates the session at timeout or upon user request

PSM supports RDP (Windows servers), SSH (Linux/Unix), database connections (Oracle, SQL Server, PostgreSQL via PSM for Databases), and web application sessions (via HTML5 Gateway).

Session recordings are stored in CyberArk and are immutable audit artifacts. Minimum retention: 90 days online, 1 year archived. Recordings are exportable for forensic review.

**PSM for SSH (PSMP)**
A dedicated component for SSH session proxying. Allows users to connect to Linux/Unix targets using their standard SSH client while the PSMP handles authentication to the target using the vaulted credential. The user connects to the PSMP address; the PSMP connects to the target.

### 3.3 Safe Design

Credentials are organized into logical containers called Safes. Safe design is critical to least privilege -- a user who has access to a safe can access all credentials within it, so safes must be scoped appropriately.

**Enterprise Safe naming convention:**

| Safe Name Pattern | Purpose | Example |
| :--- | :--- | :--- |
| `WIN-<Application>-<Env>` | Windows service accounts | `WIN-PayrollApp-Prod` |
| `LNX-<Application>-<Env>` | Linux service accounts | `LNX-WebServer-Prod` |
| `DB-<Application>-<Env>` | Database accounts | `DB-Oracle-FinSys-Prod` |
| `NET-<Platform>-<Env>` | Network device credentials | `NET-Cisco-Core-Prod` |
| `CLD-<Provider>-<Account>` | Cloud break-glass / local accounts | `CLD-AWS-123456789012` |
| `NHI-<Application>-<Env>` | Non-human identity static secrets | `NHI-PayrollAPI-Prod` |
| `BG-<Platform>-Emergency` | Break-glass accounts | `BG-EntraID-Emergency` |
| `VND-<Vendor>-<Env>` | Vendor / third-party access | `VND-AcmeCorp-Prod` |

**Safe permission model:**

Each safe has the following permission roles:

- **Owner:** Full control; manages safe membership and policies. Reserved for Identity Security Architecture.
- **Manager:** Can add and remove accounts; cannot change safe-level settings. Used by application owners.
- **User:** Can retrieve credentials and launch PSM sessions; cannot see passwords in plaintext (one-click launch model).
- **Approver:** Can approve dual-control checkout requests; cannot retrieve credentials themselves.
- **Auditor:** Read-only access to safe audit logs; cannot retrieve credentials.

### 3.4 Access Flow: Human Privileged Session

```
Administrator authenticates to Privilege Cloud Portal (MFA via Okta/Entra SSO)
        ↓
Administrator locates target account in safe
        ↓
Administrator clicks "Connect" (one-click PSM launch)
        ↓
PVWA generates session token and directs user to PSM
        ↓
PSM retrieves credential from Digital Vault (vault API call -- audited)
        ↓
PSM establishes RDP/SSH session to target system using retrieved credential
        ↓
PSM presents proxied session to administrator (RDP client or HTML5 browser session)
        ↓
PSM records full session (video + keystrokes) throughout
        ↓
Session terminates on user disconnect or 15-minute inactivity timeout
        ↓
PSM closes connection; vault credential remains unchanged (or rotated if policy requires post-session rotation)
        ↓
Session recording stored in vault; audit log entry created
```

The administrator never handles the credential at any step. The vault credential is retrieved by PSM's service identity, not by the user.

### 3.5 Platform Policies

Platform policies define how CPM interacts with specific target system types. Each platform type (Windows Domain Account, Unix via SSH, Oracle Database, Cisco IOS, etc.) has a dedicated platform with configuration for:

- Connection method (WMI, SSH, Oracle client, etc.)
- Password complexity rules matching the target system's requirements
- Rotation schedule
- Reconcile account (the account CPM uses to change the password on the target)
- Verification settings

Organizations must not use generic platforms for production accounts. Each target system type must have a correctly configured platform to ensure rotation reliability.

---

## 4. Layer 2 -- Non-Human Identity and Secrets: CyberArk Conjur

### 4.1 Platform Overview

CyberArk Conjur (also marketed as Secrets Manager) is the secrets management solution for non-human identities. While Privilege Cloud handles human access to credentials, Conjur handles machine-to-machine authentication and dynamic secrets delivery for:

- Application service accounts retrieving database passwords at runtime
- CI/CD pipelines retrieving API keys during build and deploy
- Kubernetes pods retrieving secrets without storing them in Kubernetes Secrets objects
- AI agents authenticating and retrieving tool credentials per-execution

Conjur's fundamental difference from a traditional password vault: applications do not retrieve a password and store it. They authenticate to Conjur at runtime, receive a short-lived access token, and retrieve the secret immediately before use. The secret is never persisted in application memory, environment variables, or configuration files.

### 4.2 Core Concepts

**Machine Identity**
Every workload that uses Conjur has a machine identity -- a host entry in the Conjur policy that represents the workload. The identity is authenticated using platform-native attributes (Kubernetes service account token, AWS IAM role, Azure Managed Identity) rather than a static username and password.

**Conjur Policy**
Access control in Conjur is defined in declarative YAML policy files. Policies define:
- Which host identities exist (applications, AI agents, CI/CD jobs)
- Which secrets (variables) exist
- Which host identities have permission to retrieve which secrets
- Groupings and role hierarchies

Policies are version-controlled. All changes to policy are audited. No one can grant themselves access to a secret -- policy changes require Identity Security team review.

**Authenticators**
Conjur authenticators are the mechanism by which machine identities prove who they are:

| Authenticator | Platform | How It Works |
| :--- | :--- | :--- |
| `authn-jwt/k8s` | Kubernetes | Conjur validates the Kubernetes-issued service account JWT against the cluster's OIDC endpoint |
| `authn-iam` | AWS | Conjur validates the workload's AWS IAM role via STS |
| `authn-azure` | Azure | Conjur validates the workload's Azure Managed Identity JWT |
| `authn-jwt` (generic) | Any OIDC provider | Conjur validates a JWT issued by any configured OIDC provider |
| `authn-k8s` | Kubernetes (legacy) | Mutual TLS based; use authn-jwt/k8s for new deployments |

**Dynamic Secret Delivery**
The standard Conjur retrieval flow:

```
Workload starts executing
        ↓
Workload presents platform JWT to Conjur authn-jwt endpoint
        ↓
Conjur validates JWT signature against JWKS endpoint
        ↓
Conjur issues short-lived Conjur access token (TTL: 8 minutes)
        ↓
Workload calls Conjur secrets API with Conjur token to retrieve specific secret
        ↓
Conjur returns secret value
        ↓
Workload uses secret immediately; does not persist it
        ↓
Conjur access token expires; workload must re-authenticate for next execution
```

Every step in this flow is logged to the Conjur audit log with: timestamp, host identity, variable path retrieved, client IP, and success/failure status.

### 4.3 Kubernetes Integration Pattern

For Kubernetes workloads, Conjur integrates using the Secrets Provider pattern or the Secretless Broker pattern:

**Secrets Provider (Init Container)**
An init container runs before the application container, authenticates to Conjur using the pod's service account JWT, retrieves required secrets, and writes them to a shared in-memory volume. The application container reads secrets from the volume. Secrets are never stored in Kubernetes Secrets objects (which are base64-encoded, not encrypted at rest by default).

**Secretless Broker (Sidecar)**
A sidecar container runs alongside the application. The application connects to the sidecar as if it were the target service (e.g., a database). The sidecar retrieves credentials from Conjur and injects them into the connection transparently. The application has no credential knowledge at all.

**Required Kubernetes Configuration:**
- Each application namespace must have a dedicated Kubernetes service account
- Service account tokens must have audience bindings scoped to Conjur
- The `default` service account must have no role bindings or Conjur permissions
- `automountServiceAccountToken: false` set at namespace level; enabled only for pods that require it

### 4.4 CI/CD Pipeline Integration

For CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins):

- Pipelines authenticate to Conjur using the pipeline platform's OIDC JWT (e.g., GitHub Actions OIDC token)
- Secrets are retrieved at the start of the pipeline job and used only for the duration of that job
- No secrets are stored in pipeline environment variables, repository secrets (as static values), or build artifacts
- Conjur policy restricts each pipeline to only the secrets it needs for its specific function

### 4.5 AI Agent Integration

AI agents authenticate to Conjur using the authn-jwt authenticator with the agent's platform JWT (Lambda execution role JWT, Kubernetes pod service account token, etc.). See `agent_security_standard.md` Section 5.3 for the full authentication flow.

The Conjur policy for AI agents is scoped to the specific secrets the agent requires for its documented tool set. An agent that calls the ServiceNow API has access to the ServiceNow API key variable only -- not to database passwords, not to other agents' secrets.

---

## 5. Layer 3 -- JIT Cloud Access: CyberArk Secure Cloud Access

### 5.1 Platform Overview

CyberArk Secure Cloud Access (SCA), formerly known as Secure Infrastructure Access (SIA), provides Just-In-Time privileged access to cloud consoles and CLI tools. It eliminates standing cloud IAM roles for human administrators.

The target state for cloud access:
- No human holds a standing AWS IAM role with privileged permissions
- No human holds standing Azure privileged role assignments (beyond what PIM already controls)
- All cloud console and CLI access is JIT: requested, approved, time-bounded, and automatically revoked

### 5.2 AWS JIT Access Flow

```
Cloud engineer needs AWS console access for a specific task
        ↓
Engineer submits access request in SCA portal:
  - Target AWS account
  - Required permission level (e.g., ReadOnly, PowerUser, AdministratorAccess)
  - Duration (max 4 hours for admin, 12 hours for read-only)
  - Business justification
        ↓
Request routed for approval (manager + Cloud Security team for admin access)
        ↓
SCA provisions a temporary IAM role in the target account with the requested permissions
        ↓
SCA issues time-bound federation token to the engineer
        ↓
Engineer accesses AWS console or CLI using the federation token
        ↓
At session expiry, SCA automatically revokes the temporary role
        ↓
Engineer's access is gone; no standing IAM role remains
        ↓
Full session audit trail logged: who accessed what account, what permissions, what actions taken (via CloudTrail)
```

### 5.3 Azure JIT Access

For Azure, SCA integrates with Entra ID PIM to provide JIT role activation. The flow is similar:

- Engineer requests role activation in SCA or directly in PIM
- Approval required for privileged roles (Global Administrator, Privileged Role Administrator, Subscription Owner)
- Maximum activation duration: 8 hours for administrative roles, 4 hours for Global Administrator
- Role automatically deactivates at expiration

### 5.4 Permission Level Matrix

| Access Level | AWS Permission Set | Azure Role | Requires Approval | Max Duration |
| :--- | :--- | :--- | :--- | :--- |
| Read Only | ReadOnlyAccess | Reader | Manager only | 12 hours |
| Developer | PowerUserAccess (minus IAM) | Contributor (minus RBAC) | Manager + Cloud Security | 8 hours |
| Security Audit | SecurityAudit | Security Reader | Manager + Cloud Security | 8 hours |
| Administrator | AdministratorAccess | Owner / Subscription Owner | Manager + Cloud Security + CISO | 4 hours |
| Break-Glass | Root (AWS) / Global Admin (Azure) | Global Administrator | Dual approval: CISO + VP Infra | 4 hours |

---

## 6. Layer 4 -- Governance and Compliance

### 6.1 Audit Logging

All four PAM layers generate audit logs that are forwarded to the enterprise SIEM:

| Source | Events Logged | SIEM Integration |
| :--- | :--- | :--- |
| Privilege Cloud Vault | Every credential retrieval, safe access, policy change, user authentication | Syslog to SIEM |
| CPM | Every rotation attempt (success and failure), verification events | Syslog to SIEM |
| PSM | Every session start, session end, commands executed (if command filtering enabled) | Syslog to SIEM |
| Conjur | Every authentication event, every secret retrieval, every policy change | Syslog or REST export to SIEM |
| SCA | Every access request, approval, session start, session end, role provisioning | Syslog to SIEM |
| CloudTrail | All AWS API calls made during SCA-provisioned sessions | S3 export to SIEM |

### 6.2 Compliance Reporting

Privilege Cloud provides built-in compliance reports available from the portal:

| Report | Compliance Use |
| :--- | :--- |
| Account inventory by safe | SOX CC6.1 -- privileged account inventory evidence |
| CPM rotation compliance | SOX CC6.1, PCI Req 8.3 -- rotation policy enforcement |
| Safe membership report | SOX CC5.2 -- access control evidence |
| PSM session recording coverage | SOX CC7.2, PCI Req 10.2 -- session audit evidence |
| Accounts not accessed in X days | Drift detection; orphan identification |
| Failed rotation report | Remediation tracking |
| Dual control usage report | SOX CC5.2 -- separation of duties evidence |

Reports are exported quarterly by the Identity Security team and retained for a minimum of 7 years.

### 6.3 Access Certification Integration

Privilege Cloud safe membership is included in the quarterly privileged access certification campaign:

- IGA platform (SailPoint or Entra ID Governance) pulls safe membership from Privilege Cloud via API
- Application owners certify that each account in their safe still requires access
- Accounts not certified within the review window are automatically removed from the safe
- Evidence package includes the certification report and the corresponding safe membership export before and after remediation

### 6.4 SIEM Detection Rules

The following detection rules must be active in the enterprise SIEM for PAM events:

| Rule | Trigger | Severity |
| :--- | :--- | :--- |
| Credential retrieved outside business hours | Vault retrieval event at non-standard hours for that account | High |
| Credential retrieved from new source IP | First-seen source IP for a given account | High |
| CPM rotation failure | Rotation failure event unresolved for 24 hours | High |
| PSM session duration exceeded | Session exceeds maximum allowed duration | Medium |
| Break-glass account sign-in | Any authentication by break-glass account | Critical |
| Safe membership change | Any change to safe member list | Medium |
| Conjur secret retrieved by new host identity | First-seen host authenticating to Conjur | High |
| SCA admin session -- CloudTrail IAM change | IAM policy or role modification during SCA admin session | Critical |
| Multiple failed Conjur authentications | 5+ failed authn attempts from same source in 10 minutes | High |

---

## 7. Integration Architecture

### 7.1 Identity Provider Integration

The PAM platform integrates with the enterprise IdP for human user authentication:

```
User authenticates to Okta/Entra ID (MFA enforced)
        ↓
SAML assertion issued to Privilege Cloud Portal
        ↓
Privilege Cloud maps SAML groups to safe access permissions
        ↓
User sees only the safes and accounts they are authorized to access
```

No local Privilege Cloud user accounts exist for regular users. All human authentication flows through the enterprise IdP. Emergency (break-glass) access to the PAM portal uses dedicated local accounts stored in the break-glass safe.

### 7.2 ITSM Integration

Privilege Cloud integrates with ServiceNow for access request workflows:

- Users request access to new safes via ServiceNow
- Approval workflow routes to safe owner and Identity Security team
- On approval, Identity Security team provisions safe membership in Privilege Cloud
- CPM rotation failures generate ServiceNow incidents automatically
- Break-glass checkout events create critical-priority ServiceNow incidents automatically

### 7.3 IGA Integration

The IGA platform (SailPoint or Entra ID Governance) connects to Privilege Cloud for:

- Safe membership discovery (what accounts exist, who has access)
- Quarterly access certification campaigns for privileged accounts
- Automated provisioning and deprovisioning based on HR events (joiner/mover/leaver)
- Orphan account detection (accounts with no active human owner)

### 7.4 Network Architecture

**CPM network requirements:**
- CPM must have network connectivity to all target systems it manages
- Required ports depend on platform type: WMI (135, 445), SSH (22), Oracle (1521), MSSQL (1433), etc.
- CPM connects outbound to target systems; no inbound connections required from target to CPM
- CPM connects to the Privilege Cloud vault over HTTPS (443) outbound to CyberArk's cloud

**PSM network requirements:**
- PSM must be reachable by users launching sessions (typically via corporate network or VPN)
- PSM connects outbound to target systems on the session protocol port (RDP 3389, SSH 22)
- Users connect to PSM; PSM connects to target -- users never have direct network access to targets
- HTML5 Gateway provides browser-based PSM access without requiring RDP client installation

**Conjur network requirements:**
- Conjur API endpoint reachable by all workloads that need secrets (HTTP/S 443)
- Conjur connects to the JWKS endpoints of each platform (Kubernetes OIDC, AWS STS, Azure OIDC) for JWT validation
- No inbound connections to Conjur from external sources; workloads call Conjur outbound

---

## 8. Deployment Topology

### 8.1 Privilege Cloud (SaaS)

```
CyberArk Cloud (hosted by CyberArk)
  ├── Digital Vault (encrypted credential store)
  └── Privilege Cloud Portal (PVWA equivalent)

Customer Environment
  ├── CPM Servers (1 per environment: prod, non-prod)
  │     └── Connects to target systems for rotation
  └── PSM Servers (clustered for HA)
        ├── PSM for Windows (RDP sessions)
        ├── PSM for SSH (SSH sessions)
        └── HTML5 Gateway (browser-based sessions)
```

CPM and PSM servers are deployed as Windows Server VMs in the customer's cloud (AWS EC2 or Azure VM) or on-premises. They communicate with the CyberArk-hosted vault over HTTPS. They communicate with target systems over the target's native protocol.

### 8.2 Conjur (SaaS or Self-Hosted)

```
Option A: Conjur Cloud (SaaS)
  ├── Conjur API endpoint (hosted by CyberArk)
  └── Policy and secret storage (managed by CyberArk)

Option B: Conjur Self-Hosted
  ├── Conjur Leader (primary)
  ├── Conjur Follower (read-only replicas for performance)
  └── All deployed in customer's cloud/on-premises
```

For most enterprises, Conjur Cloud (SaaS) is preferred for reduced operational overhead. Self-hosted is used where data residency requirements prevent cloud-hosted secrets storage.

### 8.3 High Availability

| Component | HA Pattern |
| :--- | :--- |
| Digital Vault (Privilege Cloud) | Managed by CyberArk with multi-region redundancy |
| CPM | Primary + standby; failover automatic on heartbeat failure |
| PSM | Load-balanced cluster; sessions routed round-robin |
| HTML5 Gateway | Load-balanced; stateless |
| Conjur Cloud | Managed by CyberArk with multi-region |
| Conjur Self-Hosted | Leader + Followers; followers serve read requests |

---

## 9. Compliance Mapping

| Control Area | SOX ITGC | NIST SP 800-53 Rev. 5 | PCI DSS v4.0 | FFIEC |
| :--- | :--- | :--- | :--- | :--- |
| Privileged credential vaulting | CC6.1 | IA-5, SC-28 | Req 8.3.1 | Authentication Management |
| Automated password rotation | CC6.1 | IA-5(1) | Req 8.3.9 | Credential Management |
| Session recording and monitoring | CC7.2 | AU-12, AU-14 | Req 10.2 | Audit Trail |
| Session isolation (PSM proxy) | CC6.1 | AC-17, SC-8 | Req 8.6 | Access Controls |
| JIT cloud access (SCA) | CC6.1 | AC-2(7), AC-6 | Req 7.2 | Access Controls |
| Dual control for sensitive accounts | CC5.2 | AC-5 | Req 8.2.4 | Separation of Duties |
| NHI secrets management (Conjur) | CC6.1 | IA-3, IA-9, SA-15 | Req 8.6 | NHI Controls |
| Audit log integrity | CC7.2 | AU-9, AU-11 | Req 10.3 | Audit Trail |
| Access certification integration | CC5.2 | AC-2(7) | Req 7.2.3 | Access Reviews |
| Break-glass vault storage | CC7.3 | AC-2(2), CP-2 | Req 8.2.2 | Emergency Access |

---

## 10. Related Documents

- `STD-PAM-001` -- Privileged Access Standard (governance requirements this architecture implements)
- `STD-NHI-001` -- Non-Human Identity Lifecycle Standard
- `STD-BG-001` -- Emergency Access (Break-Glass) Standard
- `STD-AGT-001` -- AI Agent Identity Security Standard
- `cyberark_privilege_cloud.md` -- Privilege Cloud capability summary
- `cyberark_conjur.md` -- Conjur secrets management capability summary
- `nhi_lifecycle_architecture.md` -- NHI lifecycle architecture
- `workload_identity_architecture.md` -- Workload identity patterns
- `compliance_evidence_requirements.md` -- Audit evidence guide

---

## 11. Document History

| Version | Date | Author | Change Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-06-26 | Identity Security Architecture | Initial stub -- Core PAS architecture only |
| 2.0 | 2026-06-26 | Identity Security Architecture | Full rebuild -- Privilege Cloud SaaS, Conjur integration patterns, Secure Cloud Access JIT, Kubernetes/AI agent flows, safe design, network topology, HA, compliance mapping |

---

*This document is part of the Go Cloud Architects Identity Governance RAG Assistant knowledge base. It is an original architecture document grounded in CyberArk Privilege Cloud documentation (https://docs.cyberark.com/privilege-cloud-shared-services/), CyberArk Conjur documentation (https://docs.cyberark.com/conjur-open-source/), NIST SP 800-53 Rev. 5, PCI DSS v4.0, and SOX ITGC control objectives. See SOURCE_INDEX.md for authoritative source citations.*
