# CTI Interoperability

## STIX 2.1

FraudIntelligence exports supported actor and campaign objects as STIX 2.1 JSON. Project actors map to STIX intrusion-set; project campaigns map to STIX campaign; source URLs become external references; project IDs are preserved in custom x_fraudintelligence fields.

Reference: https://www.oasis-open.org/standard/stix-version-2-1/

## TAXII 2.1

TAXII 2.1 is a REST application-layer protocol for exchanging CTI, commonly STIX. The repository provides a TAXII-ready object envelope builder and collection profile. It does not claim to run a conformant TAXII server inside GitHub Pages.

Reference: https://www.oasis-open.org/standard/taxii-version-2-1/

## TLP 2.0

Shareable products use FIRST TLP 2.0: TLP:RED, TLP:AMBER, TLP:GREEN and TLP:CLEAR. TLP controls sharing boundaries; it is not an intelligence-confidence label.

Reference: https://www.first.org/tlp/
