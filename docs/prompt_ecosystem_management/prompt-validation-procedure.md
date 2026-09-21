---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
status: BINDING
authority: Product Owner direction 2026-09-21 — persistent procedure lives in the repository, not in Notion
migrated_from: Glow Operations Hub, *Validating prompts — read the page, pipe the body, never mirror* and *Recorded identity is checked, not reported*
---

# Validating prompts, and checking recorded identity

How prompt bodies are validated now that the corpus mirror is gone, and the general rule about
recorded identities that the same repair established. Post-flight has its own procedure in
`postflight-procedure.md`; this is the everyday one.

## Validating prompts — read the page, pipe the body, never mirror

Standing procedure, Product Owner approved 2026-09-21. This is how prompt validation is performed now that the **Prompt Corpus Storage and Fidelity Policy** governs. It replaces `--prompt-dir` and every practice built on it.
### The procedure
1. **Decide which prompts the task actually concerns.** A change to one prompt needs one page. A change to the QA closure route needs three. A corpus-wide sweep is not the default because it is expensive — **not because it is disallowed.** Reading prompts is never restricted; if the work needs all fifty-five, read all fifty-five. What is forbidden is writing them anywhere. See `prompt-corpus-policy.md`, *Reading is not restricted. Copying is.*
2. **Read those pages from Notion.** That is the operative source, and reading it is sufficient evidence.
3. **Pipe the bodies in as JSON on stdin**, `{"PROMPT-ID": "<text>"}`:
   `echo "$bodies" | python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract <contract> --bodies-stdin`
   There is **no path option and there will not be one**. A file persists, and a persisted corpus is what the policy forbids.
4. **Read the coverage fields, not just ****`ok`****.** `prompt_bodies_validated` lists the ids checked; `prompt_body_checks_not_evaluated` names the set-scoped checks that could not run. A run that validated nothing still returns `ok: true`, correctly — it found no fault in nothing. **`ok`**** alone is not evidence of coverage.**
5. **Report what was checked.** "IA-10 and IA-30 validated, class-map checks not evaluated" is a true statement. "0 errors" on its own is not, and never was.
6. **Do not write the bodies anywhere.** Not to a scratch file, not to the repository, not as an appendix to a report. Quote the specific clause your finding rests on and nothing more.
### What replaced what
| before | now |
|---|---|
| `--prompt-dir <dir>`, 55 files required | `--bodies-stdin`, whatever pages you read |
| `PROMPT_BODY_MEMBER_SET` — were all 55 files there? | membership is the registry's and the graph's, which carry it without bodies |
| `PROMPT_BODY_DUPLICATE`, `_FILENAME_ID`, `_UTF8` | gone; they described a directory, not the ecosystem |
| `CANDIDATE_PROMPT_ROOT_MISMATCH` | gone; it hard-coded `<candidate-root>/prompts` as a storage location |
| `prompt_body_sha256`, body hashes | gone |
| `PROMPT_BODY_MISSING_ID` | **`PROMPT_BODY_ID_MISMATCH`** — compares the body's own `Prompt ID:` header against the key it was supplied under, and names the page you actually have |
**The new failure mode is reading the wrong page**, which a directory made hard and this makes easy. `PROMPT_BODY_ID_MISMATCH` exists for exactly that and is the reason the interface is keyed by prompt id rather than positional.
### The claim that is no longer available
*"0 errors across all 55 bodies."* It was never a continuous control — it ran only when a session built a mirror, and that practice is retired. A promotion packet now cites which prompts were validated, when, and against which release. If a corpus-wide assertion is genuinely required for a decision, that is a Product Owner call about that decision, not a standing gate.
### One hash survives, and it is not of a prompt
`SKILL_TREE_SHA256`: `flowmaster-validate` digests **its own tree** at runtime and refuses to certify anything when the bytes do not match its declaration. A skill's own bytes are not the prompt corpus. See `skill-identity-and-freeze.md` — this is that rule made mechanical, after a withdrawn package ran for a full round behind green gates.

## Recorded identity is checked, not reported

Standing rule, Product Owner direction 2026-09-21. **A hash a validator computes and prints is not a check. If an identity is worth recording, something must compare it and fail.**
Added after `SF10-12`. The GCFPE validator computed `prompt_body_sha256` for all 55 prompt bodies, put the values in its output, and compared them with nothing. The approved registry had carried a byte count and a SHA-256 for every one of those bodies since the consolidated pass. Two halves of a check that had never been introduced to each other, for four rounds.
**The cost, measured rather than asserted.** With the comparison removed and one byte appended to a body, the end-to-end gate returns **0 errors**. That is what the ecosystem did before this round: any corrupted, truncated or hand-retyped body passed every gate in silence. An independent reviewer had already reached the same conclusion from the other side and correctly refused to run the 55-body gate at all, reporting the limit instead of producing a number — *"that run would have produced a number, not evidence."*
### The rule
1. **Every recorded identity has a consumer that fails on mismatch.** A digest, byte count, revision string or page id that appears only in output is decoration. Before recording one, name the check that reads it.
2. **Absence of the expected value is an error, never a silent skip.** If the pins are missing, the artifact is unverifiable, and the run says so. A check that degrades quietly to "pass" is worse than no check, because it reports success.
3. **The parameter carrying the expectation is required, not optional.** A default of `None` is how a check stops running without anyone deciding that it should.
4. **Normalise exactly one thing, and say why in the code.** `SF10-12` strips exactly one trailing newline before hashing, because the pin is a property of the Notion page and not of the file holding it. CRLF, stripped whitespace and a second blank line stay fatal. Every additional tolerance is a class of corruption you have chosen not to detect, so each one is a decision that gets written down beside the code.
5. **Pin where the expectation lives, not where it is cheapest.** Validation expectations belong in the validation profile; contract terms belong in the contract. Cost may break a tie; it may not decide one. State the reasoning either way, because the reviewer will ask.
### Procedure — re-pinning after an authorised body change

> **Retired by the Prompt Corpus Storage and Fidelity Policy, 2026-09-21.** `SF10-12` pinned
> a SHA-256 of every prompt **body**, and body hashes are exactly what the policy forbids. The
> pins and the re-pinning sequence are gone. The sequence is kept here because the *general*
> rule above — a recorded identity must have a consumer that fails on mismatch — still binds
> every identity the ecosystem does record, and because the reasoning in the closing section
> is the part that generalises.

A pinned identity turns every legitimate edit into a failing gate until the pin moves. That is the forcing function working, not a defect, and it has a defined sequence:
1. Make the authorised change to the prompt body in Notion. Nothing else.
2. Re-extract the affected body under the recorded convention — the exact slice between the fetch result's `<content>` and `</content>` markers, **no trailing newline added** — and update its `evidence_contract` row in `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`.
3. Regenerate the profile pins **from the registry, by script**. Never hand-type a digest, and never copy one from a report.
4. Re-run the end-to-end gate. It must return to zero errors. If a body you did not touch now fails, you have found real drift — stop and report it; do not re-pin it to make the gate green.
5. The profile change moves skill bytes, so it carries a `validator_revision` increment and a fresh §10 like any other validation-behaviour change.
**Re-pinning is part of the change that caused it.** A session that edits a body and leaves the pins stale has handed the next session a gate that fails for a reason it did not cause.
### Deriving pins costs nothing if the values were already recorded

Also a record of the retired `SF10-12`, kept for the reasoning rather than the procedure.

The Product Owner's condition for authorising `SF10-12` was that it must not require reading all 55 prompt bodies through a session. It did not, and the reason generalises: **the identities already existed in the registry**, so deriving the pins was registry on disk → script → profile on disk, and confirming that all 55 reproduce was a script printing six numbers. No body content entered context.
Before concluding that a verification is too expensive, check whether the values are already written down somewhere and simply unread. This is the same shape as *`A grep proves the absence of a string, never the absence of a thing`* — the record is usually richer than the last session assumed.
