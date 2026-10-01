# FraudIntelligence

> Open, defensive and machine-readable knowledge base for **Fraud Intelligence, Scam Intelligence, Detection Engineering, OSINT and Financial Crime convergence**.

FraudIntelligence connects Fraud, CTI, Trust & Safety, AML, SOC, DFIR, identity, telecom and risk into one evidence-backed model.

## Current release: v0.2 Intelligence Expansion

v0.2 moves the project from a foundation into an operational knowledge system:

- **classification layer** with Federal Reserve FraudClassifier/ScamClassifier references and a draft **ScamClassifier-BR**;
- **crime-science layer** using Crime Script Analysis, Situational Crime Prevention and Routine Activity Theory;
- **identity/onboarding layer** anchored in NIST SP 800-63-4;
- **automation layer** using OWASP Automated Threats;
- **AI/deepfake layer** using MITRE ATLAS and C2PA;
- **telecom-signal layer** using GSMA Open Gateway / CAMARA concepts such as SIM Swap and Number Verification;
- **Brazil/LatAm threat landscape** with source-backed actors and malware;
- **upstream sync tooling** for MITRE F3 and Stripe FT3;
- **crosswalk and FraudSignal schemas**;
- **interactive Fraud Intelligence Navigator** source under `docs/`;
- **research quarantine** for emerging claims that are interesting but not yet strong enough for the core registry.

## Fraud Intelligence Fusion Model

```text
                         FRAUDINTELLIGENCE
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
 Classification &         Behavior / TTPs         Human Manipulation
 Crime Scripts            F3 · FT3 · ATT&CK       FIST · discourse
       │                        │                        │
       └───────────────┬────────┴────────┬───────────────┘
                       │                 │
                Money Movement      Identity / Telecom
                FRAML · mules       NIST · CAMARA
                       │                 │
                       └────────┬────────┘
                                │
                    Detection & Disruption
                                │
             Governance · Sharing · Feedback
```

The project-specific fusion model does **not** replace upstream frameworks.

## The analytical chain

`classification → journey → behavior → manipulation → observable → telemetry → detection → control → outcome → feedback`

This chain is the core design rule of the repository.

## Core references

| Source | Class | Primary role |
|---|---|---|
| MITRE Fight Fraud Framework (F3) | Behavioral knowledge base | Fraud TTPs |
| Stripe FT3 | Open fraud framework | Fraud tactics and techniques |
| Group-IB Fraud Matrix 2.0 | Vendor framework | Fraud behavior, actors, campaigns |
| FIST | Academic framework | Technical + social-engineering threat modeling |
| MITRE ATT&CK / DISARM | Cyber / influence | Intrusion and manipulation context |
| Federal Reserve FraudClassifier / ScamClassifier | Classification models | Consistent fraud/scam labeling |
| Crime Script Analysis | Crime science | Ordered fraud/scam scripts |
| NIST SP 800-63-4 | Digital identity guidance | Identity proofing and authentication |
| OWASP Automated Threats | Automation taxonomy | Bots and automated abuse |
| MITRE ATLAS | AI threat knowledge base | AI-enabled / AI-targeting behavior |
| C2PA | Content provenance standard | Media provenance and authenticity |
| GSMA Open Gateway / CAMARA | Network APIs | Telecom fraud signals |
| ACFE / COSO / FATF | Governance / typologies | Fraud-risk and financial-crime context |
| BCB Resolução Conjunta nº 6/2023 | Brazil regulation | Fraud-indicator sharing |
| FRIDA / FIRE / GSE | Sharing schemes | Cross-organization signals |

See [Framework Landscape](docs/framework-landscape.md).

## Repository map

```text
FraudIntelligence/
├── docs/
│   ├── index.html                  # Navigator
│   ├── classification.md
│   ├── crime-science.md
│   ├── identity-onboarding.md
│   ├── ai-automated-fraud.md
│   ├── brazil-threat-landscape.md
│   └── osint-emerging-capabilities.md
├── knowledge/
│   ├── frameworks.yml
│   ├── actors/brazil-latam.yml
│   ├── threats/brazil-latam.yml
│   ├── classifiers/scamclassifier-br.yml
│   ├── signals/telecom.yml
│   └── crosswalks/
├── schemas/
│   ├── fraud-intel-object.schema.json
│   ├── fraud-signal.schema.json
│   └── crosswalk.schema.json
├── detections/
├── research/
├── tools/
│   ├── validate_knowledge.py
│   ├── sync_frameworks.py
│   └── build_catalog.py
└── .github/workflows/
```

## Brazil / LatAm research focus

The regional layer now distinguishes:

- financially motivated actors;
- malware families;
- access brokers / criminal service platforms;
- payment-infrastructure attacks;
- retail banking malware;
- cloud / CI-CD / payment-authorization targeting.

The initial verified set includes **BREEZE COMET**, **SLIM SPIDER**, **Exilware/BraZetsu**, **Prilex**, **GoPix**, **Lazarus/FASTCash** and the current **Ploutus/jackpotting** resurgence.

## ScamClassifier-BR

`knowledge/classifiers/scamclassifier-br.yml` is a draft open classifier for Brazilian scams. It separates:

`authorization → mechanism → impersonation/relationship/product → channel → payment rail → outcome`

It is intentionally independent from TTP mapping. Classification answers *what happened*; F3/FT3 answer *how the actor behaved*.

## Upstream framework sync

```bash
python tools/sync_frameworks.py
python tools/build_catalog.py
python tools/validate_knowledge.py
```

The sync tool downloads source-native F3/FT3 JSON into a local ignored cache, calculates hashes and writes a manifest. Upstream content is not silently rewritten into project concepts.

## Evidence policy

- primary source before secondary reporting;
- source-native IDs are preserved;
- a vendor claim remains a vendor claim;
- mappings carry confidence and rationale;
- no victim blaming;
- no unsupported attribution;
- no "APT" label merely because malware is sophisticated;
- precise financial-loss figures require dated sourcing.

## Defensive boundary

FraudIntelligence is for prevention, threat intelligence, detection engineering, research, education and incident response. It does not publish instructions that materially enable fraud, credential theft, anti-fraud bypass, illicit access or cash-out optimization.
