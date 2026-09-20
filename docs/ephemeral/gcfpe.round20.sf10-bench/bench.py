#!/usr/bin/env python3
"""SF10-03 / SF10-06 bench.

Usage:
    bench.py --base <installed-tree> --work <repaired-tree> --bodies <55-body-corpus>

The three inputs are environment-resident and are deliberately not committed:

  * `--base` and `--work` are copies of the installed skills tree, which lives in a
    one-way synced directory outside the repository and is installed only by the
    Product Owner.  Vendoring it here would create a second, drifting copy of the
    thing under test.
  * `--bodies` is the 55-prompt corpus.  Prompt bodies are authored in Notion in
    place and are never mirrored into this repository, so the corpus is fetched per
    run and verified against the registry's recorded `evidence_contract` digests.

The script therefore refuses to guess: a missing or unusable input is reported as a
HARNESS FAILURE with the path it wanted, and never as a passing gate.

Three phases are kept apart, because round 18 proved that sharing one `try` lets a
setup failure be credited as a gate that fired:

  1. APPLY    -- build the fixture. A failure here is HARNESS FAILURE, exit 1.
  2. IMPORT   -- load the validator under test. A failure here is HARNESS FAILURE, exit 1.
  3. EVALUATE -- run the real check. Only this phase produces a verdict, and it
                 fails closed.

Every case runs the validator's own functions.  An earlier revision of this file
reimplemented the SF10-06 branch and selected between implementations by testing for
an unrelated symbol, so its cases would have passed even if the real branch were
absent -- a bench that tested its author's copy of the logic.  That is fixed: the
handoff cases write the mutated corpus to a temporary directory and call
`validate_prompt_bodies`, the function the validator actually uses.
"""
import argparse, importlib.util, json, pathlib, re, shutil, sys, tempfile

CONTRACT = "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
FAIL = 0


def die(message: str) -> None:
    print(f"  HARNESS FAILURE: {message}")
    sys.exit(1)


def load(tree: pathlib.Path):
    """Phase 2. Import the validator from `tree`; any failure is a harness failure."""
    path = tree / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"
    if not path.is_file():
        die(f"no validator at {path}")
    sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(f"v_{tree.name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except BaseException as exc:                      # noqa: BLE001 - harness guard
        die(f"cannot import the validator from {tree}: {exc!r}")
    finally:
        sys.path.pop(0)
    return mod


def read_bodies(bodies_dir: pathlib.Path) -> dict[str, str]:
    found = {p.stem: p.read_text(encoding="utf-8") for p in sorted(bodies_dir.glob("*.md"))}
    if len(found) != 55:
        die(f"expected 55 bodies in {bodies_dir}, found {len(found)}")
    return found


def read_contract(tree: pathlib.Path) -> dict:
    path = tree / CONTRACT
    if not path.is_file():
        die(f"no contract at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def case(name, tree, mutate, predicate, expect, *, bodies_dir):
    """Phase 1 then phase 3, separated."""
    global FAIL
    mod = load(tree)
    try:
        data = {"bodies": read_bodies(bodies_dir), "contract": read_contract(tree)}
        before = json.dumps(data["bodies"], sort_keys=True)
        if mutate is not None:
            mutate(data)
            if json.dumps(data["bodies"], sort_keys=True) == before:
                die(f"{name}: mutation changed nothing")
    except SystemExit:
        raise
    except BaseException as exc:                      # noqa: BLE001 - harness guard
        die(f"{name}: cannot build the fixture: {exc!r}")

    try:
        got = predicate(mod, data)
    except BaseException as exc:                       # noqa: BLE001 - fail closed
        got = f"RAISED {exc!r}"
    ok = got == expect
    if not ok:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n        expected {expect!r}\n        got      {got!r}")


# ---------------------------------------------------------------- predicates


def qa_errors(mod, data):
    """SF10-03: the validator's own function, on the real or mutated bodies."""
    return sorted(e for e in mod.validate_qa_closure_bodies(data["bodies"], data["contract"])
                  if e.startswith("QA_PASS_BODY_CLASS_MAP"))


def handoff_errors(mod, data):
    """SF10-06: run the validator's own `validate_prompt_bodies` over a real directory.

    Nothing about the branch under test is reimplemented here.  The corpus is written
    to a temporary directory so the function receives exactly what it receives in
    production, and only handoff-related codes are selected from its output.
    """
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="sf10-bench-"))
    try:
        for prompt_id, text in data["bodies"].items():
            (tmp / f"{prompt_id}.md").write_text(text, encoding="utf-8")
        errors, _hashes = mod.validate_prompt_bodies(tmp, data["contract"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return sorted(e for e in errors
                  if e.startswith(("PROMPT_HANDOFF_CONTRACT", "PROMPT_HANDOFF_RECEIVER",
                                   "PROMPT_TERMINAL_HANDOFF_CONTRACT")))


# ---------------------------------------------------------------- mutations


def drop_receiver(prompt_id, receiver):
    def f(data):
        data["bodies"][prompt_id] = data["bodies"][prompt_id].replace(receiver, "REDACTED-RECEIVER")
    return f


def swap_operative_receiver(prompt_id, receiver, other):
    """Retarget the LAST mention of `receiver` while leaving earlier mentions intact.

    This models the attack the whole-document predicate cannot see: the body still
    names its declared receiver somewhere harmless -- a route inventory, a phase
    description, a prohibition -- while the mention nearest its routing tail points
    somewhere else.  Replacing every occurrence would instead be caught, so the
    fixture asserts that at least one mention survives; if none does, the fixture is
    invalid and this is a harness failure rather than a result.
    """
    def f(data):
        text = data["bodies"][prompt_id]
        cut = text.rfind(receiver)
        if cut < 0:
            die(f"{prompt_id} does not mention {receiver}")
        text = text[:cut] + other + text[cut + len(receiver):]
        if receiver not in text:
            die(f"fixture invalid: {receiver} no longer appears in {prompt_id}, so the "
                f"whole-document predicate would catch this and the blind spot is not modelled")
        data["bodies"][prompt_id] = text
    return f


def break_class_map_receiver(data):
    data["bodies"]["QA-120"] = data["bodies"]["QA-120"].replace("`CL-E-10 —", "`CL-E-40 —")


def break_class_map_page_id(data):
    data["bodies"]["QA-120"] = data["bodies"]["QA-120"].replace(
        "3db4590a05eb811a8578d75885c16cac", "0000000000000000000000000000dead")


def repipe_class_map(data):
    """Re-render QA-120's HTML class map as a Markdown pipe table with bare URLs."""
    text = data["bodies"]["QA-120"]
    block = re.search(r"<table header-row=\"true\">.*?</table>", text, re.S)
    if block is None:
        die("QA-120 has no HTML table to re-render")
    rows = re.findall(
        r"<tr>\s*<td>`PASS`</td>\s*<td>`(EPIC|CRD)`</td>\s*<td>`(CL-[EC]-10) — ([^`]+)` at "
        r"<mention-page url=\"([^\"]+)\"/></td>\s*</tr>", block.group(0), re.S)
    if len(rows) != 2:
        die(f"expected 2 class-map rows to re-render, found {len(rows)}")
    lines = ["| Result | Verified change class | Required receiver |", "|---|---|---|"]
    for cls, dest, title, url in rows:
        lines.append(f"| `PASS` | `{cls}` | `{dest} — {title}` at {url} |")
    data["bodies"]["QA-120"] = text.replace(block.group(0), "\n".join(lines))


# ---------------------------------------------------------------- run

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True, type=pathlib.Path, help="copy of the installed skills tree")
    ap.add_argument("--work", required=True, type=pathlib.Path, help="copy carrying the prepared repair")
    ap.add_argument("--bodies", required=True, type=pathlib.Path, help="directory of the 55 prompt bodies")
    args = ap.parse_args()
    for label, path in (("--base", args.base), ("--work", args.work), ("--bodies", args.bodies)):
        if not path.is_dir():
            die(f"{label} is not a directory: {path}")
    base, work, bodies = args.base, args.work, args.bodies

    print("=== SF10-03 — QA-120 class map (validate_qa_closure_bodies) ===")
    case("installed build reports a defect on the real body", base, None, qa_errors,
         ["QA_PASS_BODY_CLASS_MAP"], bodies_dir=bodies)
    case("repaired build reads the real HTML body", work, None, qa_errors, [], bodies_dir=bodies)
    case("repaired build also reads the pipe rendering", work, repipe_class_map, qa_errors, [],
         bodies_dir=bodies)
    case("repaired build still rejects a wrong receiver", work, break_class_map_receiver, qa_errors,
         ["QA_PASS_BODY_CLASS_MAP"], bodies_dir=bodies)
    case("repaired build still rejects a wrong page id", work, break_class_map_page_id, qa_errors,
         ["QA_PASS_BODY_CLASS_MAP"], bodies_dir=bodies)

    print("\n=== SF10-06 — handoff obligation (validate_prompt_bodies) ===")
    case("installed build reports GCFPE-MGMT-10", base, None, handoff_errors,
         ["PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10"], bodies_dir=bodies)
    case("repaired build clears the corpus", work, None, handoff_errors, [], bodies_dir=bodies)
    case("repaired build catches a dropped receiver (PR-30 -> PR-35)", work,
         drop_receiver("PR-30", "PR-35"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:PR-30:PR-35"], bodies_dir=bodies)
    case("repaired build catches GCFPE-MGMT-10 dropping PR-10", work,
         drop_receiver("GCFPE-MGMT-10", "PR-10"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10"], bodies_dir=bodies)

    print("\n=== SF10-06 — the predicate's limit, asserted rather than hidden ===")
    print("  The check asserts that each declared receiver is NAMED in the body. It does not")
    print("  bind that name to the operative handoff, so retargeting PR-30's last mention of")
    print("  PR-35 to PR-40 -- while its earlier mentions stay -- is NOT caught. The case")
    print("  below asserts that blind spot so it cannot be mistaken for coverage; see the")
    print("  report for why a routing-section-scoped variant was measured and rejected.")
    case("retargeting the last mention is NOT caught (known limit)", work,
         swap_operative_receiver("PR-30", "PR-35", "PR-40"), handoff_errors, [], bodies_dir=bodies)

    print(f"\n{'ALL CASES AS EXPECTED' if FAIL == 0 else f'{FAIL} CASE(S) NOT AS EXPECTED'}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
