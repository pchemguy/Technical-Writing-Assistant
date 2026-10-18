# Fresh consumer-task evidence

## Provenance and scope

- Campaign: `001_dead567`; reviewed baseline: `dead5674000dfe9ee77b239f935f639937c38405`.
- Date: 2026-10-18.
- Consumer: fresh agent context `/root/consumer_tasks_oct18`; one context containing five requests, sampled once.
- The consumer received the prompt below without the coordinator's findings, expected answers or prior trial outputs.
- The coordinator packaged this returned evidence afterward. The consumer did not write this file.
- These are bounded supplied-input observations, not installation, client activation, live research, repeated experiments or evidence of improvement after a change.
- No model-version claim is made. Task-specific evidence and effect restrictions were independent.

## Exact task prompt

```text
Use Technical Writing Assistant at /workspace/scratch/843c75a4f4c3/Technical-Writing-Assistant/technical-writing-assistant to handle these five ordinary user requests. Start with SKILL.md and load only relevant resources; respect current root AGENTS.md for repository reads. Do not read any campaign report, old review/revision document, validation history, or Git history. No external retrieval, file writes, code execution, Git mutations, sending or publishing. Return actual requested outputs numbered 1–5, followed by resources read, actions and limits. Treat task-specific evidence instructions independently.
1. Review only, without research or rewriting. Documentation: `dispatch(items)` returns a count and processes the entire batch atomically. Supplied definition: `def dispatch(run_id, items):` iterates items, calls write(row) then commit() for each row, and returns None. No other code is supplied.
2. Using supplied contents only, assess the claim 'energy use fell 25%'. Supplied excerpt says 'processing time fell 25%'. A reference https://example.invalid/energy is supplied with no contents. Explicit requirement: supplied material must include comparative energy measurements. Return findings only.
3. Review composition only, no research or rewriting. Standalone instruction A: 'Follow the approach agreed in the previous revision.' No revision is identified or supplied. Instruction B: 'Use the format specified in Section 2.' Section 2 is supplied and says 'Use a two-column table: issue and remedy.' Warning C: 'Do not open the pressurized chamber.'
4. Review this outline for quality and source fidelity, no research or rewriting. Methods contains a description of tests on 18 units; Results contains the reported measurements; Reliability contains only installation instructions. Supplied source descriptions match those contents, and no other reliability information is provided. No rule requires specially descriptive section titles.
5. First develop clean short status text from these notes without research: '18 units tested under condition B; perhaps lower losses; possible Q2 launch; budget unapproved; management proposes Q2; no cost estimate.' Then, as a separate findings-only revision comparison, compare source '18 of 30 samples improved under B. Estimate = 3 kg × 0.25 × F; F is unverified' with revision 'Samples improved. Estimate = 3 kg × F.'
```

## Exact returned output

```markdown
1. The documentation conflicts with the supplied definition in three places:

   - **Signature:** `dispatch(items)` omits the required `run_id` parameter in `dispatch(run_id, items)`.
   - **Return value:** The documentation promises a count; the supplied definition returns `None`.
   - **Atomicity:** Calling `commit()` for each row does not substantiate an all-or-nothing batch guarantee. The documented guarantee conflicts with the described transaction boundaries. Without the implementations of `write` and `commit`, failure and rollback behavior cannot be established.

2. The supplied excerpt reports a **25% reduction in processing time**, which does not address the claimed reduction in energy use. The referenced URL has no supplied contents and remains uninspected; its support is **not assessed**. The explicit requirement for comparative energy measurements is **not satisfied**. The energy claim remains unsupported by the available material, rather than disproved.

3. **Instruction A:** “The approach agreed in the previous revision” has no identifiable, available referent. A standalone reader cannot determine the required approach. Supply the operative approach or identify and provide the necessary revision; its contents cannot be inferred.

   **Instruction B:** The reference resolves to the supplied Section 2, which specifies the table format. No missing-context defect is evident.

   **Warning C:** The prohibition is direct and understandable. No composition defect is evident from the supplied sentence.

4. **Methods and Results:** Their conventional headings accurately describe their supplied contents. No quality defect follows merely from their general wording. Source fidelity is satisfied within the supplied descriptions.

   **Reliability:** The heading promises reliability information, but its contents provide installation instructions. This mismatch misdirects readers and fails heading/content alignment. Retitling or relocating the installation material is an appropriate repair. The installation content itself matches its source description; no supplied reliability evidence justifies developing reliability claims. Broader completeness cannot be assessed from these descriptions alone.

5. **Clean status text**

   Eighteen units were tested under condition B. Lower losses are possible but unconfirmed. Management proposes a Q2 launch, with timing still tentative. The budget is unapproved, and no cost estimate is available.

   **Separate revision-comparison findings**

   - “Samples improved” omits **18 of 30** and **under B**, obscuring the proportion and condition and potentially suggesting improvement across all samples.
   - The revised equation omits the material factor **0.25**. For the same `F`, it produces four times the source expression’s value.
   - The revision removes the qualification that **`F` is unverified**, concealing uncertainty in the estimate.

Resources read: repository-root `AGENTS.md`; the requested package’s `SKILL.md`; and `references/software-documentation.md`, `evidence-review.md`, `composition-analysis.md`, `outline-review.md`, `draft-development.md`, and `revision-check.md`.

Actions and limits: Read the selected instructions and applied them separately to the five supplied cases. Used file discovery and text-reading commands only. No external retrieval, application-code or test execution, file writes, Git operations, sending, or publishing. No campaign reports, previous review/revision documents, validation history, or Git history were read. Findings rely exclusively on the supplied task evidence; only the status-text request authorized drafting.
```

## Assessment boundary

The report classifies these observations as SC-001 through SC-005. A successful small example does not establish reliability across all inputs. SC-006 concerns separately executed structural fixtures, not this consumer's actions.
