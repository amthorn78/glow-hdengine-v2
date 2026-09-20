#!/usr/bin/env python3
"""SF10-03 / SF10-06 bench.

Three phases are kept apart, because round 18 proved that sharing one `try` lets a
setup failure be credited as a passing gate:

  1. APPLY    -- build the fixture. A failure here is HARNESS FAILURE, never a result.
  2. IMPORT   -- load the validator under test. A failure here is HARNESS FAILURE.
  3. EVALUATE -- run the check. Only this phase produces a verdict.

Each case also refuses to run if applying it leaves the input unchanged, so a
placement that silently matches nothing cannot be scored as caught.
"""
import copy, importlib.util, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BODIES = ROOT.parent / "bodies"
CONTRACT = "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
FAIL = 0


def load(tree: pathlib.Path):
    """Phase 2. Import the validator from `tree`; any failure is a harness failure."""
    path = tree / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"
    sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(f"v_{tree.name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except BaseException as exc:                     # noqa: BLE001 - harness guard
        print(f"  HARNESS FAILURE: cannot import validator from {tree.name}: {exc!r}")
        sys.exit(1)
    finally:
        sys.path.pop(0)
    return mod


def bodies() -> dict[str, str]:
    return {p.stem: p.read_text(encoding="utf-8") for p in sorted(BODIES.glob("*.md"))}


def contract(tree: pathlib.Path) -> dict:
    return json.loads((tree / CONTRACT).read_text(encoding="utf-8"))


def case(name, tree, mutate, predicate, expect):
    """Phase 1 then 3, separated. `expect` is the verdict this case asserts."""
    global FAIL
    mod = load(tree)                                  # phase 2
    try:                                              # phase 1
        data = {"bodies": bodies(), "contract": contract(tree)}
        before = json.dumps(data["bodies"], sort_keys=True) + json.dumps(data["contract"], sort_keys=True)
        if mutate is not None:
            mutate(data)
            after = json.dumps(data["bodies"], sort_keys=True) + json.dumps(data["contract"], sort_keys=True)
            if after == before:
                print(f"  HARNESS FAILURE: {name}: mutation changed nothing")
                sys.exit(1)
    except SystemExit:
        raise
    except BaseException as exc:                      # noqa: BLE001 - harness guard
        print(f"  HARNESS FAILURE: {name}: cannot build fixture: {exc!r}")
        sys.exit(1)

    try:                                              # phase 3
        got = predicate(mod, data)
    except BaseException as exc:                       # noqa: BLE001 - fail closed
        got = f"RAISED {exc!r}"
    ok = got == expect
    if not ok:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n        expected {expect!r}\n        got      {got!r}")


def qa_errors(mod, data):
    return sorted(e for e in mod.validate_qa_closure_bodies(data["bodies"], data["contract"])
                  if e.startswith("QA_PASS_BODY_CLASS_MAP"))


def handoff_errors(mod, data):
    """Re-implement only the branch under test, over the real contract and bodies."""
    out = []
    members = mod.EXPECTED_MEMBERS
    for pid, text in data["bodies"].items():
        rows = [r for r in data["contract"]["state_routes"].get(pid, [])
                if isinstance(r, dict) and r.get("public_result") is True]
        nonterm = [r for r in rows if r.get("terminal_for_invocation") is not True]
        if not nonterm:
            continue
        if hasattr(mod, "qa_pass_class_rows"):        # the repaired build
            for r in nonterm:
                for d in (r.get("destinations") or []):
                    if d in members and d not in text:
                        out.append(f"PROMPT_HANDOFF_RECEIVER:{pid}:{d}")
        else:                                          # the installed build
            if "NEXT_PROMPT_HANDOFF" not in text:
                out.append(f"PROMPT_HANDOFF_CONTRACT:{pid}")
    return sorted(out)


def drop_receiver(pid, receiver):
    def f(data):
        data["bodies"][pid] = data["bodies"][pid].replace(receiver, "REDACTED-RECEIVER")
    return f


def break_class_map_receiver(data):
    data["bodies"]["QA-120"] = data["bodies"]["QA-120"].replace("`CL-E-10 —", "`CL-E-40 —")


def break_class_map_page_id(data):
    data["bodies"]["QA-120"] = data["bodies"]["QA-120"].replace(
        "3db4590a05eb811a8578d75885c16cac", "0000000000000000000000000000dead")


def repipe_class_map(data):
    """Re-render QA-120's HTML class map as a Markdown pipe table with bare URLs."""
    t = data["bodies"]["QA-120"]
    block = re.search(r"<table header-row=\"true\">.*?</table>", t, re.S)
    rows = re.findall(
        r"<tr>\s*<td>`PASS`</td>\s*<td>`(EPIC|CRD)`</td>\s*<td>`(CL-[EC]-10) — ([^`]+)` at "
        r"<mention-page url=\"([^\"]+)\"/></td>\s*</tr>", block.group(0), re.S)
    assert len(rows) == 2, rows
    lines = ["| Result | Verified change class | Required receiver |", "|---|---|---|"]
    for cls, dest, title, url in rows:
        lines.append(f"| `PASS` | `{cls}` | `{dest} — {title}` at {url} |")
    data["bodies"]["QA-120"] = t.replace(block.group(0), "\n".join(lines))


BASE = ROOT / "base"
WORK = ROOT / "work"

print("=== SF10-03 — QA-120 class map ===")
case("installed build reports a defect on the real body", BASE, None, qa_errors, ["QA_PASS_BODY_CLASS_MAP"])
case("repaired build reads the real HTML body", WORK, None, qa_errors, [])
case("repaired build also reads the pipe rendering", WORK, repipe_class_map, qa_errors, [])
case("repaired build still rejects a wrong receiver", WORK, break_class_map_receiver, qa_errors,
     ["QA_PASS_BODY_CLASS_MAP"])
case("repaired build still rejects a wrong page id", WORK, break_class_map_page_id, qa_errors,
     ["QA_PASS_BODY_CLASS_MAP"])

print("\n=== SF10-06 — handoff obligation ===")
case("installed build reports GCFPE-MGMT-10", BASE, None, handoff_errors,
     ["PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10"])
case("repaired build clears the corpus", WORK, None, handoff_errors, [])
case("repaired build catches a dropped receiver (PR-30 -> PR-35)", WORK,
     drop_receiver("PR-30", "PR-35"), handoff_errors, ["PROMPT_HANDOFF_RECEIVER:PR-30:PR-35"])
case("repaired build catches GCFPE-MGMT-10 dropping PR-10", WORK,
     drop_receiver("GCFPE-MGMT-10", "PR-10"), handoff_errors,
     ["PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10"])

print(f"\n{'ALL CASES AS EXPECTED' if FAIL == 0 else f'{FAIL} CASE(S) NOT AS EXPECTED'}")
sys.exit(1 if FAIL else 0)
