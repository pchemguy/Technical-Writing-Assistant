# Independent source review — Core intake, style, composition, revision, and check modules

- Reviewer: independent subagent `375b8163-6b7c-43f9-a186-b34ac6aac6f3` (`Editorial modules source reviewer`).
- Reviewed baseline: `f2000eeb61b125dd1efca421926cffd11545b4a3` (runtime tree `02b47f96efd08fd23d1e12259c9d532dd4dcd69d`).
- Criteria focus: C-002 (editorial composition) and C-003 (development and fidelity), plus module contract and cross-file handoff consistency.

## 1. Files read in full (with line counts)

### Governing and routing context

- `docs/dev/SPEC.md` — 28 lines (27 non-empty/indexed lines)
- `docs/dev/CAPABILITY_MAP.md` — 309 lines (308 indexed lines)
- `technical-writing-assistant/SKILL.md` — 53 lines (52 indexed lines)
- `technical-writing-assistant/references/manager.md` — 129 lines (128 indexed lines)

### Assigned reference modules

1. `technical-writing-assistant/references/writing-brief.md` — 34 lines
2. `technical-writing-assistant/references/material-assessment.md` — 34 lines
3. `technical-writing-assistant/references/style-guidelines.md` — 92 lines
4. `technical-writing-assistant/references/composition-analysis.md` — 57 lines
5. `technical-writing-assistant/references/composition-exploration.md` — 34 lines
6. `technical-writing-assistant/references/structural-revision.md` — 35 lines
7. `technical-writing-assistant/references/draft-development.md` — 42 lines
8. `technical-writing-assistant/references/language-revision.md` — 36 lines
9. `technical-writing-assistant/references/terminology-consistency.md` — 36 lines
10. `technical-writing-assistant/references/revision-check.md` — 42 lines

## 2. Per-file coverage summary and findings

### 1. `references/writing-brief.md` (34 lines)

- **Coverage summary:** Checked activation conditions and exclusions (`## Scope and authority`, line 5, skipping separate intake for self-contained corrections and avoiding questionnaires); inputs and missing-input handling (`## Inputs and missing information`, line 9, asking when text is absent rather than reconstructing from a title, scoping to supplied excerpts); 8-step procedure (`## Procedure`, lines 13–20, covering objective, audience, genre/dialect/register, source authority/conflicts, revision authority boundaries, materiality threshold for questions, non-blocking execution of independent work, and delegation of evidence-mode selection to `manager.md#evidence-modes-and-selection`); outputs and handoffs (`## Outputs and handoffs`, line 24, routing to `material-assessment.md` and `outline-context-exploration.md` without routine approval gates); examples/failure handling (`## Examples and failure handling`, lines 28–30); completion checks (`## Completion checks`, line 34); C-002 composition and C-003 fidelity alignment with `SPEC.md`, `CAPABILITY_MAP.md` (line 57), `SKILL.md` (line 28), and `manager.md` (line 32).
- **Result:** No finding.

### 2. `references/material-assessment.md` (34 lines)

- **Coverage summary:** Checked triage scope and exclusions (`## Scope and authority`, line 5, distinguishing readiness triage from exhaustive review or rewriting per `SPEC.md` line 16 and `CAPABILITY_MAP.md` line 58); inputs and excerpt boundary handling (`## Inputs and missing information`, line 9, inventorying inspected material and not treating absence from an excerpt as absence from the full document); 7-step triage procedure (`## Procedure`, lines 13–19, covering maturity classification, content separation, basic integrity and prompt-injection safeguard in source text on line 15, representative sampling, flagging apparent substantive/numerical conflicts without claiming unperformed external verification on line 17, consequence-based prioritization, and smallest-next-workflow recommendation); outputs and handoffs (`## Outputs and handoffs`, line 23, routing to `composition-analysis.md`, `argument-review.md`, `evidence-review.md`, and `writing-brief.md`); examples/failure handling (`## Examples and failure handling`, lines 27–30); completion checks (`## Completion checks`, line 34).
- **Result:** No finding.

### 3. `references/style-guidelines.md` (92 lines)

- **Coverage summary:** Checked shared-guidance role (`## Scope and boundary`, line 5, supplying shared criteria rather than pretending to be an independent transformation workflow, per `CAPABILITY_MAP.md` lines 59 and 233); inputs/outputs (`## Inputs and outputs`, line 9, user requirements taking precedence over defaults); 5-step application procedure for selective or direct invocation (`## Application procedure`, lines 13–17); all 7 guidance subsections and the 10-item verification checklist (`## Guidance`, lines 23–78, matching `CAPABILITY_MAP.md` lines 172–227 verbatim, including contextual qualifications on contractions, stable technical terminology over synonym variation, list parallelism, sentence/paragraph length heuristics as diagnostic signals rather than quotas, sound topic sentences with brief warning/transition exceptions, active/passive voice judgment, and collocations); optional handoffs (`## Optional handoffs`, line 82, to `language-revision.md`, `terminology-consistency.md`, `composition-analysis.md`, `structural-revision.md`, and `revision-check.md`); examples and completion criteria (`## Examples and completion criteria`, lines 86–92, including protection against silent claim changes on line 90).
- **Result:** No finding.

### 4. `references/composition-analysis.md` (57 lines)

- **Coverage summary:** Checked diagnostic scope and non-rewriting boundary (`## Scope and authority`, line 5); inputs and excerpt limits (`## Inputs and missing information`, line 9); 7-step diagnostic procedure (`## Procedure`, lines 13–19, lightweight mental/written reverse outline, trajectory vs reader needs, multi-level inspection, remedies tied to reader consequence without length-quota splitting, genuine logical transitions vs missing premises, consolidation, and handoffs to `composition-exploration.md` and `structural-revision.md`); 4-level table and 12 cross-level diagnostic dimensions (`## Diagnostic dimensions`, lines 23–45, including `Size and level of detail` on line 32 and `Contextual references and standalone completeness` on line 36, plus expository topic-sentence default and justified exceptions on line 45); outputs and failure handling (`## Outputs and failure handling`, lines 49–53, including reasoned size/detail assessment within inspected boundaries on line 51 and handoffs to `argument-review.md` and `evidence-review.md` on line 53); completion checks (`## Completion checks`, line 57). Verified full compliance with `SPEC.md` line 13 and `CAPABILITY_MAP.md` lines 60 and 128–167.
- **Result:** No finding.

### 5. `references/composition-exploration.md` (34 lines)

- **Coverage summary:** Checked scope and authority (`## Scope and authority`, line 5, exploring materially distinct compositional approaches before major restructuring or drafting without manufacturing support or silently altering authorial position, per `CAPABILITY_MAP.md` lines 61 and 124); inputs and missing-information handling (`## Inputs and missing information`, line 9, reusing `writing-brief.md`); 7-step procedure (`## Procedure`, lines 13–19, communication problem vs topic list, separating central claims/context/support/qualifications, context-appropriate organizing principles as non-exhaustive examples, 2–3 materially distinct options with foregrounded/combined/deferred/omitted elements, trade-off comparison, reasoned recommendation with author-decision boundary for position/commitment changes, and handoffs to `structural-revision.md`, `draft-development.md`, `outline-context-exploration.md`, and `outline-generation.md`); outputs (`## Outputs`, line 23); examples/failure handling (`## Examples and failure handling`, lines 27–30); completion checks (`## Completion checks`, line 34).
- **Result:** No finding.

### 6. `references/structural-revision.md` (35 lines)

- **Coverage summary:** Checked scope and authority (`## Scope and authority`, line 5, implementing authorized changes to arrangement, boundaries, hierarchy, headings, transitions, and supporting-material placement without inventing facts or silently changing arguments, per `CAPABILITY_MAP.md` line 68); inputs and source inventory retention (`## Inputs and missing information`, line 9); 8-step procedure (`## Procedure`, lines 13–20, covering unit purpose/trajectory, preserving essential reasoning/quantities/caveats/citations/examples/requirements, addressing diagnosed size/detail issues while retaining useful recurrence, reordering prerequisites and keeping qualifications near claims, combining fragments and splitting overloaded units with adequate post-split development and sound topic sentences, honest transitions without fabricated causal links, relocating figures/lists/equations/quotations with updated references and stable identifiers, handing substantive gaps to `draft-development.md`/`argument-review.md`/`evidence-review.md`, and final handoffs to `language-revision.md` and `revision-check.md`); outputs (`## Outputs`, line 24); examples/failure handling (`## Examples and failure handling`, lines 28–31); completion checks (`## Completion checks`, line 35).
- **Result:** No finding.

### 7. `references/draft-development.md` (42 lines)

- **Coverage summary:** Checked scope and authority (`## Scope and authority`, line 5, transforming bullets, notes, fragments, or outlines into developed prose without inventing facts, methods, findings, citations, commitments, or authorial positions, and stopping at an outline when only an outline is requested, per `CAPABILITY_MAP.md` line 69); inputs and missing-information handling (`## Inputs and missing information`, line 9, separating source excerpts, author ideas, and provisional hypotheses, reusing `writing-brief.md` and `composition-exploration.md`); 8-step drafting procedure (`## Procedure`, lines 13–20) and dedicated 4-step `## Missing content` decision order (lines 24–27, distinguishing central content/positions from secondary unsupported detail, keeping placeholders or content-needs notices outside clean text when a clean deliverable is requested); outputs (`## Outputs`, line 31); examples/failure handling (`## Examples and failure handling`, lines 35–38, covering small-sample provisional observations, unapproved Q4 launch/budget notes, missing premises, and contradictory figures); completion checks (`## Completion checks`, line 42).
- **Result:** No finding.

### 8. `references/language-revision.md` (36 lines)

- **Coverage summary:** Checked scope and authority (`## Scope and authority`, line 5, improving mechanics, clarity, precision, concision, register, collocations, sentence construction, pronoun references, and voice while preserving claims, certainty, scope, causality, position, obligations, and commitments, per `CAPABILITY_MAP.md` line 70); inputs and ambiguity resolution (`## Inputs and missing information`, line 9, selective use of `style-guidelines.md`); 8-step procedure (`## Procedure`, lines 13–20, reading for meaning first, protecting quotations/code/identifiers/equations/citation locators/standardized expressions, dialect-appropriate mechanics and purposeful fragments, agency/passive voice without inventing unknown actors, collocations and stable technical terms, concision preserving numerical factors/conditions/modality, functional sentence variety handing larger changes to `structural-revision.md`, register/contractions, and separating meaning-changing proposals from wording repairs with handoffs to `terminology-consistency.md` and `revision-check.md`); outputs (`## Outputs`, line 24); examples/failure handling (`## Examples and failure handling`, lines 28–32); completion checks (`## Completion checks`, line 36).
- **Result:** No finding.

### 9. `references/terminology-consistency.md` (36 lines)

- **Coverage summary:** Checked scope and authority (`## Scope and authority`, line 5, reconciling terms, definitions, abbreviations, notation, naming, units, and recurring expressions while distinguishing consistency from technical correctness and avoiding synonym-merging of distinct concepts, per `CAPABILITY_MAP.md` line 71); inputs and inspection boundary reporting (`## Inputs and missing information`, line 9); 8-step procedure (`## Procedure`, lines 13–20, compact terminology record only when useful, authority hierarchy without overriding formal names from memory, distinguishing true variants from distinct concepts such as latency/throughput or accuracy/precision, abbreviation expansion at first relevant use including independently read sections, unit/symbol/variable/code-identifier protection and verified arithmetic for unit conversions, cross-element checking across headings/prose/tables/captions/figures/references, context-sensitive replacement rather than blind global substitution, and handoffs to `evidence-review.md` and `software-documentation.md`); outputs (`## Outputs`, line 24); examples/failure handling (`## Examples and failure handling`, lines 28–32); completion checks (`## Completion checks`, line 36).
- **Result:** No finding.

### 10. `references/revision-check.md` (42 lines)

- **Coverage summary:** Checked comparative scope and authority (`## Scope and authority`, lines 5–7, comparing revised artifacts against source, instructions, and authorized decisions on affected passages and consequential dependencies without repeating a full review or fact-checking every unchanged claim, per `SPEC.md` line 15 and `CAPABILITY_MAP.md` line 75); inputs and special cases (`## Inputs and missing information`, lines 11–13, comparing drafts from notes against those notes and authorized additions without requiring an original prose draft, skipping `revision-check.md` for findings-only work, and disclosing unavailable source comparisons); 9-step procedure (`## Procedure`, lines 17–25, covering requested-change completion, essential content and numerical factors, unintended meaning shifts, protected material and citation-to-claim associations, introduced local defects and size/detail rechecks using `style-guidelines.md`, unavailable-context references introduced by revision or diagnosed in affected material with optional escalation to `composition-analysis.md`, honest evidence/execution reporting, outline validation reuse via `outline-review.md#validation-checks`, and bounded repair within authority); outputs (`## Outputs`, line 29); examples/failure handling (`## Examples and failure handling`, lines 33–38); completion checks (`## Completion checks`, line 42).
- **Result:** No finding.

## 3. Detailed findings

No defects, recommendations, or optional preferences were identified in the 10 assigned files. Every assigned executable reference satisfies the module contract in `SPEC.md` (line 11) and `CAPABILITY_MAP.md` (lines 231–233), `style-guidelines.md` properly operates as a shared criteria reference with a lightweight direct-application procedure, and the prose of all 10 files adheres to the skill's own C-002 editorial composition and C-003 fidelity standards.

## 4. Cross-file observations

1. **Cohesive handoff chain across intake, triage, exploration, revision, drafting, and check (C-003):**
    - **Intake and triage:** `writing-brief.md` (line 24) and `material-assessment.md` (line 23) cleanly divide task definition from material readiness assessment, cross-referencing each other without creating mandatory questionnaires or approval gates. `writing-brief.md` (line 19) delegates evidence-mode selection directly to `manager.md#evidence-modes-and-selection` (verified at `manager.md` line 34).
    - **Diagnosis, exploration, and implementation:** `composition-analysis.md` (line 19), `composition-exploration.md` (lines 9, 19), `structural-revision.md` (lines 13, 19–20), and `draft-development.md` (lines 9, 14–15, 20) maintain crisp authority boundaries: `composition-analysis.md` diagnoses existing composition without rewriting; `composition-exploration.md` develops and compares organizing alternatives when choices exist; `structural-revision.md` rearranges existing material and hands missing substantive content to `draft-development.md`, `argument-review.md`, or `evidence-review.md`; and `draft-development.md` develops early notes or outlines into prose with an explicit 4-step decision order for missing content (`draft-development.md` lines 24–27).
    - **Sentence/term polish and final comparative check:** `structural-revision.md` (line 20), `draft-development.md` (line 20), and `language-revision.md` (line 20) all hand off to `revision-check.md`, which reciprocally handles prose revisions, notes-derived drafts (`revision-check.md` line 11), unavailable sources (`revision-check.md` line 13), and findings-only skip conditions (`revision-check.md` line 13, matching `manager.md` lines 76 and 80).
2. **Consistent protection of meaning, numerical factors, qualifications, and protected expressions:**
    - Protected material (quotations, code, identifiers, equations, citations, standardized expressions, and official names) and substantive invariants (claims, modality/certainty, scope, causality, numerical factors, conditions, commitments, and authorial position) are enforced consistently across `SKILL.md` (line 8), `style-guidelines.md` (lines 5, 13, 90), `structural-revision.md` (lines 14–18, 29), `draft-development.md` (lines 5, 13, 18, 24–27), `language-revision.md` (lines 5, 13, 17, 28, 32), `terminology-consistency.md` (lines 5, 9, 17–18, 30–31), and `revision-check.md` (lines 18–20, 33–36).
3. **Intentional, bounded overlap on unavailable-context references (`composition-analysis.md` line 36 and `revision-check.md` line 22):**
    - Both `composition-analysis.md` (line 36) and `revision-check.md` (line 22) define checks for unresolved contextual references (`"the supplied guidelines"`, `"as agreed earlier"`, `"in the prior/earlier/previous revision"`) at the intended reading boundary while permitting valid references to available drafts, sections, or revisions. This is required by `SPEC.md` lines 13 and 15 and ensures that focused revision workflows (such as `Focused language edit` in `manager.md` line 88, which runs `revision-check.md` without loading `composition-analysis.md`) still catch unavailable-context references introduced during editing. `revision-check.md` line 22 explicitly bounds its check to introduced or affected material and defers deeper diagnosis to `composition-analysis.md`.
4. **Design-to-runtime alignment between `docs/dev/CAPABILITY_MAP.md` and runtime references:**
    - The shared style policy in `CAPABILITY_MAP.md` (lines 172–227) is reproduced in `references/style-guidelines.md` (lines 23–78), as explicitly documented in `CAPABILITY_MAP.md` line 170 ("Its operative defaults and contextual qualifications are stated below and in `style-guidelines.md`"). Within the runtime `technical-writing-assistant/references/` directory, the focused workflow modules link to `style-guidelines.md` rather than duplicating those rules.

## 5. Uncertainties and unassessed scope

- **Peer reference files outside the 10 assigned modules:** To remain strictly within the assigned scope, this subagent did not read the other 9 focused reference files under `technical-writing-assistant/references/` (`outline-context-exploration.md`, `outline-generation.md`, `outline-review.md`, `argument-review.md`, `evidence-review.md`, `source-research.md`, `software-documentation.md`, `scientific-writing.md`, and `professional-writing.md`). Outgoing links from the assigned 10 files to those 9 files were checked from the caller side here and from the callee side by the coordinator and the second source reviewer.
- **Runtime model execution:** Static source inspection verifies instruction clarity, boundaries, and internal consistency, not live execution behavior across models or hosts.
