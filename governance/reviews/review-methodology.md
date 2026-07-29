---
title: Review Methodology
artifact_type: Governance method
normative_status: Informative
---
# Review Methodology

## 1. Freeze the baseline

Record the exact commit SHA, GAAM version, included and excluded surfaces, normative requirement count, profiles, and validation-report digest in `review-baseline.json`. Change its status to `frozen-for-review` only after the source commit is exact and reproducible.

## 2. Assign the reviewer

Record the reviewer, role, independence classification, review authority, decision authority, and any conflict declaration in the relevant review register.

## 3. Collect evidence

Store attributable evidence under the review domain's evidence directory. Evidence must identify its producer, date, scope, method, and relationship to findings or exit criteria.

## 4. Exercise scenarios

Test representative positive, negative, boundary, lifecycle, failure, and affected-party scenarios. Reuse existing behavioural vectors where they provide equivalent coverage.

## 5. Submit findings

Create findings conforming to `finding-schema.json`. Findings must identify affected requirements, profiles, artifacts, scenario, impact, evidence, recommended control, change class, normative impact, and v1-blocking status.

## 6. Disposition findings

The decision authority records acceptance, mitigation, risk acceptance, evidence-backed rejection, deferral, or closure. Reviewer conclusions and maintainer dispositions remain separately attributable.

## 7. Remediate and retest

Implement approved controls in a separately reviewable change. The reviewer or another authorised verifier retests the finding and records verification evidence.

## 8. Close or retain residual risk

Closure requires verification evidence and a closure date. Risk acceptance requires an accountable authority, rationale, residual risk, reconsideration date, and conditions that trigger renewed review.

## 9. Reconcile cross-review tensions

Use `joint-disposition-register.json` where privacy, security, affected-party, interoperability, or implementation concerns compete. Record the governing principle, selected control, accountable authority, tests, evidence, residual risk, and release impact.

## 10. Update candidate readiness

Every open v1 blocker remains visible on the candidate-readiness dashboard. A review is complete only when its exit criteria and final attestation are present and no unresolved critical finding is hidden.

## 11. Decide release impact

Editorial, evidence, and informative guidance changes may remain commit-only. New normative vocabulary, mandatory schema fields, requirement semantics, profile dependencies, or security corrections affecting valid implementations require release-managed change.
