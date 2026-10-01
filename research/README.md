# Research Backlog

This directory is the quarantine zone for interesting claims that are not yet ready for the core knowledge registry.

## Promotion criteria

A claim can move into `knowledge/` when:
1. a primary source exists;
2. identity and naming are unambiguous;
3. scope is understood;
4. date/version is known;
5. claims are separated from vendor marketing;
6. reproducibility or independent corroboration is documented where appropriate.

## Promoted in v0.2

Verified strongly enough for core inclusion:
- Federal Reserve FraudClassifier / ScamClassifier;
- NIST SP 800-63-4;
- OWASP Automated Threats;
- C2PA;
- GSMA Open Gateway / CAMARA signals;
- BREEZE COMET;
- SLIM SPIDER;
- Exilware / BraZetsu;
- Prilex / GoPix;
- FBI 2026 Ploutus/jackpotting resurgence.

## Research-only / bounded

### Emerging AI and OSINT
- large-scale LLM deanonymization: track as privacy risk; do not operationalize mass re-identification;
- MOSAIV and related multi-agent verification research;
- Project Overwatch / Fusion Center as a cross-domain architecture pattern;
- torrent-metadata profiling research with explicit legal/privacy caveats;
- active underground-forum elicitation agents: research only, no autonomous impersonation implementation.

### Emerging agentic-fraud research
- Transaction Trust Score / DACP;
- CogAgent;
- explainable multi-turn scam detection;
- autonomous fraud-investigation architectures.

### Vendor platforms
- autonomous investigation performance claims;
- predictive-resilience / quantum-related marketing claims;
- distributed-tokenization platform claims.

### Large regional actor lists

The uploaded 55-item Brazil/LatAm list is treated as a candidate queue rather than a verified registry because it mixes:
- actors;
- aliases;
- malware;
- infrastructure;
- campaigns;
- duplicate entries;
- vendor naming conventions.

Each candidate must be normalized and sourced before promotion.

## Research template

```yaml
claim:
primary_source:
secondary_sources: []
date:
scope:
what_is_confirmed:
what_is_vendor_claim:
open_questions: []
confidence:
reviewer:
last_verified:
```

Interesting is not the same thing as established.
