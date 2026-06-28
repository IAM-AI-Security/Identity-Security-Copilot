# AWS IAM & Identity Center Overview

This document summarizes the core capabilities of AWS Identity and Access Management (IAM) and IAM Identity Center for enterprise cloud governance.

## IAM Identity Center (formerly AWS SSO)
IAM Identity Center is the recommended service for managing workforce access to multiple AWS accounts and business applications.

### Key Features:
- **Centralized Access:** Connects to an external identity provider (e.g., Okta, Entra ID) to provide SSO across the AWS Organization.
- **Permission Sets:** Templates of IAM policies used to assign access. Permission sets are defined centrally and applied to users/groups across multiple accounts.
- **Multi-Account Governance:** Integrates with AWS Organizations to manage access consistently across the entire cloud estate.

## AWS IAM Best Practices

1. **Require Human Users to Use Federation:** Do not create IAM users for humans; use IAM Identity Center and federate from a central IdP.
2. **Require MFA:** Enforce MFA for all console access and highly privileged API operations.
3. **Use Roles for Applications:** Workloads (EC2, Lambda, EKS) must use IAM roles to obtain temporary credentials, not long-term access keys.
4. **Apply Least Privilege:** Grant only the permissions required to perform a specific task. Use AWS IAM Access Analyzer to refine policies.

## IAM Access Analyzer
A service that helps identify and review access policies.
- **External Access Findings:** Identifies resources (e.g., S3 buckets, IAM roles) that are shared with external entities.
- **Unused Access Findings:** Identifies IAM roles and users that have not been used recently, or permissions within policies that remain unused, enabling continuous privilege drift detection and remediation.

## AWS Secrets Manager
A service that securely encrypts, stores, and retrieves credentials for databases and APIs.
- Eliminates hardcoded credentials in application code.
- Supports automatic secret rotation via AWS Lambda functions.

## Reference
AWS IAM Documentation. [https://docs.aws.amazon.com/iam/](https://docs.aws.amazon.com/iam/)
