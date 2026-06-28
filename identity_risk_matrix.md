# Identity Risk Matrix

## 1. Overview
The Identity Risk Matrix provides a standardized framework for evaluating the risk associated with access requests, identity misconfigurations, and policy exceptions. It is based on the qualitative risk assessment methodology defined in NIST Special Publication 800-30 Revision 1 [1].

## 2. Risk Determination
Risk is determined by combining the **Likelihood** of a threat exploiting an identity vulnerability with the **Impact** to the organization if the exploit occurs [1].

### 2.1 Likelihood Levels
- **High:** The threat source is highly motivated and capable, and controls to prevent the exploit are ineffective or missing.
- **Medium:** The threat source is motivated and capable, but controls are in place that may impede a successful exploit.
- **Low:** The threat source lacks motivation or capability, or controls are highly effective.

### 2.2 Impact Levels
- **High:** The exploit could result in the compromise of critical production systems, massive data exfiltration, or severe regulatory penalties. Examples include the compromise of a Global Administrator account or an unmonitored break-glass account.
- **Medium:** The exploit could result in the compromise of non-production systems, limited data exposure, or moderate operational disruption. Examples include the compromise of a developer's non-production AWS IAM role.
- **Low:** The exploit would have a negligible impact on operations or data confidentiality. Examples include unauthorized access to a read-only internal cafeteria menu.

## 3. The Risk Matrix

By intersecting Likelihood and Impact, the overall Identity Risk Level is calculated:

| Likelihood \ Impact | Low Impact | Medium Impact | High Impact |
|---------------------|------------|---------------|-------------|
| **High Likelihood** | Low Risk   | High Risk     | Critical Risk |
| **Medium Likelihood**| Low Risk   | Medium Risk   | High Risk   |
| **Low Likelihood**  | Low Risk   | Low Risk      | Medium Risk |

## 4. Required Actions by Risk Level

- **Critical Risk:** Immediate remediation required. Access must be revoked or the vulnerability patched within 24 hours. Exceptions require CISO approval.
- **High Risk:** Remediation required within 7 days. Compensating controls must be implemented immediately. Exceptions require Identity Security Director approval.
- **Medium Risk:** Remediation required within 30 days. Exceptions require System Owner approval.
- **Low Risk:** Remediation prioritized against other backlog items. Risk may be accepted by the System Owner.

## References
[1] NIST. "SP 800-30 Rev. 1: Guide for Conducting Risk Assessments." https://csrc.nist.gov/pubs/sp/800/30/r1/final
