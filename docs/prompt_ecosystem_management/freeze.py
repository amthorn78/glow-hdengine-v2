"""Freeze digest of a skill tree, rooted where the claim is.

Recipe, stated so it can be reproduced rather than trusted: walk regular files only, take each
path relative to the tree root with forward slashes, **skip the sync-infrastructure paths in
EXCLUDE**, sort the remainder by their UTF-8 bytes, and sha256 the concatenation of
"<path>\\n<sha256-of-contents>\\n" for each. The count printed is the number of files hashed,
which is one fewer than the tree's file count. **The contents of the root `SKILL.md` are taken
with its frontmatter name line plain:** `name: "<skill>"` or `name: '<skill>'` is hashed as
`name: <skill>`, and nothing else in any file changes.

`manifest.json` is excluded because it is the sync layer's own bookkeeping, not skill content.
It carries a `lastUpdated` epoch that the installer rewrites on every sync, so hashing it makes
the digest a per-container, per-sync value rather than an identity. SF10-10's first version of
this recipe did hash it, which reproduced the exact defect the recipe was introduced to remove:
the round-23 report published 318-file digests that do not reproduce in another container, and
did not reproduce in this one once a sync touched the manifest. Found by SFR-01 in §10 review
and confirmed by falsification here. The rule generalises: a freeze digest covers skill content
and never the machinery that delivers it.

The name line follows the same rule (D28, Nathan, 2026-10-12). The *Save skill* install writes
each skill's name line as `name: "<skill>"`; a package carries `name: <skill>`. YAML reads both as
the same string, so the digest of an installed tree equals the digest of the package it came from.
A tree whose name line is already plain hashes exactly as before, so every digest recorded for a
plain tree still reproduces. A digest recorded before 2026-10-12 for a tree whose name line was
quoted was taken over the raw quoted bytes and does not reproduce under this recipe.

Every run first tests both forms, in memory, through the same code that digests the tree, and
prints no digest if they differ. `--selftest` runs only that test.
"""
import hashlib
import re
import sys
from pathlib import Path

# Sync-layer bookkeeping, rooted at the skill tree. Never skill content.
EXCLUDE = {"manifest.json"}

# A quoted frontmatter name line, as the Save skill install writes it (D28).
SKILL_NAME_QUOTED_RE = re.compile(rb"(?m)^(name:[ \t]*)([\"'])([a-z0-9-]+)\2([ \t]*\r?)$")


def canonical_skill_md(data: bytes) -> bytes:
    """SKILL.md bytes with a quoted frontmatter name line written plain, as it is packaged."""
    if not data.startswith(b"---"):
        return data
    end = data.find(b"\n---", 3)
    if end < 0:
        return data
    return SKILL_NAME_QUOTED_RE.sub(rb"\1\3\4", data[:end], count=1) + data[end:]


def digest(entries) -> tuple[int, str]:
    """entries: (relative path, contents) pairs, already sorted by the path's UTF-8 bytes."""
    h = hashlib.sha256()
    count = 0
    for rel, data in entries:
        if rel == "SKILL.md":
            data = canonical_skill_md(data)
        h.update(rel.encode("utf-8") + b"\n")
        h.update(hashlib.sha256(data).hexdigest().encode("ascii") + b"\n")
        count += 1
    return count, h.hexdigest()


def selftest() -> list[str]:
    plain = b"---\nname: some-skill\ndescription: A skill.\n---\n\n# Some skill\n"
    quoted = plain.replace(b"name: some-skill", b'name: "some-skill"', 1)
    single = plain.replace(b"name: some-skill", b"name: 'some-skill'", 1)
    script = ("scripts/run.py", b"print('name: \"x\"')\n")

    def tree(skill_md: bytes, nested: bytes = b"") -> list[tuple[str, bytes]]:
        return [("SKILL.md", skill_md), *([("refs/SKILL.md", nested)] if nested else []), script]

    failures = []
    if digest(tree(quoted)) != digest(tree(plain)):
        failures.append('`name: "<skill>"` and `name: <skill>` give different digests')
    if digest(tree(single)) != digest(tree(plain)):
        failures.append("`name: '<skill>'` and `name: <skill>` give different digests")
    if canonical_skill_md(plain) != plain:
        failures.append("a plain name line is not hashed byte for byte")
    body_line = plain + b'name: "some-skill"\n'
    if canonical_skill_md(body_line) != body_line:
        failures.append("a name line after the frontmatter is changed")
    if digest(tree(plain, quoted)) == digest(tree(plain, plain)):
        failures.append("a SKILL.md below the root is changed")
    return failures


def main() -> int:
    failures = selftest()
    if failures:
        print("freeze.py self-test failed, no digest printed: " + "; ".join(failures), file=sys.stderr)
        return 2
    if sys.argv[1:] == ["--selftest"]:
        print("freeze.py self-test ok: quoted and plain name lines give the same digest")
        return 0
    root = Path(sys.argv[1]).resolve()
    paths = sorted(
        (
            rel
            for rel in (p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())
            if rel not in EXCLUDE
        ),
        key=lambda s: s.encode("utf-8"),
    )
    count, hexdigest = digest((rel, (root / rel).read_bytes()) for rel in paths)
    print(f"{count} {hexdigest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
