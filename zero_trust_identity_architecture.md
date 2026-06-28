# Zero Trust Identity Architecture

## 1. Overview
This reference architecture defines the identity components required to implement a Zero Trust Architecture (ZTA) in alignment with NIST SP 800-207. The core tenet is "never trust, always verify," shifting access controls from network perimeters to individual users, devices, and applications.

## 2. Core Identity Components

### A. Policy Decision Point (PDP)
The engine that evaluates access requests against governance rules.
- **Identity Provider (IdP):** (e.g., Okta, Entra ID) Authenticates the user and evaluates contextual signals (device health, location, risk score).
- **Governance Engine:** (e.g., SailPoint) Determines if the user holds the correct, approved entitlements to access the resource.

### B. Policy Enforcement Point (PEP)
The gateway that grants or denies access based on the PDP's decision.
- **SSO Gateways:** Enforce SAML/OIDC authentication before allowing application access.
- **PAM Proxies:** (e.g., CyberArk PSM) Isolate and monitor privileged sessions to critical infrastructure.
- **API Gateways:** Enforce token validation and rate limiting for non-human identities.

## 3. Key Architectural Principles

- **Continuous Verification:** Authentication is not a one-time event. Session risk MUST be continuously evaluated, and access revoked if the context changes (e.g., user moves to a high-risk IP).
- **Dynamic Access:** Standing privileges are minimized. Access is granted Just-In-Time (JIT) and scoped to Just-Enough-Access (JEA).
- **Device Posture:** Access decisions MUST incorporate device health. Unmanaged or compromised devices MUST be denied access to sensitive resources, regardless of user identity.

## 4. Governance Application
When asked to explain Zero Trust, the RAG Assistant MUST emphasize that identity is the new perimeter, relying on continuous verification, contextual signals (user + device), and the elimination of implicit trust based on network location.
