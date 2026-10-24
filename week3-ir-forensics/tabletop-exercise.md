# Executive Tabletop Exercise Scenario & After-Action Report

## Exercise Overview
* **Scenario Name:** Exercise "Operation DarkChain" — Supply Chain Ransomware & Cloud Persistence
* **Date Conducted:** October 18, 2026
* **Participants:** CISO, Lead IR Analyst, DevOps Engineering Manager, General Counsel, VP of Infrastructure.

---

## Scenario Inject Sequence & Inject Testing

### Inject 1: Initial Discovery (09:00 AM)
A critical third-party library update committed into internal Git repositories contains a malicious backdoor executing a reverse shell to an external C2 node (`45.33.22.11`).
* **Key Team Actions:** Triage GitHub commit logs, identify impacted build pipelines, and invoke `ir-playbook.md` (SEV-1).

### Inject 2: Lateral Movement & Cloud Escalation (10:15 AM)
The backdoor extracts CI/CD secrets, enabling the attacker to obtain AWS `AdministratorAccess` credentials and create persistent backdoor IAM users named `aws-infra-support`.
* **Key Team Actions:** Invoke AWS containment commands to revoke IAM keys, execute global session invalidation, and isolate CI/CD runner nodes.

### Inject 3: Public Disclosure Threat (11:30 AM)
The threat actor posts a extortion notice on a TOR leak site claiming 200 GB of sensitive customer healthcare records were stolen, demanding 50 BTC.
* **Key Team Actions:** General Counsel briefs executive leadership on breach reporting mandates under HIPAA/GDPR (72-hour window). PR prepares statement; no ransom paid per policy.

---

## After-Action Report (AAR) & Strategic Recommendations

| Identified Gap | Root Cause | Proposed Remediation Action | Owner | Target Completion |
| :--- | :--- | :--- | :--- | :--- |
| **G1: Delayed CI/CD Secret Invalidation** | Lack of automated secrets rotation API in GitHub pipelines | Implement HashiCorp Vault with dynamic short-lived credentials | DevOps Team | 30 Days |
| **G2: Gaps in Cloud IAM Auditing** | GuardDuty alerts routed to unmonitored Slack channel | Integrate Cloud Security Hub directly into SIEM with P1 paging | SecOps | 14 Days |
| **G3: External PR Delay** | No pre-approved crisis communication templates | Draft standardized breach response communications playbook | Legal / PR | 21 Days |
