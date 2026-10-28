---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.2"
created_date: 2026-09-21
revised_date: 2026-10-27 — the glow-merged-change-attribution-lock 1.2.0 of record (MB-005); 1.1, 2026-10-12: D28, a skill's name line reads the same quoted or plain
status: BINDING
authority: Product Owner direction 2026-09-21; derived from findings F2 (round 23), the wrong-package install, and the round-27 §10 review
supersedes_location: docs/ephemeral/gcfpe.round23/freeze.py — the script previously lived there, which was the wrong home
---

# Skill identity, freeze digests, and install verification

How a skill tree is named, how a release is frozen, and what each identity does and does not prove.
Cited by every repair round; it names no release and outlives all of them, so it lives here rather
than in `docs/ephemeral/`.

## The digest recipe

`freeze.py` in this directory. Walk regular files, skip the `EXCLUDE` set, sort paths by their UTF-8
bytes, and sha256 the concatenation of `"<path>\n<sha256-of-contents>\n"` for each. The root
`SKILL.md` is hashed with its frontmatter name line plain (`D28`, below).

```
python3 docs/prompt_ecosystem_management/freeze.py <directory>
```

**Root it at the skill directory, never at the synced tree.** This is not a preference:

| rooting | what it measures |
|---|---|
| a skill directory | that skill's content — the identity a repair round is about |
| the whole synced tree | every installed skill, including ones this project does not own |

Round 26 watched a whole-tree digest move from `2fa5b848…` to `c607cedc…` with nothing of this
project's touched: the sync layer had updated an unrelated Anthropic skill. **A whole-tree digest is
hostage to strangers.** Quote per-skill digests.

`manifest.json` is excluded because it is the sync layer's own bookkeeping and carries a
`lastUpdated` epoch the installer rewrites. Round 23 hashed it and published digests that did not
reproduce in another container or, once a sync touched the file, in the same one. **A freeze digest
covers skill content and never the machinery that delivers it.**

**The name line is read plain (`D28`, Nathan, 2026-10-12).** The *Save skill* install writes each
skill's name line as `name: "<skill>"`; the package carries `name: <skill>`. YAML reads both as the
same string, so `freeze.py` hashes `name: "<skill>"` and `name: '<skill>'` as `name: <skill>`, in the
root `SKILL.md`'s frontmatter only, and changes nothing else. An installed tree then measures the
digest of the package it came from. A plain tree hashes exactly as before, so every digest recorded
for one still reproduces; a digest recorded before 2026-10-12 for a quoted tree was taken over the
raw quoted bytes and does not. MB-008's X17 is why: all six installed packages differed from their
reviewed digests by that one line, and no gate before delivery could see it.

**Both forms are tested on every run.** Before it prints a digest, `freeze.py` digests a quoted and a
plain tree in memory through the same code, and prints nothing and exits 2 if they differ.
`python3 docs/prompt_ecosystem_management/freeze.py --selftest` runs only that test. Any check that
reads a skill's name or hashes a skill's files must give the same result on both forms; a check that
does not is a defect, whichever skill or script it lives in.

## What each identity proves

| identity | answers | does **not** answer |
|---|---|---|
| freeze digest of a skill directory | what are these bytes? | whether they are the bytes anyone approved |
| `SKILL_TREE_SHA256`, declared in `SKILL.md` and checked at runtime (name line read plain, `D28`) | have these bytes changed since packaging? | **whether this is the version that was approved** |
| the digest named in a §10 verdict | which bytes were authorised | nothing about what is installed |

**A coherently built wrong package self-certifies.** Measured on 2026-09-21: a superseded package,
checked against its own declaration, returns no error — because a correct build declares itself
correctly. `SKILL_TREE_SHA256` is a tamper and integrity check. It is not a version check, and it
would not have caught the wrong-package install that motivated building it.

## Install verification — the rule this exists to serve

**An install is complete when the installed tree measures the digest the §10 verdict named. Not when
the gates come back green.** Every gate — the hash-pin chain, the fixture suites, the self-identity
check, the independent review — passes happily against a superseded version.

The comparison is one command and it is the only control for the wrong-package case:

```
python3 docs/prompt_ecosystem_management/freeze.py <installed>/<skill>   # equals the verdict's digest?
```

The install's quoted name line does not move this digest (`D28`). Any other difference does.

Check every skill the change touched, **and every skill it deliberately did not** — an unchanged
skill proving unchanged is evidence; assuming it is not. A mismatch is reported, never reconciled:
name which package is installed, name which was expected, hand the difference back.

On 2026-09-21 a withdrawn package was installed in place of its successor, under the identical
filename the packager requires, and ran for a full round behind green gates. **Two `.skill` files
for the same skill are always indistinguishable by name**, so the digest comparison is the control,
and delivery hygiene — digest first in the caption, one package per message — only reduces the odds.

## Advertised identity must be unspent

**Before packaging, diff every advertised identity value against the previous package. A match is a
defect, not a convenience.** Run it as a command, not as a memory:

```
grep -rn 'FLOWMASTER_VALIDATE_REVISION\|validator_revision\|SKILL_TREE_SHA256' <new>/ > /tmp/new.ids
grep -rn 'FLOWMASTER_VALIDATE_REVISION\|validator_revision\|SKILL_TREE_SHA256' <prev>/ > /tmp/prev.ids
diff /tmp/prev.ids /tmp/new.ids   # a revision that did not move, beside content that did, is the defect
```

**Where a skill advertises no identity value at all, the diff is vacuous, not failing.** Prose
skills — `glow-workspace-currency`, `glow-artifact-storage`, `glow-write-boundary`,
`glow-po-reporting` — carry only `name` and `description`, declare no revision, and their identity
is the freeze digest. Run the diff, record that it returned nothing, and package on the digest.
**Do not add a version field in order to have something to bump** — `D19` rules that out, and an
instruction to "bump the version" does not authorise inventing one.

A **spent** identity is one already bound to a published §10 verdict, an install, or a delivered
package. Corrected bytes never reuse one. `SKILL_TREE_SHA256` does not satisfy this on its own: it
moves automatically with content, so it will differ even when the declared revisions did not, and
**no report emits it** — which is exactly why it cannot be the thing that distinguishes two
packages in anyone's hands.

**This rule has been broken three times, twice under a `SKILL.md` that states it.** Round 23 shipped
new validation behaviour still emitting `validator_revision: 3.2.8`; round 24's `F1` established the
rule. Rounds 28 and 29 then shipped **mutually incompatible** validators — each rejects the other's
profile — both advertising `3.2.15` / `3.2.13`, while the author edited the narrative of round 24's
finding in that same file. Round 30's §10 review, which raised the point, put the reason plainly: a
narrative *"narrates rather than prescribes"*, so a reader learns the rule was broken and is not
told what to do. The command above is what to do.

Rounds 28 and 29 remain separable only by tree hash. That cannot be repaired — both are published
and both carry `SKILL_REPAIR_REQUIRED`, so confusing them costs nothing — but it is the shape of the
damage, and it is permanent.

**One revision, two trees: glow-merged-change-attribution-lock 1.2.0.** Recorded 2026-10-27 by
`MODIFICATION-20261027-gcfpe-backlog-open-items` (MB-005). Two trees have advertised
`MERGED_CHANGE_ATTRIBUTION_SKILL_REVISION: 1.2.0`: the installed tree, 10 files, freeze digest
`c518ccb0076b042859de4d2e136ef682bb127b6524133d2a575d433490eaf48f`, and an analysed tree, 11 files,
`ee253cfaf844a5ce28da3646e469d3a926167ecb3898e5dc205b0365dc946a8e`, which is not held in this
repository or in the installed skills. **The installed 10-file tree is the 1.2.0 of record:** sessions
load it, and qualification binds it by digest (DN-E E1, `MODIFICATION-20261011-gcfpe-mb008-to-promotion`).
Revision 1.2.0 is spent on it. Any other content of this skill, the 11-file tree included, is delivered
again only under a revision that no package, verdict or install has used.

## Recording the values

A round's report names the baseline digest, the repaired digest, the package digest and
`SKILL_TREE_SHA256`. A freeze record names every installed skill, the contract, the graph proof
token and the repository controls. Both are release-scoped and belong in `docs/ephemeral/`; **this
convention is not.**
