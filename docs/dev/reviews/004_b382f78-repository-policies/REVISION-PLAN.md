# Repository policy revision plan

## Campaign and authority

- Campaign: `004_b382f78`; directory `004_b382f78-repository-policies`.
- Baseline and branch-off: `b382f7803479073a3532c62ebdf868f76549116f`, verified published `main` on 2026-11-04.
- Working branch: `revision/004_b382f78-repository-policies`; creation parent and eventual integration target: `main`.
- Authority: the user requested a new revision campaign, both supplied attachments at the root, and the exact supplied Initialization and Windows shell sections before `## Governing documents` in AGENTS.md.
- Entry: directly accepted focused amendment. No preceding review or finding is invented.
- Scope: root policy files and exact AGENTS insertion, plus this campaign's plan/report and coordinator HANDOFF.

## Ordered revision

| Action | Outcome and owner | Verification |
| --- | --- | --- |
| V-001 | Coordinator copies `WINDOWS_SHELL_POLICY.md` and `SKILL_DISCOVERY_PROTOCOL.md` unchanged from the supplied attachments and inserts the requested text once immediately before Governing documents in root AGENTS.md | Byte identity of both attachments; exact insertion and preservation of all other AGENTS bytes; current local links; whitespace and protected-source checks |

No runtime skill, governing capability requirement, installed skill or closed campaign is modified. The attachments establish repository instructions, not permission to execute an unrelated workflow. Windows shell execution checks are outside this Linux-host change.

## Persistence and stop

Publish and verify this opening checkpoint before V-001. Commit the verified revision with its report and updated HANDOFF, then publish/read back that result before any further work. Keep the campaign open on its branch for the user's next decision; do not merge, close or release automatically.

Final evidence belongs in `REVISION-REPORT.md` after execution. The supplied policy files retain their bytes and line endings. Exclude closed campaign contents from current link validation; inspect their paths/object identity only for preservation.
