# Fraud & Scam Classification

Classification is intentionally separate from TTP mapping.

## Why

If every institution calls the same event something different, trend analysis and intelligence sharing collapse before detection even starts.

The Federal Reserve's FraudClassifier and ScamClassifier are useful references because they prioritize consistent reporting rather than adversary behavior.

## Project classification axes

FraudIntelligence uses independent dimensions:

1. **Authorization**
   - authorized-by-customer
   - unauthorized
   - access-surrendered
   - unknown

2. **Primary mechanism**
   - impersonation
   - relationship-or-trust
   - goods-or-services
   - investment
   - account-takeover
   - malware-or-device
   - merchant-or-refund-abuse
   - identity
   - insider
   - other

3. **Channel**
   - voice
   - messaging
   - email
   - social
   - web
   - mobile-app
   - physical
   - multi-channel

4. **Payment rail / value channel**
   - pix
   - card
   - boleto
   - bank-transfer
   - cash
   - crypto
   - wallet
   - other

5. **Outcome**
   - attempted
   - successful-loss
   - blocked
   - recovered
   - unknown

## ScamClassifier-BR

The draft in `knowledge/classifiers/scamclassifier-br.yml` adapts classification dimensions to Brazilian reality without claiming Federal Reserve endorsement.

It deliberately does **not** make a risk decision about a person.

### Example

A fake-bank-support case may be classified as:

```yaml
authorization: authorized-by-customer
mechanism: impersonation
impersonation: bank
channel: [voice, messaging]
payment_rail: pix
outcome: successful-loss
```

The same case can then be separately mapped to F3/FT3 techniques, manipulation patterns and detections.

## Design rule

Classification is descriptive.

A label must never be treated as proof of criminal intent, guilt or identity.
