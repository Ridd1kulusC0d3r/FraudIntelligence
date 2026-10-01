# Identity, Onboarding & Mule Prevention

Identity fraud is not just an authentication problem. It begins with proofing, enrollment, account creation, device binding and recovery.

## NIST SP 800-63-4

Revision 4 of the NIST Digital Identity Guidelines supersedes SP 800-63-3 and expands fraud-related requirements and recommendations for identity proofing.

For Fraud Intelligence, the useful analytical connection is:

```text
identity proofing
→ enrollment
→ authenticator binding
→ device/account continuity
→ transaction behavior
→ recovery / re-proofing
```

## Threat themes

- synthetic identity;
- automated account creation;
- forged / manipulated evidence;
- deepfake-assisted identity proofing;
- credential compromise;
- phishing-resistant authentication gaps;
- account recovery abuse;
- mule-account onboarding.

## Observable families

- repeated enrollment attributes across nominally distinct identities;
- device reuse across unrelated accounts;
- contact-point churn;
- short account-age-to-first-high-risk-transfer interval;
- identity/document inconsistencies;
- network/telecom events inconsistent with established account history.

## Privacy

Identity-risk models should use the minimum necessary data and avoid protected-attribute profiling.

Signals are evidence inputs, not guilt labels.
