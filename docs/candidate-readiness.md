---
title: "Candidate Readiness Dashboard"
permalink: /governance/candidate-readiness/
parent: Assurance and Governance Tracking
artifact_type: "Generated governance view"
normative_status: "Informative"
grand_parent: Documentation
nav_order: 2
---
# Candidate Readiness Dashboard

{% include gaam-meta.html %}

This dashboard exposes the evidence currently available for progression from GAAM v0.9.0 to v1.0.0. The machine-readable sources are [`governance/candidate-issues.json`](../governance/candidate-issues.json) and the review records under [`governance/reviews/`](../governance/reviews/).

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
| Governed ecosystem applicability | In progress | Independent review of the [capability matrix](../governance/reviews/evidence/implementation/ecosystems/governed-ecosystem-capability-matrix.md) and candidate enhancement dispositions |
| Breaking candidate issues | No known open item | Continued register validation and explicit classification |

## Decision rule

A v1.0.0 release decision is eligible only when every `blockingV1` issue is closed with referenced evidence, all required reviews are complete, and the candidate register contains no unresolved breaking normative change or critical security finding.

## How to submit evidence

Use the repository issue forms for implementation reports, interoperability findings, review findings and change proposals. Pull requests must identify affected requirements, profiles, authority implications, compatibility, threats, tests, evidence and migration consequences.
