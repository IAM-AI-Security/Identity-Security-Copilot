# CyberArk Privilege Cloud Overview

This document summarizes the core capabilities and architecture of CyberArk Privilege Cloud for enterprise identity governance.

## Overview
CyberArk Privilege Cloud is a SaaS-based Privileged Access Management (PAM) solution. It is designed to securely store, rotate, and isolate privileged credentials and sessions, reducing the risk of unauthorized access to critical systems.

## Core Components

### 1. The Vault
The secure, encrypted repository where privileged credentials (passwords, SSH keys) are stored. In Privilege Cloud, the Vault is hosted and managed by CyberArk.

### 2. Central Policy Manager (CPM)
The component responsible for automatically changing passwords on target systems according to organizational policy (e.g., every 30 days, or after every use). The CPM resides on-premises or in the customer's cloud environment to communicate with target systems.

### 3. Privileged Session Manager (PSM)
The component that isolates, controls, and records privileged sessions. Users authenticate to the PSM, which then proxies the connection to the target system without revealing the actual credential to the user.

### 4. Privilege Cloud Portal (PVWA equivalent)
The web interface where users request access, retrieve credentials, or initiate PSM sessions, and where administrators configure policies and Safes.

## Key Governance Features

- **Safe Design:** Credentials are grouped into logical containers called "Safes." Access control (who can retrieve, who can manage) is applied at the Safe level.
- **Just-In-Time (JIT) Access:** Integration with CyberArk Secure Cloud Access or SIA to provide temporary, elevated access rather than standing privileges.
- **Dual Control:** Workflows that require a second user to approve a request before a credential can be retrieved.
- **Session Recording:** Full video and keystroke recording of privileged sessions for audit and compliance (e.g., SOX, PCI-DSS).

## Reference
CyberArk Privilege Cloud Documentation. [https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/resources/_topnav/cc_home.htm](https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/resources/_topnav/cc_home.htm)
