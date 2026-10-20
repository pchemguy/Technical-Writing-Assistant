# Technical Writing Assistant specification

## Purpose and authority

Implement the complete standalone `technical-writing-assistant` skill described in [CAPABILITY_MAP.md](CAPABILITY_MAP.md). The map governs capability boundaries, style policy, evidence modes, and contextual outline adaptation. The skill covers software documentation and scientific, technical, and professional writing, with an editing-first orientation and support for development from early material.

## Required behavior

- Preserve meaning, authorial position, essential reasoning, numerical factors, qualifications, and protected material during ordinary revision. Present substantive changes explicitly.
- Execute focused modules independently and composite workflows through the manager. Load only relevant resources; handoffs do not create routine approval gates.
- Implement all 20 references (19 focused modules and one manager) in the map with usable procedures, inputs, missing-information handling, outputs, completion checks, and examples or observable acceptance criteria.
- Retain exactly two evidence modes. Ask when evidence work is relevant and the mode is unresolved; reuse existing decisions. Without research, acquire explicitly identified task targets through permitted access but do not independently retrieve citation-only support or corroborating sources. Respect explicit no-network/no-retrieval/supplied-content-only restrictions. Target acquisition is separate from evidence-mode selection; report failures and clarify consequential ambiguity rather than invent contents. Do not treat model knowledge or inspection alone as claim verification.
- Diagnose composition across sentence, paragraph, section, and document levels. Assess document and section size and level of detail against purpose, scope, substantive content, audience needs, and genre when relevant to the request; return a reasoned assessment within the inspected boundary. Preserve useful detail and recurrence while identifying excess or insufficient development. Prefer sound topic sentences in expository paragraphs while retaining justified brief warnings and transitions; treat length heuristics as signals, not quotas. Diagnose unresolved contextual references, including unavailable prior revisions, at the intended reading boundary without banning valid local/input references.
- Generate, review, validate, and repair outlines/maps using contextual criteria, without a closed catalogue of specialized cases or mandatory schema. Outline review includes evaluative-only, validation-only, or comprehensive coverage with shared intake and consolidated findings.
- Check revisions comparatively against the source, instructions, and authorized changes: requested-change completion, essential content, protected material, meaning shifts, introduced defects including unavailable-context references, and relevant prior findings. Check affected passages and consequential dependencies; skip this comparison for findings-only work and do not fact-check unchanged claims as a compulsory second review. Disclose unavailable source comparisons; compare drafts from notes against their notes.
- Comprehensive editorial review considers all relevant dimensions and reports material exclusions, findings, consequences, and remedies without automatic rewriting. Comprehensive draft revision applies needed authorized changes and checks their effects. Triage is optional readiness assessment, not detailed review.
- Keep provenance/access, source-to-claim relationships, researched-claim outcomes, and criterion outcomes distinct. Missing evidence is not proof of falsity; criterion failure is not a claim-truth label.
- Apply software, scientific, and professional genre guidance without inventing behavior, results, requirements, or commitments. Preserve declared or consistently established project docstring conventions; Google style is the Python default only when no governing convention exists.
- Deliver the requested artifact and material unresolved issues. Distinguish source inspection, external verification, software execution, and editorial checking.

## Package and portability

Use required Agent Skills frontmatter and relative Markdown references. All references are directly discoverable from SKILL.md. The core consists of instructions; it requires no executable code or specific service. External research and file-format operations use host facilities when available. OpenAI metadata is optional client presentation, separate from portable behavior. Do not claim installation or client execution from package validation.

## Acceptance and review

Check naming, frontmatter, contained links and anchors, resource inventory, presentation metadata, and absence of implementation scaffolds. Review every capability against the map. Exercise realistic focused, composite, outline, and negative tasks through fresh agent sessions where available; preserve raw outputs and assess them against explicit criteria. These samples do not establish reliability across all models, clients, or external sources.
