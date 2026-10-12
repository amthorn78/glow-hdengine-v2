#!/usr/bin/env python3
"""Build flowmaster-validate 3.4.1 from the reviewed 3.4.0 tree (Nathan's decision 1, 2026-10-12; D28).

The Save skill install writes each skill's name line as `name: "<skill>"`. After this build every
check in flowmaster-validate that reads a skill's name or hashes a skill's files gives the same
result whether that line is quoted or not, and the suite runs a standing test of both forms.

Usage: fv341_build.py <base> <out> [--check]
  <base>  the reviewed 3.4.0 tree (freeze digest `37 02a69b8a...`); the installed tree with line 2
          of SKILL.md unquoted measures exactly that
  <out>   written fresh; refused if it exists, unless --check, which rebuilds into a temporary
          directory and compares it with <out> file by file
Every substitution names the count it must make; a count that differs stops the build.
SKILL_TREE_SHA256 is declared last, from the built tree's own skill_tree_digest.
"""
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

BASE_FREEZE = "37 02a69b8a99181e79e554299a51dcc31e8b6b629d4974d05c96b191cf948fa200"

HELPERS = '''# D28 (Nathan, 2026-10-12): the Save skill install writes a skill's name line as
# `name: "<skill>"`, and a package carries `name: <skill>`.  YAML reads both as the same string, so
# every name read and every hash of a skill's files here gives the same result on either form.
# validate_flowmaster.py tests both forms on every suite run.
SKILL_NAME_QUOTED_RE = re.compile(rb"(?m)^(name:[ \\t]*)([\\"'])([a-z0-9-]+)\\2([ \\t]*\\r?)$")


def names_skill(text: str, name: str) -> bool:
    return re.search(rf"(?m)^name:\\s*([\\"']?){re.escape(name)}\\1\\s*$", text) is not None


def canonical_skill_md(data: bytes) -> bytes:
    """SKILL.md bytes with a quoted frontmatter name line written plain, as it is packaged."""
    if not data.startswith(b"---"):
        return data
    end = data.find(b"\\n---", 3)
    if end < 0:
        return data
    return SKILL_NAME_QUOTED_RE.sub(rb"\\1\\3\\4", data[:end], count=1) + data[end:]


def skill_md_sha256(path: Path) -> str:
    return hashlib.sha256(canonical_skill_md(path.read_bytes())).hexdigest()


def find_skill(skills_root: Path, name: str) -> tuple[Path, str] | None:
    for path in sorted(skills_root.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        if names_skill(text, name):
            return path, text
    return None
'''

OLD_FIND_SKILL = '''def find_skill(skills_root: Path, name: str) -> tuple[Path, str] | None:
    pattern = re.compile(rf"(?m)^name:\\s*{re.escape(name)}\\s*$")
    for path in sorted(skills_root.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        if pattern.search(text):
            return path, text
    return None
'''

OLD_DIGEST_LOOP = '''    for name in names:
        data = (root / name).read_bytes()
        if name == "SKILL.md":
            data = SELF_IDENTITY_RE.sub(b"", data)
        digest.update(name.encode("utf-8") + b"\\n")'''
NEW_DIGEST_LOOP = '''    for name in names:
        data = skill_identity_bytes(name, (root / name).read_bytes())
        digest.update(name.encode("utf-8") + b"\\n")'''
OLD_DIGEST_DEF = '''def skill_tree_digest(root: Path) -> str:'''
NEW_DIGEST_DEF = '''def skill_identity_bytes(name: str, data: bytes) -> bytes:
    """The bytes the digest takes for one file: SKILL.md without its declaration, name line plain."""
    if name == "SKILL.md":
        return canonical_skill_md(SELF_IDENTITY_RE.sub(b"", data))
    return data


def skill_tree_digest(root: Path) -> str:'''

OLD_PRIMARY = "sha256(primary[0])"
NEW_PRIMARY = "skill_md_sha256(primary[0])"

OLD_NAME_RE = '''NAME_RE = re.compile(r"(?m)^name:\\s*([a-z0-9-]+)\\s*$")'''
NEW_NAME_RE = '''# D28: a quoted name line (`name: "<skill>"`, as the Save skill install writes it) and a plain one
# read as the same name.
NAME_RE = re.compile(r"(?m)^name:\\s*([\\"']?)([a-z0-9-]+)\\1\\s*$")'''
OLD_NAME_GROUP = "    return name_match.group(1), description_match.group(1), keys"
NEW_NAME_GROUP = "    return name_match.group(2), description_match.group(1), keys"

STANDING_TEST = '''

# D28 (Nathan, 2026-10-12): "Make every check that reads a skill's name or hashes a skill's files
# give the same result whether that line is quoted or not ... Add a standing test of both forms so
# a later change cannot bring it back."  This runs on every suite run.  Every SKILL.md under the
# root is tested in both forms, plain and quoted, through each name reader and each skill-file hash
# this skill has; and no script in this skill may carry a reader that accepts one form only.  The
# one-form idioms are written as adjacent literals, so this file does not match itself.
ONE_FORM_NAME_IDIOMS = (
    "\\\\n" "name: ",
    "^name:\\\\s*" "([a-z0-9-]",
    "^name:\\\\s*" "{re.escape",
)


def quoted_name_form(data: bytes) -> bytes:
    """SKILL.md bytes with a plain frontmatter name line quoted, as the Save skill install writes it."""
    if not data.startswith(b"---"):
        return data
    end = data.find(b"\\n---", 3)
    if end < 0:
        return data
    head = re.sub(rb"(?m)^(name:[ \\t]*)([a-z0-9-]+)([ \\t]*\\r?)$", rb'\\1"\\2"\\3', data[:end], count=1)
    return head + data[end:]


def name_line_forms(skills_root: Path) -> dict[str, object]:
    import validate_gcfpe_20260914 as v0914
    import validate_gcfpe_20261009 as v1009
    import validate_gcfpe_current as vcur

    errors: list[str] = []
    checked: list[str] = []
    for skill_md in sorted(skills_root.glob("*/SKILL.md")):
        label = skill_md.parent.name
        plain = v1009.canonical_skill_md(skill_md.read_bytes())
        quoted = quoted_name_form(plain)
        if quoted == plain or v1009.canonical_skill_md(quoted) != plain:
            errors.append(f"NAME_LINE_FORMS_UNTESTED:{label}")
            continue
        texts = (plain.decode("utf-8"), quoted.decode("utf-8"))
        try:
            parsed = [frontmatter(text, skill_md) for text in texts]
        except ValidationError:
            errors.append(f"NAME_LINE_FORMS:frontmatter:{label}")
            continue
        if parsed[0] != parsed[1]:
            errors.append(f"NAME_LINE_FORMS:frontmatter:{label}")
        name = parsed[0][0]
        for module in (v0914, v1009, vcur):
            if not all(module.names_skill(text, name) for text in texts):
                errors.append(f"NAME_LINE_FORMS:{module.__name__}.names_skill:{label}")
            if module.canonical_skill_md(plain) != module.canonical_skill_md(quoted):
                errors.append(f"NAME_LINE_FORMS:{module.__name__}.canonical_skill_md:{label}")
        for module in (v0914, v1009):
            if module.skill_identity_bytes("SKILL.md", plain) != module.skill_identity_bytes("SKILL.md", quoted):
                errors.append(f"NAME_LINE_FORMS:{module.__name__}.skill_identity_bytes:{label}")
        checked.append(label)
    for script in sorted(Path(__file__).resolve().parent.glob("*.py")):
        source = script.read_text(encoding="utf-8")
        for idiom in ONE_FORM_NAME_IDIOMS:
            if idiom in source:
                errors.append(f"NAME_LINE_ONE_FORM_READER:{script.name}:{idiom}")
    return {"ok": bool(checked) and not errors, "skills_checked": len(checked), "errors": sorted(set(errors))}
'''
OLD_MAIN_ANCHOR = "\n\ndef main() -> int:"

OLD_SUITE_SELF = '''        report["self_identity"] = self_identity or "OK"
'''
NEW_SUITE_SELF = '''        report["self_identity"] = self_identity or "OK"
        name_forms = name_line_forms(args.skills_root)
        report["name_line_forms"] = name_forms
'''
OLD_SUITE_OK = '''                and not self_identity
                and all(item["status"] == "PASS" for item in report["skills"].values())'''
NEW_SUITE_OK = '''                and not self_identity
                and bool(name_forms["ok"])
                and all(item["status"] == "PASS" for item in report["skills"].values())'''

DISCOVERY_OLD_A = "dirs=[p.parent for p in root.glob('*/SKILL.md') if '\\nname: change-flow\\n' in p.read_text()]"
DISCOVERY_NEW_A = "dirs=[p.parent for p in root.glob('*/SKILL.md') if re.search(r'(?m)^name:\\s*([\"\\']?)change-flow\\1\\s*$',p.read_text())]"
DISCOVERY_OLD_B = "            if '\\nname: change-flow\\n' in p.read_text():directory=p.parent;break"
DISCOVERY_NEW_B = "            if re.search(r'(?m)^name:\\s*([\"\\']?)change-flow\\1\\s*$',p.read_text()):directory=p.parent;break"

SKILL_NOTE_OLD = "FLOWMASTER_VALIDATE_REVISION: 3.4.0\n"
SKILL_NOTE_NEW = """FLOWMASTER_VALIDATE_REVISION: 3.4.1
"""
SKILL_NOTE_ANCHOR = "\nMaintenance addition: register the self-contained human-design-reading-flowmaster domain\n"
SKILL_NOTE_TEXT = """
3.4.1 (`D28`, Nathan, 2026-10-12): the Save skill install writes each skill's name line as
`name: "<skill>"`. Every check here that reads a skill's name or hashes a skill's files gives the
same result whether that line is quoted or not: the frontmatter parser, each profile's skill lookup,
the Primary file identity and `SKILL_TREE_SHA256`, which is measured with the name line plain. The
suite reports `name_line_forms` and fails unless every `SKILL.md` under the root reads the same in
both forms and no script carries a one-form name reader.
"""

SUBS = [
    # (file, old, new, count)
    ("SKILL.md", SKILL_NOTE_OLD, SKILL_NOTE_NEW, 1),
    ("SKILL.md", SKILL_NOTE_ANCHOR, SKILL_NOTE_TEXT + SKILL_NOTE_ANCHOR, 1),
    ("references/gcfpe-20261009.1-100926.1-validation-profile.json", '"validator_revision": "3.4.0"', '"validator_revision": "3.4.1"', 1),
    ("scripts/validate_flowmaster.py", OLD_NAME_RE, NEW_NAME_RE, 1),
    ("scripts/validate_flowmaster.py", OLD_NAME_GROUP, NEW_NAME_GROUP, 1),
    ("scripts/validate_flowmaster.py", '"validator_revision": "3.4.0"', '"validator_revision": "3.4.1"', 1),
    ("scripts/validate_flowmaster.py", OLD_MAIN_ANCHOR, STANDING_TEST + OLD_MAIN_ANCHOR, 1),
    ("scripts/validate_flowmaster.py", OLD_SUITE_SELF, NEW_SUITE_SELF, 1),
    ("scripts/validate_flowmaster.py", OLD_SUITE_OK, NEW_SUITE_OK, 1),
    ("scripts/validate_gcfpe_20261009.py", '"validator_revision": "3.4.0"', '"validator_revision": "3.4.1"', 1),
    ("scripts/run_gcfpe_20261009_fixtures.py", '"validator_revision": "3.4.0"', '"validator_revision": "3.4.1"', 1),
]
for module in ("validate_gcfpe_20260914", "validate_gcfpe_20261009", "validate_gcfpe_current"):
    SUBS += [
        (f"scripts/{module}.py", OLD_FIND_SKILL, HELPERS, 1),
        (f"scripts/{module}.py", OLD_PRIMARY, NEW_PRIMARY, 1),
    ]
for module in ("validate_gcfpe_20260914", "validate_gcfpe_20261009"):
    SUBS += [
        (f"scripts/{module}.py", OLD_DIGEST_LOOP, NEW_DIGEST_LOOP, 1),
        (f"scripts/{module}.py", OLD_DIGEST_DEF, NEW_DIGEST_DEF, 1),
    ]
SUBS += [
    ("scripts/run_alpha_feedback_fixtures.py", "import copy,json\n", "import copy,json,re\n", 1),
    ("scripts/run_alpha_feedback_fixtures.py", DISCOVERY_OLD_A, DISCOVERY_NEW_A, 1),
    ("scripts/run_final_scan_fixtures.py", "import argparse,copy,json,sys\n", "import argparse,copy,json,re,sys\n", 1),
    ("scripts/run_final_scan_fixtures.py", DISCOVERY_OLD_B, DISCOVERY_NEW_B, 1),
    ("scripts/run_integrated_readiness_fixtures.py", "import argparse,copy,json,sys\n", "import argparse,copy,json,re,sys\n", 1),
    ("scripts/run_integrated_readiness_fixtures.py", DISCOVERY_OLD_B, DISCOVERY_NEW_B, 1),
]


def freeze(root: Path) -> str:
    paths = sorted((p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()), key=lambda s: s.encode("utf-8"))
    h = hashlib.sha256()
    for rel in paths:
        h.update(rel.encode("utf-8") + b"\n")
        h.update(hashlib.sha256((root / rel).read_bytes()).hexdigest().encode("ascii") + b"\n")
    return f"{len(paths)} {h.hexdigest()}"


def load(path: Path, name: str):
    sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)
        for key in [k for k in sys.modules if k.startswith("validate_") or k.startswith("run_")]:
            del sys.modules[key]


def build(base: Path, out: Path) -> dict:
    if freeze(base) != BASE_FREEZE:
        raise SystemExit(f"base is not the reviewed 3.4.0 tree: {freeze(base)}")
    shutil.copytree(base, out, ignore=shutil.ignore_patterns("__pycache__"))
    rows = []
    for rel, old, new, count in SUBS:
        path = out / rel
        text = path.read_text(encoding="utf-8")
        found = text.count(old)
        rows.append({"file": rel, "expected": count, "found": found})
        if found != count:
            raise SystemExit(json.dumps({"error": "substitution count", "row": rows[-1], "old": old[:120]}))
        path.write_text(text.replace(old, new), encoding="utf-8")
    skill_md = out / "SKILL.md"
    declared = load(out / "scripts/validate_gcfpe_20261009.py", "fv341_v1009").skill_tree_digest(out)
    text = skill_md.read_text(encoding="utf-8")
    old_line = "SKILL_TREE_SHA256: 429eda21084062f33d5b25e9ea27373f260789e666ab08be693bd8603f90917b\n"
    if text.count(old_line) != 1:
        raise SystemExit("SKILL_TREE_SHA256 declaration not found once")
    skill_md.write_text(text.replace(old_line, f"SKILL_TREE_SHA256: {declared}\n"), encoding="utf-8")
    identity = load(out / "scripts/validate_gcfpe_20260914.py", "fv341_v0914").validate_self_identity(out)
    return {"substitutions": len(rows), "rows": rows, "skill_tree_sha256": declared, "self_identity": identity or "OK", "freeze_raw": freeze(out)}


def main() -> int:
    base, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if "--check" in sys.argv[3:]:
        with tempfile.TemporaryDirectory() as tmp:
            again = Path(tmp) / "out"
            build(base, again)
            a = sorted(p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
            b = sorted(p.relative_to(again).as_posix() for p in again.rglob("*") if p.is_file())
            equal = a == b and all((out / r).read_bytes() == (again / r).read_bytes() for r in a)
            print(json.dumps({"equal": equal, "files": len(a)}))
            return 0 if equal else 1
    if out.exists():
        raise SystemExit(f"refusing to overwrite {out}")
    print(json.dumps(build(base, out), indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
