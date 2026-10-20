# Consumer requests B

Candidate source: `28a7a005f57cbf5a24ca6b697e06973085d8125e`.

The following prompt was fixed before consumer execution. Each group used one fresh context; expected outcomes and campaign conclusions were withheld. Parent packaging of this evidence does not change the consumer's no-write task.

```text
Use Technical Writing Assistant from /workspace/scratch/843c75a4f4c3/Technical-Writing-Assistant/technical-writing-assistant for the requests below. Start with that SKILL.md and load only relevant references from that package. Treat requests separately and use only supplied content, without external research. Do not read repository campaign records, development documents, validation history or Git history. No file writes, code or test execution, Git operations, sending or publishing. Return the actual requested outputs under each case ID, followed by resources read, actions and limitations. Keep the combined response concise while answering each request.

SC-006. Assess the same text's size and level of detail for each of two specified uses. Do not rewrite. Use A: a one-page decision brief for directors deciding whether to replace the current register; they need the current operating problem and options. Use B: an audit appendix whose explicit requirement is to preserve the supplied chronological history as well as current options for auditors already familiar with the system.
Text: The current register requires manual checks before export. The decision is whether to retain it or replace it with a tool that supplies those checks. No budget or implementation estimate is yet available.
History: The register began in 2010 with paper entry forms. In 2011 the forms received new numbering. In 2012 the team changed the cover sheet. In 2013 the support desk moved. In 2014 the interface became blue. In 2015 a menu was renamed. In 2016 the manuals changed fonts. In 2017 the training room moved. In 2018 the team changed the binder labels. In 2019 the form title changed. In 2020 the help icon changed. In 2021 the printed cover changed. In 2022 the team returned to the original numbering. In 2023 the manuals were reprinted. In 2024 the interface labels changed again.

SC-007. Is the full report appropriately sized and detailed for engineers evaluating a pilot? Only this excerpt is supplied; no remaining sections or report length are available. Return an assessment using supplied contents only.
"Executive overview: Eighteen of thirty units improved under condition B. Humid-condition testing is pending. Methods, individual measurements and limitations are discussed in later sections."

SC-008. Treat these as separate requests about the same text. First, review size and level of detail for a short internal project-status update, with findings only. Second, provide a shorter clean revision, preserving its meaning and status. No research.
Text: Management proposes a Q2 launch. The proposed launch date is in Q2. A launch during the second quarter is the proposal currently put forward by management. Funding has not been approved, and the schedule remains tentative.

SC-009. Shorten this to at most four words, using complete ordinary English sentences rather than symbolic shorthand. Preserve every stated quantitative fact, condition and uncertainty. No research.
Text: Eighteen of thirty samples improved under condition B. The estimate is 3 kilograms multiplied by 0.25 and factor F. Factor F is unverified.

SC-010. Correct grammar only; return the corrected sentence.
"The report contain three tables."
```
