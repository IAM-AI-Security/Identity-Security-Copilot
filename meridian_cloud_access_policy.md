# Meridian Financial Group
## Cloud Access Policy
**Policy ID:** MFG-CLD-001  
**Version:** 2.1  
**Effective Date:** January 1, 2026  
**Next Review:** January 1, 2027  
**Policy Owner:** Chief Information Security Officer  
**Maintained By:** Cloud Security Team  
**Classification:** Internal — Restricted  
**Regulatory Alignment:** SOX ITGC, FFIEC, PCI DSS v4.0, NIST SP 800-207

---

## 1. Purpose and Scope

This policy governs all human and machine access to Meridian Financial Group's cloud environments including Amazon Web Services (AWS), Microsoft Azure, and any future cloud providers. It establishes requirements for authentication, authorization, session management, and audit logging for cloud access.

This policy applies to all Meridian employees, contractors, and automated workloads accessing Meridian cloud accounts regardless of location or device.

---

## 2. Cloud Account Inventory

Meridian operates the following cloud account structure:

| Account | Environment | Purpose | Data Classification |
| :--- | :--- | :--- | :--- |
| 533267438355 | Production — Core | Core banking, payment processing | PCI, SOX, Regulated |
| MFG-AWS-Prod-Security | Production — Security | SIEM, PAM infrastructure, security tooling | Regulated |
| MFG-AWS-NonProd | Non-Production | Development, testing, staging | Internal |
| MFG-AWS-Sandbox | Sandbox | Architecture proof-of-concept | Public |
| MFG-Azure-Prod | Production | Entra ID, M365, Azure workloads | SOX, Regulated |

All cloud accounts are managed under Meridian's AWS Organizations structure with Service Control Policies (SCPs) enforced at the Organization Unit level.

---

## 3. Authentication Requirements

### 3.1 Human Access
All human access to Meridian cloud accounts must authenticate through Meridian's enterprise identity provider:
- **AWS:** Authentication via AWS IAM Identity Center federated to Okta. Direct IAM user access is prohibited for human users except designated break-glass accounts.
- **Azure:** Authentication via Entra ID with Conditional Access policies enforced. Direct service account logins are prohibited.
- **MFA:** Phishing-resistant MFA (FIDO2 hardware key or Microsoft Authenticator with number matching) is required for all cloud console access. SMS-based MFA is prohibited.

### 3.2 Machine Access
All automated workloads, CI/CD pipelines, and AI agents must authenticate using:
- AWS Lambda and ECS: IAM execution roles via IRSA or task role (no static access keys)
- Kubernetes pods: IRSA (IAM Roles for Service Accounts) via OIDC
- Cross-service calls: AWS STS AssumeRole with scoped session policies
- Secrets retrieval: CyberArk Conjur JWT authentication (see MFG-NHI-001)

Static AWS access keys for machine identities are prohibited. Discovery of a static access key in use by an automated workload is a Critical finding requiring same-business-day revocation.

---

## 4. Authorization — Permission Set Design

Meridian uses AWS IAM Identity Center Permission Sets for all human cloud access. Permission sets follow the principle of least privilege and are reviewed quarterly.

### 4.1 Standard Permission Sets

| Permission Set | AWS Managed Policy Base | Allowed Accounts | Max Session |
| :--- | :--- | :--- | :--- |
| MFG-ReadOnly | ReadOnlyAccess | All accounts | 12 hours |
| MFG-Developer | PowerUserAccess minus IAM | NonProd, Sandbox | 8 hours |
| MFG-SecurityAudit | SecurityAudit | All accounts | 8 hours |
| MFG-CloudEngineer | Custom — infrastructure only | NonProd | 8 hours |
| MFG-ProdAdmin | AdministratorAccess | Production — JIT only | 4 hours |
| MFG-BreakGlass | AdministratorAccess | All accounts — emergency only | 4 hours |

### 4.2 Prohibited Permission Configurations
- AdministratorAccess as a standing assignment to any human user in production accounts
- Wildcard actions (`"Action": "*"`) in customer-managed IAM policies
- Wildcard resources (`"Resource": "*"`) combined with sensitive actions (iam:*, s3:Delete*, ec2:Terminate*)
- Cross-account trust policies without explicit CISO approval
- IAM users with console access in production accounts (federation required)

---

## 5. Just-In-Time Access Requirements -- JIT Provisioning via CyberArk SCA

All production account access at MFG-ProdAdmin level or above is provisioned Just-In-Time via CyberArk Secure Cloud Access:

**Request Process:**
1. Engineer submits access request in ServiceNow with business justification and change ticket reference
2. Manager approves in ServiceNow (automated notification)
3. Cloud Security team approves for MFG-ProdAdmin and above
4. CISO approves for any access to MFG-AWS-Prod-Security account
5. CyberArk SCA provisions temporary role with specified permission set
6. Federation token issued to engineer — valid for approved session duration
7. At expiry, role is automatically revoked

All JIT sessions are logged to CloudTrail and forwarded to Splunk. Session recordings are retained for 12 months.

---

## 6. Service Control Policies

Meridian enforces the following SCPs at the Organization Unit level. These cannot be overridden by any IAM policy, including AdministratorAccess:

| SCP | Purpose | Accounts Affected |
| :--- | :--- | :--- |
| MFG-SCP-DenyRootUsage | Prevent root account API calls | All accounts |
| MFG-SCP-RequireMFA | Deny console access without MFA | All accounts |
| MFG-SCP-DenyRegionUsage | Restrict to us-east-1 and us-west-2 only | All accounts |
| MFG-SCP-DenyIAMUserCreation | Prevent IAM user creation by non-Identity team | Production accounts |
| MFG-SCP-RequireEncryption | Deny unencrypted S3 bucket creation | All accounts |
| MFG-SCP-DenyPublicS3 | Prevent public S3 bucket ACLs | All accounts |
| MFG-SCP-LimitEC2Types | Restrict to approved EC2 instance types | Production accounts |

SCPs are version-controlled in Terraform and changes require Identity Security Architecture + CISO approval.

---

## 7. CloudTrail and Audit Logging

CloudTrail is enabled in all Meridian AWS accounts with the following configuration:
- Multi-region trail covering all regions (even restricted ones, for detection)
- S3 log delivery to MFG-AWS-Prod-Security account (cross-account, immutable)
- CloudTrail log file integrity validation enabled
- CloudWatch Logs integration for real-time SIEM forwarding
- Minimum retention: 7 years (S3 Glacier for years 2-7)

The following CloudTrail events generate immediate SOC alerts:
- Any root account API call
- IAM policy creation or modification in production accounts
- Security group modification allowing 0.0.0.0/0 inbound
- S3 bucket policy modification making bucket public
- CloudTrail logging disabled or modified
- Any MFG-ProdAdmin session accessing IAM modify actions outside a change window
- GuardDuty High or Critical finding

---

## 8. IAM Access Analyzer

AWS IAM Access Analyzer is enabled in all Meridian accounts and in the AWS Organizations master account for cross-account analysis.

Findings are reviewed weekly by the Cloud Security team:
- Critical findings (external access to sensitive resources): remediate within 24 hours
- High findings (unused permissions, broad access): remediate within 14 days
- Medium findings: remediate within 30 days or accept with CISO documentation

IAM Access Analyzer findings are exported to ServiceNow automatically and tracked as security tickets.

---

## 9. Compliance Mapping

| Control | SOX ITGC | NIST SP 800-53 | PCI DSS v4.0 | FFIEC |
| :--- | :--- | :--- | :--- | :--- |
| Federation-only access | CC6.1 | AC-2, IA-8 | Req 8.2 | Access Controls |
| MFA requirement | CC6.1 | IA-2(1), IA-2(2) | Req 8.4 | Authentication |
| JIT for production | CC6.1 | AC-2(7), AC-6 | Req 7.2 | Least Privilege |
| Session duration limits | CC6.1 | AC-12 | Req 8.2.8 | Session Controls |
| SCP guardrails | CC5.2 | AC-3, AC-6(9) | Req 7.3 | Access Controls |
| CloudTrail logging | CC7.2 | AU-2, AU-12 | Req 10.2 | Audit Trail |
| Access Analyzer reviews | CC5.2 | CA-7, AC-2(7) | Req 7.2.3 | Continuous Monitoring |

---

*Meridian Financial Group — Internal Policy Document. Not for external distribution. Questions: cloud-security@meridianfinancial.com*
