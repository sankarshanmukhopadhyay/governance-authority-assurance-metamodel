---
title: "Pattern Validation Guide"
permalink: /examples/pattern-validation-guide/
parent: "Implementation Patterns"
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Pattern Validation Guide
Run `python scripts/validate.py` from the repository root. Validation checks the directory contract, manifest structure, profile and requirement references, artifact existence, fixture outcomes, behavioural-vector references, scenario declarations, maturity evidence, conformance limitations, catalogue coverage and package inclusion.

A missing or malformed pattern artifact is reported as a named failure. It must not terminate the validator unexpectedly.
