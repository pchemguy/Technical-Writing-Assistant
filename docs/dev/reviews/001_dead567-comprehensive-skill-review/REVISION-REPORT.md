# Revision report

## Campaign and state

- Campaign: `001_dead567`; [revision plan](REVISION-PLAN.md); [original review](REVIEW-REPORT.md).
- Reviewed baseline: `dead5674000dfe9ee77b239f935f639937c38405`.
- Revision source and original opening/review commit: `9a76533259836801ccbb50f9389b59b6e55f506e`.
- Working branch: `revision/001_dead567-comprehensive-skill-review`; creation parent and target: `main`.
- User authorization: plan and execute the revision, 2026-10-18.
- Current state: V-001 revised and verified by source comparison and package validation; V-002 pending. These checks do not establish changed-candidate behavior.

## Publication recovery

The replacement credential restored HTTPS Git publication. Remote readback matched the original review commit `9a76533259836801ccbb50f9389b59b6e55f506e`; main remained `dead5674000dfe9ee77b239f935f639937c38405`. The earlier 403/401 attempts remain historical observations in the review report. The ignored credential is not tracked or reproduced in these records.

## Revision evidence

| Action / finding | Actual change | Checks and limits | Disposition |
| --- | --- | --- | --- |
| V-001 / R-001 | Replaced the scientific-writing completion sentence with a direct prohibition on implying unperformed analysis or external verification. | Full module and affected SKILL/revision-check boundaries compared; package validator exit 0; whitespace check passed. See V-001 below. | Verified for this wording defect. |
| V-002 / R-002 | Pending. The plan records the chosen observational reading of the illustration. | No post-change checks yet. | Accepted recommendation. |

## Persistence and integration

Plan commit `40c0126f36c3e1af06712ed828a0fa774a22cd8a` was published; remote readback matched before V-001 began. The containing V-001 source/evidence commit identifies this action checkpoint; publish/read it back before V-002. Do not embed a commit's predicted self-SHA.

Final integration is pending both verified action publications and the prospective main checks. No merge, target publication or campaign closure has occurred at this checkpoint.

## Remaining scope and limits

R-002 remains accepted and pending. Original review observations and raw consumer evidence are retained. These local wording changes do not require a new comprehensive audit, historical-record validation, independent research or installation. No changed-candidate behavior or universal reliability claim is inferred from source/structural checks.

## V-001

Changed only the last sentence in `technical-writing-assistant/references/scientific-writing.md`. It now says: “Do not imply that data analysis or external verification was performed when it was not.” The preceding reporting, uncertainty and missing-information checks remain unchanged.

Source recheck found agreement with the module's input rule, which limits work to reporting/reasoning when analysis is unavailable, and its output rule, which distinguishes editorial checks from validation actually performed. The entry's truthful-delivery rule and revision-check's evidence-status comparison remain compatible. The sentence prohibits an unsupported completion claim; it does not prohibit accurately describing separately performed analysis.

Executed `python /root/.codex/skills/remote-skills/skill-6ad49f5dd9a481918b90db50d0256cd2/scripts/validate_skill.py technical-writing-assistant` and `git diff --check`; both passed. Inspected the source diff: one sentence changed, with no new route, dependency or requirement. This verifies the local precision repair, not improved runtime reliability. No consumer trial was rerun.
