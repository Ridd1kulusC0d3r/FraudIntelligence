# AI, Automated Abuse & Fraud

## OWASP Automated Threats

OWASP OAT provides a useful automation layer for web fraud. Relevant examples include:

- OAT-001 Carding
- OAT-007 Credential Cracking
- OAT-008 Credential Stuffing
- OAT-010 Card Cracking
- OAT-012 Cashing Out
- OAT-019 Account Creation
- OAT-020 Account Aggregation

These concepts should be cross-referenced with fraud classifications and TTPs rather than copied into them.

## MITRE ATLAS

ATLAS is useful when fraud activity intersects with AI systems, such as:
- AI-assisted impersonation;
- model or application abuse;
- attacks against AI-enabled verification;
- AI supply-chain and deployment risks.

## C2PA

C2PA Content Credentials provide provenance information about digital media. For Fraud Intelligence, provenance is a **signal**, not a truth oracle.

Useful states:
- valid provenance present;
- provenance missing;
- provenance broken;
- provenance conflicts with claimed origin;
- AI-disclosure assertion present.

Absence of C2PA must not be treated as proof of manipulation.

## Agentic fraud

The project tracks agentic systems as a capability trend using a conservative taxonomy:

```text
agent-assisted research
agent-assisted content generation
agent-assisted campaign coordination
agent-assisted triage
agent-assisted investigation
agent-assisted response
```

Autonomous high-impact fraud decisions remain out of scope for this project.

## Defensive lesson from 2026

AI is reducing the cost of correlation and operational reasoning. The response should be stronger provenance, bounded automation, evidence logging, analyst review and cross-domain telemetry.
