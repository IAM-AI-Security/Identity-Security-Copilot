# NIST SP 800-53 Rev. 5: Access Control (AC) Family Summary

This document summarizes the key Access Control (AC) controls from NIST SP 800-53 Revision 5, tailored for enterprise identity governance.

## AC-2: Account Management
Organizations must manage information system accounts, including establishing, activating, modifying, reviewing, disabling, and removing accounts.
- **Key Requirements:**
  - Assign account managers.
  - Require approvals for account creation.
  - Monitor account usage.
  - Automatically disable inactive accounts.
- **Enterprise Application:** This maps directly to the Joiner, Mover, Leaver (JML) lifecycle processes governed by tools like SailPoint and Okta.

## AC-3: Access Enforcement
The information system must enforce approved authorizations for logical access to information and system resources.
- **Key Requirements:**
  - Enforce access control policies (e.g., identity-based, role-based, or attribute-based access control).
- **Enterprise Application:** Implemented via RBAC/ABAC models in Active Directory, Entra ID, and application-specific permissions.

## AC-5: Separation of Duties
Organizations must separate duties of individuals to prevent malevolent activity without collusion.
- **Key Requirements:**
  - Document separation of duties policies.
  - Define access authorizations to support separation of duties.
- **Enterprise Application:** Configured as SoD policies in Identity Governance and Administration (IGA) platforms to prevent conflicting entitlements (e.g., an individual cannot both request and approve a payment).

## AC-6: Least Privilege
Organizations must employ the principle of least privilege, allowing only authorized accesses for users (and processes acting on behalf of users) which are necessary to accomplish assigned tasks.
- **Key Requirements:**
  - Explicitly authorize access to specific functions and data.
  - Review privileges periodically.
- **Enterprise Application:** Enforced through granular role definitions, Just-In-Time (JIT) access, and continuous privilege drift detection.

## AC-17: Remote Access
Organizations must authorize, monitor, and control all methods of remote access to the information system.
- **Key Requirements:**
  - Establish usage restrictions and implementation guidance for remote access.
  - Route all remote access through managed access control points.
- **Enterprise Application:** Implemented via VPNs, Zero Trust Network Access (ZTNA), and Conditional Access policies requiring MFA for off-network connections.

## Reference
NIST Special Publication 800-53, Revision 5: Security and Privacy Controls for Information Systems and Organizations. [https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-53r5.pdf](https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-53r5.pdf)
