# Qualitative assessment of fresh consumer requests (C-007)

- Reviewed baseline: `f2000eeb61b125dd1efca421926cffd11545b4a3` (runtime tree `02b47f96efd08fd23d1e12259c9d532dd4dcd69d`).
- Raw outputs: [consumer-a.md](../evidence/consumer-a.md) (`b65c4e5a-353b-4487-91ca-3f06f02ddad5`) and [consumer-b.md](../evidence/consumer-b.md) (`e92cf31d-e66a-4d8d-a5f5-d665a6431403`).
- Method: Two fresh isolated subagent contexts received only `technical-writing-assistant/SKILL.md` as their initial entry point and three ordinary user requests each, selecting references from `SKILL.md` and `references/manager.md` without exposure to `REVIEW-PLAN.md`, expected conclusions, or historical trials. These six requests across two contexts provide qualitative behavioral observations for the stated prompts and model; they are not six independent replications and do not establish universal cross-model or cross-client reliability.

## Summary of observed routing and task compliance

| Case | Request type | References loaded by consumer | Boundary and constraint compliance | Observed quality and issues |
| --- | --- | --- | --- | --- |
| A-1 | Comprehensive findings-only review of technical decision note + size/detail assessment | `SKILL.md`, `manager.md`, `professional-writing.md`, `style-guidelines.md`, `composition-analysis.md`, `argument-review.md`, `evidence-review.md`, `terminology-consistency.md` | Kept findings-only (no rewrite); asked the exact two-mode evidence question while completing internal review; skipped `revision-check.md` and `source-research.md` | Satisfied all prompt and skill constraints; no source or sample defect observed |
| A-2 | Focused language edit of release-note paragraph with protected quotation/identifiers | `language-revision.md`, `software-documentation.md`, `revision-check.md` (reusing `SKILL.md`, `style-guidelines.md`, `terminology-consistency.md`) | Preserved meaning, scope, quantities, code identifiers (`recieve_timeout`), and exact quotation (`non-idempotent request`); asked no unnecessary mode question | Satisfied all prompt and skill constraints; flagged `recieve_timeout` typo and referential ambiguities outside the clean paragraph |
| A-3 | Customer incident update email drafted from rough internal notes | `draft-development.md` (reusing `SKILL.md`, `manager.md`, `professional-writing.md`, `style-guidelines.md`, `revision-check.md`) | Marked draft-only; separated verified `US-East` from unchecked non-EU regions; excluded unapproved service credit and unconfirmed Friday target from commitments | Satisfied all prompt and skill constraints; surfaced pending finance/engineering confirmations explicitly |
| B-1 | Outline review and requirement validation without rewriting | `SKILL.md`, `outline-review.md` | Direct routing to `outline-review.md`; no rewrite; separated genuinely missing topics from thin/merged/misordered nodes; used `Failed` and `Partly satisfied` accurately | Satisfied all prompt and skill constraints; stated inspection boundary for absent software/`config.toml` schema |
| B-2 | Comparative check of original vs. revised scientific results paragraph | `SKILL.md`, `revision-check.md` | Direct routing to `revision-check.md`; no rewrite; identified all meaning shifts and unavailable draft reference | Satisfied all prompt and skill constraints; connected changes to `(Table 2)` citation fidelity |
| B-3 | Role ownership and relationship map from process workshop notes | `SKILL.md`, `outline-generation.md`, `outline-context-exploration.md` | Map-only output (no prose essay); represented decoupled ID assignment, prerequisite gates, and non-sequential `QA` ↔ `Biobank` loops; exposed consent-check gap | Satisfied all prompt and skill constraints; no predefined profile catalogue used |

## Case-by-case qualitative evaluation

### Case A-1 — Comprehensive editorial review of a decision note

- **Routing and workflow selection:** From `SKILL.md`, Consumer A loaded `references/manager.md` for a composite review and followed the `Comprehensive editorial review` recipe (`manager.md` line 91) combined with `professional-writing.md` (`Decision brief`, line 28). It did not load `revision-check.md` (respecting the findings-only rule in `manager.md` lines 76, 80 and `revision-check.md` line 13) or `source-research.md` (respecting the mode gate).
- **Evidence-mode handling (C-004):** Recognising quantitative and normative claims (`40%` latency reduction, `3,000 jobs per minute`, `industry best practice`), Consumer A posed the manager's exact two-mode question at the top of the response and proceeded with all internal reasoning, composition, terminology, and supplied-material gap analysis without claiming external verification.
- **Size and level-of-detail assessment (C-002):** Answered the user's size/detail question directly against audience and purpose (`platform leads` evaluating a Q3 migration and ownership transfer). Rather than applying a length quota, it diagnosed an inverted distribution of detail: `Background` (125 of ~230 words) is overloaded with historical narrative (2017 team move, 2019 `rq` anecdote, past Redis upgrade numbers), while `Problem`, `Proposal`, `Risks`, and `Recommendation` (~105 words total) are underdeveloped on failure rates, component migration scope, database bloat/polling QPS, and ownership agreement. Crucially, it distinguished disposable history in `Background` from architectural facts inside `Background` that must be retained (`scheduler`, `retry wrapper`, `dead-letter list`, `session cache` co-tenancy).
- **Substantive, compositional, and terminology findings:** Identified the arithmetic conflict (`3,000 jobs per minute` = `50/sec`, not `30/sec`), the tension between `500 ms` polling (~250 ms average pickup delay) and an unexplained `40%` end-to-end latency reduction, the gap between `SELECT ... FOR UPDATE SKIP LOCKED` and duplicate execution on worker crash/retry, the conflation of storage migration with organizational ownership, the unconfirmed assignment of ownership to the platform leads, the standalone-context failure in `"As discussed in the previous revision..."` (`composition-analysis.md` line 36), the unfocused topic sentence in `Background`, and the three-way terminology drift (`Postgres`/`PostgreSQL`/`PG`, `background jobs`/`jobs`/`task`/`work items`, `Workers`/`Consumers`).

### Case A-2 — Focused language revision with protected material

- **Routing and proportionality:** Consumer A loaded `language-revision.md`, `software-documentation.md`, and `revision-check.md` while reusing `style-guidelines.md` and `terminology-consistency.md` already in session context. It did not ask an evidence-mode question or expand the local edit into a structural rewrite.
- **Fidelity and protected expressions (C-003):**
    - Preserved the quoted requirement `"clients must not retry non-idempotent request without explicit opt-in"` character-for-character, including its grammatical singular `request` (`language-revision.md` line 32).
    - Preserved the misspelled parameter identifier `` `recieve_timeout` `` intact in the edited paragraph while adding a separate verification note alerting the author to confirm the spelling against the codebase (`language-revision.md` line 13, `software-documentation.md` line 18).
    - Preserved all numerical values (`4.2`, `3`, `250 ms`, `±10%`, `max_retries=0`), conditions (`unless retry_unsafe=True is passed`), and modality (`may want to set`).
    - Corrected all grammatical defects (`retries was` → `retries were`, `parameter ... are` → `parameter ... is`, `POST requests is` → `POST requests are`) and tightened wordy phrasing (`will now retry` → `retries`, `in order to comply` → `to comply`, `may possibly want` → `may want`).
    - Flagged the three referential/scope ambiguities (`"This change"`, `"Retrying in this way"`, `"the old behaviour"`) in separate bulleted notes rather than silently altering the meaning of the release note.

### Case A-3 — Developing rough incident notes into customer correspondence

- **Routing and authority:** Consumer A loaded `draft-development.md` and applied `professional-writing.md` (`Correspondence`, line 29) and `revision-check.md` (comparing the draft against the source notes per `revision-check.md` line 11). It explicitly marked the output `Draft only—no message has been sent`.
- **Nuance, uncertainty, and unapproved commitments (C-003, C-005):**
    - Preserved exact incident timestamps and metrics (`Tuesday at 03:00 UTC`, `Wednesday morning`, `~4%` in `EU-West`, `nearly 9%` in `EU-North`, `7 days` event retention, workaround tested on `two of your tenants`).
    - Honored the verification distinction in `their other 3 regions look fine but we've only actually checked US-East`: reported `US-East` as verified and the other two non-EU regions as showing no observed issues while direct verification checks are completed.
    - Framed the gateway certificate rotation as a suspected cause under investigation (excluding internal informal phrasing `"Marco thinks"`).
    - Applied `draft-development.md`'s missing-content rules (`lines 24–27`) and `professional-writing.md`'s commitment rules (`lines 5, 9, 16`) by omitting the unapproved service credit (`need to check w/ finance first`) and the unconfirmed Friday rollback target (`target Friday?? not confirmed by eng lead`) from the customer-facing text, surfacing both in `Draft Notes and Open Decisions Before You Send`.

### Case B-1 — Outline review and requirement validation

- **Routing and coverage selection (C-005):** Consumer B routed directly from `SKILL.md` to `references/outline-review.md`, selecting comprehensive (evaluative + validation) coverage to answer both parts of the user's prompt ("what is genuinely missing versus what is there but thin, and whether it actually meets the requirements") without rewriting the outline or loading unnecessary modules.
- **Calibration on presence vs. development vs. requirement satisfaction (`outline-review.md` lines 51, 66):**
    - Clearly separated **genuinely missing** elements (Requirement 4 uninstallation and removal of cached data; Requirement 1 installation prerequisites; Requirement 2 all non-common `config.toml` keys omitted by `2.2 Common keys`; Requirement 5 initial CLI invocation and post-install verification) from elements **present in the outline but thin, merged, or misordered** (`5.2 Permissions and caches` combining two required support topics under vague nouns; `3.2 Windows` bare heading; `2. Configuration` placed before `3. Installation`; `4.1` and `4.2` thin onboarding for first-time CLI operators).
    - Used `Failed` for Requirements 2 and 4 and `Partly satisfied` (identifying the satisfied and missing subparts) for Requirements 1, 3, and 5, and explicitly noted that factual completeness against the uninspected `fieldsync` software and `config.toml` schema was not assessed.

### Case B-2 — Comparative revision check of scientific results prose

- **Routing and scope (C-003, C-005):** Consumer B routed directly from `SKILL.md` to `references/revision-check.md` (`The same procedure can assess a supplied revision`, line 5) and delivered a findings-only comparative analysis without rewriting the paragraph.
- **Detection of substantive and contextual defects:** Accurately identified and explained the scientific impact of all changes introduced by the colleague's revision:
    - Physical unit change (`18–31%` relative decrease → `18–31 mg/L` absolute decrease with unchanged numerals).
    - Methodological distortion (`The fourth sample, which had the lowest initial moisture, showed no measurable change` → `one sample was excluded`), plus deletion of the sample denominator (`three of the four`) and incubation temperature (`25 °C`).
    - Introduction of an unavailable contextual reference (`As noted in the earlier draft`) that fails at the standalone reading boundary (`revision-check.md` line 22).
    - Causal inflation (`correlated with microbial respiration (r = 0.62)` → `driven by microbial respiration (r = 0.62)`).
    - Certainty and scope inflation (`suggest that ... may contribute ... under these conditions` → `demonstrate that ... contributes`).
    - Resulting fidelity conflict with the retained `(Table 2)` citation (`revision-check.md` line 20).

### Case B-3 — Contextual role-ownership and relationship map

- **Routing and adaptation (C-005):** Consumer B loaded `outline-generation.md` and `outline-context-exploration.md` from `SKILL.md` and produced a standalone structured representation without prose expansion or a questionnaire.
- **Representation of non-hierarchical relationships, decoupled responsibilities, and cycles:**
    - Structured the deliverable into (1) a Role Ownership Map table (Role, Owned Responsibilities, Owned Records/Assets, Gating Rules & Conditions), (2) a two-part Role-to-Role Relationships view separating `Lifecycle Handoffs` from `Ongoing Oversight & Exception Loops`, and (3) `Unresolved Ownership & Source Gaps` with a focused follow-up question.
    - Explicitly captured the decoupled prerequisite structure: `Data Steward` assigns the `Permanent Sample ID` directly from the `Intake Log` without needing the sample to be physically in the `Biobank`, whereas `Biobank` requires the `Permanent Sample ID` before accepting a sample into storage.
    - Accurately represented the non-prerequisite two-way oversight/exception loop between `QA` and `Biobank` (`QA` audits `Biobank` quarterly; `Biobank` reports temperature deviations to `QA` on occurrence; `QA` requests freezer quarantine from `Biobank`) as a valid operational cycle rather than forcing a single tree or flagging a false dependency error.
    - Preserved the workshop's explicit uncertainty (whether `PI` or `Biobank` checks the `Consent Register` maintained by `Data Steward` prior to external release) and noted the unstated resolution path for samples held at `Intake Desk` due to incomplete paperwork.
