# TAXII 2.1 Publication Profile

This directory defines the intended publication profile for FraudIntelligence.

Collection:
- title: `FraudIntelligence Public CTI`
- media: `application/taxii+json;version=2.1`
- content: STIX 2.1 objects exported by `tools/export_stix.py`
- handling: only `TLP:CLEAR` objects are eligible for the public collection

Generate a static TAXII envelope:

```bash
python tools/build_taxii_package.py --out dist/taxii
```

This output is suitable as a fixture or backing data for a TAXII implementation. It is not itself a TAXII server.
