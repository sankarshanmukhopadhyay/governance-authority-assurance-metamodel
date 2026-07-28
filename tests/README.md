# GAAM Candidate Conformance Suite

Run `python scripts/validate.py`. The suite evaluates publication coherence, normative traceability, schemas, governed vocabularies, profile dependency closure, fixture validity, conformance-claim evidence rules, behavioural invariants, threat traceability, local links and governance-package integrity.

## Coverage

The behavioural suite includes positive, negative and boundary vectors for authority timing and source validity, delegation attenuation and parent constraints, decision evidence freshness, assurance validity and independence, remedy safeguards, lifecycle event ordering, stale runtime state, and profile dependency closure.

The [requirement assurance traceability matrix](../matrices/requirement-assurance-traceability.md) dispositions every normative requirement and identifies where reference tests contribute evidence. Requirements classified as reviewable, observable, procedural or mixed still require contextual evidence and competent assessment.

The included behavioural vectors are reference tests, not evidence of independent interoperability. Test identifiers and results are emitted in the validation report.
