# Privileged Access Decision Tree

## 1. Overview
This decision tree guides identity architects and access reviewers in determining the appropriate provisioning method for privileged access requests. It enforces the principle of least privilege, which requires granting only the authorized access necessary to accomplish assigned tasks [1].

## 2. Decision Logic

When evaluating a request for privileged access, reviewers must follow this logical flow:

**Step 1: Is the requested access for a privileged function?**
- **No:** Provision via standard role-based access control (RBAC) lifecycle processes.
- **Yes:** Proceed to Step 2.

**Step 2: Is the access required for a production environment?**
- **No (Non-Production):** Permanent standing privilege may be granted if strictly scoped to the non-production environment, subject to quarterly review.
- **Yes (Production):** Proceed to Step 3.

**Step 3: Is the access required for an automated workload or service account?**
- **Yes:** Provision via workload identity federation, SPIFFE, or a Secrets Management solution (e.g., CyberArk Conjur). Passwords must be rotated automatically and not known to humans.
- **No (Human User):** Proceed to Step 4.

**Step 4: Is the access required 24/7 for a break-glass emergency scenario?**
- **Yes:** Provision as a dedicated emergency access account. The account must be excluded from federation, use distinct FIDO2 authentication, and trigger immediate Security Operations Center (SOC) alerts upon use [2].
- **No:** Proceed to Step 5.

**Step 5: Provisioning Method (Zero Standing Privilege)**
Human access to production privileged roles must not be permanent. The access must be provisioned using Just-In-Time (JIT) elevation [1].
- The user is granted an *eligible* role assignment, not an *active* assignment.
- When access is needed, the user must request activation for a time-bound period (e.g., 4 hours).
- Activation requires multi-factor authentication and, for critical roles, peer or manager approval.
- Access is automatically revoked when the time window expires.

## 3. Governance Rationale
This decision tree aligns with NIST 800-53 AC-6 (Least Privilege), which mandates that non-privileged users are prevented from executing privileged functions, and that privileged access is strictly controlled and logged [1]. By enforcing JIT for human production access, the organization moves toward Zero Standing Privilege, significantly reducing the attack surface.

## References
[1] NIST. "AC-6 Least Privilege." https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-6/
[2] Microsoft. "Manage emergency access accounts in Microsoft Entra ID." https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access
