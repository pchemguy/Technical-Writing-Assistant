# Policy cleanup and metadata revision plan

## Authority and baseline

- Campaign: `007_a3d514b-policy-cleanup-and-metadata`.
- The user explicitly requested opening this revision campaign, implementing the supplied scope and closing it. This is a direct accepted amendment, with no separate review stage.
- Published starting baseline: `a3d514bb2b8ce6e311d8b5cabb2130f61548a2fa`, verified on 2026-11-05. Campaign 006 is integrated and closed; campaigns 001–006 remain frozen.
- Working branch: `revision/007_a3d514b-policy-cleanup-and-metadata`; creation parent, integration target and return branch: `main`. No suspended parent workflow.
- Interpret `AHENTS.md` as the existing root `AGENTS.md`. The existing README `urls` list already contains the requested conversation URL; retain that list and add the requested singular `url` field to its one existing frontmatter block.

## Accepted action

A-001 is one coherent repository cleanup and metadata amendment:

1. Delete root `SKILL_DISCOVERY_PROTOCOL.md` and `WINDOWS_SHELL_POLICY.md`.
2. Remove the complete `Initialization` and `Windows shell` sections from root `AGENTS.md`.
3. Add `url: https://chatgpt.com/c/6abe25da-8604-83ea-82be-c9c4f1a86eb8` to README frontmatter.
4. Add the supplied `metadata` mapping to `technical-writing-assistant/SKILL.md`: display name `Technical Writing Assistant`, aliases as the string `["TWA", "twa"]`, author `PChemGuy`, and repository `https://github.com/pchemguy/Technical-Writing-Assistant`.

Keep the skill's name, description, Markdown body, reference files and presentation unchanged. Do not edit closed campaign records or install the revised skill into a client.

## Verification and completion

- Publish and read back this opening before source edits.
- Compare the exact deletions, AGENTS section removal and frontmatter values/types with the request; verify all other source bytes and prior campaign trees are unchanged.
- Run the installed package validator/inventory on the actual repository skill; run the repository checker on a bounded current-source fixture excluding closed records. Represent the three historical link targets from current governing documents as empty existence-only placeholders, without reading their contents.
- Check whitespace, current links/anchors and full branch scope. Record actual commands/results and limitations in REVISION-REPORT.md; no fresh writing tasks or client activation trials are required for metadata-only runtime changes.
- Publish/read back A-001, explicitly merge the verified campaign tip into refreshed `main`, verify and publish the two-parent merge, then return clean on `main` and stop. No version bump, release or installation is requested.
