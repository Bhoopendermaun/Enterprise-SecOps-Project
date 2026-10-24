# Incident Investigation Reports

## Incident Report 1: INC-2026-8812 - Ransomware Infection & Exfiltration Attempt

### Executive Summary & Scope
On October 12, 2026, at 03:14:22 UTC, the SOC detected anomalous, high-volume outbound network traffic from host `FIN-WRK-089` to an external IP (`185.220.101.5`). Subsequent process execution analysis revealed deployment of **LockBit 3.0 Ransomware** following initial access obtained via a phishing attachment.

### Chronological Event Timeline
* **02:10:11 UTC:** User `j.doe@corp.internal` receives phishing email containing ISO image `INVOICE_881.iso`.
* **02:14:05 UTC:** User mounts ISO and executes `INVOICE_PDF.exe`, initiating DLL sideloading of `msimg32.dll`.
* **03:00:15 UTC:** Attacker initiates local system discovery (`whoami /priv`, `net group "Domain Admins"`).
* **03:14:22 UTC:** Rclone execution detected transferring 5.2 GB of file data to external C2 IP `185.220.101.5`.
* **03:22:00 UTC:** SIEM alert fires on network volumetric threshold; EDR automatically isolates host `FIN-WRK-089`.

### Evidence Artifacts
* **Host Affected:** `FIN-WRK-089` (10.100.4.15)
* **File Hashes (SHA-256):** 
  * `INVOICE_PDF.exe`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  * Payload: `8f3c3a21193db2ad823451e04c54101673898083fe8bf61b3433604bc8654161`
* **C2 IP:** `185.220.101.5`

---

## Incident Report 2: INC-2026-9041 - AWS Cloud Credential Theft & Resource Hijacking

### Executive Summary & Scope
On October 14, 2026, at 14:02:10 UTC, AWS GuardDuty raised a high-severity alert indicating programmatic API calls originating from an unapproved Tor exit node (`198.51.100.44`) using an AWS IAM Access Key exposed in a public repository.

### Chronological Event Timeline
* **11:30:00 UTC:** Developer accidentally commits hardcoded IAM access key into a public GitHub repository.
* **11:34:12 UTC:** Automated external web scraper harvests the exposed IAM credentials.
* **14:02:10 UTC:** Attacker issues `aws sts get-caller-identity` from IP `198.51.100.44`.
* **14:15:00 UTC:** Attacker provisions 20 High-Performance GPU EC2 Instances (`g4dn.12xlarge`) for crypto-mining.
* **14:22:00 UTC:** Cloud Security Automation triggers; keys revoked and instances terminated.

### Evidence Artifacts
* **AWS Account ID:** `123456789012`
* **Compromised Key:** `AKIAIOSFODNN7EXAMPLE`
* **Attacker IP:** `198.51.100.44`
