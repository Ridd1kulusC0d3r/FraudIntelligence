# Methodology

## 1. Evidence hierarchy

Preferred order:

1. official framework / standards repository;
2. regulator / government / law-enforcement publication;
3. peer-reviewed or preprint research with methods;
4. vendor primary research;
5. reputable secondary reporting;
6. community discussion;
7. unsupported claim.

Lower-tier material can be a lead, but not silently promoted to fact.

## 2. Required metadata

Every durable knowledge object should include:

- `id`
- `name`
- `type`
- `description`
- `source`
- `source_class`
- `status`
- `confidence`
- `first_seen` when applicable
- `last_verified`
- `tags`

## 3. Preserve native identifiers

Never overwrite source IDs. Crosswalks should link IDs, not replace them.

## 4. Mapping confidence

Cross-framework mappings use:

- `exact`
- `strong`
- `partial`
- `contextual`
- `none`

Every mapping needs a rationale.

## 5. From intelligence to detection

```text
claim → behavior → observable → telemetry → analytic → control → outcome
```

Example:

```text
unauthorized ATM dispensing
→ dispense command without normal transaction sequence
→ XFS/EJ dispense event with no matching switch authorization
→ ATM journal + switch telemetry
→ reconciliation analytic
→ alert / hold / investigation
→ confirmed or rejected fraud case
```

## 6. Detection by absence

Fraud systems often have expected event pairs or sequences. Missing expected signals can be stronger than a suspicious positive event.

Patterns:
- transaction without expected authentication;
- payout without source event;
- dispense without authorization;
- beneficiary change without expected verification;
- device activity without heartbeat;
- abrupt logging silence in an otherwise active channel.

Absence rules must model telemetry failure separately from fraud.

## 7. Human factors

Do not infer vulnerability from protected characteristics or create victim “risk stereotypes.”

Prefer event- and context-based observations such as urgency, channel switching, prolonged grooming, authority impersonation, isolation instructions and repeated payment escalation.

## 8. Safe research boundary

This repository documents fraud from a defensive perspective. It excludes instructions that materially enable credential theft, anti-fraud bypass, laundering/cash-out optimization, victimization scripts or monitoring evasion.
