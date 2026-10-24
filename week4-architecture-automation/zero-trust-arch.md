# Enterprise Zero Trust Architecture (ZTA) Framework

## Core Architectural Principles (NIST SP 800-207)
1. **Never Trust, Always Verify:** All access requests, regardless of network origin (internal or external), are fully authenticated, authorized, and encrypted before granting access.
2. **Least Privilege Access:** Microsegmentation and Just-In-Time (JIT) access are enforced across all workforce endpoints and service communication channels.
3. **Assume Breach:** Continuous monitoring, log telemetry collection, and automated threat containment are active across all enterprise environments.

---

## Zero Trust Architecture Diagram

```text
┌────────────────────────┐     ┌───────────────────────────┐     ┌──────────────────────────────┐
│  Workforce Endpoints   │ ──► │ Policy Enforcement Point  │ ──► │      Enterprise Resource     │
│ (Managed / Unmanaged)  │     │      (Identity Proxy)     │     │   (ERP / K8s / AWS Cloud)    │
└────────────────────────┘     └─────────────┬─────────────┘     └──────────────────────────────┘
                                             │
                                             ▼
                               ┌───────────────────────────┐
                               │  Policy Decision Point    │
                               │  (Azure AD / Conditional) │
                               └───────────────────────────┘
