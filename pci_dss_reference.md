# PCI DSS v4.0.1 Reference -- Identity and Access Control Requirements
## Payment Card Industry Data Security Standard

**Source:** PCI DSS v4.0.1, PCI Security Standards Council (2024)

---

## 1. Overview

PCI DSS applies to all entities that store, process, or transmit cardholder data (CHD) or sensitive authentication data (SAD). It consists of 12 requirements organized into six goals.

**Cardholder Data Environment (CDE):** Systems that store, process, or transmit CHD or SAD, and systems that can connect to or impact the security of those systems.

**Applicability:** Any organization that accepts, processes, stores, or transmits payment card data -- merchants, service providers, financial institutions.

---

## 2. Identity-Relevant Requirements

### Requirement 7 -- Restrict Access to System Components and Cardholder Data by Business Need to Know

**7.1 -- Processes and mechanisms for restricting access are defined and understood**
- 7.1.1: All security policies addressing Requirement 7 are documented, kept current, and in use
- 7.1.2: Roles and responsibilities for performing activities in Requirement 7 are documented, assigned, and understood

**7.2 -- Access to system components and data is appropriately defined and assigned**

**7.2.1:** An access control model is defined and includes:
- Access needs for each role including system components and data resources each role needs
- Level of privilege required for each role
- Appropriate access controls covering least privilege

**7.2.2:** Access is assigned to users based on:
- Job classification and function
- Least privilege (minimum access necessary to perform job function)
- Need-to-know

**7.2.3:** Required privileges are approved by authorized personnel

**7.2.4:** All user accounts and access privileges are reviewed at minimum every **6 months** to confirm user accounts and access remain appropriate.
- Reviews must confirm whether access privileges are still appropriate for the user's job function
- Inappropriate or excessive access must be removed
- Management must acknowledge that access is appropriate for each account reviewed

**7.2.5:** All application and system accounts and related access privileges are reviewed at minimum every **6 months**
- Reviews must confirm accounts are necessary for the defined business purpose
- Accounts that are no longer needed must be removed or disabled

**7.2.6:** All user access to query repositories of cardholder data is restricted via application layer security

**7.3 -- Access to system components and data is managed via an access control system**
- 7.3.1: An access control system is in place that restricts access based on need-to-know and is set to "deny all" by default
- 7.3.2: The access control system is configured to enforce permissions assigned to individuals, applications, and systems based on the access control model
- 7.3.3: The access control system is kept current

---

### Requirement 8 -- Identify Users and Authenticate Access to System Components

**8.1 -- Processes and mechanisms for identifying users and authenticating access are defined and understood**

**8.2 -- User identification and related accounts for users and administrators are strictly managed**

**8.2.1:** All user IDs and authentication credentials are managed as follows:
- Only authorized users, applications, and devices can access system components
- Access is revoked immediately when no longer required
- Generic, shared, or default credentials are not used

**8.2.2:** Group, shared, or generic accounts and authentication credentials are not used except where specifically required for operational necessity. When used:
- Account use is monitored when used by individuals
- Shared credentials are changed as often as possible, immediately after shared use

**8.2.3:** Additional requirement for service providers: User IDs and related accounts for third-party/vendor remote access are managed as follows:
- Enabled only during the time period needed and disabled when not in use
- Usage is monitored for unexpected activity

**8.2.4:** Addition, deletion, and modification of user IDs, authentication credentials, and other identifier objects are managed as follows:
- Managed according to an authorization process
- Changes to user accounts are authorized

**8.2.5:** Access for terminated users is immediately revoked

**8.2.6:** Inactive user accounts are removed or disabled within **90 days** of inactivity

**8.2.7:** Accounts used by third parties to access, support, or maintain system components via remote access are managed as follows:
- Enabled only during the time period needed
- Disabled when not in use
- Use is monitored for unexpected activity

**8.2.8:** If a user session is idle for more than 15 minutes, the session is re-authenticated

**8.3 -- User authentication for users and administrators is established and managed**

**8.3.1:** All user passwords and passphrases for user authentication must meet the following minimum level of complexity:
- Minimum length of 12 characters (or if the system does not support 12, a minimum of 8 characters)
- Contains both numeric and alphabetic characters

**8.3.2:** Strong cryptography is used to render all authentication credentials unreadable during transmission and storage

**8.3.3:** User identity is verified before modifying any authentication factor

**8.3.4:** Invalid authentication attempts are limited as follows:
- A maximum of 10 attempts before the account is locked
- Lock-out duration of a minimum of 30 minutes or until the account is reset by an administrator

**8.3.5:** If passwords or passphrases are used as authentication factors, they do not match any of the last four passwords used

**8.3.6:** If passwords or passphrases are used as authentication factors, they must be changed at least once every 90 days. Alternatively, real-time security posture assessment (e.g., behavioral analytics) may be used.

**8.3.7:** Individuals are not allowed to submit a new password or passphrase that is the same as any of the last four they have used

**8.3.8:** Authentication policies and procedures are documented and communicated to all users including: guidance on selecting strong authentication credentials, guidance for protecting their authentication credentials, instructions not to reuse previously used passwords

**8.3.9:** If passwords or passphrases are used as the only authentication factor for user access (not system/application accounts), either change passwords at least once every 90 days, OR dynamically analyze account security posture to assess risk and protect account access

**8.3.10:** Additional guidance for passwords:
- Passwords must be changed immediately if there is suspicion the password has been compromised
- Password change confirmation required

**8.4 -- Multi-factor authentication is implemented to secure access to the CDE**

**8.4.1:** MFA is implemented for all non-console access into the CDE for personnel with administrative access

**8.4.2:** MFA is implemented for all access into the CDE

**8.4.3:** MFA systems are implemented as follows:
- MFA cannot be bypassed by any individual including administrative users
- MFA is not subject to replay attacks
- MFA uses at least two different authentication factors

**8.5 -- Multi-factor authentication systems are configured and managed**

**8.5.1:** MFA systems are configured and managed to prevent misuse:
- MFA cannot be bypassed by any individual including administrative users
- Non-successful authentication is handled appropriately
- MFA is not subject to replay attacks
- MFA uses at least two different authentication factors

**8.6 -- Use of application and system accounts and associated authentication factors is strictly managed**

**8.6.1:** If accounts used by systems or applications can be used for interactive login, they are managed as follows:
- Interactive use is prevented unless needed for an exceptional circumstance
- Interactive use is limited to the time needed for the exceptional circumstance
- Business justification is documented
- Interactive use is explicitly authorized by management
- Individual user identity is confirmed before access to account is granted

**8.6.2:** Passwords or passphrases for application and system accounts that can be used for interactive login are not hard-coded in scripts, configuration/property files, or custom/bespoke source code

**8.6.3:** Passwords or passphrases for application and system accounts are protected against misuse:
- Passwords are changed periodically (per the entity's risk analysis) and after any suspected compromise
- Passwords are constructed with sufficient complexity appropriate for how frequently the credential is changed
- Passwords are reviewed (manually or automated) at least once every 12 months to confirm whether change is needed

---

### Requirement 10 -- Log and Monitor All Access to System Components and Cardholder Data

**10.1 -- Processes and mechanisms for logging and monitoring all access are defined and understood**

**10.2 -- Audit logs are implemented to support the detection of anomalies and suspicious activity**

**10.2.1:** Audit logs capture all individual user access to cardholder data (10.2.1.1), all actions taken by root or administrative privileges (10.2.1.2), access to all audit logs (10.2.1.3), invalid logical access attempts (10.2.1.4), use of and changes to identification and authentication mechanisms including changes to accounts such as elevation of privileges, and all changes, additions, and deletions to accounts with root or administrative privileges (10.2.1.5), initialization, stopping, or pausing of the audit logs (10.2.1.6), creation and deletion of system-level objects (10.2.1.7)

**10.2.2:** Audit logs capture all individual user access to system components

**10.3 -- Audit logs are protected from destruction and unauthorized modifications**

**10.3.1:** Read access to audit log files is limited to those with a job-related need

**10.3.2:** Audit log files are protected to prevent modifications by individuals

**10.3.3:** Audit log files are backed up to a central log server or media that is difficult to alter

**10.3.4:** File-integrity monitoring or change-detection mechanisms are used on audit logs

**10.4 -- Audit logs are reviewed to identify anomalies or suspicious activity**

**10.4.1:** Daily review of the following audit log events:
- All security events
- Logs of all system components that store, process, or transmit CHD or SAD
- Logs of all critical system components
- Logs of all servers and system components that perform security functions

**10.4.2:** Logs of all other system components are reviewed periodically

**10.4.3:** Exceptions and anomalies identified during the review process are addressed

**10.5 -- Audit log history is retained and available for analysis**

**10.5.1:** Retain audit log history for at least **12 months** with at least the most recent **3 months** available for immediate analysis

**10.6 -- Time-synchronization mechanisms support consistent time settings across all systems**

**10.7 -- Failures of critical security controls are detected, reported, and responded to promptly**

---

## 3. Service Provider Additional Requirements

Service providers face additional requirements:

- Maintain an inventory of all hardware and software used to provide services to customers (12.5.2.1)
- Perform reviews at least every 6 months to confirm personnel are following security policies and procedures (12.11)
- Provide written agreement to customers detailing which PCI DSS requirements the service provider manages (12.9.1)

---

## 4. PCI DSS Access Review Requirements Summary

| Requirement | Frequency | Scope |
|---|---|---|
| User access reviews (7.2.4) | Every 6 months | All user accounts and access privileges |
| Application/system account reviews (7.2.5) | Every 6 months | All application and system accounts |
| Inactive account removal (8.2.6) | Within 90 days of inactivity | All user accounts |
| Session re-authentication (8.2.8) | After 15 minutes idle | All user sessions |
| Password changes (8.3.6/8.3.9) | Every 90 days | All user passwords |
| System account password review (8.6.3) | At least every 12 months | Application and system accounts |
| Audit log review (10.4.1) | Daily | Security events and critical systems |
| Log retention (10.5.1) | 12 months total, 3 months immediately available | All audit logs |

---

## 5. PCI DSS and CyberArk Alignment

| PCI DSS Requirement | CyberArk Control |
|---|---|
| 7.2 -- Least privilege access | Safe-level permissions, granular entitlements |
| 7.2.4 -- Access reviews | Privileged access review reports |
| 8.2.1 -- No shared accounts | Individual vault accounts, no shared credentials |
| 8.2.5 -- Immediate revocation on termination | Automated account deactivation |
| 8.2.6 -- Inactive account removal | Dormancy detection and alerts |
| 8.3.2 -- Encryption of credentials | AES-256 encryption in CyberArk vault |
| 8.4 -- MFA | CyberArk MFA enforcement |
| 8.6.2 -- No hardcoded passwords | Conjur secrets management |
| 10.2.1 -- Audit all privileged access | PSM session recording, CPM audit logs |
| 10.3 -- Protect audit logs | Immutable vault audit trail |

---

## 6. Compensating Controls

When an entity cannot meet a PCI DSS requirement as stated due to legitimate documented technical or business constraints, compensating controls may be considered if they:

- Meet the intent and rigor of the original PCI DSS requirement
- Provide a similar level of defense as the original requirement
- Are above and beyond other PCI DSS requirements

Compensating controls must be documented, reviewed by a QSA, and include the constraints, objective, identified risks, definition of compensating controls, and validation and maintenance.
