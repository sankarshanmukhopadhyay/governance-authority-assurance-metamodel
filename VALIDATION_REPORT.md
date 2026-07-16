# GAAM v0.5.0 Validation Report

**Status:** PASS
**Checks:** 36  
**Passed:** 36  
**Failed:** 0

| Check | Status | Evidence |
|---|---|---|
| `requirement-uniqueness` | PASS | 190 requirements |
| `requirement-index` | PASS | 190 indexed requirements |
| `schema:authority` | PASS | valid Draft 2020-12 schema |
| `schema:delegation` | PASS | valid Draft 2020-12 schema |
| `schema:evidence` | PASS | valid Draft 2020-12 schema |
| `schema:assurance` | PASS | valid Draft 2020-12 schema |
| `schema:decision-receipt` | PASS | valid Draft 2020-12 schema |
| `schema:governance-event` | PASS | valid Draft 2020-12 schema |
| `schema:appeal` | PASS | valid Draft 2020-12 schema |
| `schema:remedy` | PASS | valid Draft 2020-12 schema |
| `schema:agent-governance-identity` | PASS | valid Draft 2020-12 schema |
| `schema:runtime-envelope` | PASS | valid Draft 2020-12 schema |
| `schema:profile-manifest` | PASS | valid Draft 2020-12 schema |
| `schema:conformance-claim` | PASS | valid Draft 2020-12 schema |
| `schema:gaam-package` | PASS | valid Draft 2020-12 schema |
| `profile:foundation` | PASS | 36 requirements; dependency closure=True |
| `profile:machine-actionable-governance` | PASS | 26 requirements; dependency closure=True |
| `profile:delegated-authority` | PASS | 32 requirements; dependency closure=True |
| `profile:runtime-governance` | PASS | 21 requirements; dependency closure=True |
| `profile:agentic-systems` | PASS | 51 requirements; dependency closure=True |
| `profile:trust-graph` | PASS | 9 requirements; dependency closure=True |
| `profile:continuous-assurance` | PASS | 19 requirements; dependency closure=True |
| `profile:high-impact-systems` | PASS | 22 requirements; dependency closure=True |
| `valid-fixture:cross-registry-recognition/authority.valid.json` | PASS | accepted as expected |
| `valid-fixture:cross-registry-recognition/decision-receipt.valid.json` | PASS | accepted as expected |
| `invalid-fixture:cross-registry-recognition/authority.invalid.json` | PASS | rejected as expected |
| `claim:cross-registry-recognition` | PASS | valid conformance claim |
| `valid-fixture:delegated-agent-purchase/authority.valid.json` | PASS | accepted as expected |
| `valid-fixture:delegated-agent-purchase/decision-receipt.valid.json` | PASS | accepted as expected |
| `invalid-fixture:delegated-agent-purchase/authority.invalid.json` | PASS | rejected as expected |
| `claim:delegated-agent-purchase` | PASS | valid conformance claim |
| `valid-fixture:high-impact-multi-agent-service/authority.valid.json` | PASS | accepted as expected |
| `valid-fixture:high-impact-multi-agent-service/decision-receipt.valid.json` | PASS | accepted as expected |
| `invalid-fixture:high-impact-multi-agent-service/authority.invalid.json` | PASS | rejected as expected |
| `claim:high-impact-multi-agent-service` | PASS | valid conformance claim |
| `local-links` | PASS | all local links resolve |
