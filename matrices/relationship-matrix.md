---
title: "Canonical Relationship Matrix"
permalink: /matrices/relationships/
parent: "Matrices"
---
| Relationship | Source | Target | Source cardinality | Target cardinality | Propagation/transitivity | Required semantic boundary |
|---|---|---|---:|---:|---|---|
| holds | actor | authority | 0..* | 1 | no | Authority possession is contextual |
| governs | framework | entity | 1..* | 0..* | no | Governance scope must be explicit |
| delegates | delegator | delegate | 0..* | 0..* | bounded | Cannot enlarge parent authority |
| recognises | framework | external assertion | 0..* | 0..* | no | Does not imply delegation or universal trust |
| accredits | authority | evaluator | 0..* | 0..* | no | Does not guarantee every output |
| asserts | actor | claim | 0..* | 1..* | no | Requires attributable provenance |
| supports | evidence | claim | 0..* | 0..* | no | Does not establish truth alone |
| verifies | verifier | claim | 0..* | 0..* | no | Bounded by method and context |
| assesses | evaluator | subject | 0..* | 0..* | no | Produces contextual assurance |
| permits | policy | effect | 0..* | 0..* | no | Subject to constraints |
| prohibits | policy | effect | 0..* | 0..* | no | Conflict resolution required |
| constrains | policy | authority/effect | 0..* | 0..* | no | Narrows operation |
| depends-on | artifact | artifact | 0..* | 0..* | yes | Dependency state may affect operation |
| accounts-for | party | effect | 1..* | 1..* | no | Machine actor cannot be terminal |
| revokes | authority | artifact | 0..* | 0..* | propagates | Requires effective time and authority |
| suspends | authority | artifact | 0..* | 0..* | propagates | Temporary non-operative state |
| supersedes | artifact | artifact | 0..1 | 0..1 | no | Prior artifact becomes non-current |
| appeals | party | decision | 0..* | 0..* | no | Review body must change outcomes |
| remedies | remedy | effect | 0..* | 1..* | no | Evidence linked to original decision |
