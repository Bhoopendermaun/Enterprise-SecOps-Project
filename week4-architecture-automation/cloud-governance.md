# Enterprise Cloud Security Governance, Compliance, & Posture Management

## Regulatory Compliance Alignment
* **ISO/IEC 27001:2022:** Information Security Management System (ISMS) controls covering asset management, access control, and cryptography.
* **NIST SP 800-53 Rev. 5:** Security and privacy controls for federal information systems and organizations.
* **PCI-DSS v4.0:** Strict segmentation and encryption standards for cardholder data environments (CDE).

---

## Cloud Security Posture Management (CSPM) Enforcement

| Control Domain | Baseline Policy Requirement | Automated Enforcement Tool | Remediation Action |
| :--- | :--- | :--- | :--- |
| **Storage Security** | Zero public S3 buckets / Azure Blobs allowed | AWS Config / Azure Policy | Automatic bucket policy override to `Private` |
| **Identity Management** | Multi-Factor Authentication (MFA) required for all IAM users | AWS IAM Access Analyzer | Suspend access keys lacking MFA associations |
| **Encryption at Rest** | Mandatory customer-managed KMS keys for all EBS/RDS volumes | Terraform Compliance / Checkov | Fail CI/CD deployment pipelines on violation |
| **Network Exposure** | No unrestricted inbound security group rules (`0.0.0.0/0`) on SSH (22) or RDP (3389) | AWS GuardDuty / Security Hub | Auto-revoke security group ingress rule |
