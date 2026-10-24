# Forensic Analysis & Incident Timeline Reconstruction

## Forensics Case Overview: Scenario "Operation StealthExfil"
A volatile memory dump (`mem_dump.raw`) and disk artifacts (`$MFT`, `$LogFile`, Windows Security Logs) were analyzed from target server `HR-FILE-01` (10.0.1.105) following detection of unauthorized administrative activity.

## Reconstructed Chronological Event Timeline

| Timestamp (UTC) | Source Artifact | Event Description / Technical Detail | Executed User Account | MITRE ID |
| :--- | :--- | :--- | :--- | :--- |
| **2026-10-15 08:00:12** | Event ID 4624 | Successful RDP Network Logon from external IP `198.51.100.12` | `CORP\b.smith` | T1078 |
| **2026-10-15 08:05:44** | Sysmon Event 1 | `cmd.exe` spawned execution of `whoami /all` and `netstat -ano` | `CORP\b.smith` | T1059.003 |
| **2026-10-15 08:12:01** | Sysmon Event 1 | Execution of custom binary `C:\Users\Public\update.exe` | `CORP\b.smith` | T1204 |
| **2026-10-15 08:12:05** | Memory Dump | Process injection into `lsass.exe` via `VirtualAllocEx` / `WriteProcessMemory` | `NT AUTHORITY\SYSTEM` | T1053 |
| **2026-10-15 08:15:30** | Volatility Analysis | Extraction of cleartext credentials from LSASS memory | `NT AUTHORITY\SYSTEM` | T1003.001 |
| **2026-10-15 08:22:10** | MFT `$FILE_NAME` | Creation of staging archive `C:\Windows\Temp\hr_db_export.7z` | `NT AUTHORITY\SYSTEM` | T1560.001 |
| **2026-10-15 08:30:00** | Firewall / Proxy | Encrypted outbound HTTPS traffic stream (4.8 GB) to `mega.nz` via curl | `NT AUTHORITY\SYSTEM` | T1567.002 |
| **2026-10-15 08:35:00** | Event ID 1102 | Windows Security Event log explicitly cleared | `NT AUTHORITY\SYSTEM` | T1070.001 |

## Technical Artifact Evidence

```text
Volatile Memory Artifact Analysis (Volatility 3):
--------------------------------------------------
Kernel Base: 0xf80002800000
Target Process: lsass.exe (PID: 672)
Injected DLL Found: 0x7ff8a1230000 (Size: 0x12000) -> Memory page PAGE_EXECUTE_READWRITE
Extracted MD5: 44d88612fea8a8f36de82e1278abb02f

MFT File System Parsing:
--------------------------------------------------
File Record: 45102
Path: C:\Windows\Temp\hr_db_export.7z
Timestamp: 2026-10-15 08:22:10 UTC
File Size: 5,153,960,755 Bytes

