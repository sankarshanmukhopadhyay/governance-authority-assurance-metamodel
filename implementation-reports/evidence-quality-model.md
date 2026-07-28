---
title: "Evidence Quality Model"
permalink: /implementation-reports/evidence-quality/
parent: "Implementation Reports"
nav_order: 4
artifact_type: "Assurance guidance"
normative_status: "Informative"
---
# Evidence Quality Model

{% include gaam-meta.html %}

Evidence quality is multidimensional. A large volume of weak evidence should not be treated as equivalent to a smaller set of relevant, attributable and reproducible evidence.

## Quality dimensions

| Dimension | Strong evidence demonstrates | Common weakness |
|---|---|---|
| Relevance | Direct relationship to the requirement, target, environment and period | Generic policy or evidence from another deployment |
| Authenticity | Attributable source and verifiable origin | Unattributed export or screenshot |
| Integrity | Detectable modification and controlled custody | Mutable file with no digest or event commitment |
| Provenance | Traceable generation, transformation and transfer history | Derived result with missing inputs or processing steps |
| Freshness | Collection and validity times appropriate to the claim | Old evidence used after policy, software or authority changes |
| Completeness | Material cases, components and time periods are represented | Selective successful samples with omitted failures |
| Reproducibility | Another reviewer can repeat the method or verify the result | Undocumented manual judgement |
| Specificity | Supported proposition and limitations are explicit | Evidence is cited as proof of broad trustworthiness |
| Independence | Producer and assessor relationships are known and suitable | Operator-generated evidence presented as independent proof |
| Contestability | Contradictions, exceptions and review routes are preserved | Failed or disputed evidence is suppressed |
| Confidentiality fitness | Disclosure supports verification without unnecessary exposure | Over-disclosure or redaction that prevents verification |
| Retention fitness | Evidence remains available for the claim, audit and remedy horizon | Evidence expires before claims or disputes can be reviewed |

## Evidence disposition

Use one of the following informative dispositions in an implementation report:

| Disposition | Meaning |
|---|---|
| Accepted | Suitable for the stated proposition and scope |
| Accepted with limitation | Usable only with an explicit qualification |
| Restricted | Valid but available only to authorised reviewers |
| Contested | Material disagreement or contradictory evidence remains unresolved |
| Superseded | Replaced by identified later evidence, while history is preserved |
| Expired | No longer sufficiently fresh for the claim |
| Rejected | Authenticity, integrity, relevance or method is inadequate |
| Not available | Required evidence was not produced or retained |

## Quality assessment worksheet

| Evidence ID | Supported requirement or proposition | Relevance | Integrity | Freshness | Completeness | Independence | Disposition | Limitations |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Use qualitative ratings only when the report defines their meaning. Avoid combining the dimensions into a single score that conceals a decisive failure. Missing authenticity or scope alignment, for example, should not be offset by high volume or freshness.

## Assurance decision rule

The report should identify the evidence that is decisive for each material conclusion and explain any inference. A conclusion should be lowered, limited or withheld when:

- decisive evidence is unavailable, expired or contested;
- the evidence does not cover the claimed target or period;
- independence is insufficient for the asserted level;
- failed cases are omitted or unresolved;
- evidence cannot be linked to applicable authority and policy;
- verification depends on undisclosed methods or inaccessible source material.
