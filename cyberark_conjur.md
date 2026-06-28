# CyberArk Conjur (Secrets Manager) Overview

This document summarizes the core capabilities of CyberArk Conjur for securing non-human identities.

## Overview
CyberArk Conjur (also known as Secrets Manager) is a secrets management solution designed specifically for dynamic, cloud-native environments, CI/CD pipelines, and containerized workloads (e.g., Kubernetes). It eliminates the need for hardcoded credentials in source code.

## Core Concepts

### 1. Machine Identity and Authentication
Conjur authenticates non-human identities (applications, scripts, AI agents) using native platform attributes rather than static passwords. For example, it can authenticate a pod based on its Kubernetes Service Account token, or an AWS Lambda function based on its IAM role.

### 2. Role-Based Access Control (RBAC)
Access to secrets is governed by strict RBAC policies defined in declarative YAML files. These policies specify exactly which machine identity can read which secret.

### 3. Dynamic Secrets Delivery
Applications retrieve secrets dynamically at runtime via the Conjur REST API or specialized authenticators (e.g., Kubernetes authenticator, Secretless Broker).

## Enterprise Governance Use Cases

- **CI/CD Pipeline Security:** Removing hardcoded API keys from Jenkins, GitLab, or GitHub Actions pipelines.
- **Kubernetes Workload Identity:** Providing secrets to containers without storing them in native Kubernetes Secrets (which are base64 encoded, not encrypted by default).
- **AI Agent Execution:** Authenticating AI agents via short-lived JWTs to retrieve the API keys necessary to execute their tasks, ensuring the agent cannot leak static credentials.

## Reference
CyberArk Conjur Documentation. [https://docs.cyberark.com/conjur-open-source/latest/en/content/resources/_topnav/cc_home.htm](https://docs.cyberark.com/conjur-open-source/latest/en/content/resources/_topnav/cc_home.htm)
