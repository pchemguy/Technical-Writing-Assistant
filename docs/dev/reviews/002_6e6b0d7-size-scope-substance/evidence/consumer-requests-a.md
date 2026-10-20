# Consumer requests A

Candidate source: `28a7a005f57cbf5a24ca6b697e06973085d8125e`.

The following prompt was fixed before consumer execution. Each group used one fresh context; expected outcomes and campaign conclusions were withheld. Parent packaging of this evidence does not change the consumer's no-write task.

```text
Use Technical Writing Assistant from /workspace/scratch/843c75a4f4c3/Technical-Writing-Assistant/technical-writing-assistant for the requests below. Start with that SKILL.md and load only relevant references from that package. Treat requests separately and use only supplied content, without external research. Do not read repository campaign records, development documents, validation history or Git history. No file writes, code or test execution, Git operations, sending or publishing. Return the actual requested outputs under each case ID, followed by resources read, actions and limitations. Keep the combined response concise while answering each request.

SC-001. Review this internal memo's size and level of detail for trained operations staff who read it from beginning to end. Its purpose is to explain the daily log-archiving task. Findings only; do not rewrite.
Overview: At the end of each shift, export the completed daily log to the archive folder and compare the exported file's checksum with the original.
Work instructions: When a shift finishes, create an export of that shift's completed log, place it in the archive folder, and confirm its checksum matches the source.
Additional guidance: The finished log for each shift must be copied by export into the archive location. Compare the source and exported checksums to confirm the copy. Keep the original until the checksums match.

SC-002. Review the size and level of detail of this complete procedure for operators who are new to this fictional internal transfer tool. Its scope includes preparation, transfer, recovery and completion records. Review the supplied writing only, without verifying or running commands; return findings or an assessment, not rewritten prose.
Purpose: Transfer one completed shift log to the read-only archive without losing the original.
Inputs: Obtain the shift ID, the original log and the operator's archive access. The source log must be marked Complete; otherwise wait for the shift owner.
Preparation: Confirm the shift ID agrees with the log header. Check that the archive has room for the exported file. If access is denied, contact the archive owner; do not change access settings.
Export: Select the completed log and choose Export. The tool returns either OK with an export path or ERR with an error code. If it returns ERR, retain the original and record the code. An operator may retry once after an archive-space error has been resolved; other errors go to the tool owner.
Verification: Use the tool's Compare operation with the original and export paths. MATCH confirms identical checksums. On DIFFERENT, quarantine the export and retain the original; do not repeat the transfer until the tool owner responds.
Archive: On MATCH, use Mark archived for the exported path. Record the shift ID, export path and MATCH result. The archive owner alone can change archived files.
Completion: Confirm the record has all three fields and that the archived export is visible. Retain the original for seven days under the supplied retention rule; transfer completion does not authorize earlier deletion.
Limits: The procedure covers one completed log. It does not authorize transferring an active log, changing a mismatch result or overriding archive access.

SC-003. Review the size and detail of this standalone equipment label. Its sole purpose is to state the prohibition shown; it is not an operating manual. Findings only.
"Do not open the chamber while it is pressurized."

SC-004. Review this complete procedure intended to let a novice back up a project database. No other instructions or technical information are supplied. Assess size/detail and usability; findings only, no invented operating steps.
"Back up the database. Verify success."

SC-005. Review these two task pages for amount of text and detail. Operators open either page independently at the task. A shared overview is available through a link on each page and already contains the system background. Findings only.
Shared overview background: The register was introduced in 2010 and replaced paper forms. Its first release had a blue interface. Later releases changed its menu names while preserving its role as the record of approved entries.
Export page: Prerequisite: work from a read-only copy of production data. The register was introduced in 2010 and replaced paper forms. Its first release had a blue interface. Later releases changed its menu names while preserving its role as the record of approved entries. Select Export, choose the completed entry, and save its generated file. Record the generated file's identifier.
Import page: Prerequisite: work from a read-only copy of production data. The register was introduced in 2010 and replaced paper forms. Its first release had a blue interface. Later releases changed its menu names while preserving its role as the record of approved entries. Select Import, choose the approved generated file, and record the imported entry's identifier.
```
