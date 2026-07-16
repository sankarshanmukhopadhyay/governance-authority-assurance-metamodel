# Governance, Authority and Assurance Metamodel

[![Version](https://img.shields.io/badge/version-0.5.0-blue.svg)](VERSION)
[![Status](https://img.shields.io/badge/status-feature%20complete%20draft-orange.svg)](releases/v0.5.0.md)
[![Validation](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel/actions/workflows/validate.yml/badge.svg)](.github/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**A vendor-neutral, protocol-independent metamodel for governing authority, delegation, accountability, evidence and trust decisions across distributed digital and agentic systems.**

## Release status

Version **0.5.0** is the **Feature Complete Draft**. The planned architectural surface, profiles, canonical schemas, lifecycle model, implementation patterns and executable validation baseline are present. It remains a draft for interoperability, security and independent implementation validation.

## Core governance chain

```text
principal → authority → delegation → actor or agent
          → policy + evidence + assurance
          → trust decision → effect
          → accountability + remedy
```

## Navigate the rendered documentation

- [GitHub Pages home](index.md)
- [Normative specification](specification/governance-authority-assurance-metamodel.md)
- [Architecture overview](docs/architecture-overview.md)
- [Implementation guide](docs/implementation-guide.md)
- [Conformance guide](docs/conformance-guide.md)
- [Lifecycle model](docs/lifecycle-model.md)
- [Profiles](profiles/)
- [Canonical schemas](schemas/) and [vocabularies](vocabularies/)
- [Implementation patterns](examples/)
- [Threat model](threat-model/README.md)
- [Architectural decisions](decisions/)
- [Release notes](releases/v0.5.0.md)
- [AI/LLM usage disclosure](AI_USAGE.md)

## Validate

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

The command generates machine-readable and human-readable evidence in `validation/` and refreshes `VALIDATION_REPORT.md`.

## Maturity path

| Milestone | Meaning |
|---|---|
| v0.1.0 | Initial Public Draft |
| **v0.5.0** | **Feature Complete Draft** |
| v0.9.0 | Candidate Specification |
| v1.0.0 | Stable Initial Release |

## License and accountability

Specification and documentation content are licensed under [CC BY 4.0](LICENSE). Contributions remain governed by [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and the [AI usage disclosure](AI_USAGE.md).


## Provenance

- [Source attributions](ATTRIBUTIONS.md)
- [Mappings and source crosswalks](mappings/index.md)
