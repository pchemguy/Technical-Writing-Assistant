# Checker revision plan

## Accepted scope and provenance

- Campaign: `008_fecf8cc-critical-comprehensive-review`; continue its existing revision branch and creation parent `main`.
- The user now explicitly requests “Prepare revision plan. Fix. Close.” This accepts correction of the review findings, publication, final verified integration and closure. The subsequent routing-table question also requires correction of the overbroad entry assessment (R-003). No further human checkpoint is pending.
- Original branch-off/reviewed baseline: `fecf8cc097c9bccc78c0ac29676d397a1fefaa15`; opening: `fc769adb516eba514f0a4987f902634a546af3a2`; published completed review: `7fff37d4720ba38665ce688635a34e62b006fe48`.
- Canonical baseline findings remain in [REVIEW-REPORT.md](REVIEW-REPORT.md). Original review evidence and its unrun consumer-trial boundary remain unchanged. Current revision results belong in REVISION-REPORT.md.
- Preserve the runtime skill except its bounded entry-routing clarification, and preserve campaigns 001–007. This is focused checker/test/documentation maintenance, not a new writing capability, installation, release or comprehensive review replay.

## Ordered actions and acceptance

| Action | Finding / affected owners | Accepted change and objective recheck |
| --- | --- | --- |
| A-001 | R-001; checker and regression tests | Implement a bounded standard-library frontmatter parser: required string fields; duplicate top-level/nested-key detection; string-to-string metadata; supported standard optional fields; explicit nonzero unverified/error results for unhandled syntax. Prove failing tests first, then verify valid current/quoted/optional input and rejected duplicates/nonstring/unsupported inputs. Retain routing/link/presentation checks. |
| A-002 | R-002; checker CLI, regression tests, README and AGENTS | Provide a documented current-source mode by default, excluding retained review/revision/validation/feature/report collections and legacy review documents from content inspection. Include explicitly selected active campaign directories; validate excluded historical link targets by existence only, without reading their contents/fragments. Keep an explicit full-repository mode. Prove historical exclusion, active/current error detection, contained selection and useful CLI outcomes. |
| A-003 | R-003; entry and source recheck | Clarify per-reference load conditions and role/scope boundaries, plus minimal composite review/revision handoffs in SKILL.md. Compare every row with the owning procedure and check owners/order/output/stop without duplicating manager recipes. Preserve metadata, focused procedures and recipe parity. |
| A-004 | User README cleanup | Remove the complete Status section, Illustrative revision subsection and user-identified safeguard paragraph, as requested during execution. Preserve capability/use guidance, frontmatter and the revised check instructions; inspect the diff and current links without adding content-mirroring tests. |


The supported parser subset includes one-line plain/single-quoted/double-quoted string scalars and a two-space metadata mapping; complex YAML remains explicitly unverified, not silently accepted. Focused procedure contents and skill metadata need no editing; A-003 clarifies only entry routing. R-002 selection is explicit; no attempt to guess campaign closure from names or HANDOFF text.

## Evidence and persistence

- Publish/read back this plan before code/test changes.
- Use pytest for regression tests. Resolve the missing pytest dependency in an isolated session location, without adding runtime dependencies or global packages to the project. Record actual installation or alternative facility results.
- For each action, observe meaningful RED failures before production edits, run focused GREEN/regression checks and update REVISION-REPORT.md. Commit and publish/read back that action's source, tests and evidence before the next action.
- Preserve earlier review observations/helper/JSON and source/scenario assessments as baseline evidence. Do not rerun its observation helper against revised code and overwrite the reproduced-defect record.
- Verify the documented current-source command and selected campaign on the real checkout; compare unchanged runtime and prior campaign object identities without reading frozen contents. Update finding dispositions by an appended current-revision note.
- Reconcile HANDOFF, merge the complete verified campaign tip into refreshed `main` with two parents, rerun applicable merged checks, publish/read back and return clean on `main`. Stop after closure; no release or installation.

## Amendment during execution

The user asked whether the routing/routine table had been checked. R-003 and evidence/routing-review.md correct the earlier overly broad C-001 pass. A-001 regression tests already exist with an observed RED run (19 failed, 10 passed); production code is still unchanged at this amendment. Preserve those uncommitted tests, publish the scoped review/plan correction, then continue A-001, A-002 and A-003 in order, publishing each verified result before the next action. No full review restart or independent consumer claim is introduced.

The user subsequently requested deleting README’s “Illustrative revision” and “Status” blocks. A-004 records that explicit cleanup; it does not change runtime capabilities or expand historical evidence review.

The additional README paragraph beginning “The skill preserves quotations” is also explicitly selected for removal within A-004.
