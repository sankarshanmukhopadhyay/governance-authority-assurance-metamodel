---
title: "CTWG v1.4.1 Glossary Alignment"
permalink: /mappings/ctwg-v1.4.1-glossary-alignment/
parent: "Mappings"
artifact_type: "Terminology crosswalk"
normative_status: "Informative; GAAM glossary remains normative"
---
# CTWG v1.4.1 Glossary Alignment

{% include gaam-meta.html %}

## Purpose

This crosswalk records how the GAAM glossary aligns with the CTWG Main Glossary v1.4.1 supplied for this review. It improves cross-repository interoperability without importing external normative authority into GAAM.

## Alignment policy

- **Adopted** means the GAAM definition is materially aligned with the CTWG definition.
- **Extended** means the CTWG meaning is retained but GAAM adds constraints required for executable governance.
- **Local** means GAAM requires a term for which no exact CTWG entry was identified or for which an adjacent CTWG term has a different abstraction level.

GAAM definitions remain controlling for GAAM conformance. Implementations claiming CTWG alignment SHOULD use the crosswalk to prevent silent semantic substitution.

## Crosswalk

| GAAM term | Status | CTWG term | Alignment note |
|---|---|---|---|
| Accountability | `local` | No exact CTWG entry identified | GAAM accountability includes explanation, correction and remedy. |
| Actor | `extended` | actor | CTWG baseline retained; GAAM permits organizational participation through authorized actors. |
| Agent | `extended` | agent | CTWG principal-agent relationship retained; GAAM adds policy- and evidence-driven software behavior. |
| Assertion | `local` | No exact CTWG entry identified | GAAM term for attributable claims. |
| Assurance | `local` | assurance-level | GAAM defines the assurance process/conclusion; CTWG separately defines assurance level. |
| Authority | `extended` | authority | CTWG recognition concept retained; GAAM emphasizes bounded powers and effects. |
| Capability | `adopted` | capability | Definition aligned. |
| Constraint | `local` | No exact CTWG entry identified | GAAM execution-bound limitation. |
| Decision receipt | `extended` | decision-receipt | CTWG structured receipt adopted; GAAM identifies it as a governance record. |
| Delegation | `adopted` | delegation | Definition aligned; GAAM uses delegate as the role label while CTWG uses delegatee. |
| Effect | `local` | No exact CTWG entry identified | GAAM-specific material-change abstraction. |
| Evidence | `extended` | evidence-artifact; evidence-bundle | GAAM uses an umbrella definition across evidence forms. |
| Governance context | `local` | governance | GAAM-specific decision-context abstraction. |
| Governance event | `local` | governance | GAAM-specific attributable state-change abstraction. |
| Obligation | `local` | No exact CTWG entry identified | GAAM decision-output requirement. |
| Permission | `extended` | permission | CTWG authorization baseline retained; GAAM adds effect and scope. |
| Policy | `adopted` | policy | Definition aligned. |
| Principal | `adopted` | principal | Definition aligned. |
| Prohibition | `local` | No exact CTWG entry identified | GAAM normative decision constraint. |
| Recognition | `local` | No exact CTWG entry identified | GAAM governed acceptance decision. |
| Registry | `extended` | registry | CTWG authoritative-source baseline retained; GAAM adds governance, assertions, status and relationships. |
| Role | `extended` | role | CTWG contextual role baseline retained and condensed. |
| Rule | `extended` | rule | CTWG baseline retained; GAAM requires machine-testability where the term is used normatively. |
| Trust decision | `extended` | trust-decision | CTWG risk-based interaction decision retained; GAAM adds effect constraints. |
| Trust graph | `extended` | trust-graph | CTWG relationship graph retained; GAAM adds typed attribution and bounded transitive reasoning. |
| Verification | `extended` | verification | CTWG authenticity baseline retained; GAAM also supports criteria and condition checks. |

## Governance rules for future terminology changes

1. A proposed GAAM term that overlaps CTWG MUST be checked against the current CTWG controlled entry.
2. Exact adoption is preferred where it does not weaken GAAM authority, scope, enforcement, revocation, evidence or remedy semantics.
3. Any extension MUST state the added GAAM constraint and MUST NOT silently redefine the CTWG baseline.
4. Any local term MUST document why an existing CTWG term is insufficient.
5. Changes to aligned terms MUST update this crosswalk and the machine-readable alignment register in the same commit.

## Assurance evidence

The repository validator checks that every GAAM glossary term appears exactly once in the alignment register and that every register status is one of `adopted`, `extended` or `local`.
