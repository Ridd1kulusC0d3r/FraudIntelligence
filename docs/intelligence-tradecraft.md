# Intelligence Tradecraft

**Status:** v0.3 operating-model foundation  
**Last reviewed:** 2026-10-01

FraudIntelligence should not become a museum of threat names. Intelligence exists to reduce uncertainty for a decision.

## What was missing

### 1. Intelligence requirements

The repository previously started at collection and normalization. That is backwards for mature intelligence work.

The correct chain is:

```text
decision → intelligence requirement → collection → analysis
→ assessment → detection/control → outcome → feedback
```

The first machine-readable PIRs now live in `knowledge/intelligence-requirements.yml`.

### 2. Source quality vs analytic confidence

These are different concepts.

- **source quality** asks how credible, direct and methodologically strong the evidence is;
- **analytic confidence** asks how strongly the available evidence supports the assessment.

A prestigious source can still make a low-confidence attribution. Multiple mediocre sources repeating one another do not create independent corroboration.

The project should evolve toward an explicit source-evaluation model while keeping the current claim-confidence field.

Reference: ODNI ICD 203 Analytic Standards  
https://www.dni.gov/files/documents/ICD/ICD-203.pdf

## 3. Hypotheses, alternatives and signposts

Actor attribution should be represented as competing hypotheses, not just a string field.

Future objects should support:

```yaml
hypothesis:
alternatives: []
supporting_evidence: []
contradicting_evidence: []
indicators_or_signposts: []
confidence:
what_would_change_our_mind:
```

This matters especially when vendor naming overlaps.

## 4. Actor identity resolution

Threat-actor naming is messy.

APT38 and Lazarus are a useful example: public reporting overlaps, but treating them as simple aliases destroys analytical precision.

The graph needs:
- canonical actor object;
- aliases;
- associated groups;
- vendor-specific names;
- relationship confidence;
- first/last seen;
- attribution basis;
- temporal validity.

## 5. Campaign layer

The biggest structural gap is now **campaign intelligence**.

An actor profile answers *who*. A campaign object should answer:

- when;
- against whom;
- through which infrastructure;
- using which procedures;
- with what objective;
- with what observable changes over time.

This should become the bridge between actor knowledge and detections.

## 6. Collection management

Every PIR should map to:
- required sources;
- existing coverage;
- collection gaps;
- refresh cadence;
- legal/privacy constraints;
- stale-data threshold.

Without collection management, “OSINT” degenerates into browsing with better branding.

## 7. Detection engineering crosswalk

MITRE ATT&CK now exposes Detection Strategies and Data Components. FraudIntelligence should map:

```text
actor/campaign
→ behavior
→ ATT&CK/F3/FT3
→ observable
→ data component
→ detection strategy
→ project analytic
→ D3FEND countermeasure
```

Primary references:
- https://attack.mitre.org/detectionstrategies/
- https://attack.mitre.org/datacomponents/
- https://d3fend.mitre.org/

## 8. Exchange standards

The internal graph should be exportable rather than trapped in project-specific YAML.

Targets:
- **STIX 2.1** for CTI objects and relationships;
- **TAXII 2.1** for exchange;
- MISP interoperability where useful;
- GraphML / JSON for analytical graphs.

Primary references:
- https://www.oasis-open.org/standard/stix2-1/
- https://www.oasis-open.org/standard/taxii-version-2-1/

## 9. Handling and sharing

Add FIRST TLP 2.0 to every shareable intelligence product.

```text
TLP:RED · TLP:AMBER · TLP:GREEN · TLP:CLEAR
```

Reference: https://www.first.org/tlp/

TLP controls sharing boundaries; it is not a confidence score.

## 10. Intelligence products

A mature repository should generate reproducible products from the same knowledge graph:

- Threat Actor Profile;
- Campaign Brief;
- Intelligence Estimate;
- Watch & Warning note;
- Weekly Fraud Threat Brief;
- Detection Coverage Assessment;
- Collection Gap Report;
- Executive one-page assessment.

The source objects should remain the same. Only the view changes.

## 11. Metrics that matter

Avoid vanity metrics such as number of actors or links collected.

Measure:
- PIR coverage;
- stale-source percentage;
- percentage of claims with primary evidence;
- actor/campaign objects with temporal bounds;
- TTP → observable coverage;
- observable → telemetry coverage;
- telemetry → tested detection coverage;
- intelligence-to-detection conversion rate;
- mean time from new evidence to updated assessment;
- percentage of assessments later revised;
- false-positive / confirmed-outcome feedback.

## Target state

```text
KNOWLEDGE BASE
     ↓
INTELLIGENCE REQUIREMENTS
     ↓
COLLECTION + SOURCE EVALUATION
     ↓
HYPOTHESES + TEMPORAL GRAPH
     ↓
CAMPAIGNS + ACTORS + INFRASTRUCTURE
     ↓
DETECTION / CONTROL COVERAGE
     ↓
WATCH & WARNING
     ↓
MEASURED FEEDBACK
```

That is the difference between a very good repository and an intelligence system.
