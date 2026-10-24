# Enterprise Incident Containment & Eradication Standard Operating Procedures

## Phase 1: Immediate Network & Endpoint Isolation Protocols

### 1. Endpoint Host Network Isolation (EDR API / Firewall Rule)
When an endpoint is flagged for severe compromise, isolate the system using enterprise EDR or network-level blocking:
```bash
# EDR CLI Isolation Command Example (SentinelOne / CrowdStrike CLI)
falcon-agent isolate-host --id=FIN-WRK-089 --comment="Active Ransomware Containment INC-2026-8812"

# Local Network Isolation Rule via IP tables (Linux systems)
iptables -A INPUT -i eth0 -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -i eth0 -j DROP
iptables -A OUTPUT -o eth0 -j DROP
