# Enterprise Incident Response Playbook and Crisis Escalation Matrix

## Incident Response Lifecycle Stages
1. **Preparation:** Maintain tools, playbooks, communication channels, and isolated forensic workstations.
2. **Detection & Analysis:** Triage SIEM alerts, determine incident severity, and establish breach scope.
3. **Containment:** Execute network host isolation, revoke session tokens, and block malicious IPs/hashes.
4. **Eradication:** Purge malicious artifacts, remove persistence mechanisms, and patch underlying vulnerabilities.
5. **Recovery:** Restore systems from verified clean backups, validate monitoring, and return to production.
6. **Lessons Learned:** Conduct post-mortem review, update playbooks, and track corrective action items.

---

## Severity & SLA Classification Matrix
* **SEV-1 (Critical):** Enterprise-wide ransomware propagation, domain admin compromise, active data exfiltration. **SLA:** `< 15 mins`.
* **SEV-2 (High):** Single critical asset compromise (`P1/P2`), active C2 beaconing, localized malware infection. **SLA:** `< 30 mins`.
* **SEV-3 (Medium):** Isolated credential theft, successful phishing without execution, policy violation. **SLA:** `< 2 hours`.
* **SEV-4 (Low):** Port scanning, spam email delivery, failed brute-force attempt. **SLA:** `< 8 hours`.

---

## Crisis Escalation Contact Matrix

| Role | Contact Channel | Primary Responsibility | Engagement Trigger |
| :--- | :--- | :--- | :--- |
| **Incident Commander** | `ic@corp.internal` | Overall IR operations & decision making | SEV-1 / SEV-2 Incidents |
| **Lead Forensic Analyst** | `forensics@corp.internal` | Technical artifact & memory analysis | Confirmed System Breach |
| **Chief Information Security Officer (CISO)** | `ciso@corp.internal` | Executive steering & board briefing | SEV-1 / Confirmed Exfiltration |
| **General Counsel** | `legal@corp.internal` | Regulatory & breach notification strategy | PII / Sensitive Data Loss |
| **Corporate Communications** | `comms@corp.internal` | External PR & public messaging | Public Inquiries / Mass Disruption |
