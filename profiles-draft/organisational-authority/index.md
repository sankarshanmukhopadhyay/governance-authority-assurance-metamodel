---
title: Organisational Authority
permalink: /profiles-draft/organisational-authority/
parent: Draft Profile Candidates
grand_parent: Future Evolution
nav_order: 2
artifact_type: Draft profile candidate
normative_status: Informative and non-conformant
---
# Organisational Authority

> This is a research profile candidate. It does not modify GAAM v0.9.0, create a conformance target, or permit a conformance claim.

## Purpose

Appointment, office holding, representation, approval, mandate, delegation and execution chains.

## Candidate conformance target

A future implementation that elects to govern this capability as a coherent assurance boundary. The target remains intentionally provisional until the candidate requirements and evidence model have been exercised in Commit 3.

## Candidate dependencies

- GAAM Foundation Profile v0.9.0 as the conceptual baseline, without changing its requirements.
- Future-evolution candidates: `FE-005`, `FE-009`.
- Applicable existing profiles selected by the implementation context.

## Candidate requirement themes

1. Declare the governed object, decision rights, authority source and accountability boundary.
2. Represent lifecycle states, transition authority, evidence and temporal effect.
3. Preserve traceability from governance source to runtime decision and consequential effect.
4. Define suspension, revocation, continuity, challenge and remedy behaviour.
5. State privacy, security, affected-party and interoperability limitations.

## Evidence expected before promotion

- At least two independently authored implementation patterns.
- Positive and negative behavioural vectors covering material boundary failures.
- Review by privacy, security, affected-party and implementation reviewers.
- A demonstrated need that cannot be met reliably through existing v0.9.0 constructs and guidance.

## Unresolved questions

- Which concepts belong in the core metamodel rather than this specialised profile?
- Which records require canonical schemas and controlled vocabularies?
- What minimum evidence supports interoperable conformance testing?
- Which lifecycle transitions require cross-system propagation guarantees?

## Promotion criteria

Promotion requires an approved normative-impact assessment, stable machine-readable artefacts, implementation evidence and a later GAAM version. Until then, this page is informative research only.
