# Brazil & LatAm Financial Threat Landscape

**Last reviewed:** 2026-10-01

This page intentionally separates **state-linked actors**, **financially motivated eCrime**, **malware families** and **criminal services**.

## Verified high-priority clusters

### BREEZE COMET

GTIG/Mandiant tracks BREEZE COMET, formerly UNC5669, as a financially motivated actor targeting Brazilian financial services, retail and e-commerce organizations.

Strategic relevance:
- targets payment systems and banking software;
- seeks access that can support Pix, STR and Boleto transactions;
- targets mTLS credentials, CI/CD, cloud and Active Directory;
- develops custom tooling for reconnaissance, persistence, lateral movement and exfiltration;
- GTIG reported evidence of generative-AI use in malware development.

This is a strong example of **payment-infrastructure intrusion**, not traditional endpoint banking malware.

### SLIM SPIDER

CrowdStrike tracks SLIM SPIDER as a Brazil-based eCrime adversary active against Brazilian financial institutions since at least March 2026.

Strategic relevance:
- cloud credential theft;
- secrets / credential-manager discovery;
- cryptocurrency-custody targeting;
- DevOps / pipeline and container environment interest;
- deep operational knowledge of Pix and Brazilian financial infrastructure.

### Exilware / BraZetsu

Group-IB attributes BraZetsu with high confidence to Brazilian actor Exilware.

Strategic relevance:
- Python/Nuitka Windows framework;
- deep reconnaissance of banking, ERP, e-commerce, industrial and corporate environments;
- searches for Brazilian CNAB financial-remittance artifacts and digital certificates;
- supports an Initial Access Broker business model through the Infected Marketplace;
- evidence suggests extensive generative-AI use in development and possibly backend triage.

BraZetsu is important because it **separates compromise from monetization**.

### Prilex

Prilex evolved from Brazilian ATM attacks into modular PoS malware.

Important correction: describing this as “breaking EMV cryptography” is imprecise. Kaspersky documented manipulation of the transaction flow, interception of PoS/PIN-pad communication and the generation of fresh EMV cryptograms for so-called GHOST transactions.

A useful defensive observable is not only malware presence but **transaction-flow anomalies**, including unexpected shifts from contactless to chip transactions and abnormal cryptogram behavior.

### GoPix

Kaspersky documents GoPix as an advanced Brazilian banking threat targeting financial and cryptocurrency users, with memory-resident components and man-in-the-middle behavior.

### Lazarus / FASTCash

Lazarus remains the major state-linked reference for payment-switch attacks. FASTCash demonstrates that the ATM can behave normally while authorization logic upstream has been compromised.

## ATM resurgence

The FBI reported in February 2026 that more than 700 of roughly 1,900 U.S. ATM jackpotting incidents reported since 2020 occurred in 2025, with more than US$20 million in 2025 losses. The FBI specifically referenced Ploutus-family malware.

DOJ cases in 2026 also document a large Tren de Aragua-linked ATM-jackpotting investigation.

## Intelligence conclusion

The regional progression is better described as:

```text
credential theft
→ session / transaction manipulation
→ access brokerage
→ cloud / CI-CD compromise
→ payment authorization and infrastructure targeting
```

That progression is more useful than calling every sophisticated criminal cluster an “APT”.
