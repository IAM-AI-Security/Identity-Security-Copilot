# Okta Lifecycle Management & SCIM Overview

This document summarizes Okta's capabilities for automated identity provisioning and lifecycle management.

## Overview
Okta Lifecycle Management automates the Joiner, Mover, Leaver (JML) process by connecting an authoritative HR source (e.g., Workday, BambooHR) to downstream applications (e.g., Salesforce, Slack, Microsoft 365).

## Core Concepts

### 1. Universal Directory
Okta's central repository for all user profiles, groups, and devices. It acts as the single source of truth for identity data across the enterprise.

### 2. Automated Provisioning
When a user is created or updated in the HR system, Okta automatically provisions or updates the corresponding accounts in downstream applications based on predefined group memberships and rules.

### 3. Automated Deprovisioning
When a user is terminated in the HR system, Okta immediately deactivates their accounts across all connected applications, closing a major security gap.

## System for Cross-domain Identity Management (SCIM)

SCIM is an open standard (RFC 7643 and 7644) that facilitates the automated provisioning of user identities.
- **RESTful API:** SCIM provides a defined schema and RESTful API for Create, Read, Update, and Delete (CRUD) operations on user and group resources.
- **Integration:** Applications that support SCIM can be seamlessly integrated with Okta for automated lifecycle management without requiring custom API connectors.

## Okta Workflows
A no-code/low-code platform within Okta that allows administrators to build complex identity automation logic. For example, a workflow could detect a title change in Workday, remove the user from specific Okta groups, add them to new ones, and send a notification to a Slack channel.

## Reference
Okta Lifecycle Management Documentation. [https://www.okta.com/products/lifecycle-management/](https://www.okta.com/products/lifecycle-management/)
