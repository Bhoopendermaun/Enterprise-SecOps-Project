# Enterprise Security Assessment Report

## 1. Executive Summary
A comprehensive security assessment was performed across the simulated enterprise infrastructure spanning the DMZ (`10.10.1.0/24`), Core Corporate Servers (`10.20.10.0/24`), Restricted Data Tier (`10.20.20.0/24`), and Corporate Endpoints (`10.30.0.0/16`).

Key systemic weaknesses identified include:
* **Perimeter & Web Exposure:** Unpatched edge VPN gateway software (`VPN-GW-01`) and legacy TLS/input-validation weaknesses on `WEB-GW-01`.
* **Identity & Authentication Weaknesses:** Lack of phishing-resistant MFA (FIDO2) on remote/administrative access, weak service account passwords susceptible to Kerberoasting (`T1558.003`), and legacy authentication allowances.
* **Privilege & Configuration Drift:** Stale/over-privileged accounts in Active Directory and local administrators on workstations (`WS-FIN-042`), alongside unencrypted legacy protocols (`SMBv1`, `HTTP`) and missing database/Kerberos audit telemetry.

---

## 2. Assessment Scope & Methodology
* **In-Scope Systems:** `FW-EDGE-01`, `VPN-GW-01`, `WEB-GW-01`, `DC01.corp.internal`, `FS01.corp.internal`, `DB-PROD-01`, `WS-FIN-042`.
* **Evaluation Areas:**
  * Operating system patch levels and exposed network services
  * Active Directory identity hygiene, authentication flows, and privilege boundaries
  * Database configuration, access controls, and audit logging
  * Endpoint hardening and local privilege management
* **Mapping Standards:** MITRE ATT&CK techniques, NIST CSF functions, and ISO/IEC 27001 control themes.

---

## 3. System & Domain Findings

### 3.1 Perimeter & DMZ Tier (`VPN-GW-01`, `WEB-GW-01`)
* **Outdated VPN Firmware & Exposed Management/Auth Surface (`VPN-GW-01` — `10.10.1.10`):** Running an outdated SSL/IPSec VPN build with known authentication/session flaws. An internet-facing VPN without phishing-resistant MFA creates a high-impact initial access path (`T1190` / `T1078`). **Rating: Critical.**
* **Input Validation & Legacy Protocol Support (`WEB-GW-01` — `10.10.1.20`):** API/web endpoints exhibit weak input sanitization on payment/query parameters and permit older TLS versions/weak cipher suites alongside plain `HTTP` redirect gaps. **Rating: High.**

### 3.2 Identity & Core Corporate Servers (`DC01.corp.internal`, `FS01.corp.internal`)
* **Weak Authentication & Kerberoastable Service Accounts (`DC01` — `10.20.10.5`):** Remote and SaaS sign-ins lack enforced FIDO2 hardware/passkey authentication, leaving accounts exposed to credential harvesting and adversary-in-the-middle token theft (`T1556` / `T1539`). Additionally, domain service accounts with Service Principal Names (SPNs) use weak/static passwords vulnerable to offline cracking (`T1558.003`). **Rating: Critical.**
* **Excessive & Stale Privileged Access (`DC01`):** Several legacy service and administrative accounts retain membership in high-privilege groups (`Domain Admins` / `Account Operators`) without Just-In-Time (JIT) elevation or regular access recertification (`T1078.002`). **Rating: High.**
* **Unencrypted File Sharing & Incomplete Telemetry (`FS01` — `10.20.10.15` & `DC01`):** Legacy `SMBv1` remains enabled on internal file shares, increasing lateral movement and relay/worm risk (`T1021.002`). Meanwhile, Kerberos service ticket request logging (Event ID `4769`) and centralized SIEM forwarding lack full coverage, limiting detection of credential abuse. **Rating: High.**

### 3.3 Restricted Data Tier (`DB-PROD-01` — `10.20.20.10`)
* **Over-Broad Access & Missing Query Audit Trail:** Application service accounts connect to `DB-PROD-01` with broader table/schema privileges than required for least privilege, and detailed SQL query/authentication audit logs are not consistently streamed to the SIEM. **Rating: High.**
* **Encryption & Network Exposure:** Ensure TLS enforcement is mandatory for all client-to-database connections and restrict direct database access strictly to approved application/jump hosts (`WEB-GW-01` / authorized admin bastion). **Rating: High.**

### 3.4 Corporate Endpoints (`WS-FIN-042` — `10.30.14.42`)
* **Local Admin Rights & Outdated Third-Party Software:** Standard users on `WS-FIN-042` possess local administrative privileges, enabling unauthorized tool execution or defense tampering (`T1548.002`), while outdated browser/plugin/utility packages remain unpatched (`T1203`). **Rating: Medium-High.**

---

## 4. Summary Risk Matrix

| Finding Area | Affected Assets | Severity | Primary ATT&CK IDs |
| :--- | :--- | :--- | :--- |
| Unpatched Edge VPN & Weak MFA | `VPN-GW-01`, `DC01` | **Critical** | `T1190`, `T1078`, `T1539` |
| Kerberoastable SPNs & Privileged Drift | `DC01.corp.internal` | **High** | `T1558.003`, `T1078.002` |
| `SMBv1` & Insufficient Audit Logging | `FS01`, `DC01`, `DB-PROD-01` | **High** | `T1021.002`, `T1562` |
| Unsanitized Web Input & Weak Ciphers | `WEB-GW-01` | **High** | `T1190`, `T1557` |
| Local Admin & Outdated Endpoint Apps | `WS-FIN-042` | **Medium-High** | `T1548.002`, `T1203` |

---

## 5. High-Level Recommendations
1. **Patch & Lock Down Perimeter Access:** Immediately upgrade `VPN-GW-01` firmware and enforce FIDO2 MFA across remote and privileged access.
2. **Harden Active Directory & Least Privilege:** Rotate weak SPN account credentials, enforce strong managed service accounts (gMSA), prune excessive privileged group memberships, and remove local admin rights on endpoints.
3. **Eliminate Legacy Protocols & Expand Telemetry:** Disable `SMBv1`, enforce strong TLS (`TLS 1.2+` / `SMBv3`), fix input validation on `WEB-GW-01`, and enable full Kerberos (`4769`) and database audit logging in the SIEM.
