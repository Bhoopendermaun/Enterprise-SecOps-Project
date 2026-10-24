# Security Control Gap Analysis and Executive Summary

## Executive Summary: Enterprise Risk Profile
An enterprise-wide Security Risk Assessment and Threat Modeling exercise conducted across 15 critical infrastructure, cloud, and application assets indicates an **ELEVATED** risk posture. Primary exposure points stem from IAM gaps, cloud storage misconfigurations, and legacy application vulnerabilities. Implementing the 90-day remediation roadmap reduces enterprise risk exposure by an estimated **78%**.

## ISO 27001 / NIST CSF Control Gap Matrix

| ISO 27001 Control Domain | NIST CSF Function | Identified Security Gap | Business / Technical Risk | Proposed Control Enhancement | Resource Estimate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A.9 Identity & Access** | **PROTECT (PR.AC)** | Lack of FIDO2 MFA on edge remote access and SaaS platforms. | Account compromise, Session Hijacking. | Enforce Azure AD Conditional Access rules with hardware keys. | $45,000 |
| **A.12 Operations Security** | **DETECT (DE.CM)** | Incomplete logging of internal database queries and AD Kerberos requests. | Inability to detect credential extraction and unauthorized data access. | Enable Event ID 4769 logging; expand SIEM ingestion to DB cluster. | $20,000 |
| **A.14 System Acquisition** | **PROTECT (PR.DS)** | Unsanitized input vectors in payment application code (`APP-PAY-GW01`). | SQL Injection, PCI-DSS non-compliance. | Integrate SAST/DAST into CI/CD pipeline. | $30,000 |
| **A.13 Communications** | **PROTECT (PR.PT)** | Unencrypted network protocols (SMBv1, HTTP) active on legacy VLANs. | MitM interception, wormable lateral movement. | Enforce SMBv3 with encryption; enforce HTTPS via HSTS. | $15,000 |
| **A.18 Compliance** | **GOVERN (GV.OV)** | AWS S3 storage buckets missing centralized "Block Public Access" guardrails. | Data exposure, regulatory fines. | Deploy AWS Control Tower Guardrails and automated CSPM scanning. | $12,000 |
