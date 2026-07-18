---
title: "Delegated Authority Profile"
permalink: /profiles/delegated-authority/
parent: "Conformance Profiles"
---
# Delegated Authority Profile

**Version:** 0.9.0  
**Status:** Candidate Specification

## Purpose

This profile defines the GAAM requirements for **delegated authority** conformance targets. It is a conformance package rather than a descriptive label.

## Applicability and targets

- `authority-service`
- `delegation-service`

## Dependencies

- [Foundation Profile](foundation-profile.md)

## Normative requirement mapping

The machine-readable manifest is authoritative for the profile mapping: [`manifests/delegated-authority.json`](manifests/delegated-authority.json).

This profile maps **32 normative requirements**. Implementations SHALL satisfy every mapped requirement unless a future profile version declares a specific permitted exclusion.

## Required artifacts

- Conformance claim identifying GAAM v0.9.0 and this profile version.
- Requirement traceability evidence.
- Reproducible validation results.
- Governance artifacts applicable to the conformance target.

## Required tests

- Profile manifest schema validation.
- Dependency closure.
- Normative requirement identifier validity.
- Applicable schema and governance-invariant tests.

## Claim limitations

A structurally valid artifact set does not by itself establish operational trustworthiness. Partial implementation MUST NOT be represented as full profile conformance.
