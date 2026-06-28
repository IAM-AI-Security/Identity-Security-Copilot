# Access Approval Decision Matrix

This matrix defines the required approval chains for different types of access requests across the enterprise.

| Access Type | Target System/Resource | Required Approvers | SLA for Approval | Review Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **Birthright** | Email, Intranet, Basic Productivity | Auto-provisioned (HR trigger) | Immediate | Annual |
| **Standard User** | Business Applications (e.g., Salesforce, Jira) | Direct Manager | 48 hours | Annual |
| **Sensitive Data** | HR systems, Financial systems (read-only) | Manager + Data Owner | 72 hours | Semi-Annual |
| **Developer** | Non-Production AWS/Azure, Source Code Repos | Manager | 48 hours | Semi-Annual |
| **Privileged (Cloud)** | AWS Production (Admin), Azure Production (Contributor) | Manager + Cloud Security | 24 hours | Quarterly |
| **Privileged (On-Prem)** | CyberArk Safes, Domain Admin, Root | Manager + IAM Security | 24 hours | Quarterly |
| **Break-Glass** | Emergency accounts (AWS Root, CyberArk Master) | Dual Approval (CISO + VP Infrastructure) | Immediate | Monthly |
| **Non-Human (Service Account)** | Application integration, CI/CD pipelines | Manager + Architecture Review Board | 5 Days | Semi-Annual |

## Rules for Exceptions
1. **Manager Unavailability:** If a direct manager is unavailable, the request escalates to the manager's manager (skip-level).
2. **Self-Approval Prohibited:** An individual cannot approve their own access request under any circumstances (Separation of Duties).
3. **Contractors:** All contractor requests must be approved by their FTE sponsor, regardless of the access type.
