# Brazil Fraud Intelligence Layer

## Why Brazil needs its own layer

Brazil combines instant payments, high digital-banking adoption, active social-engineering ecosystems, account-mule networks, mobile-first fraud and a regulatory requirement for fraud-indicator information sharing.

The goal here is not a separate taxonomy. It is a regional context layer mapped into the common object model.

## Regulatory anchor

### Resolução Conjunta CMN/BCB nº 6, de 23 de maio de 2023

The rule establishes requirements for sharing data and information on indications of fraud among financial institutions, payment institutions and other institutions authorized by Banco Central do Brasil.

Primary source:
https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=6&tipo=Resolu%C3%A7%C3%A3o+Conjunta

## Brazil-specific intelligence themes

- Pix-related social engineering and authorized transfer scams;
- account takeover and device compromise;
- mule-account recruitment and beneficiary networks;
- fake support / fake bank representative scams;
- SIM/telecom and messaging-channel abuse;
- boleto / QR-code redirection;
- merchant and marketplace fraud;
- identity fraud and synthetic identities;
- card-present / card-not-present fraud;
- ATM / PoS malware and skimming;
- deepfake / impersonation fraud;
- fraud-as-a-service ecosystems.

## Data-sharing design

A useful implementation should separate:

1. **signal** — observable risk indicator;
2. **claim** — analytical assertion;
3. **case** — institution-specific investigation;
4. **entity** — account, device, identity, beneficiary, domain, phone, merchant;
5. **relationship** — typed connection between entities;
6. **disposition** — confirmed fraud, false positive, under review, unknown.

This reduces the temptation to treat a shared indicator as proof of wrongdoing.

## Privacy and governance

Data minimization, purpose limitation, access control, retention, auditability and legal review should be first-class design requirements.

This repository is technical research, not legal advice.
