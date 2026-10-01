# FraudIntelligence

> Open, defensive and machine-readable knowledge base for **Fraud Intelligence, Scam Intelligence, Detection Engineering, OSINT and Financial Crime convergence**.

FraudIntelligence connects what fraud teams, CTI, Trust & Safety, AML, SOC, DFIR and risk teams usually keep in separate silos.

## Why this repository exists

Fraud is not one problem. A useful intelligence model needs to describe:

1. **Behavior / TTPs** — what the fraud actor does.
2. **Journey / Kill Chain** — how a scam or fraud operation progresses.
3. **Human Manipulation** — how trust, authority, urgency, grooming and situational vulnerability are exploited.
4. **Money Movement** — how value is transferred, layered, cashed out or moved through mule networks.
5. **Governance & Sharing** — how organizations prevent, investigate, share and disrupt fraud safely.

This repository treats those as separate but connected planes.

## Core references

| Source | Class | Primary role |
|---|---|---|
| MITRE Fight Fraud Framework (F3) | Open behavioral knowledge base | Fraud TTPs and a shared fraud/cyber language |
| Stripe FT3 | Open vendor framework | Fraud tools, tactics and techniques |
| Group-IB Fraud Matrix 2.0 | Vendor framework | Fraud behavior, actors, campaigns, detections and mitigations |
| FIST | Academic/open framework | Technical + social-engineering threat modeling |
| MITRE ATT&CK / DISARM | Cyber / influence frameworks | Technical intrusion and manipulation context |
| ACFE Fraud Tree | Taxonomy | Occupational fraud classification |
| COSO/ACFE Fraud Risk Management Guide | Governance | Fraud risk management program |
| FATF | Typologies / AML | Money movement, laundering and financial crime |
| BCB Resolução Conjunta nº 6/2023 | Regulation / Brazil | Sharing data and information on suspected fraud |
| FRIDA | Emerging EU sharing scheme | Standardized inter-PSP fraud information sharing |
| FIRE / GSE | Sharing networks | Cross-sector scam and fraud signals |

See [Framework Landscape](docs/framework-landscape.md) for maturity, scope and primary sources.

## Fraud Intelligence Fusion Model

```text
                 ┌──────────────────────────────┐
                 │ Governance & Sharing         │
                 │ COSO · BCB · FRIDA · FIRE   │
                 └──────────────┬───────────────┘
                                │
  ┌────────────┐  ┌─────────────▼─────────────┐  ┌──────────────┐
  │ Human      │  │ Behavior / TTPs           │  │ Money        │
  │ Manipul.   ├──► F3 · FT3 · ATT&CK · FIST ├──► Movement     │
  └─────┬──────┘  └─────────────┬─────────────┘  └──────┬───────┘
        │                       │                        │
        └──────────────┬────────┴──────────────┬─────────┘
                       │ Scam / Fraud Journey  │
                       │ contact → trust →     │
                       │ action → monetization │
                       └───────────┬────────────┘
                                   │
                            Detection & Disruption
```

This model is project-specific. It does **not** replace any referenced framework.

## Repository map

```text
FraudIntelligence/
├── docs/                  # Architecture, methodology, Brazil and verticals
├── knowledge/             # Machine-readable framework and fraud knowledge
│   └── crosswalks/        # Mapping philosophy and future mappings
├── schemas/               # JSON Schemas for fraud-intel objects
├── detections/            # Defensive analytics and detection examples
├── osint/                 # Ethical OSINT methodology
├── research/              # Research backlog and evidence requirements
├── tools/                 # Validation utilities
└── .github/workflows/     # CI validation
```

## Intelligence object model

The common object model connects:

`actor → campaign → scheme → tactic → technique → procedure → observable → detection → control → regulation`

with contextual entities:

`identity · account · device · channel · transaction · beneficiary · mule · infrastructure · organization`

Every knowledge object should carry **source, confidence, last_verified and status**.

## Design principles

- **Evidence before hype.** Primary sources beat vendor claims.
- **Facts are not frameworks.** Regulations, sharing networks and products are classified separately.
- **No victim blaming.** Human-factor analysis distinguishes perpetrator motivation from victim manipulation and situational vulnerability.
- **Detection first.** TTPs should map to observable signals and defensive controls.
- **Machine-readable by default.** YAML/JSON are first-class artifacts, not exports from prose.
- **Brazil + global.** Global coverage with a dedicated Brazil layer.
- **Defensive use only.** No operational fraud instructions, credential abuse, evasion guidance or illicit enablement.

## Current release: v0.1 Foundation

- verified framework registry;
- layered Fraud Intelligence architecture;
- fraud-type taxonomy;
- common intelligence schema;
- first detection examples;
- Brazil regulatory layer;
- ATM/PoS threat-intelligence vertical;
- research gate for unverified or emerging claims;
- CI validation.

## Next

See [Roadmap](docs/roadmap.md). The next milestone is a versioned **F3/FT3/FIST/ATT&CK crosswalk engine**, case-library schema and coverage matrix.

## Sources and attribution

This project links to source material rather than duplicating proprietary knowledge bases. MITRE F3 and ATT&CK, Stripe FT3 and other sources retain their respective licenses and trademarks.

## Responsible use

FraudIntelligence is intended for fraud prevention, threat intelligence, detection engineering, research, education and incident response. Contributions that materially facilitate fraud, evasion or victimization are out of scope.
