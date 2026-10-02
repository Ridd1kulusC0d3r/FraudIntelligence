# Intelligence Operations

**Release:** v0.4  
**Last reviewed:** 2026-10-01

FraudIntelligence now treats intelligence as an operating cycle rather than a content library.

~~~text
PIR
 ↓
Collection Plan
 ↓
Source Evaluation
 ↓
Evidence
 ↓
Competing Hypotheses
 ↓
Campaign / Actor Assessment
 ↓
Watch & Warning
 ↓
Detection Coverage
 ↓
Intelligence Product
 ↓
Sharing / STIX / TAXII
 ↓
Outcome & Feedback
 └──────────────→ PIR
~~~

## Implemented objects

| Capability | Machine-readable source |
|---|---|
| Intelligence requirements | knowledge/intelligence-requirements.yml |
| Collection management | knowledge/collection-plans.yml |
| Source evaluation | knowledge/source-assessments.yml |
| Campaign intelligence | knowledge/campaigns/ |
| Competing hypotheses | knowledge/hypotheses/ |
| Watch & Warning | knowledge/watch-warning.yml |
| Detection coverage | knowledge/detection-coverage.yml |
| STIX IDs | interoperability/stix/id-map.yml |

## Executable outputs

~~~bash
python tools/validate_knowledge.py
python tools/build_coverage.py
python tools/export_stix.py
python tools/build_taxii_package.py
python tools/build_products.py
python tools/build_graph.py
~~~

## Analytical standards

The model adopts useful disciplines described by ICD 203: characterize source quality, distinguish evidence from judgment, express uncertainty, analyze alternatives and maintain decision relevance. The repository does not claim formal U.S. Intelligence Community compliance.

## Detection model

ATT&CK Detection Strategies organize detection methodologies, while Data Components identify properties relevant to detecting techniques. FraudIntelligence uses those where they fit and preserves project-native fraud detections where ATT&CK has no precise match.

D3FEND is used as a defensive-technique vocabulary and knowledge graph. A D3FEND relationship does not by itself prove a control is effective in a specific environment.

## Sharing model

Public repository artifacts are TLP:CLEAR unless explicitly stated otherwise. FIRST TLP 2.0 markings express sharing boundaries, never confidence.
