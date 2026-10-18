# Revision plan

## Campaign and decisions

- Campaign: `001_dead567`; original baseline: `dead5674000dfe9ee77b239f935f639937c38405`.
- Revision source and published review checkpoint: `9a76533259836801ccbb50f9389b59b6e55f506e`.
- Branch: `revision/001_dead567-comprehensive-skill-review`; creation parent and integration target: `main`.
- [Review report](REVIEW-REPORT.md); [revision report](REVISION-REPORT.md).
- Authorization: the user requested “Plan and execute revision” on 2026-10-18 after the review checkpoint was published.
- Decisions: accept R-001 as a local precision repair and R-002 as a clarification of the illustrative example. No finding is deferred or rejected.
- State at this checkpoint: planned; execution and checks are recorded separately.

R-002 is an ambiguity, not a demonstrated factual contradiction. For this authored illustration, choose the observational reading: 12 devices were tested under dry conditions and lower losses were observed; humid performance was not tested. Revise the illustrative input and output together. This decision clarifies the example and supplies no real pilot evidence.

## Authoritative project updates

No project requirements, capability boundaries, module layout or executable task list change. SPEC, PLAN and CAPABILITY_MAP remain governing inputs and require no amendment. The changes belong to the existing scientific-writing reference and root README. Presentation metadata remains applicable because purpose, invocation and scope are unchanged.

## Ordered revisions

| Action | Finding | Outcome and owner | Dependency | Acceptance and regression checks |
| --- | --- | --- | --- | --- |
| V-001 | R-001 | Replace the scientific-writing completion disclaimer with a direct prohibition on claiming unperformed analysis or verification. | Published plan checkpoint. | Compare the full module and its affected entry/revision-check interfaces. Editorial work alone must not imply analysis; separately performed analysis may still be reported accurately. Preserve all other module instructions. Run package validation. |
| V-002 | R-002 | Clarify both README example versions and their explanation to describe dry testing without suggesting a tested humid-condition result. | V-001 committed, published and read back. | Compare input/output for 12 devices, observed lower losses, dry testing, humid testing absent and the illustrative label. Add no comparator, magnitude, significance or broader effect. Recheck both changes together, package validity, current-source links and scoped Git differences. |

## Execution and persistence

1. Commit and publish this plan, revision-entry continuity and the initial revision report; verify the remote commit before source changes.
2. For each action, apply only its owned source change, record actual checks and finding disposition in the revision report, then commit, push and read back before the next action.
3. Inspect the complete campaign difference from its creation parent. Preserve closed records and the stopped legacy checkout.
4. Merge the verified campaign tip explicitly into refreshed main using a two-parent merge. Check the prospective merged source and current records; refresh HANDOFF for the parent return and record integration evidence in that merge.
5. Publish and read back the target merge commit before declaring the campaign closed.

These are focused maintenance actions, not invented executable TASKS. Their stable action IDs do not substitute for task IDs.

## Verification and limits

Use Technical Writing Assistant language revision and revision comparison, plus proportionate Agent Package Author source/structure checks. Run the existing repository checker on a bounded copy of runtime sources, governing current documents and active campaign records. Historical link targets may be empty existence-only placeholders; do not load or repair old contents.

No new executable test suite is warranted for these wording changes. Source comparison establishes the specific wording outcomes; structural checks establish their own narrow properties. Do not reinterpret the earlier consumer tasks as post-change trials or claim behavioral improvement. No external fact checking, live research, client activation, installation or presentation regeneration is needed.

Stop after verified publication and integration of these accepted revisions. Do not start another campaign, extend product behavior or modify unrelated skills.
