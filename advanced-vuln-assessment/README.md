# Advanced Security Assessment & Vulnerability Management (Week 1)

## Overview
This module covers an in-depth security assessment and vulnerability management workflow across a simulated hybrid enterprise environment. It evaluates servers, endpoints, databases, network segmentation, firewall policies, authentication controls, and live packet traffic to produce actionable, risk-prioritized remediation guidance.

## Simulated Enterprise Topology
| Zone / Subnet | Asset / Hostname | IP Address | Role & Criticality |
| :--- | :--- | :--- | :--- |
| **DMZ / Perimeter** (`10.10.1.0/24`) | `FW-EDGE-01` | `10.10.1.1` | Edge Firewall & NAT Gateway (**Critical**) |
| **DMZ / Perimeter** (`10.10.1.0/24`) | `VPN-GW-01` | `10.10.1.10` | Remote Access SSL/IPSec VPN Gateway (**Critical**) |
| **DMZ / Perimeter** (`10.10.1.0/24`) | `WEB-GW-01` | `10.10.1.20` | Public Web & Payment API Gateway (**High**) |
| **Core Identity & Infra** (`10.20.10.0/24`) | `DC01.corp.internal` | `10.20.10.5` | Active Directory Domain Controller, DNS, KDC (**Critical**) |
| **Core Corporate Servers** (`10.20.10.0/24`) | `FS01.corp.internal` | `10.20.10.15` | Internal File & Print Server (**High**) |
| **Restricted Data Tier** (`10.20.20.0/24`) | `DB-PROD-01` | `10.20.20.10` | Production Relational Database Server (**Critical**) |
| **Corporate Endpoints** (`10.30.0.0/16`) | `WS-FIN-042` | `10.30.14.42` | Finance Workstation — Sample Endpoint (**Medium**) |

## Assessment Methodology & Standards
* **Vulnerability Scoring:** CVSS v3.1 base/temporal ratings paired with asset criticality and exploitability context.
* **Network & Traffic Analysis:** Packet capture inspection (`Wireshark` / `tshark`), port/service enumeration, firewall rule review, and VLAN segmentation analysis.
* **Framework Alignment:** Mapped to **MITRE ATT&CK** techniques, **NIST CSF**, and **ISO/IEC 27001** security control principles.

## Week 1 Deliverables
1. [`week1-vuln-assessment/01-enterprise-security-assessment.md`](week1-vuln-assessment/01-enterprise-security-assessment.md) — **Enterprise Security Assessment Report**
2. [`week1-vuln-assessment/02-cvss-vulnerability-scans.md`](week1-vuln-assessment/02-cvss-vulnerability-scans.md) — **Vulnerability Scan Results with CVSS Classification**
3. [`week1-vuln-assessment/03-network-security-analysis.md`](week1-vuln-assessment/03-network-security-analysis.md) — **Network Security Risk Analysis**
4. [`week1-vuln-assessment/04-prioritized-remediation-plan.md`](week1-vuln-assessment/04-prioritized-remediation-plan.md) — **Prioritized Remediation Plan**
