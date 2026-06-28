# OWASP Top 10 for LLM Applications (2025) Summary

This document summarizes the OWASP Top 10 risks for Large Language Model (LLM) applications, focusing on identity and access control implications.

## The Top 10 Risks

1. **LLM01: Prompt Injection**
   - **Description:** Attackers manipulate the LLM via crafted inputs, causing it to execute unintended actions.
   - **Identity Implication:** An injected prompt might trick the LLM into accessing data or executing functions using its own execution role (a confused deputy attack). Strict least privilege on the LLM's service account is critical.

2. **LLM02: Insecure Output Handling**
   - **Description:** Vulnerabilities occur when an downstream component blindly accepts LLM output without validation.
   - **Identity Implication:** If the LLM generates commands or queries, the executing identity must be constrained to prevent unauthorized actions.

3. **LLM03: Training Data Poisoning**
   - **Description:** Tampering with the data used to train or fine-tune the model.
   - **Identity Implication:** Access to training data repositories must be strictly governed and audited to prevent unauthorized modifications.

4. **LLM04: Model Denial of Service**
   - **Description:** Attackers cause resource exhaustion in the LLM service.
   - **Identity Implication:** Rate limiting and authentication must be enforced at the API gateway level to tie usage to specific, authenticated identities.

5. **LLM05: Supply Chain Vulnerabilities**
   - **Description:** Compromises in third-party datasets, pre-trained models, or plugins.
   - **Identity Implication:** Procurement and integration of external models require rigorous vendor identity verification and secure secret management for API keys.

6. **LLM06: Sensitive Information Disclosure**
   - **Description:** The LLM inadvertently reveals sensitive data in its responses.
   - **Identity Implication:** The LLM must not have access to data beyond the authorization level of the user prompting it. Data access must be contextual to the user's identity.

7. **LLM07: Insecure Plugin Design**
   - **Description:** Plugins or tools invoked by the LLM lack proper access controls or validation.
   - **Identity Implication:** Plugins must authenticate the user and enforce authorization checks independently; they should not implicitly trust the LLM's request.

8. **LLM08: Excessive Agency**
   - **Description:** Granting the LLM excessive functionality, permissions, or autonomy.
   - **Identity Implication:** This is a direct failure of least privilege. LLM agents must operate under scoped execution roles with strict boundary policies.

9. **LLM09: Overreliance**
   - **Description:** Systems or users trusting LLM outputs without oversight.
   - **Identity Implication:** Critical actions proposed by an LLM (e.g., modifying access policies) must require human-in-the-loop (dual approval) before execution.

10. **LLM10: Model Theft**
    - **Description:** Unauthorized access, copying, or exfiltration of proprietary LLM models.
    - **Identity Implication:** Access to model weights and hosting infrastructure must be protected by strong PAM controls and MFA.

## Reference
OWASP Top 10 for Large Language Model Applications (2025). [https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
