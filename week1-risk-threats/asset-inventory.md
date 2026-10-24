# Enterprise Asset Inventory and Classification Matrix

| Asset ID | Asset Name / Hostname | System Description | Data Classification | Criticality Level | Asset Owner | Location / Environment |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AST-001** | `DC01.corp.internal` | Primary Active Directory Domain Controller | **Restricted** | Critical (P1) | IT Infrastructure | On-Prem Data Center |
| **AST-002** | `DB-SQL-PROD01` | Enterprise Core ERP Database (Customer PII/Financials) | **Restricted** | Critical (P1) | Database Admin | AWS Cloud (`us-east-1`) |
| **AST-003** | `APP-PAY-GW01` | Payment Processing API Gateway (PCI Environment) | **Restricted** | Critical (P1) | DevSecOps | AWS Cloud (`us-east-1`) |
| **AST-004** | `EHR-PORTAL-01` | Healthcare Patient Portal Web Server | **Restricted** | Critical (P1) | Web Engineering | Hybrid / On-Prem |
| **AST-005** | `SIEM-COR-01` | Enterprise Log Aggregator & SIEM Cluster | **Confidential** | High (P2) | SecOps / SOC | On-Prem Data Center |
| **AST-006** | `K8S-PROD-CLUSTER` | Customer-Facing SaaS Application Platform | **Confidential** | High (P2) | Cloud DevOps | AWS Cloud (`us-west-2`) |
| **AST-007** | `VPN-GW-01` | Edge Remote Access VPN Gateway | **Confidential** | High (P2) | Network Engineering | DMZ Edge |
| **AST-008** | `M365-TENANT-01` | Enterprise Email & Collaboration Infrastructure | **Confidential** | High (P2) | Cloud Admin | Azure / SaaS |
| **AST-009** | `DEV-SRV-04` | Internal Software Engineering Build Server | **Internal** | Medium (P3) | Engineering | On-Prem Subnet |
| **AST-010** | `BI-REPORT-01` | Business Intelligence Reporting Analytics Server | **Confidential** | Medium (P3) | Data Analytics | AWS Cloud (`us-east-1`) |
