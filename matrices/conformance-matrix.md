---
title: "Conformance Matrix"
permalink: /matrices/conformance/
parent: "Matrices"
artifact_type: "Conformance matrix"
normative_status: "Normative supporting"
---
# Conformance Matrix

{% include gaam-meta.html %}

## Profile applicability

| Requirement domain | Foundation | Machine-Actionable | Delegated Authority | Agentic Systems | Trust Graph | Continuous Assurance | High-Impact |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Primary Document and controlled documents | Required | Required | Required | Required | Required | Required | Required |
| Authority topology | Required | Required | Required | Required | Required | Required | Required |
| Machine-actionable package | Optional | Required | Optional | Recommended | Recommended | Required | Recommended |
| Delegation lineage and attenuation | Optional | Optional | Required | Required where delegated | Required where represented | Required where monitored | Required where delegated |
| Agent lifecycle and tool governance | Not applicable | Optional | Optional | Required | Optional | Optional | Required where agents operate |
| Runtime governance envelope | Recommended | Required for automated effects | Required for consequential delegated effects | Required | Required for automated graph decisions | Required | Required |
| Decision receipts | Recommended | Required for consequential effects | Required for consequential delegated effects | Required | Required for consequential graph decisions | Required | Required |
| Typed graph semantics | Optional | Optional | Recommended | Recommended | Required | Recommended | Required where graph reliance occurs |
| Continuous assurance | Optional | Optional | Optional | Recommended | Recommended | Required | Required where conditions change materially |
| Affected-party analysis and redress | Required | Required | Required | Required | Required | Required | Enhanced requirement |
| Systemic harm monitoring | Recommended | Recommended | Recommended | Required where foreseeable | Required where foreseeable | Required | Required |

## Conformance targets and minimum evidence

| Target | Minimum evidence expected |
|---|---|
| Governance framework | Primary Document, controlled-document schedule, profile claim, requirements traceability, revision record |
| Controlled document | Document identifier, version, authority, applicability, normative requirements, approval and status |
| Governed organisation | Applicable policy assessment, control evidence, incidents, exceptions and remediation status |
| Authority record | Authority source, subject, scope, context, effective period, status and issuer authority |
| Delegation record | Delegator, delegate, origin, scope, parent, redelegation, validity, acceptance and revocation |
| Agent | Identity and continuity data, principal, accountable parties, permitted effects, tools, lifecycle and assurance |
| Registry | Operator authority, record semantics, write rights, status, provenance, correction and security controls |
| Trust graph | Node and edge semantics, provenance, path rules, conflicts, status and integrity |
| Trust decision | Context, effect, decision-maker, authority, policy, evidence, outcome, conditions and time |
| Transaction/effect | Decision reference, execution evidence, outcome, obligations and exception handling |
| Evidence package | Provenance, integrity, freshness, permitted use, subject, related claims and retention |
| Decision receipt | Decision fields, policy and authority references, evidence references, reason codes and integrity |
| Assurance service | Criteria, evaluator competence, evidence sources, validity, gaps, conflicts and challenge process |
| Governance package | Framework/version binding, integrity, schemas, policies, state endpoints, tests and precedence |
