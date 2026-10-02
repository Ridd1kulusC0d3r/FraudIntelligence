<p align="center">
  <strong>F R A U D I N T E L L I G E N C E</strong>
</p>

<h1 align="center">Fraud Intelligence Knowledge & Detection Platform</h1>

<p align="center">
  Fraud · CTI · OSINT · Scam Intelligence · Detection Engineering · Financial Crime
</p>

<p align="center">
  <img alt="release" src="https://img.shields.io/badge/release-v0.4%20Intelligence%20Operations-2563eb">
  <img alt="knowledge" src="https://img.shields.io/badge/knowledge-evidence--first-16a34a">
  <img alt="actors" src="https://img.shields.io/badge/threat%20actors-11-7c3aed">
  <img alt="frameworks" src="https://img.shields.io/badge/core%20references-20-0891b2">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-475569">
</p>

<p align="center">
  <a href="docs/index.html"><strong>Navigator</strong></a> ·
  <a href="docs/brazil-threat-landscape.md">Threat Landscape</a> ·
  <a href="docs/framework-landscape.md">Frameworks</a> ·
  <a href="detections/README.md">Detections</a> ·
  <a href="docs/intelligence-tradecraft.md">Intelligence Tradecraft</a> ·
  <a href="docs/roadmap.md">Roadmap</a>
</p>

---

> **FraudIntelligence** is an open, defensive and machine-readable knowledge base that connects fraud prevention, CTI, Trust & Safety, AML, SOC, DFIR, identity, telecom and OSINT into one evidence-backed intelligence model.

## ⚡ At a glance

| Intelligence layer | What this repository models |
|---|---|
| **Threat Actors** | APT/state-linked groups, financial eCrime, access brokers and regional clusters |
| **Behavior** | MITRE F3, Stripe FT3, ATT&CK, Fraud Matrix, FIST |
| **Fraud Journey** | Scam classification, crime scripts and manipulation patterns |
| **Signals** | Identity, device, telecom, transaction, infrastructure and provenance |
| **Detection** | Observable → telemetry → analytic → control → outcome |
| **Intelligence** | Requirements, evidence, confidence, hypotheses, gaps and feedback |

## 🎯 Threat Actor Radar

The landing page deliberately distinguishes **state-linked/APT activity** from **financial eCrime**. Sophistication alone does not magically turn criminals into an APT. Taxonomy has suffered enough.

| Class | Actor | Region | Financial relevance |
|---|---|---|---|
| 🟥 **State-linked / APT** | **APT38 · G0082** | North Korea | Banks, SWIFT, ATMs, cryptocurrency and financial cyber operations |
| 🟥 **State-linked** | **Lazarus Group · G0032** | North Korea | Broader DPRK cyber umbrella with financial-operation overlap |
| 🟪 **Financial eCrime** | **BREEZE COMET** | Brazil | Pix, STR, Boleto, mTLS, cloud and CI/CD |
| 🟪 **Financial eCrime** | **SLIM SPIDER** | Brazil | Financial institutions, cloud credentials, Pix and digital assets |
| 🟪 **Financial eCrime** | **FIN7 · G0046** | Global | Payment data, PoS, financial services and ransomware |
| 🟪 **Financial eCrime** | **Cobalt Group · G0080** | Multi-region | ATMs, card processing, payment systems and SWIFT |
| 🟦 **Cybercrime** | **Carbanak · G0008** | Global | Financial institutions and payment infrastructure |
| 🟪 **Financial eCrime** | **Silence · G0091** | Europe / Central Asia | Banks, ATMs and card processing |
| 🟪 **Financial eCrime** | **FIN8 · G0061** | Global | PoS, retail, hospitality and financial-sector targeting |
| 🟧 **Brazilian cybercrime** | **Prilex** | Brazil | PoS/TEF, payment-flow and EMV implementation abuse |
| 🟧 **Access ecosystem** | **Exilware / BraZetsu** | Brazil | Initial-access brokerage and high-value host reconnaissance |

→ Machine-readable actors: [Brazil/LatAm](knowledge/actors/brazil-latam.yml) · [Global financial actors](knowledge/actors/global-financial.yml)

## 🧭 Intelligence operating model

```text
          REQUIREMENTS / PIRs
                 │
                 ▼
       Collect → Evaluate → Correlate
          │          │          │
          │      provenance     ├──── actor / campaign / infrastructure
          │      confidence     ├──── identity / device / telecom
          │                     └──── transaction / beneficiary / mule
          ▼
     CHARACTERIZE
 classification + crime script + TTP + manipulation
          │
          ▼
  OBSERVABLE → TELEMETRY → DETECTION → CONTROL
          │                              │
          └────────── feedback ──────────┘
                         │
                         ▼
                UPDATE ASSESSMENT
```

The analytical chain is:

`requirement → claim → evidence → hypothesis → behavior → observable → telemetry → analytic → control → outcome → feedback`

## 🧩 Fusion model

FraudIntelligence keeps different analytical questions separate instead of forcing everything into one giant taxonomy.

| Plane | Question | Main references |
|---|---|---|
| Classification | **What happened?** | FraudClassifier, ScamClassifier, ScamClassifier-BR |
| Journey | **Where are we in the operation?** | Crime Script Analysis, scam/fraud kill chains |
| Behavior | **What did the actor do?** | F3, FT3, ATT&CK, Fraud Matrix |
| Manipulation | **How was trust/action shaped?** | FIST, behavioral vocabulary |
| Money | **How did value move?** | beneficiaries, mules, rails, wallets |
| Detection | **What can we observe?** | ATT&CK Detection Strategies, project analytics |
| Intelligence | **What decision does this answer?** | PIRs, hypotheses, confidence, signposts |

## 🇧🇷 Brazil / LatAm focus

The regional model follows the evolution:

```text
credential theft
      ↓
session / transaction manipulation
      ↓
access brokerage
      ↓
cloud / CI-CD compromise
      ↓
payment authorization & infrastructure targeting
```

High-priority clusters include **BREEZE COMET**, **SLIM SPIDER**, **Exilware/BraZetsu**, **Prilex**, **GoPix**, **APT38/FASTCash** and the current **Ploutus** ATM-jackpotting resurgence.

## 🧠 Intelligence Operations v0.4

The repository now implements the operational intelligence loop:

**PIR → collection plan → source assessment → hypothesis → campaign → watch & warning → detection coverage → intelligence product → exchange → feedback**

New machine-readable layers:
- campaigns with temporal bounds and actor relationships;
- competing hypotheses with explicit alternatives and falsification criteria;
- signposts and Watch & Warning thresholds;
- collection plans mapped to PIRs and collection gaps;
- source-quality assessment separated from analytic confidence;
- ATT&CK Detection Strategy / Data Component crosswalks plus D3FEND controls;
- STIX 2.1 export and TAXII-ready public collection packaging;
- product factory for Campaign Briefs, Watch & Warning, Detection Coverage and Collection Gap reports;
- graph export for actor → campaign → hypothesis → warning → PIR relationships.

See [Intelligence Operations](docs/intelligence-operations.md), [Source Evaluation](docs/source-evaluation.md), [Watch & Warning](docs/watch-warning.md) and [Interoperability](docs/interoperability.md).

## 🔬 Current capabilities

- **ScamClassifier-BR** for Brazilian scam classification;
- **Crime Script Analysis** + F3/FT3/ATT&CK cross-framework modeling;
- NIST SP 800-63-4 identity/onboarding layer;
- OWASP Automated Threats for bot and automated abuse;
- MITRE ATLAS + C2PA for AI/deepfake/provenance context;
- GSMA Open Gateway / CAMARA telecom fraud signals;
- Brazil/LatAm + global financial threat-actor registries;
- FraudSignal and Crosswalk JSON Schemas;
- F3/FT3 upstream synchronization and change watching;
- interactive Navigator covering actors, campaigns, PIRs, warnings, threats and references;
- defensive OSINT research with an evidence gate;
- executable coverage, graph, STIX/TAXII and intelligence-product builders.

## 🧠 Intelligence requirements

v0.3 introduces explicit **Priority Intelligence Requirements** so the project stops being merely encyclopedic.

Examples:

- Which actors can reach or manipulate Brazilian payment-authorization infrastructure?
- Which F3/FT3/ATT&CK behaviors have no detection coverage?
- Which identity/telecom signals materially improve fraud decisions?
- Which emerging AI capabilities are reproducible evidence versus vendor claims?
- Which infrastructure and TTP overlaps indicate campaign convergence?

See [Intelligence Tradecraft](docs/intelligence-tradecraft.md) and [machine-readable requirements](knowledge/intelligence-requirements.yml).

## 🗂 Repository map

```text
FraudIntelligence/
├── docs/                       # Navigator, landscapes and methodology
├── knowledge/
│   ├── actors/                 # Regional + global financial threat actors
│   ├── threats/                # Malware, operations and services
│   ├── classifiers/            # ScamClassifier-BR
│   ├── signals/                # Telecom and future signal families
│   ├── crosswalks/             # Framework mappings
│   └── intelligence-requirements.yml
├── schemas/                    # Versioned intelligence object contracts
├── detections/                 # Defensive analytics
├── osint/                      # Ethical collection methodology
├── research/                   # Evidence quarantine / research backlog
└── tools/                      # Validation, catalog and upstream sync
```

## 🛡 Evidence policy

- primary source before secondary reporting;
- native IDs and naming are preserved;
- actor, alias, malware, campaign and service are different object types;
- mappings require rationale and confidence;
- vendor claims stay labeled as vendor claims;
- uncertainty is explicit;
- a signal is not proof of guilt;
- precise impact/loss figures require dated sourcing.

## Defensive boundary

FraudIntelligence is intended for fraud prevention, threat intelligence, detection engineering, research, education and incident response. It does not publish instructions that materially enable fraud, credential theft, anti-fraud bypass, illicit access or cash-out optimization.
