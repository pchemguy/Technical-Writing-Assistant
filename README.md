---
url: https://chatgpt.com/c/6abcb9c4-7980-83eb-85b2-e910c0fdf297
---

# Technical Writing Assistant

A modular agent skill for software documentation and scientific, technical, and professional writing. It reviews and revises existing material for clarity, structure, terminology, style, composition, and consistency while preserving technical meaning and authorial intent.

It also develops early notes into prose, explores composition, critiques reasoning, assesses evidence, and generates, reviews, validates, or repairs structured outlines and maps. Specialized maps emerge from contextual exploration rather than a fixed catalogue.

## Status

**Implemented and reviewed.** The package contains 19 focused references and a coordinating manager with 17 workflow recipes (20 reference files total). Each reference includes usable procedures, handling of missing information, examples, and completion criteria. The initial implementation passed structural checks and 11 offline sample tasks were reviewed; implementation does not establish reliability across all models or clients. This repository does not install the skill into a client.

## Use

Use `technical-writing-assistant/` as the standalone skill package in a host that supports Agent Skills. The core uses Markdown instructions and standard frontmatter; it requires no executable scripts or particular service. OpenAI presentation metadata under `agents/` is optional and separate from portable behavior.

Focused requests load only relevant references; composite requests use the manager. Examples:

- “Polish this paragraph while preserving its numbers and qualifications.”
- “Audit the composition of this draft without rewriting it.”
- “Develop these preliminary bullets into a report and identify missing support.”
- “Review evidence using only the supplied contents, without external research.”
- “Independently fact-check these claims and report source limitations.”
- “Explore what this project map needs to represent, then generate and validate it against the supplied materials.”

Evidence work has exactly two modes: independent external research and verification, or review using supplied material and model knowledge without external research. The assistant asks when relevant and unresolved, retains the choice, and does not treat remembered information as verified. Bounded acquisition of an explicitly requested review target is distinct from corroborating research; explicit retrieval restrictions still control. External research and file-format operations depend on authorized facilities provided by the host.

### Illustrative revision

Input: “In a pilot that involved 12 devices, lower losses were observed only under dry conditions, and performance in humid conditions was not tested.”

Revision: “A 12-device pilot showed lower losses only under dry conditions. Performance in humid conditions was not tested.”

The sample size and conditions survive; broader applicability remains unestablished. This is an illustrative example, not a new trial result. A review-only request instead receives located findings and remedies, without an automatic rewrite.

## Project contents

- [Skill entry point](technical-writing-assistant/SKILL.md): safeguards, execution, and direct routing to every reference.
- [Manager](technical-writing-assistant/references/manager.md): evidence modes, workflow selection, iteration, and 17 composite recipes.
- [Focused references](technical-writing-assistant/references/): independent procedures and shared guidance.
- [Capability map](docs/dev/CAPABILITY_MAP.md): scope, boundaries, design rationale, and contextual outline adaptation.
- [Initial implementation review](docs/dev/REVIEW.md): historical coverage and sample evidence.
- [Post-revision comprehensive review](docs/dev/REVISION_REVIEW.md): issue resolution, consistency, migration completeness, new trials, and verification limits.
- [Specification](docs/dev/SPEC.md) and [implementation plan](docs/dev/PLAN.md): project requirements and the ordered module campaign.

The skill preserves quotations, code, equations, identifiers, essential reasoning, numerical factors, and qualifications. Substantive proposals remain explicit. Drafting does not authorize sending messages, publishing, or changing software.

Run local resource, routing, and presentation checks with Python 3.11 or newer:

```console
python tools/check_package.py
```

This development checker does not execute the skill or retrieve external sources.

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).
