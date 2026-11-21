# Network Security Risk Analysis

## 1. Scope & Analytical Approach
This analysis evaluates network exposure, traffic behavior, segmentation boundaries, and firewall enforcement across the simulated enterprise environment:
- **DMZ / Perimeter (`10.10.1.0/24`):** `FW-EDGE-01` (`10.10.1.1`), `VPN-GW-01` (`10.10.1.10`), `WEB-GW-01` (`10.10.1.20`)
- **Core Corporate Servers (`10.20.10.0/24`):** `DC01.corp.internal` (`10.20.10.5`), `FS01.corp.internal` (`10.20.10.15`)
- **Restricted Data Tier (`10.20.20.0/24`):** `DB-PROD-01` (`10.20.20.10`)
- **Corporate Endpoints (`10.30.0.0/16`):** `WS-FIN-042` (`10.30.14.42`)

---

## 2. Wireshark Traffic Inspection Findings

### 2.1 Periodic Beaconing & Anomalous Outbound Egress
- **Observed Pattern:** Regular, low-volume outbound connections from an internal host (`10.30.14.42`) to a non-standard external destination port over TCP/HTTPS at fixed intervals (`~60s` jittered cadence), accompanied by asymmetric packet sizes (small outbound check-ins, larger inbound responses).
- **Wireshark Filter:** `ip.src == 10.30.14.42 && !ip.dst == 10.0.0.0/8`
- **Risk & ATT&CK Mapping:** Potential C2 beaconing or unauthorized external callback (`T1071`). **Severity: High.**

### 2.2 Potential Data Exfiltration / Large Outbound Transfers
- **Observed Pattern:** Sustained high-volume outbound data transfers outside normal backup/cloud windows or large DNS TXT/long-subdomain query bursts.
- **Wireshark Filter:** `dns.qry.type == 16 || (ip.src == 10.20.0.0/16 && !ip.dst == 10.0.0.0/8 && tcp.len > 1000)`
- **Risk & ATT&CK Mapping:** Potential data exfiltration over web, encrypted tunnels, or DNS (`T1048`, `T1041`). **Severity: High.**

### 2.3 Cleartext & Legacy Protocol Traffic (`SMBv1`, `HTTP`)
- **Observed Pattern:** Cleartext `HTTP` requests lacking TLS redirection and `SMBv1` negotiation on TCP `445`.
- **Wireshark Filter:** `smb || smb2 || http.request`
- **Risk & ATT&CK Mapping:** Credential/session interception, MitM, and SMB lateral movement (`T1557`, `T1021.002`). **Severity: High.**

### 2.4 Unauthorized East-West / Cross-Subnet Probes
- **Observed Pattern:** Workstation subnet (`10.30.14.42`) sending TCP SYN probes or RDP/SMB/RPC attempts toward restricted database tier (`10.20.20.10`).
- **Wireshark Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0 && ip.dst == 10.20.20.10`
- **Risk & ATT&CK Mapping:** Network scanning and lateral movement attempts (`T1046`, `T1021`). **Severity: Medium-High.**

---

## 3. Firewall, Access Control & Segmentation Evaluation
- **Firewall Rule Hygiene:** Tighten broad outbound egress rules, audit shadowed/permissive entries on `FW-EDGE-01`, log explicit denies to the SIEM, and restrict admin management interfaces (`SSH`, `RDP`, `HTTPS` admin) to a dedicated jump/PAW VLAN with MFA.
- **DMZ to Internal (`10.10.1.0/24` -> `10.20.0.0/16`):** Allow only required application API/auth flows; block direct workstation-to-database (`10.30.0.0/16` -> `10.20.20.10`) access and limit lateral workstation-to-workstation SMB/RPC/WinRM (`445`, `135`, `139`, `5985/5986`).

## 4. Network Risk Summary

| Risk Area | Affected Zones / Hosts | Severity | Key Recommendation |
| :--- | :--- | :--- | :--- |
| Suspicious Egress / Beaconing & Exfiltration | `10.30.14.42`, Egress | **High** | Restrict outbound egress, monitor DNS/TLS anomalies, alert on beaconing & large transfers. |
| Cleartext / Legacy Protocols (`SMBv1`, `HTTP`) | `FS01`, `WEB-GW-01` | **High** | Disable `SMBv1`, enforce `SMBv3` encryption, enforce `HTTPS` + HSTS. |
| Weak Micro-Segmentation to Restricted Tier | `10.30.0.0/16` -> `10.20.20.10` | **High** | Allow-list only authorized app/admin hosts to `DB-PROD-01`; block lateral SMB/RPC. |
| Broad Firewall Egress & Admin Plane Access | `FW-EDGE-01`, Core/Mgmt | **Medium-High** | Tighten egress ACLs, isolate management plane, log blocked traffic to SIEM. |
