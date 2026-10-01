# Architecture

## Goal

FraudIntelligence is a **fusion layer** between fraud prevention, CTI, Trust & Safety, AML, DFIR, SOC and risk management.

The project separates five analytical planes so different teams can contribute without forcing unrelated concepts into one taxonomy.

## Plane 1 — Behavior / TTPs

Describes observable adversary behavior.

Primary references:
- MITRE F3
- Stripe FT3
- Group-IB Fraud Matrix
- MITRE ATT&CK
- DISARM
- FIST

Output: tactics, techniques, procedures, actors, campaigns and behavioral hypotheses.

## Plane 2 — Scam / Fraud Journey

Describes sequence and progression.

Typical stages:
- targeting / discovery;
- initial contact or access;
- trust establishment / positioning;
- action or execution;
- payment / transfer;
- monetization / cash-out;
- concealment / recycling / re-targeting.

A journey is **not** a TTP taxonomy. It is an ordering model.

## Plane 3 — Human Manipulation

Describes victim-facing social and cognitive mechanisms without victim blaming.

Examples:
- authority impersonation;
- urgency and time pressure;
- trust grooming;
- scarcity;
- social proof;
- reciprocity;
- fear / loss framing;
- cognitive overload;
- situational vulnerability;
- channel migration and isolation.

Important distinction: the Fraud Triangle / Diamond is useful for conditions associated with **committing fraud**, especially occupational fraud. It should not be treated as a general model of why victims fall for scams.

## Plane 4 — Money Movement

Describes how value moves after or during fraud.

Objects include:
- origin account;
- beneficiary;
- mule;
- merchant;
- wallet;
- payment rail;
- cash-out method;
- laundering stage;
- transaction cluster.

This plane supports FRAML convergence without collapsing fraud and AML into one discipline.

## Plane 5 — Governance & Sharing

Describes obligations, control programs and intelligence exchange.

Examples:
- COSO/ACFE Fraud Risk Management Guide;
- BCB Resolução Conjunta nº 6/2023;
- FATF typologies and guidance;
- FRIDA;
- FIRE;
- Global Signal Exchange;
- Australia's Scams Prevention Framework.

## Fusion pipeline

```text
Collect → Normalize → Correlate → Characterize → Detect → Disrupt → Learn
             │            │             │           │
             └──── provenance / confidence / time ──┘
```

### Collect
Open-source reporting, internal telemetry, complaints, cases, transaction data, platform signals, malware/CTI and regulatory publications.

### Normalize
Map source-specific terms into project objects while preserving original source IDs.

### Correlate
Join identities, devices, accounts, domains, channels, beneficiaries, techniques and campaigns.

### Characterize
Produce a multi-plane description: TTP + journey + manipulation + money movement + governance context.

### Detect
Turn intelligence into observables, analytics, thresholds, graph patterns and absence/reconciliation checks.

### Disrupt
Block, challenge, hold, review, take down, report, share or investigate according to lawful policy.

### Learn
Measure coverage, false positives, misses, drift, new procedures and control effectiveness.

## Confidence model

- `confirmed`: primary evidence or directly observed;
- `high`: multiple reliable sources with strong consistency;
- `medium`: credible but incomplete or partially corroborated;
- `low`: hypothesis, weak attribution or single secondary source;
- `unverified`: research backlog only.

Confidence describes **the claim**, not the prestige of the source.
