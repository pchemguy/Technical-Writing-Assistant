# Checker revision plan

## Accepted scope and provenance

- Campaign: `008_fecf8cc-critical-comprehensive-review`; continue its existing revision branch and creation parent `main`.
- The user now explicitly requests “Prepare revision plan. Fix. Close.” This accepts correction of R-001 and R-002, publication, final verified integration and closure. No further human checkpoint is pending.
- Original branch-off/reviewed baseline: `fecf8cc097c9bccc78c0ac29676d397a1fefaa15`; opening: `fc769adb516eba514f0a4987f902634a546af3a2`; published completed review: `7fff37d4720ba38665ce688635a34e62b006fe48`.
- Canonical baseline findings remain in [REVIEW-REPORT.md](REVIEW-REPORT.md). Original review evidence and its unrun consumer-trial boundary remain unchanged. Current revision results belong in REVISION-REPORT.md.
- Preserve the complete runtime skill and campaigns 001–007. This is focused checker/test/documentation maintenance, not a new writing capability, installation, release or comprehensive review replay.

## Ordered actions and acceptance

| Action | Finding / affected owners | Accepted change and objective recheck |
| --- | --- | --- |
| A-001 | R-001; checker and regression tests | Implement a bounded standard-library frontmatter parser: required string fields; duplicate top-level/nested-key detection; string-to-string metadata; supported standard optional fields; explicit nonzero unverified/error results for unhandled syntax. Prove failing tests first, then verify valid current/quoted/optional input and rejected duplicates/nonstring/unsupported inputs. Retain routing/link/presentation checks. |
| A-002 | R-002; checker CLI, regression tests, README and AGENTS | Provide a documented current-source mode by default, excluding retained review/revision/validation/feature/report collections and legacy review documents from content inspection. Include explicitly selected active campaign directories; validate excluded historical link targets by existence only, without reading their contents/fragments. Keep an explicit full-repository mode. Prove historical exclusion, active/current error detection, contained selection and useful CLI outcomes. |

The supported parser subset includes one-line plain/single-quoted/double-quoted string scalars and a two-space metadata mapping; complex YAML remains explicitly unverified, not silently accepted. Current skill contents need no editing. R-002 selection is explicit; no attempt to guess campaign closure from names or HANDOFF text.

## Evidence and persistence

- Publish/read back this plan before code/test changes.
- Use pytest for regression tests. Resolve the missing pytest dependency in an isolated session location, without adding runtime dependencies or global packages to the project. Record actual installation or alternative facility results.
- For each action, observe meaningful RED failures before production edits, run focused GREEN/regression checks and update REVISION-REPORT.md. Commit and publish/read back that action's source, tests and evidence before the next action.
- Preserve earlier review observations/helper/JSON and source/scenario assessments as baseline evidence. Do not rerun its observation helper against revised code and overwrite the reproduced-defect record.
- Verify the documented current-source command and selected campaign on the real checkout; compare unchanged runtime and prior campaign object identities without reading frozen contents. Update finding dispositions by an appended current-revision note.
- Reconcile HANDOFF, merge the complete verified campaign tip into refreshed `main` with two parents, rerun applicable merged checks, publish/read back and return clean on `main`. Stop after closure; no release or installation.
