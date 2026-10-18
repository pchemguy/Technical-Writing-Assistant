# Revision report

## Campaign and state

- Campaign: `001_dead567`; [revision plan](REVISION-PLAN.md); [original review](REVIEW-REPORT.md).
- Reviewed baseline: `dead5674000dfe9ee77b239f935f639937c38405`.
- Revision source and original opening/review commit: `9a76533259836801ccbb50f9389b59b6e55f506e`.
- Working branch: `revision/001_dead567-comprehensive-skill-review`; creation parent and target: `main`.
- User authorization: plan and execute the revision, 2026-10-18.
- Current state: both actions revised and verified by source comparison and structural checks; V-001 published, V-002 at its source/evidence checkpoint. Integration remains pending. These checks do not establish changed-candidate behavior.

## Publication recovery

The replacement credential restored HTTPS Git publication. Remote readback matched the original review commit `9a76533259836801ccbb50f9389b59b6e55f506e`; main remained `dead5674000dfe9ee77b239f935f639937c38405`. The earlier 403/401 attempts remain historical observations in the review report. The ignored credential is not tracked or reproduced in these records.

## Revision evidence

| Action / finding | Actual change | Checks and limits | Disposition |
| --- | --- | --- | --- |
| V-001 / R-001 | Replaced the scientific-writing completion sentence with a direct prohibition on implying unperformed analysis or external verification. | Full module and affected SKILL/revision-check boundaries compared; package validator exit 0; whitespace check passed. See V-001 below. | Verified for this wording defect. |
| V-002 / R-002 | Clarified the input and output together to describe dry-condition testing; explanation now identifies preserved testing limits. | Both versions preserve 12 devices, observed lower losses and untested humidity. Full combined source comparison and structural checks passed. See V-002 below. | Verified for the accepted clarification. |

## Persistence and integration

Plan commit `40c0126f36c3e1af06712ed828a0fa774a22cd8a` was published; remote readback matched before V-001 began. V-001 source/evidence commit `ad3a83b04ea5d3646220695cbcf464f176c85166` was published and read back before V-002 began. The containing V-002 source/evidence commit identifies this checkpoint; publish/read it back before integration. No predicted self-SHA is embedded.

Final integration is pending V-002's verified publication and the prospective main checks. No merge, target publication or campaign closure has occurred at this checkpoint.

## Remaining scope and limits

No accepted finding remains unresolved by the source revision. Original review observations and raw consumer evidence are retained. These local wording changes do not require a new comprehensive audit, historical-record validation, independent research or installation. No changed-candidate behavior or universal reliability claim is inferred from source/structural checks.

## V-001

Changed only the last sentence in `technical-writing-assistant/references/scientific-writing.md`. It now says: “Do not imply that data analysis or external verification was performed when it was not.” The preceding reporting, uncertainty and missing-information checks remain unchanged.

Source recheck found agreement with the module's input rule, which limits work to reporting/reasoning when analysis is unavailable, and its output rule, which distinguishes editorial checks from validation actually performed. The entry's truthful-delivery rule and revision-check's evidence-status comparison remain compatible. The sentence prohibits an unsupported completion claim; it does not prohibit accurately describing separately performed analysis.

Executed `python /root/.codex/skills/remote-skills/skill-6ad49f5dd9a481918b90db50d0256cd2/scripts/validate_skill.py technical-writing-assistant` and `git diff --check`; both passed. Inspected the source diff: one sentence changed, with no new route, dependency or requirement. This verifies the local precision repair, not improved runtime reliability. No consumer trial was rerun.

## V-002

Changed only the README's paired illustration and its immediate explanation. The input says the 12 devices were tested under dry conditions; the output describes a 12-device pilot under those conditions. Both retain observed lower losses and explicitly say humid performance was not tested. Removed the ambiguous exclusivity wording from both versions together. The clarification is an accepted choice for the authored illustration, not an inferred correction to actual experimental data.

The source comparison retained sample size, observation, dry conditions, untested humidity, unestablished broader applicability and the illustrative/non-trial label. Neither version adds a comparator, numerical effect, statistical significance, causal mechanism or tested humidity outcome. The review-only behavior explanation remains unchanged.

Combined checks on the revised package:

| Check | Observed result and boundary |
| --- | --- |
| APA package validator | Exit 0. Offline structure only. |
| APA package inspector | Exit 0; 20 references, one asset, zero errors/warnings. Runtime not verified by inventory. |
| Existing checker on bounded current-source copy | Exit 0; 37 copied current files and three historical path placeholders. Final link count is recorded with the integration checks after record updates. Historical contents were not read. |
| Protected-source comparison | No difference in SPEC, PLAN, CAPABILITY_MAP, historical reviews, revision plans or validation records from the original baseline. |
| Editorial comparison | The runtime diff contains only V-001's final sentence; product documentation changes contain only V-002's paired example and explanation, plus the earlier workflow navigation. No new finding was identified in these affected passages. |
| Whitespace checks | Worktree and staged checks passed; final staged check is repeated after this report update. |

These are source and structural checks. Earlier consumer outputs remain evidence of the earlier source, and no post-change workflow or target-client trial is claimed.
