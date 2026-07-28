---
title: "Implementation Self-Assessment Checklist"
permalink: /implementation-reports/self-assessment/
parent: "Implementation Reports"
nav_order: 2
artifact_type: "Assessment aid"
normative_status: "Informative"
---
# Implementation Self-Assessment Checklist

{% include gaam-meta.html %}

Complete this checklist before preparing an implementation report or conformance claim. A checked item means evidence has been located and reviewed, not merely that the implementation team believes the statement to be true.

## Scope and authority

- [ ] The target of evaluation has a stable identifier, version, environment and technical boundary.
- [ ] Governed effects and material exclusions are explicit.
- [ ] Every authority source is attributable, current and within its declared scope.
- [ ] Delegations preserve purpose, effect, duration, jurisdiction and redelegation constraints.
- [ ] Revocation, suspension, expiry and supersession are enforced at relevant decision points.
- [ ] Accountable parties are distinguishable from software agents, operators and evidence producers.

## Profiles and requirements

- [ ] Claimed profiles match implemented governance semantics.
- [ ] Profile dependency closure is complete.
- [ ] Applicable normative requirement identifiers are recorded.
- [ ] Partial implementation is disclosed and is not represented as full profile conformance.
- [ ] Extensions do not silently weaken governed vocabulary or schema constraints.

## Machine-readable artifacts

- [ ] Artifacts validate against the declared GAAM v0.9.0 schemas where applicable.
- [ ] Canonical identifiers and versions are preserved.
- [ ] Lifecycle states and transitions are internally consistent.
- [ ] Integrity material can be verified using documented procedures.
- [ ] Unknown or unsupported values fail or degrade according to declared policy.

## Behaviour and enforcement

- [ ] Positive, negative and boundary cases have been executed for applicable controls.
- [ ] Expired, revoked, out-of-scope and unauthorised actions are rejected or routed as required.
- [ ] Delegation chains cannot amplify authority.
- [ ] Runtime decisions identify applicable authority, policy, evidence, outcome and accountable party.
- [ ] High-impact effects include notice, challenge, review and remedy pathways where applicable.
- [ ] Failure modes, stale state and unavailable dependencies have declared behaviour.

## Evidence quality

- [ ] Each material claim has relevant evidence tied to the evaluated target and period.
- [ ] Evidence provenance and collection time are recorded.
- [ ] Integrity and verification procedures are documented.
- [ ] Freshness and validity limits are explicit.
- [ ] Contradictory or superseded evidence is retained and dispositioned where necessary.
- [ ] Evidence producer and assessor relationships are disclosed.
- [ ] The evidence set is sufficient for the claimed level and does not rely on unsupported inference.

## Privacy, security and affected parties

- [ ] Evidence collection is proportionate to its assurance purpose.
- [ ] Access, disclosure, retention and disposal controls are recorded.
- [ ] Decision receipts and relationship data are assessed for correlation and confidentiality risk.
- [ ] Affected parties can understand material decisions and available challenge mechanisms.
- [ ] Review and remedy authorities are identified and operationally reachable.
- [ ] Security incidents that affect the claim are recorded as limitations, exceptions or invalidation triggers.

## Claim and report integrity

- [ ] The report identifies methods, dates, tools and test-suite versions.
- [ ] Failed, skipped and indeterminate checks are disclosed.
- [ ] Deviations, compensating controls and residual risks are explicit.
- [ ] The proposed conformance level does not exceed the weakest supporting evidence.
- [ ] An L4 claim is not issued by the implementation operator or an entity under its control.
- [ ] Review, expiry, suspension, withdrawal and supersession conditions are defined.

## Completion record

| Field | Entry |
|---|---|
| Completed by |  |
| Role and organisation |  |
| Target identifier and version |  |
| GAAM version | 0.9.0 |
| Profiles reviewed |  |
| Completion date |  |
| Open failures or exceptions |  |
| Evidence repository or bundle |  |
| Proposed evidence level |  |
| Independent review required |  |
