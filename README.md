---
url: https://chatgpt.com/c/6abe25da-8604-83ea-82be-c9c4f1a86eb8
urls: 
  - https://chatgpt.com/c/6abcb9c4-7980-83eb-85b2-e910c0fdf297
  - https://chatgpt.com/c/6abe25da-8604-83ea-82be-c9c4f1a86eb8
---

# Technical Writing Assistant

A modular agent skill for software documentation and scientific, technical, and professional writing. It reviews and revises existing material for clarity, structure, terminology, style, composition, and consistency while preserving technical meaning and authorial intent.

It also develops early notes into prose, explores composition, critiques reasoning, assesses evidence, and generates, reviews, validates, or repairs structured outlines and maps. Specialized maps emerge from contextual exploration rather than a fixed catalogue.

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

## Project contents

- [Skill entry point](technical-writing-assistant/SKILL.md): safeguards, execution, and direct routing to every reference.
- [Manager](technical-writing-assistant/references/manager.md): evidence modes, workflow selection, iteration, and 17 composite recipes.
- [Focused references](technical-writing-assistant/references/): independent procedures and shared guidance.
- [Capability map](docs/dev/CAPABILITY_MAP.md): scope, boundaries, design rationale, and contextual outline adaptation.
- [Initial implementation review](docs/dev/REVIEW.md): historical coverage and sample evidence.
- [Post-revision comprehensive review](docs/dev/REVISION_REVIEW.md): issue resolution, consistency, migration completeness, new trials, and verification limits.
- [Specification](docs/dev/SPEC.md) and [implementation plan](docs/dev/PLAN.md): project requirements and the ordered module campaign.

Run current-source resource, routing, frontmatter and presentation checks with Python 3.11 or newer:

```console
python tools/check_package.py
```

The default `current` scope checks root Markdown, the runtime skill and current documents under `docs/`. Retained review, feature, phase-report, revision-plan and validation collections, plus legacy review documents, are excluded from content checks. Links to excluded records are checked for target existence only, without reading their contents or validating historical heading fragments.

Include each selected active campaign with `--active-campaign docs/dev/reviews/<campaign>` (replace `<campaign>` with its directory name; repeat the option for multiple active campaigns). Use `--scope all` only for an explicitly intended full-repository check; it includes retained and tool-directory Markdown and should not be used for routine current-source validation.

The checker supports one-line plain or quoted string scalars and a two-space string-to-string `metadata` mapping. Duplicate keys, nonstring values and unsupported YAML produce a nonzero invalid/unverified result; this is not a general YAML validator. It does not execute the skill or retrieve external sources.

With pytest available, run checker regression tests with `python -m pytest tests -q`. Pytest is a development dependency; the checker itself uses only the standard library.

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).
