# Authoritative Source Document Index
### Identity Governance RAG Assistant: Knowledge Base Grounding Sources

This index lists every **official, authoritative source document** used to ground the RAG assistant's knowledge base. For RAG, these are the documents you *retrieve from and cite*, not the documents used to "train" the model. Each entry lists the canonical publisher, the current version, the direct official URL, and a licensing/redistribution note so you know what can be bundled into the repo versus what should be summarized and linked.

> **Licensing principle:** U.S. Government works (NIST, Federal Reserve, OCC, AWS public docs) are generally not subject to copyright and may be redistributed with attribution. Vendor documentation (CyberArk, Microsoft, Okta) and consortium content (CIS, OWASP, MITRE) are copyrighted, so **summarize in your own `.md` files and link to the source** rather than redistributing the full PDFs. The `vendors/` and `frameworks/` markdown files in this repo are original summaries written for this purpose; the URLs below are the citations.

---

## 1. NIST Frameworks (U.S. Government: public domain, redistributable with attribution)

| Document | Version / ID | Official Source URL |
| :--- | :--- | :--- |
| Security and Privacy Controls for Information Systems and Organizations | SP 800-53 Rev. 5 (Release 5.2.0, Aug 2025) | https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-53r5.pdf |
| Guide for Conducting Risk Assessments | SP 800-30 Rev. 1 | https://csrc.nist.gov/pubs/sp/800/30/r1/final |
| Landing page / control catalog (CPRT) | SP 800-53 Rev. 5 | https://csrc.nist.gov/pubs/sp/800/53/r5/final |
| Zero Trust Architecture | SP 800-207 | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf |
| Zero Trust landing page | SP 800-207 | https://csrc.nist.gov/pubs/sp/800/207/final |
| Artificial Intelligence Risk Management Framework | AI RMF 1.0 (NIST AI 100-1) | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf |
| AI RMF landing page | AI 100-1 | https://www.nist.gov/itl/ai-risk-management-framework |
| Cybersecurity Framework 2.0 | CSF 2.0 (NIST CSWP 29) | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf |

## 2. AI / LLM Security Frameworks (consortium: copyrighted, summarize + link)

| Document | Version | Official Source URL |
| :--- | :--- | :--- |
| OWASP Top 10 for LLM Applications | 2025 | https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf |
| OWASP Gen AI Security Project (living) | 2025 | https://genai.owasp.org/llm-top-10/ |
| MITRE ATLAS (adversarial threats to AI systems) | Living KB | https://atlas.mitre.org/ |

## 3. Model Risk Governance (U.S. Government: public domain)

| Document | Version | Official Source URL |
| :--- | :--- | :--- |
| **Revised Guidance on Model Risk Management** (supersedes SR 11-7 as of 2026-04-17) | SR 26-02 / OCC Bulletin 2026-13 | https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf |
| Supervisory Guidance on Model Risk Management (predecessor, still widely referenced) | SR 11-7 (2011) | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm |

> **Scope note.** SR 26-02 places generative and agentic AI models outside its scope at footnote 3, while directing that an organization's own risk management practices should govern systems the guidance does not cover. This assistant is generative, so the guidance does not apply to it by its own terms. It is indexed here because the knowledge base retrieves and cites it, not because this system claims conformance with it. See `MODEL_RISK.md`.

## 4. Cloud Security Benchmarks (CIS: copyrighted, free download w/ registration; summarize + link)

| Document | Version | Official Source URL |
| :--- | :--- | :--- |
| CIS Amazon Web Services Foundations Benchmark | v5.0.0 (latest) | https://www.cisecurity.org/benchmark/amazon_web_services |
| CIS Microsoft 365 Foundations Benchmark | latest | https://www.cisecurity.org/benchmark/microsoft_365 |

## 5. Vendor Governance Documentation (copyrighted: summarize + link)

### CyberArk
| Topic | Official Source URL |
| :--- | :--- |
| Docs home | https://docs.cyberark.com/ |
| PAM Self-Hosted Architecture | https://docs.cyberark.com/pam-self-hosted/latest/en/content/pasimp/privileged-account-security-solution-architecture.htm |
| Privilege Cloud | https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/resources/_topnav/cc_home.htm |
| Conjur (Secrets Manager / open source) | https://docs.cyberark.com/conjur-open-source/latest/en/content/resources/_topnav/cc_home.htm |
| Secrets Manager (SaaS) | https://docs.cyberark.com/secrets-manager-saas/latest/en/content/resources/_topnav/cc_home.htm |
| Secure Cloud Access / Secure Infrastructure Access | https://docs.cyberark.com/ (Secure Cloud Access section) |
| Certificate Manager | https://docs.cyberark.com/ (Certificate Manager section) |

### Microsoft Entra
| Topic | Official Source URL |
| :--- | :--- |
| Emergency Access Accounts | https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access |
| Entra ID Governance overview | https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview |
| Privileged Identity Management (PIM) | https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure |
| Conditional Access | https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview |
| Microsoft Graph API | https://learn.microsoft.com/en-us/graph/overview |

### Okta
| Topic | Official Source URL |
| :--- | :--- |
| Lifecycle Management | https://www.okta.com/products/lifecycle-management/ |
| SCIM concept | https://developer.okta.com/docs/concepts/scim/ |
| Lifecycle mgmt (OIN) | https://developer.okta.com/docs/guides/oin-lifecycle-mgmt-overview/ |

### AWS (public docs: generally redistributable with attribution)
| Topic | Official Source URL |
| :--- | :--- |
| IAM Security Best Practices | https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html |
| Validate policies with IAM Access Analyzer | https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html |
| IAM Identity Center: permission sets | https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html |
| IAM Access Analyzer | https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html |
| AWS Secrets Manager | https://docs.aws.amazon.com/secretsmanager/ |
| Organizations / SCPs | https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html |

---

## Redistribution Quick-Reference

| Source | Bundle full PDF in repo? | Recommended approach |
| :--- | :---: | :--- |
| NIST (800-53, 800-207, AI RMF, CSF) | Yes (public domain) | Place PDFs in `knowledge_base/sources/`, summarize key controls in `frameworks/*.md` |
| Federal Reserve / OCC model-risk guidance | Yes (public domain) | Same as above |
| AWS public documentation | Yes (with attribution) | Summarize; optionally save HTML/PDF |
| OWASP LLM Top 10 | Check CC license (usually CC BY-SA) | Summarize + attribute + link |
| MITRE ATLAS | Copyrighted, terms of use | Summarize + link, do not bundle |
| CIS Benchmarks | No (license restricts redistribution) | Summarize controls + link; do not bundle the PDF |
| CyberArk / Microsoft / Okta docs | No (vendor copyright) | Write original summaries; cite URLs |

**Bottom line for the repo:** bundle the NIST and Federal Reserve PDFs (public domain) under `knowledge_base/sources/`, and for everything copyrighted, rely on the original summary `.md` files in this repo with citations to the official URLs above. This keeps the project clean, legal, and enterprise-credible.
