---
title: Review Governance and Evidence
artifact_type: Governance process
normative_status: Informative
---
# Review Governance and Evidence

This directory governs the independent Privacy, Security, Affected-Party, Interoperability, and Implementation-Evidence workstreams for the GAAM v0.9.0 candidate.

## Authority model

Reviewers produce attributable findings and evidence. GAAM maintainers disposition findings and determine release impact. A reviewer conclusion must not be overwritten by a maintainer disposition; both remain separately attributable.

## Required records

- `review-baseline.json` identifies the exact candidate surface under review.
- `review-methodology.md` defines the review lifecycle.
- `finding-schema.json` and `finding-vocabulary.json` govern findings.
- The five review registers record assignment, status, evidence, blockers, and attestation.
- `joint-disposition-register.json` records decisions spanning review domains.
- `evidence/` contains attributable review and closure evidence.

## Evidence conventions

Evidence references are repository-relative paths under `governance/reviews/evidence/`. Published evidence is recursively included in the GAAM package manifest and checksums. `.gitkeep`, editor files, caches, temporary files, and unapproved working notes are excluded.

Templates and empty directories are not evidence that a review has occurred. A review may be marked complete only when its exit criteria, attestation, evidence, and finding dispositions satisfy repository validation.

## Finding lifecycle

Findings move through governed states defined in `finding-vocabulary.json`. Closure requires verification evidence and a closure date. Risk acceptance requires accountable authority, rationale, residual risk, and a reconsideration date. Deferral requires an owner and target date.
