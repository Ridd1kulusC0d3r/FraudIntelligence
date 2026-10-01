# OSINT for Fraud Intelligence

## Mission

Use public information to understand fraud ecosystems, infrastructure, campaigns, narratives, controls and trends without interacting with victims or enabling criminal activity.

## Passive source classes

- regulator and government publications;
- law-enforcement cases and advisories;
- court records where lawful;
- framework and standards repositories;
- vendor threat research;
- academic papers;
- public scam reports and complaint trends;
- domain / certificate / infrastructure metadata;
- public company and platform safety reporting;
- public code and package repositories;
- archived public web content.

## Analytical outputs

- campaign timelines;
- infrastructure clusters;
- entity graphs;
- scam-narrative evolution;
- actor / alias hypotheses;
- framework mappings;
- regional trend reports;
- observable catalogs;
- detection hypotheses.

## Evidence rules

- preserve source URL and capture time;
- distinguish observation from inference;
- track confidence per claim;
- do not infer guilt from a single indicator;
- document contradictory evidence;
- separate entity resolution from attribution.

## Graph model

Useful nodes:
`actor, alias, campaign, domain, URL, phone, email, account, beneficiary, device, wallet, merchant, malware, technique, organization, source`

Useful edges:
`uses, controls, mentions, resolves-to, transacts-with, attributed-to, observed-in, overlaps-with, supported-by`

## Ethical boundary

Do not purchase illicit data, impersonate victims, engage in social engineering, redistribute stolen credentials or operationalize criminal access.

The project favors passive and lawful collection.
