# Conformance Test Surface

The executable release checks are implemented by `scripts/validate.py` and exercised by `.github/workflows/validate.yml`. The suite validates requirement traceability, profile dependency closure, JSON Schemas, positive and negative fixtures, conformance claims, package integrity and local documentation links.

Future v0.6.x validation work should split behavioural invariants into independently addressable test modules as external implementations become available.
