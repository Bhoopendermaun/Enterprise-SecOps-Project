# MITRE ATT&CK Framework Mapping Matrix

## Threat Actor Behavior Mapping across Investigated Incidents

| MITRE Tactic | Technique Name | Technique ID | Observed Evidence / Indicator | Associated Incident |
| :--- | :--- | :--- | :--- | :--- |
| **Initial Access** | Phishing: Malicious Attachment | T1566.001 | Delivery of `INVOICE_881.iso` via email | INC-2026-8812 |
| **Initial Access** | Unsecured Credentials | T1552.001 | AWS Access Key committed to public Git repository | INC-2026-9041 |
| **Execution** | Command & Scripting: PowerShell | T1059.001 | Obfuscated PowerShell download cradles | INC-2026-8812 |
| **Execution** | User Execution: Malicious File | T1204.002 | Execution of mounted ISO payload `INVOICE_PDF.exe` | INC-2026-8812 |
| **Persistence** | Account Manipulation | T1098 | Unauthorized creation of local administrative accounts | Enterprise Baseline |
| **Privilege Escalation** | Domain Account Escalation | T1078.002 | Compromise of Kerberos service account hashes | INC-2026-9300 |
| **Defense Evasion** | Indicator Removal: Clear Event Logs | T1070.001 | Execution of `Clear-EventLog -LogName Security` | INC-2026-8812 |
| **Defense Evasion** | Deobfuscate/Decode Files | T1027 | Base64 encoded payload strings executed via CLI | INC-2026-8812 |
| **Credential Access** | Steal/Forge Kerberos Tickets: Kerberoasting | T1558.003 | Abnormal TGS-REQ requests with RC4 encryption | INC-2026-9300 |
| **Discovery** | System Network Configuration Discovery | T1016 | Execution of `netstat -ano` and `whoami /priv` | INC-2026-8812 |
| **Lateral Movement** | Remote Services: SMB/Windows Admin Shares | T1021.002 | Inbound lateral movement attempts to DB servers | INC-2026-9300 |
| **Exfiltration** | Exfiltration Over C2 Channel | T1041 | Volumetric HTTPS data transfer to external C2 IP | INC-2026-8812 |
| **Impact** | Resource Hijacking | T1496 | Provisioning of EC2 GPU instances for mining | INC-2026-9041 |
