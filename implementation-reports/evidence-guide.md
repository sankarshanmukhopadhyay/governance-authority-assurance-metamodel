---
title: "Implementation Evidence Guide"
permalink: /implementation-reports/evidence-guide/
parent: "Implementation Reports"
nav_order: 3
artifact_type: "Implementation guidance"
normative_status: "Informative"
---
# Implementation Evidence Guide

{% include gaam-meta.html %}

This guide explains how to organise evidence supporting an implementation report. It is informative. The normative requirements, schemas, profile manifests and conformance rules remain authoritative.

## Evidence bundle structure

A portable evidence bundle may use the following structure:

```text
implementation-report/
├── report.md
├── claim/
│   └── conformance-claim.json
├── scope/
│   ├── target-inventory.md
│   └── profile-selection.md
├── artifacts/
│   ├── governance-package/
│   └── machine-readable-records/
├── tests/
│   ├── test-plan.md
│   ├── results/
│   └── logs/
├── evidence/
│   ├── structural/
│   ├── behavioural/
│   ├── operational/
│   └── assessment/
├── exceptions/
│   └── exception-register.md
└── integrity/
    ├── manifest.json
    └── checksums.json
```

The directory names are recommended conventions, not required GAAM artifacts.

## Evidence record minimums

For every material evidence item, record:

| Attribute | Question answered |
|---|---|
| Identifier | Which exact evidence item is referenced? |
| Type | What kind of observation, test, receipt, record or assessment is it? |
| Subject | Which target, control, action or state does it concern? |
| Claim | Which proposition does the evidence support or contradict? |
| Source | Who or what produced it? |
| Provenance | How was it generated, transferred and transformed? |
| Collection time | When was it observed or obtained? |
| Validity or freshness | Until when, or under which conditions, is it usable? |
| Verification method | How can another reviewer reproduce or validate it? |
| Integrity reference | Which digest, signature, log commitment or custody record protects it? |
| Access classification | Who may inspect it, and under what authority? |
| Independence relationship | How is the producer related to the target, operator and assessor? |
| Contradictions | Which conflicting or superseding evidence is known? |
| Disposition | Accepted, restricted, contested, superseded, expired or another declared state |

Where suitable, represent the core fields using [`schemas/evidence.schema.json`](../schemas/evidence.schema.json).

## Evidence classes

The [evidence catalogue](evidence-catalogue.md) groups evidence into six practical classes:

1. governance and authority evidence;
2. structural and schema evidence;
3. behavioural and enforcement evidence;
4. operational and lifecycle evidence;
5. affected-party, review and remedy evidence;
6. independent assessment and interoperability evidence.

An implementation may use different artifacts, provided the report explains how they support the applicable requirements and claimed level.

## Evidence-level boundaries

| Level | Evidence focus | Typical evidence |
|---|---|---|
| L0 | Declared governance and scope | Policies, control schedules, target declaration and profile selection |
| L1 | Structural validity | Schema validation, vocabulary checks, package integrity and dependency closure |
| L2 | Behavioural validity | Positive, negative, boundary, lifecycle and invariant test results |
| L3 | Operational support | Runtime receipts, event histories, monitoring, incident and remedy execution records |
| L4 | Independent assessment | Independent method, sampling, findings, exceptions, validity period and assessor declaration |

Evidence from a higher row does not cure missing evidence in a lower row. For example, an independent report cannot establish structural validity if the assessed artifacts were not identified and validated.

## Provenance and reproducibility

A reviewer should be able to determine:

- the exact target and version that produced the evidence;
- the tool, configuration and test data used;
- whether evidence was generated before or after a relevant authority or policy change;
- whether logs or receipts are complete or sampled;
- whether transformations removed material fields;
- whether the source can equivocate or rewrite history;
- whether the result can be reproduced from retained inputs.

Use immutable digests for retained files and record the source commit, package version or deployment identifier. Avoid screenshots as the sole evidence when machine-readable output exists.

## Exceptions and contradictory evidence

Do not delete failed results merely because a later run passed. Record:

- the failed control or requirement;
- detection time;
- affected scope and period;
- root cause, where known;
- corrective action;
- verification of correction;
- residual risk;
- whether previously issued claims must be restricted, suspended, withdrawn or superseded.

Contradictory evidence should be linked and dispositioned. The report should explain why one item is more authoritative, current or relevant rather than silently excluding the conflict.

## Independence disclosure

For each assessment or judgement, disclose whether it is:

- self-assessment by the operator;
- second-party assessment by a customer, principal or relying party;
- independent assessment by an organisationally separate party.

Also disclose funding, control, shared management, subcontracting and evidence-production relationships that could affect independence. The label “external” does not by itself establish independence.

## Sensitive evidence

Implementation evidence may contain personal data, security details, confidential policies or relationship graphs. The report should publish the minimum needed to support the claim and describe how restricted evidence can be inspected by authorised reviewers. Redaction must not remove information necessary to verify scope, provenance, outcome or exceptions.
