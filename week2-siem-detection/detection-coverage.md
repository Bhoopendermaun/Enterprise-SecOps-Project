# Detection Coverage Matrix and False-Positive Reduction Strategy

## Detection Tuning & False-Positive Mitigation Matrix

| MITRE Tactic | Technique Name & ID | SIEM Rule | Baseline Detection Rule Logic | Identified False-Positive Risk | Noise Reduction Strategy / Filter |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Credential Access** | Kerberoasting (T1558.003) | Rule 1 | Event Code 4769 with RC4 encryption (`0x17`) | Authorized vulnerability scanners requesting TGS tickets | Exclude designated scanner service accounts (`svc_qualys$`) |
| **Execution** | PowerShell (T1059.001) | Rule 2 | PowerShell `-enc` parameter flag usage | Enterprise IT deployment scripts (e.g., SCCM, Datto RMM) | Whitelist parent process IDs originating from signed RMM binary paths |
| **Defense Evasion** | Clear Event Logs (T1070.001) | Rule 3 | Event Code 1102 / System Event 104 | Automated maintenance scripts during system re-imaging | Require dual-authorization tags for maintenance windows |
| **Exfiltration** | Dynamic C2 DNS (T1071.004) | Rule 8 | High-frequency queries to dynamic DNS domains | Legitimate CDN/cloud services (e.g., AWS API endpoints) | Enforce domain age checks; exclude Top 10,000 global domains |

## Noise Reduction Framework Objectives
1. Maintain SOC False-Positive Rate **< 5%**.
2. Require 14-day baseline observation before promoting detection rules to High-Severity alerting.
3. Automate alert enrichment via Threat Intelligence APIs (VirusTotal / GreyNoise) prior to analyst triage.
