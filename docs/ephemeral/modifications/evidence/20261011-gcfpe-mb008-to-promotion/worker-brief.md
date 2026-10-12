# Body-scan worker brief — MB-008 ANALYZE, 2026-10-11

You are a read-only maintenance worker for one GCFPE-MGMT-10 ANALYZE run (Modification for backlog item MB-008). Your job is classification of text in Notion prompt pages, under rules that are already settled. Apply them; do not revisit them. If a rule looks wrong, say so in `unresolved_questions` and carry on.

## Boundaries (binding)
- Write nothing: no repository file, branch, commit, PR, Notion write or comment. Read and return only.
- Prompt bodies must not be kept on disk. If the harness saves a large fetch result to a tool-results file, you may run a read-only regex/python over that file for this scan only; never copy it elsewhere, hash it, or reopen it after your scan. Report in `transient_files` every such file path (D22 disclosure).
- One fetch per page. Fetch your pages in parallel batches. Do not re-fetch a page.
- Quote verbatim, minimum span (one sentence). A paraphrase is not evidence.

## Settled rules you apply
1. **PF10 addendum 2.1 (canon, 2026-10-11):** in GCFPE, the model and reasoning-level guidance for a downstream session is the TypeSafe reading printed by the installed TypeSafe scoring skill (cell, every probability, flags). No agent gives its own recommendation, assessment or ranking of model, reasoning level or effort. A reading that cannot be obtained is reported "not read" with the reason. Advice on execution surface is unchanged. The reading is not an approval or gate.
2. **D23-B (ruling):** a NEXT_PROMPT_HANDOFF block carries only: destination prompt name/version/URL; receiving role and task/artifact binding; input artifact paths with labels; PR reference when continuing a PR; minimum exceptional context.
3. **F05 repair (parent Modification, applied to six producers CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40 and PE):** the qualifying producer resolves the next continuous PF10 addendum number at creation; nobody edits PF10 except Nathan's paste. A non-producer saying *it itself* does not number is a permitted exception. A universal statement that *no agent* numbers contradicts the producers.

## For each assigned page
Read the text between `<content>` and `</content>`. Record `page_last_edited_at` and the page title.

A. **Broad match, PF10 2.1.** Find EVERY sentence containing any of these stems (case-insensitive): `model`, `reasoning`, `effort`, `strength`, `advice`, `advise`, `advisory`, `recommend` (any form), `TypeSafe`, `runtime setting`, `Analyzer`, `configuration`, `surface`. Count all such sentences (`a_sentences_total`). Classify each into exactly one:
   - `T1_PROHIBITS_GUIDANCE_GENERAL` — forbids model/reasoning/effort/strength/runtime-setting guidance, evaluation, assessment or recommendation by the prompt or its response in general (would forbid reporting a TypeSafe reading beside the handoff).
   - `T2_PROHIBITS_IN_HANDOFF_BLOCK_ONLY` — forbids such content only inside the NEXT_PROMPT_HANDOFF block.
   - `T3_GIVES_OR_REQUIRES_AI_GUIDANCE` — tells an agent to give its own model/reasoning/effort recommendation, or carries a fixed model/effort recommendation.
   - `T4_TYPESAFE` — mentions TypeSafe.
   - `T5_SURFACE_OR_OPERATOR_DECISION` — says runtime surface/configuration/tools are operator decisions, without forbidding guidance.
   - `T6_UNRELATED` — another sense (data model, mechanics model, "recommended disposition" of a conflict, Analyzer retired history, etc.). Count only; no quote needed.
   Quote every T1–T5 sentence verbatim with its nearest heading.
B. **Handoff preamble.** Does the page contain a sentence beginning `Anything before it is at most a few lines`? Give the count (0, 1, ...).
C. **F05 surviving text.** Find every sentence containing `numbering`, or containing `number` together with `PF10` or `addendum`. Classify: `N1_UNIVERSAL_NO_AGENT_NUMBERS` (e.g. "No agent ... allocates PF10 numbering"), `N2_SELF_SCOPED_NONPRODUCER`, `N3_PRODUCER_RESOLVES_NUMBER`, `N4_NATHAN_ALLOCATES_OR_NUMBERS`, `N5_OTHER`. Quote each verbatim with its nearest heading.
D. **Handoff emission.** Count occurrences of the literal `NEXT_PROMPT_HANDOFF`.
E. **Escape hatch.** Report any sentence you judge in scope of rules 1–3 that this brief does not account for, in `cross_batch_observations`.

## Return — JSON only, no prose
{
 "batch_id": "<given>",
 "prompt_ids_surveyed": [...],            // must equal your assigned set exactly
 "pages": [
   {"prompt_id": "...", "page_id": "...", "title": "...", "page_last_edited_at": "...",
    "fetched_ok": true, "returned_size_chars": <int or null>,
    "a_sentences_total": <int>, "a_counts": {"T1":0,"T2":0,"T3":0,"T4":0,"T5":0,"T6":0},
    "a_quotes": [{"class":"T1","heading":"...","quote":"..."}],
    "b_preamble_count": <int>,
    "c_quotes": [{"class":"N1","heading":"...","quote":"..."}],
    "d_handoff_literal_count": <int>,
    "coverage": "CHECKED" | "NOT_CHECKED", "reason": "<required when NOT_CHECKED>"}
 ],
 "cross_batch_observations": [],
 "unresolved_questions": [],
 "transient_files": [],
 "blocked": []
}
An absent array is a malformed return. A page you could not read is NOT_CHECKED with the reason, never omitted.
