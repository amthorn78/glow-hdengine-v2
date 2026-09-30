"""Guard proof for PART-02's six new tw-flowmaster forbidden identifiers (CHK-001).

Usage: python3 guard_proof.py <isolated-root-with-the-edited-skills> <scratch-dir>
For each identifier: (a) injected into tw-flowmaster's specialization, the validator reports
"superseded contract present: <id>"; (b) with that one identifier also removed from
CONTRACT_FORBIDDEN in the copy, the same injection is not reported. Copies go under <scratch-dir>,
which must not exist; the root is only read. Prints one line per case and exits 0 only if all pass.
"""
import json, os, pathlib, shutil, subprocess, sys

GUARDS = ["TW-ASSESS-10", "PRE_CREATION_ASSESSMENT", "PRE_APPLY_ASSESSMENT",
          "STRENGTH_ANALYZER_PROMPT_ID", "APPLICATION_REASONING_POLICY", "PF_RENDERED_PAGE_COUNTS"]
END = "<!-- FLOWMASTER_SPECIALIZATION_END -->"


def run(root):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, str(root / "flowmaster-validate/scripts/validate_flowmaster.py"),
                        "--skills-root", str(root)], capture_output=True, text=True, env=env)
    return p.returncode, json.loads(p.stdout)["skills"]["tw-flowmaster"].get("errors") or []


def main(root, scratch):
    root, scratch = pathlib.Path(root), pathlib.Path(scratch)
    if scratch.exists():
        sys.exit(f"refused: {scratch} exists")
    ok = True
    for i, g in enumerate(GUARDS):
        for disabled in (False, True):
            case = scratch / f"{i}{'b' if disabled else 'a'}"
            shutil.copytree(root, case, symlinks=True)
            md = case / "tw-flowmaster/SKILL.md"
            t = md.read_text(encoding="utf-8")
            assert t.count(END) == 1
            md.write_text(t.replace(END, f"Injected for the guard proof: {g}.\n{END}"), encoding="utf-8")
            if disabled:
                v = case / "flowmaster-validate/scripts/validate_flowmaster.py"
                s = v.read_text(encoding="utf-8")
                line = f'        "{g}",\n'
                assert s.count(line) == 1, g
                v.write_text(s.replace(line, "", 1), encoding="utf-8")
            code, errors = run(case)
            hit = f"superseded contract present: {g}" in errors
            passed = (not hit) if disabled else (hit and code != 0)
            ok &= passed
            print("PASS" if passed else "FAIL", g, "guard disabled" if disabled else "guard live",
                  f"exit={code}", f"tw-flowmaster errors={len(errors)}")
            shutil.rmtree(case)
    scratch.rmdir()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(*sys.argv[1:3])
