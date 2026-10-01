# ATM & PoS Fraud Intelligence Vertical

This vertical demonstrates how the project converts threat intelligence into defensive analytics.

## Threat families

The ATM ecosystem has two broad defensive problem classes:

- **logical / software attacks**: ATM malware, jackpotting, switch manipulation, digital skimming;
- **physical attacks**: skimming hardware, black-box attacks, cabinet tampering and destructive attacks.

Brazil adds a strong PoS/ATM context through Prilex history, skimming and physical attacks against cash infrastructure.

## Representative families / operations

Skimer, Ploutus, Tyupkin/Padpin, Carbanak/Anunak, GreenDispenser, Alice, Cutlet Maker, ATMitch, ATMDtrack/Dtrack, WinPot/ATMPot, FASTCash and Prilex.

These are tracked as intelligence entities, not as malware deployment instructions.

## Detection engineering model

### Reconciliation

For every cash-dispense event, expect a corresponding authorized transaction in the payment/switch layer.

```text
ATM dispense event
AND no matching switch authorization within tolerance window
→ investigate as possible jackpotting / authorization manipulation
```

### Expected sequence

A normal transaction produces a predictable chain of events. A dispense command without expected card/PIN/transaction events is suspicious.

### Detection by absence

Useful negative signals:
- missing heartbeat before/after suspicious activity;
- journal stops while physical or switch activity continues;
- dispense without host authorization;
- missing peripheral status;
- unexplained telemetry silence.

### Correlation

Strong combinations:
- cabinet-open event + new USB + new process;
- network disable + dispense;
- unexpected reboot + XFS activity;
- abnormal cassette depletion + repeated dispense sequence.

## Telemetry

- Electronic Journal (EJ)
- XFS / middleware logs
- Windows Event Logs
- ATM monitoring / heartbeat
- switch / ISO 8583 telemetry
- cabinet and vibration sensors
- camera / physical-security events

## Framework mapping

Use MITRE ATT&CK for technical cyber behavior and MITRE F3 for fraud behavior. Do not confuse MITRE **F3** with MITRE **FiGHT**, which is a different 5G-focused project.

## Defensive modernization

Priorities:
- application allowlisting;
- removable-media control;
- host hardening;
- device authentication;
- protected key management;
- switch-side integrity / authentication;
- physical sensor correlation;
- modern XFS security capabilities where supported.

## Research questions

- How effective is device authentication across mixed legacy ATM estates?
- Can switch-host reconciliation detect manipulation with acceptable false-positive rates?
- How should absence baselines differ by ATM location and operating profile?
- How can Brazilian physical-attack data be fused with cyber/fraud telemetry?
- How should F3 and ATT&CK mappings represent hybrid ATM/PoS incidents?
