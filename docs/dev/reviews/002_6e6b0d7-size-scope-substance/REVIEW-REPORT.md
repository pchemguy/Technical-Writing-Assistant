# Review report: document size relative to scope and substance

## Campaign and conclusion

- Campaign: `002_6e6b0d7`; branch/directory suffix: `002_6e6b0d7-size-scope-substance`.
- Review date: 2026-10-20.
- Starting and reviewed source: `6e6b0d7eca36b2db317aaa64cbe55d4aa250cb73`.
- Working branch: `revision/002_6e6b0d7-size-scope-substance`; creation parent/prospective target: `main`.
- [Review plan](REVIEW-PLAN.md); [proposed revision plan](REVISION-PLAN.md).
- State: review and accepted revision actions complete, including explicit size and level-of-detail assessment against purpose, scope, substantive content and audience needs. The revision report records actual verification and publication/integration limits; baseline observations below are retained.
- Evidence boundary: inspected current instructions and governing source, with source-level scenario analysis. No new consumer execution, external fact checking or client trial.

The skill already has substantial coverage of this subject. It explicitly checks unnecessary wording, redundant repetition, duplicated passages, overlapping sections, underdevelopment, disproportionate emphasis and reader burden. The capability map goes further than a generic concision rule: its “Unit size and load” dimension asks whether units are fragmented, underdeveloped or overloaded.

The remaining opportunity is to make an overall proportionality judgment explicit: whether a document's and its sections' extent and detail are justified by their purpose, scope, substance, genre and audience. Existing criteria support that judgment, but do not clearly name it as a document-level review objective and a scoped conclusion to return when requested.

One consolidated recommendation, R-001, covers that clarification and its consequences for routing, diagnosis and rechecking. This is not a finding that duplication detection is absent or that the skill has demonstrated a behavioral failure. A new reference, size metric, mandatory questionnaire or separate workflow is unnecessary.

## What the objective should assess

Size appropriateness means sufficiency and economy relative to the document's actual job. It is not an unconditional preference for shorter text.

| Dimension | Appropriate question | Important boundary |
| --- | --- | --- |
| Required scope and substance | Does the text supply the explanation, support, instructions and qualifications its purpose requires? | Missing substance is not repaired by filler or invented facts. |
| Contribution | What distinct function does each paragraph, section, example or supporting element serve? | A repeated idea may serve a different legitimate reading need. |
| Economy | Could wording or an explanation be removed or consolidated without losing useful meaning or usability? | Preserve precision, prerequisites, numerical reasoning, conditions and evidence. |
| Development | Is a unit too thin to perform its stated role? | A complete warning, transition or narrow answer may properly be short. |
| Distribution | Does detail receive space appropriate to importance, audience and genre? | Unequal section lengths can be justified; required appendices are not automatically excess. |
| Reading boundary | Is the unit read alone, sequentially or through reference lookup? | Recurring warnings or prerequisites may be necessary for independent use. |
| Overall adequacy | Is the inspected artifact appropriately developed, unnecessarily expanded, insufficiently developed, mixed, or not assessable within available material? | These are possible descriptions, not a required status schema. Explain the judgment with locations and reasons. |

Word/page counts may describe the material or an explicit user constraint. They cannot establish quality, justify a split or prove wasted content. No numerical size-to-substance ratio, compression target or token-saving claim is recommended.

## Existing coverage

| Concern | Current owner and baseline location | Assessment |
| --- | --- | --- |
| Wordiness and empty phrasing | `language-revision.md:17–18`; `style-guidelines.md:43–51` | Explicit. Removes unnecessary words without deleting essential reasoning or padding short paragraphs. |
| Useful versus redundant repetition | `style-guidelines.md:35`; `composition-analysis.md:38–39` | Explicit. Repetition can clarify concepts, preserve terminology or support orientation. |
| Duplicate passages and overlap | `material-assessment.md:15`; `composition-analysis.md:28,38`; outline review evaluative steps 4–6 | Explicit across triage, prose composition and outline boundaries. Not limited to exact-string matching. |
| Unit size, load and development | Capability map, Composition analysis coverage; `composition-analysis.md:25–28,32–44` | Explicit for local units and cross-level diagnosis. Broad shallow material and narrow detailed material can each serve their purpose. |
| Overall length/detail against document scope and substance | Composition analysis document row, proportion/distribution dimensions and outputs; manager composition/comprehensive-review recipes | Supported indirectly. No consolidated overall objective or requested conclusion; R-001. |
| Reader, purpose, genre and hard constraints | Writing brief procedure 1–5; manager task decisions | Explicit. A user limit is a constraint, not a generic quality measure. |
| Structural repair and supported development | Structural revision procedure 2–8; draft development and its missing-content order | Explicit preservation and development boundaries. Add only a small connection from the new diagnosis to these existing remedies. |
| Concision and summaries | Manager recipe at line 95; professional-writing executive-summary criteria | Explicit shorter-output path. A request to assess size must not silently become a summary request. No actual misrouting was observed. |
| Revision fidelity and affected rechecks | Revision check procedure 1–9 | Explicit protection against omissions and meaning shifts. Connect any new size-related diagnosis to affected rechecks without another whole-document audit. |
| Outline granularity and appropriate detail | Outline context exploration, generation step 4 and outline review evaluative steps 4–6 | Strong explicit coverage. No need to impose prose length on an outline or equal branch depth. |
| Genre-specific indispensable detail | Software procedures/docstrings, scientific methods/results and professional decision support | Explicit. Preserve material needed for reproducibility, task completion and informed decisions. |
| Global size targets | Composition analysis scope; style application/checklist; SPEC composition requirement | Already rejects quota-based diagnosis. Retain this safeguard. |

The generic composition route is available from the entry and selected by the manager's composition/comprehensive-review recipes. A size assessment is therefore possible today. Improving its visibility and explicit completion evidence is a refinement, not a missing standalone capability.

## Canonical finding

### R-001 — Make document proportionality an explicit, scoped review objective

| Field | Assessment |
| --- | --- |
| Type and priority | Coverage clarification/recommendation; medium implementation priority for the requested improvement, not a blocking defect. |
| Confidence | High about the textual coverage distinction; behavioral impact unmeasured. |
| Baseline evidence | `references/composition-analysis.md:5,13–18,25–28,37–44,48,54`; `references/manager.md:24–30,87–95`; `docs/dev/CAPABILITY_MAP.md:129–165`; SPEC required composition behavior. |
| Observation | Local redundancy, development, proportion and reader burden are well covered. The document-level diagnostic row does not explicitly connect total extent and detail to scope/substance, and the outputs/completion wording does not explicitly request an overall proportionality judgment when that is the review's objective. |
| Consequence | A reviewer may report local wordiness or overlap without answering whether the document as a whole is appropriately sized for its job. This is a plausible omission risk inferred from the instructions, not an observed failed task. |
| Bounded correction | Keep composition analysis as the diagnostic owner. Name the objective, explain how to ground it in contribution/development and reading context, and return a proportionate conclusion when requested. Add only the necessary routing and affected-recheck reminders. |
| Meaning and scope protections | Do not require every focused edit to audit document size. Do not equate repetition with waste, length with overload or shortness with incompleteness. Do not delete essential content or invent missing support. |
| Objective recheck | Source and later consumer cases distinguish excess, legitimate detail, inadequate development, useful recurrence, excerpt limits and review-only scope; each substantive diagnosis has located evidence and a bounded remedy. |
| Disposition | Verified for the accepted clarification under V-001 through V-004. [REVISION-REPORT.md](REVISION-REPORT.md) retains source checks, fixed prompts and actual outputs; original coverage observation remains unchanged. |

The related routing/remedy/verification changes share this cause and are not inflated into separate findings. Existing wordiness, duplication and fidelity safeguards need preservation, not replacement.

## Source coverage and limits

All 21 runtime Markdown files were considered for this subject. Central workflow/criteria texts were read across this and the immediately preceding source inspection against the same unchanged baseline; supporting modules received subject-focused inspection of purpose, relevant procedure clauses and completion/interface boundaries. This is comprehensive coverage of the selected concern, not a new all-purpose review of every instruction.

| Runtime file | Assessed depth and subject contribution |
| --- | --- |
| `SKILL.md` | Entry/routing/effects: composition route, focused selection, no unrequested rewrite. |
| `references/manager.md` | Complete subject pipeline: decisions, selection, recipes, consolidation, stop and delivery. |
| `references/writing-brief.md` | Purpose/audience/genre/constraints and authority; no new intake needed. |
| `references/material-assessment.md` | Focused triage/interface inspection: duplicates, maturity and excerpt boundaries. |
| `references/style-guidelines.md` | Complete shared criteria: wordiness, recurrence, length heuristics, relevant-only checklist and handoffs. |
| `references/composition-analysis.md` | Complete diagnostic owner and outputs; primary R-001 location. |
| `references/composition-exploration.md` | Complete alternatives/trade-offs: length, evidence, audience and reader burden. |
| `references/outline-context-exploration.md` | Complete contextual scope, detail, repetition and representation criteria. |
| `references/outline-generation.md` | Complete granularity, purposeful combinations/splits and scoped completeness. |
| `references/outline-review.md` | Complete evaluative/validation selection, duplicates, detail and source limits. |
| `references/argument-review.md` | Focused preservation/interface inspection: necessary reasoning is not disposable length. |
| `references/evidence-review.md` | Focused support/qualification inspection: shortening cannot manufacture support or hide uncertainty. |
| `references/source-research.md` | Focused scope/evidence boundary: no source retrieval needed to assess supplied prose size. |
| `references/structural-revision.md` | Complete repair procedure: combine/split/reorder/develop, preserve indispensable content. |
| `references/draft-development.md` | Complete development/missing-content procedure: fill supported explanation, flag missing substance. |
| `references/language-revision.md` | Complete local repair owner: remove empty phrasing while retaining substantive meaning. |
| `references/terminology-consistency.md` | Focused preservation/interface inspection: repeated technical terms and distinct concepts. |
| `references/software-documentation.md` | Focused genre/detail/interface inspection: reader task, prerequisites, appropriate docstring detail. |
| `references/scientific-writing.md` | Focused genre/detail/interface inspection: reproducibility, uncertainty and summary fidelity. |
| `references/professional-writing.md` | Focused genre/detail/interface inspection: decision needs, concise explanations and summaries. |
| `references/revision-check.md` | Complete comparison owner: requested changes, omissions, protected material and affected dependencies. |

Current governing/documentation coverage: SPEC and PLAN were read; capability-map decomposition, composition/style policy and mirrored recipes were inspected for this subject; README scope/use/example/status wording was checked against the selected concern. The map already supplies substantial explicit coverage, supporting a narrow refinement rather than a new workflow.

Excluded: optional YAML/SVG presentation content, unrelated format/brand assessment, historical trials and closed campaign contents. Presentation does not supply the editorial criterion in question. The existing checker is used only for authored-record/current-source structural checks; it cannot judge proportionality.

## Source-level contrasts and future acceptance

These are analyst comparisons of current instructions with case types, not consumer-run outputs.

| Case type | Current coverage assessment | Planned recheck |
| --- | --- | --- |
| Verbose paraphrase or repeated explanation | Already covered by language/style and composition distribution. | Detect semantic duplication with locations; preserve any distinct qualification. |
| Long text with distinct necessary functions | Protected by purpose, genre, scope and anti-quota rules. | Give a reasoned appropriate-size conclusion when supported. |
| Short complete warning | Explicitly protected by style and composition examples. | Retain brevity; do not add filler. |
| Thin procedure missing prerequisites or recovery | Existing completeness and genre checks identify missing substance. | State actual missing needs without inventing operational details. |
| Recurring prerequisite in independently read units | Useful repetition is protected; reading boundary is already recognized. | Keep necessary local guidance; consolidate only redundant explanation. |
| Minor detail dominates a decision document | Existing proportion and reader-burden checks apply. | Relate space/detail to the decision and genre rather than visual balance. |
| Supplied excerpt only | Existing inspection limits apply. | Restrict size judgment to the excerpt; identify missing whole-document context. |
| Assess size versus shorten or summarize | Existing authority and recipe selection distinguish tasks. | Review-only findings and a bounded assessment; no automatic rewritten summary. |
| Explicit hard length limit | Writing brief retains the constraint; fidelity rules protect essentials. | Explain material trade-offs/conflicts rather than silently delete required meaning. |
| Size-related authorized revision | Existing revision comparison protects content. | Recheck the diagnosed issue and affected dependencies, not every unchanged claim. |

## Verification and persistence

Opening checkpoint `df6774d3a6a33fca5342c457309b9c5460752b0a` was published and remote readback matched before U-001. The reviewed runtime and current governing sources remained unchanged throughout assessment.

Final checks on the authored candidate:

| Check | Actual result and limit |
| --- | --- |
| Existing repository checker on bounded fixture | Exit 0: 35 copied current files, 20 references and 169 local Markdown links; zero errors. Three linked historical files were empty existence-only placeholders. Historical contents/anchors were not validated. |
| Runtime/current-source preservation | No diff from the reviewed baseline in the skill, README, governing SPEC/map/PLAN, root orientation/disclosure/attribution or checker. |
| Historical preservation | No diff in campaign 001, historical reviews, revision plans or validation records. Path/object comparison only; contents were not loaded as current review inputs. |
| Authored Markdown | Heading/list separation, list-marker spacing and indentation checks passed; prose, tables, blockquote and companion navigation inspected. |
| Whitespace and staged scope | Worktree check passed; staged checks and owned-path inspection are required immediately before the containing commit. |

The containing assessment/plan commit and its remote readback establish publication identity. These checks do not establish observed editing behavior or verify the proposed future scenarios. No fresh package-conformance or client result is claimed from the record-only change.

## Revision handoff

The proposed plan keeps the diagnostic owner, repairs only the missing explicit connection, and preserves existing semantic safeguards. No new reference/module, forced shortening, broad terminology rewrite, token budget or automatic full-audit requirement is justified.

The original review/planning checkpoint was followed by user-authorized revision. R-001 now has the verified disposition above. Main integration, installation and campaign closure are not inferred from source revision; their actual state is distinguished in the revision report.
