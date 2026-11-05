# Agent orientation

This repository develops the standalone Technical Writing Assistant skill. Its runtime entry is [technical-writing-assistant/SKILL.md](technical-writing-assistant/SKILL.md); focused procedures and shared guidance are under its references directory. Optional OpenAI presentation is under agents and assets inside that package.

## Governing documents

- [Specification](docs/dev/SPEC.md) defines required behavior.
- [Capability map](docs/dev/CAPABILITY_MAP.md) defines capability boundaries and shared policy.
- [Implementation plan](docs/dev/PLAN.md) describes the whole project.
- Read applicable nested instructions for the selected paths. Load this file explicitly if the host does not discover it.

## Continuity and active ownership

Start with [HANDOFF.md](docs/dev/HANDOFF.md) and the active campaign records it identifies. HANDOFF is a named checkpoint; recover later work from the owning records and Git. SDD Manager's coordinator owns campaign continuity and persistence.

Do not routinely load or edit closed campaign plans, reports or historical trial records. Discover their paths for identity and preservation, and consult selected history only for a specific task need.

## Checks and workflow boundaries

The documented development command is `python tools/check_package.py` with Python 3.11 or newer. Its default current-source scope checks root Markdown, the runtime skill and current docs while excluding retained collections and legacy review contents. Add `--active-campaign docs/dev/reviews/<campaign>` for each explicitly selected active campaign; excluded historical targets receive existence-only link checks. `--scope all` is a deliberate full-repository mode, not a routine current-source check. See README for exact exclusions and supported frontmatter syntax. The checker does not execute the skill or verify external URLs. With pytest available, run `python -m pytest tests -q` for regressions.

Preserve unrelated work. Review requests authorize findings and requested campaign artifacts, not runtime repairs, installation or a merge by implication. Commit and publish coherent owned checkpoints within the established scope, verifying remote persistence. For task-list implementation, use one executable task's result, evidence and initial completion checkbox in its owning task commit.

See [SDD-MANAGER.md](SDD-MANAGER.md) for development-workflow attribution and [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for AI assistance and maintainer responsibility.
