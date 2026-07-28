---
title: "Illustrative Implementation Report"
permalink: /implementation-reports/examples/illustrative-report/
parent: "Implementation Reports"
nav_order: 8
artifact_type: "Illustrative implementation report"
normative_status: "Informative; non-conformant example"
---
# Illustrative Implementation Report

{% include gaam-meta.html %}

> **Status:** Illustrative and non-authoritative. This report is intentionally non-conformant and does not describe a real implementation. It demonstrates how to disclose scope, evidence and failures without overstating assurance.

## 1. Implementation identity

| Field | Illustrative entry |
|---|---|
| Implementer | Example Services Cooperative |
| Target | `urn:example:delegated-purchase-service:test-2026-07` |
| Target version | Build `2026.07.18-test1` |
| Environment | Isolated test environment |
| GAAM version | 0.9.0 |
| Profiles evaluated | Foundation; Delegated Authority; Runtime Governance |
| Proposed evidence level | No conformance claim issued |
| Observation period | 2026-07-18 to 2026-07-20 |

## 2. Scope

The target accepts purchase requests from a software agent acting for an organisational principal. It evaluates the agent's delegation, transaction ceiling, permitted merchant category and validity period before permitting or denying the purchase.

Included components are the delegation store, policy decision point, decision-receipt generator and test event store. Payment execution, identity proofing, merchant onboarding and production operations are excluded.

## 3. Profile selection

| Profile | Included | Rationale | Dependency status |
|---|---:|---|---|
| Foundation | Yes | Core authority, evidence, decision and accountability semantics are in scope | Applicable |
| Delegated Authority | Yes | Agent authority derives from a constrained delegation | Foundation included |
| Runtime Governance | Yes | Each proposed purchase is evaluated before execution | Foundation included |
| Agentic Systems | No | Agent-specific lifecycle and accountability requirements were not evaluated | Not claimed |
| Other profiles | No | Outside the declared target and test plan | Not claimed |

The omission of the Agentic Systems Profile is material. The implementation must not present this report as evidence that its agent lifecycle or agent accountability controls conform to GAAM.

## 4. Authority and delegation evidence

The test delegation authorises purchases up to 500 units for office supplies from 2026-07-18T00:00:00Z until 2026-07-31T23:59:59Z. Redelegation is prohibited.

Evidence reviewed:

| Evidence ID | Description | Disposition |
|---|---|---|
| `EX-EVD-001` | Test authority record and source fixture | Accepted for test scope only |
| `EX-EVD-002` | Delegation record with purpose, ceiling and validity | Accepted for test scope only |
| `EX-EVD-003` | Delegation status export | Accepted with limitation: export has no independent integrity protection |

## 5. Validation and behavioural results

| Test | Expected | Actual | Result |
|---|---|---|---|
| Schema validation of authority and receipt | Accept valid fixtures | Accepted | Pass |
| Purchase at 450 units within scope | Permit | Permitted | Pass |
| Purchase at 650 units | Deny | Denied | Pass |
| Purchase after delegation expiry | Deny | Denied | Pass |
| Purchase after delegation revocation | Deny | Permitted for up to 12 minutes | **Fail** |
| Redelegation attempt | Deny | Denied | Pass |

The revocation test failed because the decision point refreshed its delegation cache every 15 minutes and did not receive an invalidation event. This creates a period during which revoked authority may continue to be accepted.

## 6. Deviations and residual risk

| ID | Deviation | Consequence | Proposed correction | Status |
|---|---|---|---|---|
| `EX-DEV-001` | Revocation is not propagated immediately to the decision point | Revoked authority may remain usable during cache lifetime | Add signed invalidation events and fail-closed maximum-staleness policy | Open |
| `EX-DEV-002` | Evidence export lacks an independently verifiable digest | Historical evidence may be altered without detection | Generate manifest and signed digest at export | Open |
| `EX-DEV-003` | No affected-party notice workflow was evaluated | A denied or disputed action may lack an operational challenge route | Define notice and review workflow before production use | Open |

The failed revocation control is material to the Delegated Authority and Runtime Governance profile claims. Passing structural and other behavioural tests does not offset this failure.

## 7. Evidence quality and independence

All evidence was produced by the illustrative implementation operator. No independent assessor participated. The evidence therefore cannot support an L4 claim. Operational evidence is absent because the target was not evaluated in production. The short observation period also prevents a claim about continuous control effectiveness.

## 8. Review and remedy

No real affected parties or transactions were involved. The test did not evaluate notice, standing, review independence, interim protection, correction or downstream remedy propagation. These exclusions must be closed before any high-impact or production claim relying on those controls.

## 9. Conclusion

No GAAM conformance claim is issued. The report demonstrates partial structural and behavioural evidence but identifies a material revocation-enforcement failure, insufficient integrity protection and unevaluated review and remedy controls.

A later report should identify the corrected build, rerun all applicable tests, preserve this failed result, provide integrity-protected evidence and state whether an assessor independent of the operator reviewed the target.
