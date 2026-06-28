# IAM Policy Review Guide

## 1. Overview
This guide establishes the standard operating procedure for reviewing Identity and Access Management (IAM) policies. It enforces the principle of least privilege, ensuring that users and workloads are granted only the permissions required to perform their assigned tasks [1].

## 2. Core Review Principles

When reviewing a custom IAM policy, the reviewer must verify compliance with the following AWS security best practices [1]:

1. **No Long-Term Credentials for Workloads:** Workloads must use temporary credentials via IAM roles. Long-term access keys must not be hardcoded or embedded in applications [1].
2. **Federated Access for Humans:** Human users must access the environment via federation (e.g., IAM Identity Center) using temporary credentials, rather than using long-lived IAM user access keys [1].
3. **Condition Keys:** Policies should use condition keys (e.g., `aws:SourceIp`, `aws:PrincipalOrgID`) to further restrict access based on network origin or organizational boundaries [1].
4. **Least Privilege:** Policies must not use overly permissive wildcards (e.g., `Action: "*"`, `Resource: "*"`) unless strictly necessary and documented. Permissions must be scoped to specific actions and specific resource ARNs [1].

## 3. Automated Policy Validation

Manual review is prone to human error. All IAM policies must be evaluated using automated tooling before deployment.

- **IAM Access Analyzer Policy Validation:** Reviewers must run the policy through AWS IAM Access Analyzer. This tool validates the policy against IAM grammar and AWS best practices, generating actionable findings categorized as Security Warnings, Errors, General Warnings, and Suggestions [2].
- **Security Warnings:** Any finding flagged as a "Security Warning" (indicating overly permissive access) must be resolved before the policy is approved [2].
- **Errors:** Any syntax errors must be fixed to ensure the policy functions correctly [2].

## 4. Unused Access Reviews

Least privilege is an ongoing process, not a one-time configuration.

- **Access Analyzer Unused Access:** The organization must utilize IAM Access Analyzer to generate findings for unused access. Permissions, roles, or users that have not been used within the organization-defined time period must be reviewed and removed to rightsize permissions [1].

## References
[1] AWS. "Security best practices in IAM." https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
[2] AWS. "Validate policies with IAM Access Analyzer." https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html
