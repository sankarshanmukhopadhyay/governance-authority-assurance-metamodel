---
title: "Cross-Registry Recognition"
permalink: /examples/cross-registry-recognition/
parent: "Implementation Patterns"
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Cross-Registry Recognition
This assurance-ready implementation pattern demonstrates **cross-registry reliance and recognition** using GAAM v0.9.0. It is informative and does not alter normative requirements or conformance semantics.

## Governance objective

The pattern makes authority, policy, runtime enforcement, evidence, assurance, lifecycle, review and remedy separately inspectable.

## Actors

- source registry
- relying registry
- registry operator
- governance authority
- recognition authority
- assurance assessor
- record subject
- relying service
- review authority

## Included documentation

- [Recognition Model](recognition-model.md)
- [Trust Boundaries](trust-boundaries.md)
- [Authority and Delegation Model](authority-model.md)
- [Recognition Lifecycle and Suspension](lifecycle-and-suspension.md)
- [Evidence and Assurance Model](evidence-model.md)
- [Review and Correction](review-and-correction.md)
- [Privacy and Security Analysis](privacy-security-analysis.md)
- [Affected-Party Analysis](affected-party-analysis.md)
- [Requirement Mapping](requirement-mapping.md)

## Validation

Run `python scripts/validate.py` from the repository root. See `pattern.json` for exact artifact, fixture, behavioural-vector and requirement references.

## Conformance boundary

The included claim is self-assessed implementation evidence. It is not an L4 independent assessment and does not establish interoperability testing.
