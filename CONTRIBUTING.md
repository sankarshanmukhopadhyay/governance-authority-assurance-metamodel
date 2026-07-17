---
layout: page
title: "Contributing"
permalink: /governance/contributing/
artifact_type: "Contribution guide"
normative_status: "Normative process"
---
GAAM welcomes conceptual review, normative text, implementation evidence, threat analysis, diagrams and examples.

## Before contributing

1. Read the specification, design rationale and open questions.
2. Search existing issues and pull requests.
3. Identify whether the proposal changes terminology, normative behaviour, conformance or only explanatory material.
4. For substantial changes, open a design issue before submitting a pull request.

## Contribution requirements

A normative proposal should include:

- the problem being addressed;
- the affected concepts and requirement identifiers;
- proposed text;
- compatibility and conformance consequences;
- security, privacy, safety and redress implications;
- at least one example or testable scenario.

## Style

- Use BCP 14 terms only for normative requirements.
- Use `GAAM-<AREA>-<NNN>` identifiers for new requirements; maintainers assign final numbers.
- Define terms before relying on them normatively.
- Avoid protocol-specific requirements unless the text is explicitly informative.
- Prefer bounded, testable requirements over broad aspirations.

## Pull requests

Pull requests must pass Markdown and internal-link checks. A pull request that changes normative text must update the requirement index and, where applicable, the conformance and relationship matrices.
## Machine-verifiable contributions

Changes to schemas, profiles, vocabularies or examples must include positive and negative fixtures, update affected documentation and pass `python scripts/validate.py`. Normative changes must use a unique requirement identifier and update generated traceability evidence.
