---
title: "Downstream Remedy Propagation"
permalink: /examples/downstream-remedy-propagation/
parent: "Implementation Patterns"
nav_order: 90
artifact_type: Informative research pattern
normative_status: Informative
---
# Downstream Remedy Propagation

> **Status:** Informative research pattern for GAAM v0.9.0. This pattern exercises candidate future-evolution concepts and experimental artefacts. It does not create a conformance target or change the normative specification.

## Purpose

This pattern examines **machine-verifiable correction across dependent systems**. It is linked to future-enhancement candidate `FE-021` and is intended to generate implementation evidence before any promotion decision.

## Scenario

The scenario uses the experimental record `experimental-remedy-execution.valid.json` together with current GAAM authority, evidence, runtime and accountability requirements. The experimental record is supporting research evidence only.

## Governance sequence

1. Establish the current normative authority and governance context.
2. Evaluate the candidate future-evolution condition represented by `FE-021`.
3. Apply a bounded, fail-safe decision at the relevant enforcement point.
4. Produce evidence identifying assumptions, limitations and unresolved semantics.
5. Route ambiguity or conflict to an authorised review authority.

## Evidence generated

- current GAAM authority and policy references;
- the experimental research record;
- the behavioural vector `remedy-propagation-verified-valid`;
- a decision or escalation record;
- reviewer observations on whether existing GAAM concepts are sufficient.

## Requirement relationship

This research pattern is anchored in `GAAM-HARM-003` and the Foundation and Runtime Governance profiles. Any additional semantics remain candidates, not v0.9.0 requirements.

## Limitations

- No normative sufficiency or interoperability claim is made.
- The experimental record may change or be withdrawn.
- Jurisdictional and sectoral implementation details remain external.
- Successful execution does not by itself justify normative promotion.

## Validation

```bash
python scripts/validate.py
```
