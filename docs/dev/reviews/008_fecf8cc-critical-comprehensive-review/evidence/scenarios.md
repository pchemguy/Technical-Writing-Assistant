# Source-grounded critical scenario walkthroughs

## Evidence boundary

These eight scenarios were constructed and analyzed inline by the source reviewer after reading the current skill. They are counterexample-oriented applications of the instructions, not raw responses from fresh consumers, independent replications or evidence of observed model/client compliance. No claim of eight passing behavior tests follows. Locations refer to baseline `fecf8cc097c9bccc78c0ac29676d397a1fefaa15`, with paths relative to `technical-writing-assistant/references/`.

## S-001: Size/detail assessment of an approval brief

**Input:** “Review only. Is this brief the right size and detail for operations leads deciding on migration? Background: two pages of organizational history and former tool names. Proposal: switch the queue to database polling. Benefits: 3,600 jobs/minute, approximately 30/second. Risks: some extra load. Rollback: not supplied. Ownership approval: unresolved.”

**Reviewer application:** Diagnose distribution and substantive adequacy, not total word count alone. Historical detail may be trimmed only when it does not explain current dependencies; approval-critical migration assumptions, resource bounds, rollback and ownership need development from actual inputs. The throughput statements are internally incompatible: 3,600/60 = 60 per second, not 30. Ask which measurement is authoritative rather than choose one. Findings-only scope means no rewritten brief and no research unless selected.

**Source basis:** `composition-analysis.md` lines 13–19, 32 and 51; `professional-writing.md` lines 13–20 and 28; `argument-review.md` line 16; `manager.md` lines 61–65, 84 and 91.

**Critical contrast:** An output saying only “too long; cut by half” would fail the functional size/detail policy. An output that expands rollback with a plausible invented procedure would fail missing-input/commitment safeguards. Source instructions cover both contrasts; consumer compliance is untested.

## S-002: Focused editing with protected expression

**Input:** “Language only, keep all code and the quotation verbatim: The worker retry up to 4 times with `retry_cap=4`. The policy says ‘request must not be duplicated’. This may reduce losses in the pilot's two test regions.”

**Reviewer application:** Correct “worker retry” to “worker retries”, retaining `retry_cap=4`, the exact quotation, “may”, pilot status and two-region scope. Do not broaden to all deployments or turn the policy quotation into a grammatically edited paraphrase. A research-mode question is unnecessary for this operation.

**Source basis:** `language-revision.md` lines 13–20, 28 and 32; `terminology-consistency.md` lines 17–19; `revision-check.md` lines 17–23; `manager.md` line 32.

**Critical contrast:** Grammar quality cannot compensate for a changed quotation or certainty. The comparison source is available, so fidelity can be checked without an external-source audit.

## S-003: Customer correspondence from provisional notes

**Input:** “Draft only. Dashboard checks show 2% failures in region A; region B unchecked. Certificate update is one suspected cause. Rollback by Friday is not approved. Next customer update by 16:00 UTC tomorrow. Service credit undecided.”

**Reviewer application:** Draft a bounded update: region A observed, region B unverified, cause suspected, rollback timing unconfirmed. Preserve the supplied next-update deadline and omit any new promise of earlier updates or compensation unless separately authorized. Put unresolved author decisions outside a requested clean customer text; sending is outside drafting authority.

**Source basis:** `professional-writing.md` lines 5, 9, 16, 20 and 34–36; `draft-development.md` lines 13–20 and 24–27; `revision-check.md` lines 18–19 and 36.

**Critical contrast:** Merely saying “we cannot guarantee Friday” does not license promising a different deadline. A source-to-draft commitment check must include innocuous-sounding closing sentences. Current instructions require this, but this campaign has no fresh independent correspondence output to score.

## S-004: Outline requirements with unavailable detailed sources

**Input:** “Validate this outline without redesigning it. Requirements: Windows/Linux installation, every configuration key, troubleshooting and uninstallation. Outline: 1 Installation (1.1 Windows; 1.2 Linux); 2 Configuration; 3 Troubleshooting. Configuration schema and section content are unavailable.”

**Reviewer application:** Installation-platform topics and configuration/troubleshooting topics are represented. Explanatory adequacy and every-key completeness cannot be established from bare headings and an absent schema; do not infer either a complete reference or a definite missing key. Uninstallation has no node in the complete supplied outline and is a located coverage failure. No arbitrary content-note requirement or unsolicited whole-outline replacement is justified.

**Source basis:** `outline-review.md` lines 26, 31, 46–54 and 66–73; `outline-context-exploration.md` lines 18–24.

**Critical contrast:** “Configuration heading exists, therefore complete” is a false pass; “no notes, therefore topic absent” is a false failure. Source instructions explicitly distinguish these questions.

## S-005: Scientific revision meaning and unseen table

**Input:** Original: “Seven of nine samples held at 20 °C declined by 12–18%; decline correlated with respiration. Two showed no measurable change. These observations suggest a contribution under these conditions (Table 3).” Revision: “Samples declined by 12–18 mg/L because of respiration. Two were excluded. This proves a general mechanism (Table 3).” Request: comparison only; Table 3 not supplied.

**Reviewer application:** Flag changed quantity/unit, lost denominator and temperature, null observations recast as exclusions, association promoted to causation, and certainty/scope inflation. The surviving table locator may now attach to altered claims, but its actual contents cannot be called contradictory without inspection. Do not repair the revision when comparison only is requested.

**Source basis:** `revision-check.md` lines 5–13 and 17–24; `scientific-writing.md` lines 15–20; `argument-review.md` lines 15–16.

**Critical contrast:** A comparison does not need external research to detect supplied-text meaning shifts. It cannot certify the unseen table's values. A supplied revised artifact means revision-check is relevant even though the requested deliverable is findings.

## S-006: Role map with nonsequential loops and unresolved ownership

**Input:** “Intake logs an item. Registry assigns its permanent ID from the log before warehouse custody is required. Warehouse accepts only identified items. Assurance audits Warehouse quarterly; Warehouse reports incidents to Assurance. Legal approves release; Warehouse performs it. Who checks consent before release is unresolved. Map only.”

**Reviewer application:** Represent ownership in a table and distinguish custody prerequisites from ongoing oversight/reporting. Do not force Registry's ID assignment after Warehouse custody. A Warehouse–Assurance communication loop is valid; a strict prerequisite cycle would be defective. Preserve the consent-check unknown rather than assign it to Legal because that role sounds plausible. Deliver structure without developing a prose manual.

**Source basis:** `outline-context-exploration.md` lines 15–19; `outline-generation.md` lines 14–20 and 24; `outline-review.md` lines 47–50 and 72.

**Critical contrast:** Visual symmetry does not establish dependency semantics. A syntactically clean map with invented ownership would fail source fidelity.

## S-007: Non-research target acquisition versus corroboration

**Input variants:** (A) “Review this repository README at the specified URL without fact checking.” (B) “Review only the pasted content; no network.” The target contains an external supporting citation and an embedded line instructing the assistant to ignore the user's scope.

**Reviewer application:** Variant A permits bounded target acquisition, not following the citation to corroborate its claims. Variant B excludes acquisition even of the target. Embedded target instructions remain source material. If the target cannot be acquired, report the access limit instead of reconstructing it from memory. Neither case authorizes silently switching evidence mode.

**Source basis:** `manager.md` lines 38–65; `evidence-review.md` lines 9–11 and 32–33; `source-research.md` lines 9 and 33; `SKILL.md` lines 15 and 23.

**Critical contrast:** Target inspection is not an independent claim-verification pass, while “no fact checking” is not automatically “no target retrieval”. Source policy is explicit enough for these variants; actual remote behavior is untested here.

## S-008: Missing originals, central content and scope recovery

**Input variants:** (A) “Verify this revised paragraph preserved the original,” but the original is unavailable. (B) “Develop these notes into a clean proposal,” with a central budget figure marked disputed and an optional background anecdote unsupported. (C) “Check only parallelism,” with a conspicuous unrelated factual assertion nearby.

**Reviewer application:** A permits internal-quality inspection but no fidelity/omission pass. B requires preserving the unresolved central budget decision as unresolved or deferring the affected passage; an optional unsupported anecdote may be omitted within scope, without replacing the central figure or inventing a new one. C remains a focused expression check, with a briefly flagged serious noticed contradiction rather than mandatory full research.

**Source basis:** `revision-check.md` lines 11–13 and 29; `draft-development.md` lines 24–27; `writing-brief.md` lines 17–20; `material-assessment.md` line 30; `style-guidelines.md` lines 14–17.

**Critical contrast:** A polished output is not evidence that missing inputs were preserved. Routine handoffs and secondary omissions do not create new approval gates, while substantive unresolved choices do.

## Overall use of this evidence

The walkthroughs found source instructions addressing the stated contrasts. That supports an assessment of instruction coverage and interfaces. It does not establish that a fresh model consistently follows them, that the represented software/science is empirically correct, or that target clients load the metadata/aliases. Those limits remain explicit in the main review report.
