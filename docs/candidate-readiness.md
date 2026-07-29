---
title: "Candidate Readiness Dashboard"
permalink: /governance/candidate-readiness/
parent: "Documentation"
artifact_type: "Generated governance view"
normative_status: "Informative"
---
# Candidate Readiness Dashboard

{% include gaam-meta.html %}

This dashboard exposes the evidence currently available for progression from GAAM v0.9.0 to v1.0.0. The machine-readable sources are [`governance/candidate-issues.json`](../governance/candidate-issues.json), the [review methodology](../governance/reviews/review-methodology.md), the [review baseline](../governance/reviews/review-baseline.json), and the five review registers under [`governance/reviews/`](../governance/reviews/).

## Current status

| Stable-release gate | State | Evidence needed |
|---|---|---|
| Two independent implementations | Not started | Two accepted reports covering Foundation and at least one composed profile |
| Requirement testability disposition | Complete | Maintained traceability for all normative requirements |
| Canonical identifier publication | In progress | Public resolution, checksum and historical-retention evidence |
| Privacy review | Not started | Completed review and disposition of material findings |
| Security review | Not started | Completed review with no unresolved critical issue |
| Affected-party review | Not started | Completed review of notice, standing, challenge and remedy execution |
| Cross-implementation interoperability | Not started | Cross-validator evidence from independent implementations |
| Breaking candidate issues | No known open item | Continued register validation and explicit classification |

## Review control state

The review programme now has a shared baseline, finding schema, governed vocabulary, evidence directories, attribution model, and joint-disposition register. The baseline remains in `draft` until its `sourceCommit` is replaced with the exact commit SHA and the record is frozen for review.

## Decision rule

A v1.0.0 release decision is eligible only when every `blockingV1` issue is closed with referenced evidence, all required reviews are complete, and the candidate register contains no unresolved breaking normative change or critical security finding.

## How to submit evidence

Use the repository issue forms for implementation reports, interoperability findings, review findings and change proposals. Pull requests must identify affected requirements, profiles, authority implications, compatibility, threats, tests, evidence and migration consequences.
