# Model Risk Management Guidance (SR 11-7 / SR 26-02) Summary

This document summarizes the principles of Model Risk Management as defined by the Federal Reserve and OCC. While historically known as SR 11-7, this guidance was superseded in April 2026 by the revised SR 26-02 / OCC Bulletin 2026-13. The core principles remain foundational for governing AI and quantitative models.

## Definition of Model Risk

Model risk occurs when a model is used to measure quantitative information, but the model performs inadequately or is used incorrectly. This can lead to financial loss, poor business decisions, or reputational damage.

## Core Elements of Model Risk Management

### 1. Model Development, Implementation, and Use
- **Purpose and Design:** Models must have a clear statement of purpose and design aligned with their intended use.
- **Data and Information:** The data used to develop the model must be rigorous and relevant.
- **Identity Governance Context:** Access to training data, model weights, and the deployment pipeline must be strictly controlled and audited to ensure data integrity and prevent unauthorized modifications.

### 2. Model Validation
Model validation is an independent review process to ensure the model is performing as expected.
- **Evaluation of Conceptual Soundness:** Assessing the quality of the model design and construction.
- **Ongoing Monitoring:** Verifying that the model is implemented correctly and continues to perform as intended.
- **Outcomes Analysis:** Comparing model outputs to actual outcomes.
- **Identity Governance Context:** The validation team must be logically separated from the development team (Separation of Duties). Access controls must enforce this separation.

### 3. Governance, Policies, and Controls
Strong governance provides oversight and accountability.
- **Board and Management Oversight:** The board of directors and senior management are responsible for establishing a strong model risk management framework.
- **Policies and Procedures:** Formalized, documented policies must dictate how models are developed, validated, and used.
- **Internal Audit:** Internal audit must verify that the model risk management framework is functioning effectively.
- **Identity Governance Context:** All model changes must be traceable to a specific, authenticated identity. Privileged access to model hosting environments must be managed via PAM solutions.

## Reference
Revised Guidance on Model Risk Management (SR 26-02). [https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf)
