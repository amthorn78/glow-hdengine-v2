---
artifact_type: TOOL_NOTE
artifact_version: "1.0"
created_date: 2026-09-21
authority: Product Owner authorization, 2026-09-21
subject: Deterministic claim inventory for changed documentation
---

# Claim inventory

A pre-push check that every claim-bearing line a change introduces is **owned by something**.

```sh
python3 docs/ephemeral/claim_inventory/claim_inventory.py                    # uncommitted work
python3 docs/ephemeral/claim_inventory/claim_inventory.py --since-baseline   # everything it covers
python3 docs/ephemeral/claim_inventory/claim_inventory.py --range A..B       # one commit or span
```

## It has a baseline, and that is a scope limit rather than a default

`allow.json` records a **baseline commit** — the commit that introduced this tool. Claim-bearing
lines authored before it are **not** inventoried, and the reason is arithmetic: the branch carries
**180** of them across the repair report, the decision briefs and the run record. Writing 180
ownership notes for historical narrative would produce a large artefact of little value and make the
allow-list itself unreviewable.

So the first version of this file documented `--range origin/main..HEAD` as the pre-push check, and
**that command exits 1 with 180 unaccounted claims** — it could not validate the change that
introduced it, and would have blocked every push on this branch. Review found that. A range reaching
behind the baseline is now **refused with its reason** rather than reported as 180 findings, because
a check that looks like a gate and cannot pass is worse than one with a stated limit.

What the baseline does not excuse: every line touched from that commit onward is inventoried,
including lines in older documents. The figures that go stale are the ones a change moves.

## What it checks, and what it does not

It finds each line a change adds or modifies that states a digest, a count, a size, a dotted
revision or a percentage, and requires it to be either inside a `<!-- generated: … -->` block, or
listed in `allow.json` with a note naming what recomputes it or why it is fixed.

**It does not verify that any value is correct**, and it cannot — it has no idea what the number
means. It converts *a reader must notice a stale figure* into *an author must say, in writing, who
owns this figure*. Limits, stated because an unstated limit is how the guards in this package kept
over-claiming: Markdown only, so a figure in a docstring is out of scope; only the paths given by
`--paths`; and "generated" means marker-delimited and nothing else.

## Why it exists

Three consecutive review cycles on #425 produced three stale claims while the evidence itself
stayed correct — a validator-difference summary falsified by a later retirement, a
`regenerated at <commit>` attribution four commits out of date, and a corpus byte total that was
never summed. Each was a sentence describing a derivable value, sitting beside blocks that were
derived. Re-reading every summary after every change was tried, and failed four times in one round.

## The allow-list is keyed on the exact line text

That is the design, not an implementation detail: edit the line and its entry stops matching, so
the claim comes back for accounting. Entries are checked in **both** directions — an entry whose
line no longer exists is reported too, because a dead entry is how an allow-list grows quietly into
a blanket exemption.

## Controls, all fired

| injected | result |
|---|---|
| the three claims that actually went stale, at the commits that introduced them | all three reported |
| a new prose claim added to a brief | reported |
| an allow-listed line edited | reported **twice** — as an unaccounted claim and as a stale entry |
| a dead allow-list entry | reported |
| an allow-listed file **deleted**, no claim lines added | reported — all of its entries are stale |
| an allow-list entry with an **empty** note | reported as unaccounted |
| a placeholder note (`"see above"`) | reported as unaccounted |
| a range reaching **behind the baseline** | refused, with the reason and the remedy |

## Two defects of its own, found by running it

Both were the same shape as the findings it exists to catch, which is worth recording rather than
hiding. It first took line numbers from `git diff` of an old range and then read the file from
**disk**, so every number indexed into content the commit never had. And a bare revision is not a
range — `git diff <rev>` compares the **working tree** against it — so reading that revision
reproduced the same mismatch from the other direction. Both were caught by the tool reporting lines
that were plainly inside a marker block, not by re-reading the code.

A third and a fourth, found by review rather than by me, and both the shape this tool exists to
catch. A **deleted** allow-listed file returned `None` and skipped every one of its entries, so
removing a document could leave all its exemptions behind and still exit clean — contradicting the
two-direction check advertised two paragraphs above. And the allow-list was a **membership test on
the key**: the note was never inspected, so an empty string permitted the claim and the tool did not
enforce its own central requirement. Notes are now required to say something.

It also originally recognised generated regions by **shape**, carrying its own copy of the
recorder's table and fence patterns. Two copies of one rule is how the guard drift in this package
began, so the regions are now marker-delimited in the document and both tools read that one
declaration.
