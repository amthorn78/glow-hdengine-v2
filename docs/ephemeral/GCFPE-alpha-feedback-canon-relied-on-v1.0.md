---
artifact_type: ALPHA_FEEDBACK_BRIEF
artifact_version: "1.0"
subject: Review and approval prompts must produce a "Canon relied on" block
requested_by: Nathan / Product Owner, 2026-09-27
author: Claude Code session https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq
route: GCFPE-MGMT-10 (prompt maintenance); prompt bodies are in Notion and are not edited here
related: docs/ephemeral/HDE-EPIC040-QA70-planning-failure-rca-v1.1.md; PR #538
---

# Alpha feedback: "Canon relied on" block in review artifacts

## 1. What happened

At HDE-EPIC040 QA-70, the reviewer approved a QA Plan whose rails model contradicted canon. The Plan had a mixed `SAFE_MODE=0` / `ALLOW_NETWORK=0` state, per-command rails and live database checks that need users who do not exist before the App. The review said the Plan matched the QA Guide and Plan Templates, but the reviewer had not read their rails sections. The Product Owner rejected the approval. The RCA puts the root cause in execution: canon was not read.

Nothing in the review artifact exposed the gap. It did not have to say which canon had been read, so an approval grounded in no canon looked the same as one grounded in all of it.

## 2. Request

Every GCFPE prompt that reviews, approves or decides on a governed artifact requires, in its output artifact, a block titled **Canon relied on**:

* each PF document by title, with the sections actually read, including the applicable PF10 addenda;
* each in-flight change document read (Specification, Plans, prior reviews, Product Owner dispositions), by repository path and version;
* one line per topic the artifact rules on (for example rails, environments, evidence, storage), naming the section that governs it, or stating that canon is silent.

A review whose block is missing, empty or lacks a governing section for a topic it rules on is incomplete. It cannot approve.

## 3. Prompts in scope

These are the prompts whose output carries a decision on a governed artifact. The current membership must be checked against the register before the change.

| Stage | Prompt family |
| :---- | :---- |
| Specification | CF-C-30, CF-E-30 (approval of Specification deltas) |
| Implementation | IA-30 (whole-change Plan review), PR-40 (PR work-unit lineage review) |
| QA | QA-10 (readiness), QA-70 (QA Plan review), QA-110 (QA disposition) |
| Rescope and escalation | RS-20, ESC-40 |
| Closure | CL-20 |

## 4. What already exists in the repository

These pieces are in PR #538 and take effect only when it merges.

* **AGENTS.md canon-first rule.** Agents search canon for every task, read the governing sections in full, and record the PF titles and sections relied on.
* **Per-turn reminder hook** (`UserPromptSubmit`). Every Claude Code turn in this repository carries the canon-first reminder.
* **Review-artifact hook** (`PostToolUse`). When a Claude Code session writes a review or approval file under `docs/ephemeral/`, the hook sends the write back to the agent if the file has no non-empty "Canon relied on" block.

The hooks run only in Claude Code, and they check that the block exists, not that its contents are true. The prompt requirement in §2 is what makes the block binding on every surface.

## 5. Acceptance for the prompt change

* Each in-scope prompt body requires the block and names it exactly "Canon relied on", so the hook and the prompts agree.
* Each prompt's approval outcome is unavailable while the block is missing or empty.
* The contract registry records the block as a required output element for those prompts.
* A replay of the HDE-EPIC040 QA-70 input yields a review whose block must name the rails sections of the QA Guide and PF10. Without them it cannot approve.

## 6. Decision needed

Admit this to the Alpha Feedback list and route it to a GCFPE-MGMT-10 Modification.
