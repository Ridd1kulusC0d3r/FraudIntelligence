# Detection Engineering

Fraud intelligence becomes useful when it changes what defenders can observe, detect, prevent or disrupt.

## Detection chain

```text
TTP → observable → telemetry → analytic → decision → outcome → feedback
```

## Detection families

### Transaction reconciliation
Compare records that should agree: payout ↔ authorization, transfer ↔ authentication, refund ↔ original purchase, ATM dispense ↔ switch authorization.

### Sequence integrity
Model expected event ordering and alert on impossible or suspicious sequences.

### Behavioral deviation
Use peer and entity baselines with explicit false-positive controls.

### Graph detection
Detect risky structures and relationships such as dense beneficiary fan-in/fan-out, shared device clusters, repeated infrastructure reuse or rapid multi-account convergence.

### Detection by absence
Alert when expected telemetry or event pairs disappear.

## Requirements for contributed detections

Each detection documents hypothesis, data sources, logic, false positives, blind spots, response, framework mappings and test method.

Detection examples are defensive templates, not production-ready rules.
