# Repository policy revision report

## Campaign and result

- Campaign: `004_b382f78`; baseline `b382f7803479073a3532c62ebdf868f76549116f`; date 2026-11-04.
- Plan: [REVISION-PLAN.md](REVISION-PLAN.md).
- Branch: `revision/004_b382f78-repository-policies`; creation parent and eventual integration target: `main`.
- Published opening: `7c69e4d74ad771aea8c4605883300db654787239`, read back before V-001.
- V-001 is implemented and verified within the checks below. The containing result commit requires publication/readback before the next checkpoint.

## V-001 changes and verification

| Target / check | Actual result |
| --- | --- |
| Root WINDOWS_SHELL_POLICY.md | Copied byte for byte from the attachment, including original line endings: 4,273 bytes; SHA-256 `099ba1d864adc90e8511f152f33472acf6b49ce090c15bda8c461c42857694b3` |
| Root SKILL_DISCOVERY_PROTOCOL.md | Copied byte for byte from the attachment, including original line endings: 3,029 bytes; SHA-256 `a87f8dac06d206d5873fdd6ae454156f8c1e335be05c732b3b58efe040eff084` |
| Root AGENTS.md | Exact requested Initialization and Windows shell sections inserted once immediately before Governing documents; all other bytes match baseline |
| Discovery initialization | Read-only inspection found neither `.agents/skills/` nor `.agents/plugins/`; absent categories reported in chat. No workflow execution or Git operation occurred during discovery |
| Current local links and package | Bounded current-source fixture checked with `tools/check_package.py`: 20 references, 166 local links, zero errors. Historical contents excluded; existence-only placeholders used for existing historical link targets |
| Preservation and diff | Runtime package, governing documents and all closed campaign records unchanged; only the requested root files and campaign/continuity records are in the proposed delta |
| Whitespace and stored content | Staged whitespace check accepts retained CRLF line endings; staged root-policy blobs match supplied attachment bytes |

The bounded fixture includes current root guidance, both new policies, current governing documents, the runtime package, the active campaign and the development checker. Existing historical targets `docs/dev/REVIEW.md`, `docs/dev/REVISION_REVIEW.md` and `docs/dev/revision_plans/REVISION_PLAN_1cc08a2.md` are represented by empty files for existence checks only. No historical report or trial content was loaded or validated.

## Publication and limits

The restored checkout had no saved shell credential or configured credential helper. The supervised opening push failed to authenticate; cleanup was confirmed and readback found the branch absent. A bounded dry-run identified the unavailable username prompt. The connected GitHub app then published an equivalent opening checkpoint with the exact same Git tree; it was read back before execution. The unpublished local opening was replaced by that verified equivalent. Subsequent publication uses the connected app, with an expected-head check and exact remote readback.

This is a repository-guidance amendment, not a runtime skill revision or installed-skill update. The Windows policy was preserved as supplied; native Windows shell behavior was not exercised on this Linux host. No comprehensive review, release or prior optional finding repair was added to scope.

V-001 is complete. After result publication/readback, leave campaign 004 open on its branch for the user's next decision. Main integration and closure have not been requested.
