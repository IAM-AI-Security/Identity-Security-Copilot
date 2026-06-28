# Microsoft Entra ID Governance Overview

This document summarizes the core capabilities of Microsoft Entra ID Governance.

## Overview
Microsoft Entra ID Governance is a comprehensive identity governance and administration (IGA) solution integrated directly into the Entra ID (formerly Azure AD) platform. It helps organizations balance security and productivity by ensuring the right people have the right access to the right resources at the right time.

## Core Capabilities

### 1. Entitlement Management
- **Access Packages:** Bundles of resources (groups, applications, SharePoint sites) that users can request.
- **Lifecycle Workflows:** Automated processes for Joiner, Mover, Leaver (JML) events. For example, automatically granting access when an employee joins and revoking it when they leave.

### 2. Access Reviews
- Automated campaigns that require managers or resource owners to periodically review and certify user access.
- Helps maintain compliance with least privilege principles and regulatory requirements (e.g., SOX).

### 3. Privileged Identity Management (PIM)
- Provides time-bound, Just-In-Time (JIT) access to highly privileged roles in Entra ID and Azure resources.
- Requires justification and/or approval for activation.
- Enforces MFA during role activation.

### 4. Conditional Access
- Evaluates signals (user identity, location, device health, risk score) to make real-time access decisions.
- Can require MFA, block access, or force a password reset based on the evaluated risk.

## Integration with Microsoft Graph API
Entra ID Governance features can be managed and automated programmatically using the Microsoft Graph API, allowing for custom lifecycle workflows and integration with external HR systems or ITSM platforms (e.g., ServiceNow).

## Reference
Microsoft Entra ID Governance Documentation. [https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview)
