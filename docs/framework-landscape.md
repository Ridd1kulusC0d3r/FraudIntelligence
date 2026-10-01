# Fraud Intelligence Framework Landscape

**Last reviewed:** 2026-10-01

The term “framework” is overused. This page separates behavioral knowledge bases, taxonomies, journey models, governance guidance, regulations and sharing networks.

## Verified core

| Name | Class | Scope | Maturity / status | Primary source |
|---|---|---|---|---|
| MITRE Fight Fraud Framework (F3) | Open behavioral knowledge base | Financial cyber fraud TTPs | Published 2026; active | https://ctid.mitre.org/categories/fraud |
| Stripe FT3 | Open vendor framework | Fraud tools, tactics, techniques | Public repository | https://github.com/stripe/ft3 |
| Group-IB Fraud Matrix 2.0 | Vendor framework | Cross-industry digital fraud | v2.0 launched 2025 | https://www.group-ib.com/products/fraud-protection/fraud-matrix/ |
| FIST | Academic/open framework | Fraud threat modeling + social engineering | Research framework | https://arxiv.org/abs/2506.05740 |
| MITRE ATT&CK | Open knowledge base | Cyber adversary TTPs | Mature | https://attack.mitre.org/ |
| DISARM | Open framework | Information manipulation TTPs | Active | https://www.disarm.foundation/ |
| ACFE Fraud Tree | Taxonomy | Occupational fraud | Mature | https://www.acfe.com/fraud-resources/fraud-tree |
| COSO/ACFE Fraud Risk Management Guide | Governance guidance | Enterprise fraud risk management | 2nd ed. 2023 | https://www.acfe.com/fraud-resources/fraud-risk-tools---coso |
| FATF | Standards / typologies | AML/CFT, proceeds and financial crime | Global standard-setter | https://www.fatf-gafi.org/ |
| FRIDA | Emerging sharing scheme | Inter-PSP fraud information | Rulebook v0.1 consultation in 2026 | https://www.europeanpaymentscouncil.eu/what-we-do/other-schemes/fraud-information-distribution-arrangement |
| FIRE | Sharing program | Financial institutions ↔ Meta scam intelligence | Operational program | https://about.fb.com/news/2024/10/meta-partners-with-uk-banks-to-combat-scams/ |
| Global Signal Exchange | Cross-sector sharing network | Scam/fraud/abuse signals | Operational network | https://www.globalsignalexchange.org/ |
| BCB Resolução Conjunta nº 6/2023 | Regulation | Fraud-indicator information sharing in Brazil | In force | https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=6&tipo=Resolu%C3%A7%C3%A3o+Conjunta |
| Scams Prevention Framework | Regulation / governance | Australia; banks, telcos, digital platforms | Staged implementation | https://www.accc.gov.au/about-us/scams-prevention-framework |

## Key observations

### MITRE F3
F3 is the strongest candidate for a shared cyber/fraud behavioral backbone because it is open, behavior-based and explicitly designed to relate fraud and cyber events.

### FT3
FT3 is valuable as a second open ATT&CK-style fraud model and as a source for crosswalk research. Keep native FT3 identifiers and wording rather than flattening it into F3.

### Group-IB Fraud Matrix
Useful for practical fraud operations, actor/campaign context, detections and mitigations. It is a vendor framework, so the project links and maps rather than cloning proprietary content.

### FIST
Important because it makes social engineering and psychological manipulation explicit in fraud threat modeling. It also provides an academic bridge between cybersecurity, criminology and behavioral science.

### FRIDA
As of 2026-10-01, FRIDA should be treated as an **emerging scheme**, not a fully deployed Europe-wide intelligence platform. The EPC published rulebook v0.1 for consultation from September to December 2026; formal v1.0 is planned for 2027.

### Scam Prevention Framework — Australia
The Act was assented in February 2025. The ACCC describes staged implementation: AFCA membership from September 2026 for covered entities and most substantive obligations from March 2027.

## Not promoted to the core registry yet

Claims about emerging products, academic systems or protocols must be verified against a primary publication or repository before inclusion. See [Research Backlog](../research/README.md).

This includes, until independently validated:
- Transaction Trust Score / DACP;
- CogAgent;
- SentinelAI;
- “Open-Source Fraud Intelligence Exchange” claims;
- product performance claims for autonomous investigation platforms;
- quantitative vendor claims without a reproducible methodology.

The rule is simple: interesting is not the same thing as established.
