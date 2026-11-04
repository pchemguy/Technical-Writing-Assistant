# Independent source review — Entry, coordination, evidence, outlines, and genre modules

- Reviewer: independent subagent `83f9ac52-54f8-4d2b-bdd2-836f2467c1a6` (`Evidence and outline source reviewer`).
- Reviewed baseline: `f2000eeb61b125dd1efca421926cffd11545b4a3` (runtime tree `02b47f96efd08fd23d1e12259c9d532dd4dcd69d`).
- Criteria focus: C-001 (entry and coordination), C-004 (evidence), C-005 (outlines and genres), and module contract across all 20 references.

## 1. Files read in full (with line counts)

### Governing and routing sources

- `docs/dev/SPEC.md` — 27 lines
- `docs/dev/CAPABILITY_MAP.md` — 308 lines
- `technical-writing-assistant/SKILL.md` — 52 lines

### Assigned reference files (10 files, all read in full, line by line)

1. `technical-writing-assistant/references/manager.md` — 128 lines
2. `technical-writing-assistant/references/argument-review.md` — 35 lines
3. `technical-writing-assistant/references/evidence-review.md` — 38 lines
4. `technical-writing-assistant/references/source-research.md` — 37 lines
5. `technical-writing-assistant/references/outline-context-exploration.md` — 37 lines
6. `technical-writing-assistant/references/outline-generation.md` — 35 lines
7. `technical-writing-assistant/references/outline-review.md` — 77 lines
8. `technical-writing-assistant/references/software-documentation.md` — 46 lines
9. `technical-writing-assistant/references/scientific-writing.md` — 36 lines
10. `technical-writing-assistant/references/professional-writing.md` — 42 lines

### Additional peer reference files read in full (to verify both sides of consequential handoffs)

- `technical-writing-assistant/references/writing-brief.md` — 34 lines
- `technical-writing-assistant/references/material-assessment.md` — 34 lines
- `technical-writing-assistant/references/style-guidelines.md` — 92 lines
- `technical-writing-assistant/references/composition-analysis.md` — 57 lines
- `technical-writing-assistant/references/composition-exploration.md` — 34 lines
- `technical-writing-assistant/references/structural-revision.md` — 35 lines
- `technical-writing-assistant/references/draft-development.md` — 42 lines
- `technical-writing-assistant/references/language-revision.md` — 36 lines
- `technical-writing-assistant/references/terminology-consistency.md` — 36 lines
- `technical-writing-assistant/references/revision-check.md` — 42 lines

## 2. Per-file coverage summary and findings

### Context file: `technical-writing-assistant/SKILL.md` (52 lines)

- **Coverage checked:** C-001 entry-point routing table (lines 26–46) covering all 19 focused modules plus `references/manager.md` (line 24); direct routing vs. composite coordination; direct evidence-mode selection without initiating a full composite workflow (lines 18, 24); C-004 non-research target acquisition vs. citation/corroboration retrieval and `no-network`/`no-retrieval`/`supplied-content-only` overrides (line 18); C-005 contextual criteria for outlines/maps without a predefined special-case catalogue and no automatic prose expansion (lines 17, 19); delivery and portable-core boundaries (lines 50–52).
- **Result:** No finding.

### 1. `technical-writing-assistant/references/manager.md` (128 lines)

- **Coverage checked:**
    - **C-001:** Scope and boundary (lines 14–16); all 7 task decisions matching `CAPABILITY_MAP.md` (lines 18–32); selection and execution sequence (lines 67–76); all 17 composite workflow recipes matching `CAPABILITY_MAP.md` lines 279–297 verbatim (lines 78–104); step-name mapping to `SKILL.md`'s direct routing table (lines 72, 82); conflict reconciliation, severity by task consequence, justified iteration, return conditions, and non-blocking handoffs (lines 106–114); proportional delivery and verification-status accuracy (lines 116–120).
    - **C-004:** Exactly two evidence modes (`External research and verification` and `Review without external research`, lines 36–58); explicit statement that target acquisition and source inspection are not a third mode (line 48); bounded acquisition of explicitly requested task targets vs. ban on citation-only retrieval/bibliography following/corroboration in non-research mode (line 44); override by `no-network`/`no-retrieval`/`supplied-content-only` restrictions (line 44); unavailable host tool handling without silent mode switching (line 40); separation of the 4 outcome dimensions (`Provenance/access`, `Source-to-claim relationship`, `Researched-claim outcome`, `Criterion outcome`, lines 50–56); exact clarifying question and persistence rules (lines 59–65).
    - **Module contract & composition:** Internal contents links (`#scope-and-boundary` through `#examples-and-failure-handling`, lines 5–12), procedures, examples, failure handling (lines 122–128), and completion criteria.
- **Result:** No finding.

### 2. `technical-writing-assistant/references/argument-review.md` (35 lines)

- **Coverage checked:**
    - **C-004:** Separation of internal reasoning critique from empirical verification (lines 5, 19); charitable reconstruction labeled as inference rather than inserted into the author's argument (line 9); deductive vs. probabilistic inference standards, proportionality, and numerical/unit/denominator compatibility (lines 15–16); handoff to `evidence-review.md` for factual premise assessment and `manager.md#evidence-modes-and-selection` before independent research (line 19); handling unfamiliar premises as verification needs rather than false claims (line 31).
    - **Module contract & composition:** Activation/exclusions (`Scope and authority`, lines 3–5), inputs and missing-input handling (`Inputs and missing information`, lines 7–9), 8-step procedure and change authority (lines 11–20), proportional outputs without unrequested rewriting (lines 22–24), concrete examples/failure handling including preserving calculation factors (lines 26–31), and completion checks (lines 33–35).
- **Result:** No finding.

### 3. `technical-writing-assistant/references/evidence-review.md` (38 lines)

- **Coverage checked:**
    - **C-004:** Ownership of claim-to-support relationships, evidence gaps, and prospective evidence planning across both evidence modes (line 5); mode gate linking to `manager.md#evidence-modes-and-selection` including direct invocation (line 9); target acquisition vs. citation-only retrieval and `no-network`/`no-retrieval`/`pasted-content-only` overrides (lines 11, 32); provenance distinctions (`inspected source content`, `uninspected reference`, `author assertion`, `inference`, `model recollection`, `prospective support`, line 16); source-to-claim outcomes (`supports`, `partially supports`, `contradicts`, `does not address`, plus `not assessed` for unavailable content, line 19); conditional handoff to `source-research.md` in research mode vs. stopping at gap assessment in non-research mode without labeling it completed fact-checking (line 21); separation of the 4 outcome dimensions in outputs (line 26).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/mode gate (lines 7–11), 8-step procedure (lines 13–22), outputs (lines 24–26), 5 concrete examples/failure cases (lines 28–34), and completion checks (lines 36–38).
- **Result:** No finding.

### 4. `technical-writing-assistant/references/source-research.md` (37 lines)

- **Coverage checked:**
    - **C-004:** Execution restricted strictly to `external research and verification` mode (lines 5, 9); return to `evidence-review.md` if external research is prohibited (line 9); distinction from bounded intake target acquisition (line 9); tool-unavailability disclosure without silent mode downgrade (line 9); full-source inspection vs. snippets/titles/abstracts/paywalls (lines 15, 31); ban on reconstructing missing bibliographic metadata from memory (line 16); separate numerical/unit/arithmetic verification (line 18); researched-claim outcomes (`supported`, `partially supported`, `contradicted`, `unresolved` within scoped inspected evidence) kept distinct from provenance and per-source relationships (line 20); security/authority boundaries against credentials or instructions in source webpages (line 33).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/prerequisites (lines 7–9), 9-step procedure (lines 11–21), outputs (lines 23–25), examples/failure handling (lines 27–33), and completion checks (lines 35–37).
- **Result:** No finding.

### 5. `technical-writing-assistant/references/outline-context-exploration.md` (37 lines)

- **Coverage checked:**
    - **C-005:** Contextual exploration for generic and unfamiliar specialized outlines/maps without a fixed profile catalogue (lines 5, 18, 24, 37); activation only when representation choices are consequentially unresolved (lines 5, 15, 32); lightweight working contract in ordinary prose/Markdown covering purpose/audience, source authority/limits, elements/relationships, fields/representation, scope/exclusions, and completeness/consistency/usefulness checks (line 18); non-hierarchical representations (tables, relationship maps, combinations, lines 16, 30); boundary with `composition-exploration.md` and `writing-brief.md` (lines 9, 26); handoff to `outline-generation.md` or `outline-review.md` (line 20).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/missing-info handling (lines 7–9), 8-step procedure (lines 11–20), outputs/boundaries (lines 22–26), examples/failure handling including skill capability map derivation (lines 28–33), and completion checks (lines 35–37).
- **Result:** No finding.

### 6. `technical-writing-assistant/references/outline-generation.md` (35 lines)

- **Coverage checked:**
    - **C-005:** Generation from brief, notes, documents, or project materials using contextual criteria without a special-case catalogue or automatic prose expansion (lines 5, 9, 35); classification of source-derived content, inference, proposed additions, and unresolved questions, plus evidence-backed status distinctions (`declared`, `described`, `implemented`, `tested`, lines 14, 28); support for hierarchies, tables, and cross-cutting relationship maps without inventing dependencies (lines 15, 29); first-pass self-check and shared-inspection handoff to `outline-review.md` (line 20) and `draft-development.md` when prose is authorized (line 24).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/missing-info handling (lines 7–9), 8-step procedure (lines 11–20), outputs/handoffs (lines 22–24), examples/failure handling (lines 26–31), and completion checks (lines 33–35).
- **Result:** No finding.

### 7. `technical-writing-assistant/references/outline-review.md` (77 lines)

- **Coverage checked:**
    - **C-005:** Selectable coverage table (`Evaluative only`, `Validation only`, `Comprehensive`) with explicit bans on unsolicited cross-mode reporting and consolidation of shared findings (lines 21–27, 60, 67); shared intake inventory (lines 31, 46); evaluative dimensions (lines 33–42); validation checks including structural validity, source fidelity, requirement coverage, and cross-view consistency (lines 44–52); non-hierarchical relationships, uneven branch depth, and valid vs. defective cycles ("A cycle is a defect only when the relationship requires acyclicity", lines 47, 72); criterion outcomes (`satisfied`, `partly satisfied` only for identifiable subparts, `failed`, `not assessable`, and `not applicable` only when genuinely outside scope, line 51); separation of criterion outcomes from provenance, source-to-claim support, and researched-claim outcomes (line 54); explicit distinction between topic presence, explanatory adequacy, and explicit content-note requirements (line 66); handoffs to `outline-context-exploration.md`, `outline-generation.md`, and `revision-check.md` (lines 29, 62).
    - **Module contract & composition:** Internal contents links (lines 5–11), activation/authority (lines 13–15), inputs/coverage (lines 17–31), dual procedures (lines 33–54), outputs/repairs (lines 56–62), 8 concrete examples/failure cases (lines 64–73), and completion checks (lines 75–77).
- **Result:** No finding.

### 8. `technical-writing-assistant/references/software-documentation.md` (46 lines)

- **Coverage checked:**
    - **C-005:** Coverage of READMEs, tutorials/procedures, API references, architecture documents, and docstrings (lines 5, 28–36); strict boundary against implementing software, executing commands without separate authorization, or claiming tested behavior from static inspection (lines 5, 9, 16, 19, 40–42, 46); interface-to-implementation comparison (line 15); docstring maintenance rules preserving declared/established project conventions with Google style as the Python default only when no governing convention exists (lines 22–26, matching `SPEC.md` line 18); handoffs to `composition-analysis.md`, `terminology-consistency.md`, `language-revision.md`, and `revision-check.md` (lines 17, 20); evidence-mode governance for external API docs (line 42).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/missing-info handling (lines 7–9), procedure + docstring maintenance + genre table (lines 11–36), outputs/examples/failure handling (lines 38–42), and completion checks (lines 44–46).
- **Result:** No finding.

### 9. `technical-writing-assistant/references/scientific-writing.md` (36 lines)

- **Coverage checked:**
    - **C-005:** Coverage of scientific explanations, manuscripts, methods, results, discussions, abstracts, and summaries (lines 5, 11–20); strict prohibition against inventing methods, calibration details, results, statistical significance, effect sizes, confidence intervals, p-values, ethical approvals, or journal requirements (lines 5, 9, 15, 16, 24, 28–32, 36); separation of observation from interpretation and association from causation (line 17); preservation of passive voice when appropriate to foreground a procedure (line 31); handoffs to `argument-review.md`, `evidence-review.md`, composition/language/terminology workflows, and `revision-check.md` (lines 18, 20).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/missing-info handling (lines 7–9), 8-step procedure (lines 11–20), outputs (lines 22–24), 5 examples/failure cases (lines 26–32), and completion checks (lines 34–36).
- **Result:** No finding.

### 10. `technical-writing-assistant/references/professional-writing.md` (42 lines)

- **Coverage checked:**
    - **C-005:** Coverage of reports, proposals, decision briefs, technical correspondence, and executive summaries (lines 5, 22–30); separation of facts, analysis, recommendations, requests, and commitments (line 14); strict prohibition against inventing organizational positions, promises, approvals, commercial terms, responsibilities, deadlines, or legal/medical/financial conclusions, and against sending/publishing a draft (lines 5, 9, 15, 16, 34–38, 42); preservation of essential reasoning, assumptions, and numerical factors in shorter memos and executive summaries (lines 18, 30, 36); handoffs to `composition-analysis.md`, `structural-revision.md`, `language-revision.md`, and `revision-check.md` (lines 18, 20).
    - **Module contract & composition:** Activation/authority (lines 3–5), inputs/missing-info handling (lines 7–9), 8-step procedure + genre table (lines 11–30), outputs/examples/failure handling (lines 32–38), and completion checks (lines 40–42).
- **Result:** No finding.

## 3. Detailed findings

**0 defects, 0 recommendations, and 0 optional-preference findings.** All 10 assigned files and `SKILL.md` satisfy `SPEC.md`, `CAPABILITY_MAP.md`, C-001, C-004, C-005, and the Module Contract without defects.

## 4. Cross-file observations and handoff verification

1. **Intentional, self-consistent recurrence of evidence-mode and outcome-distinction rules (C-004):**
    - `manager.md` (lines 34–65) is the canonical owner of the two evidence modes, the mode-selection question, the target-acquisition vs. corroborating-retrieval boundary, and the 4 outcome dimensions (`Provenance/access`, `Source-to-claim relationship`, `Researched-claim outcome`, `Criterion outcome`).
    - Because `SKILL.md` (line 24) and `SPEC.md` (line 10) allow focused modules to execute independently without loading the full manager workflow, `SKILL.md` (line 18), `evidence-review.md` (lines 9–11, 26), `source-research.md` (lines 9, 20), and `outline-review.md` (line 54) each include a concise operational summary of their slice of those rules while linking to `manager.md#evidence-modes-and-selection`.
    - Across all five files, the terminology, outcome labels, target-acquisition boundaries, and `no-network`/`no-retrieval`/`supplied-content-only` overrides are completely consistent and free of conflict.
2. **Both sides of consequential handoffs verified:**
    - **Direct evidence-mode gate (`SKILL.md` / focused modules ↔ `manager.md#evidence-modes-and-selection`):** `SKILL.md` line 24, `writing-brief.md` line 19, `argument-review.md` line 19, `evidence-review.md` line 9, `source-research.md` line 9, and `outline-review.md` line 54 all link to `manager.md#evidence-modes-and-selection` (resolving to `manager.md` line 34), which explicitly permits direct evidence invocation to load only that section (`manager.md` line 16).
    - **Reasoning vs. support vs. retrieval (`argument-review.md` ↔ `evidence-review.md` ↔ `source-research.md` ↔ `composition-analysis.md` / `draft-development.md` / `structural-revision.md`):**
        - `composition-analysis.md` (line 53), `structural-revision.md` (line 19), `draft-development.md` (line 15), and `scientific-writing.md` (line 18) hand reasoning issues to `argument-review.md` and support issues to `evidence-review.md`.
        - `argument-review.md` (line 19) hands empirical premise checks to `evidence-review.md`.
        - `evidence-review.md` (lines 5, 21) and `source-research.md` (lines 9, 20) have symmetric handoffs for research-mode retrieval and return of claim outcomes with provenance and limitations.
    - **Outline/map lifecycle (`outline-context-exploration.md` ↔ `outline-generation.md` ↔ `outline-review.md` ↔ `composition-exploration.md` / `draft-development.md` / `revision-check.md`):**
        - `outline-context-exploration.md` (lines 20, 26) hands off to `outline-generation.md`, `outline-review.md`, and coordinates with `composition-exploration.md` (which reciprocally links back at line 19).
        - `outline-generation.md` (lines 9, 20, 24) links to `outline-context-exploration.md`, `outline-review.md`, and `draft-development.md` (which reciprocally links back at line 14).
        - `outline-review.md` (line 62) links to `outline-generation.md` and `revision-check.md`; reciprocally, `revision-check.md` (line 24) links to `outline-review.md#validation-checks` (resolving to `outline-review.md` line 44).
    - **Genre workflows (`software-documentation.md`, `scientific-writing.md`, `professional-writing.md` ↔ editorial & check modules):**
        - All three genre modules hand off to composition, language, terminology/structural workflows and `revision-check.md`; reciprocally, `manager.md` (line 71 and recipes 4, 9, 11, 12), `terminology-consistency.md` (line 20, linking to `software-documentation.md`), and `revision-check.md` (lines 19, 24, 36, 38) check genre-specific execution, analysis, and commitment fidelity.
    - **Minor non-defect stylistic variations noted across files:**
        - In `scientific-writing.md` line 20 (`Apply selected composition, language, and terminology workflows`), those three modules are named in plain text without Markdown hyperlinks, whereas `software-documentation.md` line 17 and `professional-writing.md` line 18 hyperlink them. All three are directly linked in `SKILL.md`'s routing table, so navigation is unaffected.
        - In `manager.md` line 97 (Recipe 10, `Concision or executive summary`: `Identify indispensable content → select emphasis/structure → compress or develop summary → revision check`), the first three steps describe functional stages (matching `CAPABILITY_MAP.md` line 290 verbatim) rather than literal module names, which is explicitly covered by `manager.md` line 72 (`Choose a recipe below or construct a smaller sequence`).

## 5. Uncertainties and anything not assessed

- Per instructions, this was a strictly read-only static source review of the skill files at commit `f2000eeb61b125dd1efca421926cffd11545b4a3`. No live web search/fact-checking, package validation script execution, or multi-model runtime trial execution was performed, and historical records under `docs/dev/reviews/`, `docs/dev/validation/`, `docs/dev/revision_plans/`, `docs/dev/REVIEW.md`, `docs/dev/REVISION_REVIEW.md`, and `.agents/` were not read.
