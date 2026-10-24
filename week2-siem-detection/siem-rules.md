# SIEM Detection Rules and Test Cases (Splunk SPL / Elastic KQL)

## Rule 1: Active Directory Kerberoasting Activity Detection
* **Description:** Detects abnormal Kerberos Service Ticket requests (`TGS-REQ`) requesting weak RC4 encryption (`0x17`), indicative of Kerberoasting attacks.
* **Target Attack Vector:** MITRE ATT&CK T1558.003 (Kerberoasting).
* **Splunk SPL Query:**
```spl
index=winlogbeat EventCode=4769 TicketOptions="0x40810000" TicketEncryptionType="0x17" ServiceName!="*$"
| stats count dc(ServiceName) as unique_services values(ServiceName) as requested_services by TargetUserName, ClientAddress
| where unique_services >= 3
