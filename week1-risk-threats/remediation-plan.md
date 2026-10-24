# Prioritized Vulnerability Remediation Plan

## SLA Framework
* **Critical Risk:** Remediation within **7 days** (Emergency Patch Window).
* **High Risk:** Remediation within **30 days** (Standard Patch Window).
* **Medium Risk:** Remediation within **60 days**.
* **Low Risk:** Remediation within **90 days** or accepted.

## Remediation Tracks & Timeline

### Phase 1: Emergency Actions (Days 1–7)
* **Action 1:** Apply zero-day security updates to Edge VPN Gateway (`VPN-GW-01`) [RSK-001].
* **Action 2:** Enforce global Azure AD Conditional Access policy requiring FIDO2 tokens for all administrative and remote user access [RSK-002].
* **Action 3:** Execute global S3 `BlockPublicAccess` setting across AWS Organizations [RSK-006].

### Phase 2: High-Priority Hardening (Days 8–30)
* **Action 1:** Convert legacy Active Directory service accounts to Group Managed Service Accounts (gMSA) [RSK-003].
* **Action 2:** Deploy WAF rules to block SQL Injection patterns and implement dynamic parameter validation on legacy payment applications [RSK-004].
* **Action 3:** Enable EDR automated blocking modes and AppLocker endpoint rules to block unauthorized binary execution [RSK-005].

### Phase 3: Medium/Long-Term Remediation (Days 31–90)
* **Action 1:** Implement Pod Security Admissions and Falco runtime detection in Kubernetes clusters [RSK-010].
* **Action 2:** Isolate legacy OS workloads into dedicated, microsegmented VLANs with strict firewall rules [RSK-013].
* **Action 3:** Integrate TruffleHog automated secret scanning into GitHub CI/CD pre-commit hooks [RSK-011].
