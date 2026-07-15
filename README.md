# Governance, Authority and Assurance Metamodel

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](VERSION)
[![Status](https://img.shields.io/badge/status-initial%20public%20draft-orange.svg)](releases/v0.1.0.md)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**A vendor-neutral, protocol-independent metamodel for governing authority, delegation, accountability, evidence and trust decisions across distributed digital systems. Defines concepts, relationships, conformance profiles and governance semantics for interoperable trust architectures, agentic systems and decentralized trust graphs.**

## Why this project exists

Distributed systems increasingly make consequential decisions through combinations of human institutions, software agents, registries, credentials, policy engines and evidence services. These components frequently use the same words—authority, trust, delegation, assurance and accountability—while assigning them incompatible meanings.

GAAM provides a common governance layer. It defines the concepts, relationships, constraints and conformance expectations needed to answer five operational questions:

1. **Who or what is acting?**
2. **Under whose authority is the action taken?**
3. **Which policy, evidence and assurance support the decision?**
4. **What effect may occur, under which constraints?**
5. **Who remains accountable, and how can the outcome be challenged or remedied?**

## Release status

Version **0.1.0** is the Initial Public Draft. It establishes the complete architecture and first normative baseline. It is suitable for review, crosswalk development and experimental implementation, but it is not yet a stable specification.

| Milestone | Meaning |
|---|---|
| v0.1.0 | Initial Public Draft |
| v0.5.0 | Feature Complete Draft |
| v0.9.0 | Candidate Specification |
| v1.0.0 | Stable Initial Release |

## Start here

- [Specification](specification/governance-authority-assurance-metamodel.md)
- [Architecture overview](docs/architecture-overview.md)
- [Implementation guide](docs/implementation-guide.md)
- [Conformance guide](docs/conformance-guide.md)
- [Design rationale](docs/design-rationale.md)
- [Glossary](docs/glossary.md)
- [Reviewer guide](docs/reviewer-guide.md)
- [Open questions](docs/open-questions.md)
- [Specification roadmap](SPECIFICATION_ROADMAP.md)

## Core proposition

GAAM models the complete governance chain:

```text
principal → authority → delegation → actor or agent
          → policy + evidence + assurance
          → trust decision → effect
          → accountability + remedy
```

The specification is built around several non-negotiable distinctions:

- capability does not imply authority;
- identification does not imply entitlement;
- delegation does not extinguish accountability;
- a trust path is evidence for a decision, not the decision itself;
- assurance is contextual and time-bounded;
- consequential effects require reconstructable governance evidence.

## Repository contents

```text
specification/   Normative metamodel specification
profiles/        Composable conformance profiles
examples/        Informative application examples
mappings/        Cross-model adoption and alignment notes
matrices/        Requirements, relationships and conformance indexes
diagrams/        Architecture and lifecycle diagrams
docs/            Guides, rationale, glossary and review material
releases/        Release notes
.github/         Contribution and review workflows
```

## Contributing

Review comments, issue reports, implementation feedback and proposed text are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md) before opening a pull request.

## License

Documentation and specification content are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).
