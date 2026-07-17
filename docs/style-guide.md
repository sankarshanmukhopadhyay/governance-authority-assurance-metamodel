---
layout: page
title: Editorial and Normative Style Guide
permalink: /docs/style-guide/
---
GAAM uses **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** only for normative statements. Every normative requirement has a stable `GAAM-<DOMAIN>-NNN` identifier. Defined terms use sentence case in prose and canonical lower-case values in machine-readable vocabularies. Informative examples must not introduce undeclared requirements. Human-readable normative text governs substantive meaning; designated schemas govern artifact structure.

## Page headings

For any Markdown document using `layout: page`, the front-matter `title` is the authoritative and sole level-one heading. The body MUST NOT repeat the title with Markdown `#` syntax and SHOULD begin with introductory prose or a level-two heading. This contract preserves accessible document structure and prevents duplicate or overlapping titles in the rendered publication.
