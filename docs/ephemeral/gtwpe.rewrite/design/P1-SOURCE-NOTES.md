---
artifact_type: GTWPE_P1_SOURCE_NOTES
purpose: W1's working notes from the P1 complete reads, committed as they are made so a compaction or resume (D26-C) loses nothing. The design package cites the sources, not these notes.
status: WORKING RECORD. Merging preserves the record and approves nothing (D21-C)
---

# P1 source notes

All PF files are read at `main` @ `8eb4ce0`, from `docs/pfcanon/`.

## PF03 — `PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` (39,259 B, 613 lines): complete

- Title "PF03-Reference-Technical-Writing-Best-Practices", v1.8.7, Status Reference, Last Update Gate "BN 12.8.9".
- §1: PF03 governs the writing portion only; "An instruction to write about an action does not authorize the action" (no apply, commit, push, merge, drain).
- §2: the Product Owner "controls the requested scope, output contract, and authorized editorial changes".
- §3: read every relied-on source completely; unknown stays unknown; one canonical home per truth; route by exact in-document title, no version in durable cross-document prose; no ASCII three-period or Unicode ellipsis in PF documents (explicit omission markers only).
- §6 source precedence: operator instruction; complete target; topic-owning canon; PF10 only where an exact addendum addresses the point; one repository snapshot.
- §7 output forms (full rewrite, section rewrite, redline, review). "Do not change a supplied title, version, status, effective date, gate, invocation identifier, or other document-control value unless the Product Owner or a governing source explicitly authorizes the change." Findings from an audit/review source: account for every one (change, no-change, gap, blocking decision).
- §8 redlines: fields (number; mapped findings/anchors; change type and one operation `INSERT`/`REPLACE`/`DELETE`; target's exact in-document title; target evidence; controlling basis; rationale; complete heading path; one direct action; exact boundaries and uniqueness counts; complete paste text). INSERT boundaries = the complete lines immediately before and after the gap, both unchanged; REPLACE and DELETE boundaries = complete first and last lines of the inclusive range; a one-line range may use one line as both. Heading path and each boundary match exactly once in scope; widen to the smallest unique range, then REPLACE and reproduce captured text. Each redline executes independently against the complete original; ranges must not overlap; consolidate edits to one gap. No redline when unique placement cannot be established. No outer-bold headings; one blank line after a heading; no code fences around paste text unless the PO asks. Judge anchors against raw bytes.
- §9 PF10 content: read the complete latest active PF10 base; overlapping addenda: highest-numbered applies; cite an addendum by exact number and title; inside PF10, cite another PF by exact in-document title and section only; do not claim drafted text was pasted, merged or drained.
- §11 state language: "The text was applied" needs direct observation of the updated bytes; "committed/pushed/merged" needs direct repository evidence; none proves the next state.
- §12: ask only when the answer materially changes the result; answer "Yes"/"No" first on a PF09 row closure question.
- §15.1 document-control pattern: Title, Version, Status, Effective date, Last Update Gate, Invocation tag, Provenance. "Do not invent, infer, normalize, or increment a document-control value."
- §15.2 the redline block template (fields as §8, plus "Action: `<OP> ONCE <complete action wording>`", "Uniqueness: `section-path matches=1 | each required boundary matches within scope=1`").

## PF06 — `PF06-Canon-Change-Process-Guide-v2.5.3.md` (415,416 B, 4,623 lines): complete

Read in eight slices, lines 1–500, 500–1049, 1050–1599, 1600–2149, 2150–2749, 2750–3369, 3370–4009, 4010–4623.

- Title "PF06-Canon-Change-Process-Guide", v2.5.3, Status Canon, Last Update Gate "redlines-PF06-Canon-Change-Process-Guide-v2.5.1-from-PF10-HDE-Build-Notes-v12.9" (a gate value can name the redline package that produced the version).
- §0.1A: PF06 owns the end-to-end change process. Lifecycle steps 12 "Build Notes recording", 13 "Canon drainage when applicable", 14 "PF09 or PF30 record completion". Routing: HDE Governance controls "canon-change requirements"; Plan Templates controls templates; HDE CRD Records controls PF30 registration and result tracking; HDE Build Notes records "temporary pre-drain authority".
- §0.2: "Coding agents and Implementation Agents MAY NOT directly modify PF-Canon documents as part of implementation PR work"; a canon edit "remains separate documentation work". "Documentation drainage is never an execution or closeout gate." "PF-canon drainage applies stable documentation updates to the permanent PF homes. PF10 can stage live truth before drainage, but the drain itself is a separate documentation action." For a PR route "the Product Owner is the sole merger and uses squash". Landing a canonical file on `main` "establishes repository reality and, for a current canonical artifact, authority in its declared content lane" and nothing more. Build Notes references: "Do not reference Build Notes by version strings. Prefer referencing by addendum number + addendum title."
- §0.6.1: "Plans MUST NOT mandate PF document updates"; implied PF maintenance "is PO-owned and out of plan scope". ADR doc deltas are paste-ready: target doc (title) and section, current proof excerpt (verbatim 1–5 lines), replacement block, why, evidence pointers.
- §0.6.10 redline bundle construction discipline: one-pass, non-overlapping edits against the unchanged base; anchors in original-document space only; one strategy per region; parent-child prohibition; no second-pass layering; repeated-anchor safeguard (widen to the nearest unique enclosing heading); coverage-before-emission; merge-on-conflict; "One-pass apply simulation required"; bundle validity gate; a violation is "a mechanical redline-construction failure" treated as Revise and Resubmit.
- §1.0.3 and §1.0.6: a CRD gets "a concise initial record in PF30 before implementation begins"; at closure "update the existing PF30 CRD record with the concise final result. PF30 is the accountability register".
- §1.1.2, §3.5.1, §6.3: PF20 receives the epic record "once, at epic close, as the final archived entry. In-flight epics MUST NOT be recorded there"; "After an authorized close, PF20 … MAY record the final historical epic disposition." This bears on plan Q1 (default: no PF20).
- §3.5.2.8 "Post-QA documentation drainage ordering (normative)": drainage into canon "occurs only after all QA tasks for the epic are complete"; until then PF10 is the controlling temporary source; undrained deltas never block QA or closeout.
- Document shapes a Path A input may arrive in: §2.2 "Findings → Doc Delta Map" (FND blocks, DELTA blocks: target doc, section, delta, why, evidence, PF proof excerpt); §4.6 "Doc Deltas (PF-Canon only; ALWAYS INCLUDED)"; §0.6.1 ADR doc-delta entries; audit/docdeltas surfaces (§0.5.1).
- §1.1.11: approval-submitted planning artifacts carry the sentinel `ASK OK?`.
- §6.2: current PF09 status values "Done, Partial, Not done, Consolidation pending, and Optional"; PF09.5 adds "Pending Revalidation"; "Canceled" is future-only until drained. §4.6 "PF09 Impact & Status Posture": supported later-drain action is exactly one of change to Done | Partial | Not done | Consolidation pending | Optional | No status change recommended; artifacts "MUST NOT phrase a supportable status move as though the canon row has already been updated".
- §3.5.3: a repo docs sweep "MUST NOT modify any PF-Canon docs".
