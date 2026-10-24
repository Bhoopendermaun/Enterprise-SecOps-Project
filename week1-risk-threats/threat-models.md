# Enterprise STRIDE Threat Models

## Threat Model 1: AWS Web Application & SaaS Platform (`K8S-PROD-CLUSTER`)

### Architecture Diagram
```text
   [ External Client ] ──( HTTPS )──► [ Cloudflare WAF ] ──► [ AWS Ingress Gateway ] ──► [ Microservices / Pods ] ──► [ Amazon RDS ]
