# Fraud Intelligence Framework Landscape

**Last reviewed:** 2026-10-01

“Framework” is not a useful bucket by itself. FraudIntelligence classifies sources by analytical function.

## Behavioral and TTP knowledge

| Name | Class | Use |
|---|---|---|
| MITRE Fight Fraud Framework (F3) | behavioral knowledge base | financial-fraud TTPs |
| Stripe FT3 | open vendor framework | fraud tactics and techniques |
| Group-IB Fraud Matrix 2.0 | vendor framework | fraud behavior, campaigns, detections |
| MITRE ATT&CK | cyber knowledge base | technical intrusion |
| DISARM | manipulation framework | information manipulation |
| FIST | academic/open framework | technical + social-engineering fraud modeling |

## Classification

| Name | Class | Use |
|---|---|---|
| Federal Reserve FraudClassifier | payment-fraud classification | consistent classification of payment fraud |
| Federal Reserve ScamClassifier | scam classification | scam reporting and trend analysis |
| EBA payment-fraud reporting concepts | regulatory taxonomy | payer manipulation vs. fraudster-initiated payment |
| FraudIntelligence ScamClassifier-BR | project draft | Brazilian Pix/card/boleto/relationship scam classification |

## Journey / crime scripts

| Name | Class | Use |
|---|---|---|
| Fraud / Scam Kill Chains | journey models | sequence and interruption points |
| Online Operations Kill Chain | cross-platform operations model | multi-channel campaigns |
| Crime Script Analysis | crime science | scenes, prerequisites and transitions |

## Prevention theory

| Name | Class | Use |
|---|---|---|
| Situational Crime Prevention | crime-science prevention model | increase effort/risk; reduce reward/opportunity |
| Routine Activity Theory | criminology model | offender + target + absent guardian |
| ACFE Fraud Triangle / Diamond | perpetrator-side explanatory models | occupational/insider context |

These perpetrator models should not be used as a generic explanation for why scam victims comply.

## Identity and onboarding

| Name | Class | Use |
|---|---|---|
| NIST SP 800-63-4 | digital identity guidance | identity proofing, authentication, federation, fraud controls |
| GSMA Open Gateway / CAMARA | network APIs | SIM/device/number signals |

## Automated abuse and AI

| Name | Class | Use |
|---|---|---|
| OWASP Automated Threats | automation taxonomy | carding, credential stuffing, fake accounts and related bot abuse |
| MITRE ATLAS | AI threat knowledge base | threats to and involving AI systems |
| C2PA | provenance standard | content provenance / AI-media transparency |

## Governance / sharing

ACFE/COSO, FATF, BCB Resolução Conjunta nº 6/2023, FRIDA, FIRE, Global Signal Exchange and the Australian Scams Prevention Framework remain governance and sharing references, not behavioral TTP frameworks.

## Crosswalk rule

Do not flatten these into one matrix.

A useful case can simultaneously carry:

```text
classification: ScamClassifier-BR
journey: crime script / scam kill chain
behavior: F3 + FT3 + ATT&CK
manipulation: FIST / project vocabulary
automation: OWASP OAT
identity: NIST 800-63-4
telecom: CAMARA signal
control: situational prevention / technical control
governance: BCB / FRIDA / GSE
```

That preserves what each source actually explains.
