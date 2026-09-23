"""E2 canonical texts, read from the v2 execution specification's §3 (never re-authored).

Token names follow spec §8a.0 / §8b.0. `T[...]` values are byte-exact strings.
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
SPEC = Path("/home/user/glow-hdengine-v2/docs/ephemeral/modifications/specs/"
            "EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md").read_text(encoding="utf-8")
S3 = SPEC[SPEC.index("## §3 Canonical wording, final"):SPEC.index("## §4 Graph transforms")]


def block_after(marker, nth=0):
    i = S3.index(marker)
    assert S3.count(marker) == 1, marker
    for _ in range(nth + 1):
        j = S3.index("```text\n", i)
        k = S3.index("\n```", j + 8)
        val = S3[j + 8:k]
        i = k + 4
    return val


T = {
    "C-ART": block_after("**C-ART** (PART-03)"),
    "C-HANDOFF": block_after("**C-HANDOFF** (PART-04"),
    "C-PLACE": block_after("**C-PLACE** (PART-05)"),
    "C-DEC": block_after("**C-DEC** (PART-06"),
    "C-LAT": block_after("**C-LAT** (PART-07"),
    "C-D22": block_after("**C-D22** (PART-13)"),
    "C-SESSION": block_after("**C-SESSION** (PART-09), amended"),
    "C-SUB": block_after("**C-SUB** (PART-10), A1-5"),
    "C-DISPATCH": block_after("**C-DISPATCH** (PART-11), A1-5"),
    "C-TOP": block_after("**C-TOP** (A1-8), new"),
    "OVERRIDE": block_after("**GCFPE override** (A1-6), new"),
    "C-PROCEED": block_after("**C-PROCEED** (the single-Proceed rule"),
    "C-PR20-ENTRY": block_after("**C-PR20-ENTRY**"),
    "STEP2": block_after("**Step 2** — C-NOTION in the relay"),
    "INVARIANT": block_after("**Governance-audit invariant**"),
}
# §8a.0 and §8b.0 tokens, read from their fenced token blocks.
S8A = SPEC[SPEC.index("### 8a.0 Conventions"):SPEC.index("### 8a.1 ")]
S8B = SPEC[SPEC.index("### 8b.0 Conventions"):SPEC.index("### 8b.1 ")]


def token_block(section):
    body = section[section.index("```\n{") + 4:]
    body = body[:body.index("\n```")]
    out, name = {}, None
    for line in body.split("\n"):
        if line.startswith("{") and line.endswith("}") and " " not in line:
            name = line[1:-1]
        elif line.strip() and name:
            assert name not in out, name
            out[name] = line
    return out


for sec in (S8A, S8B):
    for k, v in token_block(sec).items():
        assert T.get(k, v) == v, k
        T[k] = v
assert set(T) >= {"NINE", "TEN", "V5", "V6", "FALLBACK", "LANDED", "A18", "W9", "S6", "S7"}, sorted(T)
assert T["C-SESSION"].endswith(T["A18"])
assert T["INVARIANT"] == token_block(S8A)["INVARIANT"]
assert T["C-DISPATCH"].count(T["FALLBACK"]) == 1


def x(s: str) -> str:
    """Expand {TOKEN} placeholders."""
    for k, v in T.items():
        s = s.replace("{" + k + "}", v)
    return s


if __name__ == "__main__":
    import hashlib
    for k, v in T.items():
        print(f"{k:12} {len(v):5} {hashlib.sha256(v.encode()).hexdigest()[:16]} {v[:70]!r}")
