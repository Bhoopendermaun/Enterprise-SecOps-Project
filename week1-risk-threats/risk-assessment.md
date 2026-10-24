# Comprehensive Enterprise Risk Assessment

## Risk Scoring Methodology
* **Likelihood Scale:** 1 (Rare) to 5 (Almost Certain)
* **Impact Scale:** 1 (Insignificant) to 5 (Catastrophic)
* **Risk Score Matrix:** Risk Score = Likelihood x Impact
  * **Critical:** 20–25 | **High:** 12–19 | **Medium:** 6–11 | **Low:** 1–5

## Enterprise Risk Register

| Risk ID | Vulnerability / Threat Scenario | Affected Asset | Likelihood | Impact | Pre-Mitigation Score | Current Security Controls | Mitigating Strategy / Countermeasure | Post-Mitigation Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :---: |
| **RSK-001** | **Unpatched Zero-Day/N-Day in External VPN Gateway:** Remote Code Execution via unauthenticated API endpoint. | `VPN-GW-01` | 4 | 5 | **20 (Critical)** | Edge Firewall, Local Auth | Deploy Multi-Factor Authentication (MFA), patch cadence within 24 hours, mandate ZTNA. | 6 (Medium) |
| **RSK-002** | **Credential Stuffing on Employee Email / SSO:** Lack of mandatory FIDO2 MFA allowing account takeover. | `M365-TENANT-01` | 5 | 4 | **20 (Critical)** | Basic Password Policy | Enforce phishing-resistant Hardware Tokens (FIDO2 WebAuthn) and Conditional Access rules. | 5 (Low) |
| **RSK-003** | **Unauthenticated Active Directory Kerberoasting:** Weak passwords on service accounts bound to SPNs. | `DC01.corp.internal` | 4 | 4 | **16 (High)** | Local AD Policies | Implement Group Managed Service Accounts (gMSA) and set 128-character passwords. | 4 (Low) |
| **RSK-004** | **SQL Injection in Legacy Payment Application:** Unsanitized user inputs allowing data extraction. | `APP-PAY-GW01` | 3 | 5 | **15 (High)** | Basic WAF rules | Enforce parameterized queries/ORMs, WAF blocking rules, and CI/CD SAST/DAST scanning. | 3 (Low) |
| **RSK-005** | **Ransomware Execution via Phishing Artifacts:** User runs malicious macro or executable payload. | Fleet (`CORP-LAP`) | 4 | 4 | **16 (High)** | Standard Antivirus | Deploy EDR in blocking mode, implement Application Whitelisting (AppLocker). | 4 (Low) |
