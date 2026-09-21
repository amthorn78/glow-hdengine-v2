#!/usr/bin/env python3
"""SF10-03 / SF10-06 bench.

Usage:
    bench.py --base <installed-tree> --work <repaired-tree> --bodies <55-body-corpus> \
             [--registry docs/prompt_ecosystem_management/project-prompt-contract-registry.md]

No environment variable is required: the script sets `sys.dont_write_bytecode` itself, so
running it exactly as written above leaves both supplied trees byte-unchanged.

The three inputs are environment-resident and are deliberately not committed:

  * `--base` and `--work` are copies of the installed skills tree, which lives in a
    one-way synced directory outside the repository and is installed only by the
    Product Owner.  Vendoring it here would create a second, drifting copy of the
    thing under test.
  * `--bodies` is the 55-prompt corpus.  Prompt bodies are authored in Notion in
    place and are never mirrored into this repository, so the corpus is fetched per
    run -- and this script verifies it before using it, against the `evidence_contract`
    SHA-256 recorded for each of the 55 rows in
    `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`, which IS
    repository-resident.  An earlier revision accepted any 55 Markdown files by count
    alone while its own documentation promised that verification, so a stale or
    substituted corpus could have produced exit 0 and been credited as evidence for
    the current one.

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
import argparse, hashlib, importlib.util, json, pathlib, re, shutil, sys, tempfile

# Bytecode writing is disabled HERE rather than left to the caller's environment.  `load()`
# calls `exec_module` on a validator inside each supplied tree, and CPython would write
# `__pycache__/*.pyc` beside it -- mutating inputs this bench describes as frozen, and
# contaminating a `--work` tree that is later packaged.  That is not hypothetical: it
# happened in this session, putting two .pyc files into a .skill archive, and it happened
# because a measurement script relied on an environment variable the usage block never
# showed.  A harness must not depend on how it was invoked to leave its inputs untouched.
sys.dont_write_bytecode = True

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


REPO = pathlib.Path(__file__).resolve().parents[3]
REGISTRY_DEFAULT = pathlib.Path("docs/prompt_ecosystem_management/project-prompt-contract-registry.md")
_REGISTRY_DIGESTS: dict[str, str] | None = None


def registry_digests(registry_path: pathlib.Path) -> dict[str, str]:
    """The 55 `prompt_key` -> `evidence_contract` SHA-256 pairs, from the approved registry.

    Parsed with a regex rather than a YAML loader so the bench carries no dependency
    beyond the standard library.  Each row's digest is the one recorded under
    `evidence_contract` as "SHA-256 of that extraction".
    """
    global _REGISTRY_DIGESTS
    if _REGISTRY_DIGESTS is not None:
        return _REGISTRY_DIGESTS
    if not registry_path.is_file():
        die(f"no registry at {registry_path}; pass --registry")
    # The registry is the ROOT OF TRUST for every body-level claim in this package, and it was
    # a caller-supplied path checked only for parsing to 55 pairs.  A stale or fabricated
    # registry holding 55 plausible pairs would have let a DIFFERENT corpus pass the gate while
    # the records described it as the approved one -- the corpus gate trusting its argument.
    # The supplied bytes must now be the committed registry's bytes.
    committed = REPO / REGISTRY_DEFAULT
    if not committed.is_file():
        die(f"the committed registry is missing at {REGISTRY_DEFAULT}; the corpus gate has no "
            f"identity to bind to")
    text = registry_path.read_text(encoding="utf-8")
    if hashlib.sha256(text.encode()).hexdigest() != hashlib.sha256(
            committed.read_bytes()).hexdigest():
        die(f"the supplied registry is not the committed registry.\n"
            f"  supplied:  {registry_path} {hashlib.sha256(text.encode()).hexdigest()[:16]}…\n"
            f"  committed: {REGISTRY_DEFAULT} "
            f"{hashlib.sha256(committed.read_bytes()).hexdigest()[:16]}…\n"
            f"A corpus verified against an unapproved registry is not verified.")
    pairs: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        key = re.match(r"^- prompt_key:\s*(\S+)\s*$", line)
        if key:
            current = key.group(1)
            continue
        digest = re.search(r"SHA-256 of that extraction:\s*([0-9a-f]{64})", line)
        if digest and current:
            pairs.setdefault(current, digest.group(1))
    if len(pairs) != 55:
        die(f"expected 55 registry digests in {registry_path}, parsed {len(pairs)}")
    _REGISTRY_DIGESTS = pairs
    return pairs


def read_bodies(bodies_dir: pathlib.Path, registry_path: pathlib.Path) -> dict[str, str]:
    """Load the corpus and refuse to proceed unless it is the corpus the registry names."""
    expected = registry_digests(registry_path)
    found = {p.stem: p for p in sorted(bodies_dir.glob("*.md"))}
    if set(found) != set(expected):
        missing = sorted(set(expected) - set(found))
        extra = sorted(set(found) - set(expected))
        die(f"corpus in {bodies_dir} is not the registry's 55 prompts; missing {missing}, unexpected {extra}")
    bodies: dict[str, str] = {}
    mismatched: list[str] = []
    for prompt_id, path in found.items():
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected[prompt_id]:
            mismatched.append(prompt_id)
        bodies[prompt_id] = raw.decode("utf-8")
    if mismatched:
        die(f"{len(mismatched)} body/bodies do not match their registry evidence_contract "
            f"digest: {mismatched}. The corpus is stale or substituted; refusing to run.")
    return bodies


def read_contract(tree: pathlib.Path) -> dict:
    path = tree / CONTRACT
    if not path.is_file():
        die(f"no contract at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def case(name, tree, mutate, predicate, expect, *, bodies_dir, registry):
    """Phase 1 then phase 3, separated."""
    global FAIL
    mod = load(tree)
    try:
        data = {"bodies": read_bodies(bodies_dir, registry), "contract": read_contract(tree)}
        # The landed-mutation guard must cover BOTH halves of the input.  It hashed only
        # the bodies until a contract-mutating case existed, at which point it misfired on
        # a mutation that had in fact landed -- and, worse, would have scored a
        # contract-mutating case that changed nothing at all.  No case exercised that path
        # before, which is exactly how a half-built guard survives.
        before = json.dumps(data, sort_keys=True, default=repr)
        if mutate is not None:
            mutate(data)
            if json.dumps(data, sort_keys=True, default=repr) == before:
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
    # Every handoff-related code the two builds can emit.  An earlier revision omitted
    # PROMPT_HANDOFF_LITERAL, so the bench filtered out the very error its own literal
    # case asserted and reported a working check as missing -- the instrument hiding the
    # signal rather than the subject failing.
    return sorted(e for e in errors
                  if e.startswith(("PROMPT_HANDOFF_CONTRACT", "PROMPT_HANDOFF_LITERAL",
                                   "PROMPT_HANDOFF_RECEIVER",
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


def drop_literal(prompt_id):
    """Remove the handoff-block literal from a prompt the registry requires it on.

    The replacement must not itself contain the literal.  A first version substituted
    `NEXT_PROMPT_HANDOFF_REMOVED_BY_FIXTURE`, which still contains the token, so the
    check correctly stayed silent and the case looked like a missing check rather than a
    broken fixture.  The assertion below makes that failure mode impossible to repeat.
    """
    def f(data):
        text = data["bodies"][prompt_id].replace("NEXT_PROMPT_HANDOFF", "HANDOFF_BLOCK_ELIDED")
        if "NEXT_PROMPT_HANDOFF" in text:
            die(f"fixture invalid: the literal still appears in {prompt_id} after removal")
        data["bodies"][prompt_id] = text
    return f


def collide_receiver_prefix(prompt_id, receiver, longer):
    """Replace every complete `receiver` token with `longer`, which contains it.

    Models the prefix collision: a body that has dropped all real `QA-10` references
    while retaining `QA-100` satisfies a plain substring test.  The fixture asserts the
    substring is still present afterwards, so a failure to fire cannot be explained by
    the name having disappeared.
    """
    def f(data):
        text = re.sub(rf"(?<![0-9A-Za-z-]){re.escape(receiver)}(?![0-9A-Za-z-])",
                      longer, data["bodies"][prompt_id])
        if receiver not in text:
            die(f"fixture invalid: {receiver} is not even a substring of {prompt_id} after "
                f"the swap, so the collision is not modelled")
        data["bodies"][prompt_id] = text
    return f


def bury_receiver_in_enum_token(prompt_id, receiver, enum_suffix):
    """Replace every complete `receiver` token with `receiver + enum_suffix`.

    Models the underscore hazard with a token the corpus really contains: the bodies
    write `PR_RETURN_PHASE` values as `PR-30_PREPUBLICATION`, which is an enum value and
    not a routing mention.  If `_` were absent from the boundary class, a body whose only
    remaining `PR-30` text sat inside that token would satisfy a branch routing to
    `PR-30`.  The fixture asserts afterwards that the receiver survives as a substring
    but no longer as a complete identifier, so a fire cannot be explained by the name
    having simply disappeared and a miss cannot be explained by the mutation not landing.
    """
    def f(data):
        buried = receiver + enum_suffix
        text = re.sub(rf"(?<![0-9A-Za-z_-]){re.escape(receiver)}(?![0-9A-Za-z_-])",
                      buried, data["bodies"][prompt_id])
        if receiver not in text:
            die(f"fixture invalid: {receiver} is not even a substring of {prompt_id} "
                f"after burial, so the hazard is not modelled")
        if buried not in text:
            die(f"fixture invalid: {buried} is absent from {prompt_id}, so the mutation "
                f"did not land")
        if re.search(rf"(?<![0-9A-Za-z_-]){re.escape(receiver)}(?![0-9A-Za-z_-])", text):
            die(f"fixture invalid: {prompt_id} still names {receiver} as a complete "
                f"identifier, so a passing check would be correct rather than blind")
        data["bodies"][prompt_id] = text
    return f


def typo_destination(prompt_id, bad, label):
    """Replace a real member destination with a near-miss string such as `PR-300`.

    A value that is neither a member prompt nor a declared symbol used to be skipped in
    silence -- indistinguishable from `NATHAN_PROCEED` -- so the receiver the row meant to
    name went unchecked.  The fixture asserts the bad value landed and that it is neither a
    member nor a symbol, so a fire cannot be explained by it accidentally being either.
    """
    def f(data):
        rows = [r for r in data["contract"].get("state_routes", {}).get(prompt_id, [])
                if isinstance(r, dict) and r.get("public_result") is True
                and r.get("terminal_for_invocation") is not True
                and isinstance(r.get("destinations"), list) and r["destinations"]]
        if not rows:
            die(f"fixture invalid: {prompt_id} has no non-terminal public row, so {label} "
                f"cannot be modelled")
        row = rows[0]
        row["destinations"] = [bad] + list(row["destinations"])[1:]
        if bad not in row["destinations"]:
            die(f"fixture invalid: {bad} did not land in {prompt_id}")
    return f


def blank_destinations(prompt_id, mode, label):
    """Set a real non-terminal public row's `destinations` to null, or remove the key.

    A non-terminal public row's whole meaning is that the invocation continues somewhere,
    so a row declaring no route at all is malformed.  The old guard read
    `destinations is not None and not isinstance(..., list)`, so null and absent both
    slipped through and the loop then iterated nothing -- silence where a verdict belonged.
    """
    def f(data):
        rows = [r for r in data["contract"].get("state_routes", {}).get(prompt_id, [])
                if isinstance(r, dict) and r.get("public_result") is True
                and r.get("terminal_for_invocation") is not True
                and isinstance(r.get("destinations"), list) and r["destinations"]]
        if not rows:
            die(f"fixture invalid: {prompt_id} has no non-terminal public row with a "
                f"non-empty destinations list, so {label} cannot be modelled")
        row = rows[0]
        if mode == "null":
            row["destinations"] = None
        elif mode == "absent":
            del row["destinations"]
        else:
            die(f"fixture invalid: unknown mode {mode!r}")
        if mode == "null" and row.get("destinations") is not None:
            die(f"fixture invalid: {prompt_id}'s destinations are not null")
        if mode == "absent" and "destinations" in row:
            die(f"fixture invalid: {prompt_id}'s destinations key is still present")
    return f


def corrupt_destination_element(prompt_id, bad_element, label):
    """Put one malformed element into a real nonterminal-public row's `destinations`.

    The container was already validated; the elements were not.  A non-string scalar is
    silently absent from `EXPECTED_MEMBERS` and skipped without a word, and an unhashable
    element -- a dict or a list -- makes the membership test raise `TypeError`, aborting
    body validation rather than reporting a contract defect.  Both must instead surface as
    the structured `MALFORMED_DESTINATIONS` the code already promises.

    The fixture asserts it found a real row and actually changed it, so a passing case
    cannot be a mutation that never landed.
    """
    def f(data):
        rows = [r for r in data["contract"].get("state_routes", {}).get(prompt_id, [])
                if isinstance(r, dict) and r.get("public_result") is True
                and isinstance(r.get("destinations"), list) and r["destinations"]]
        if not rows:
            die(f"fixture invalid: {prompt_id} has no public row with a non-empty "
                f"destinations list, so {label} cannot be modelled")
        row = rows[0]
        before = list(row["destinations"])
        row["destinations"] = [bad_element] + before[1:]
        if row["destinations"] == before:
            die(f"fixture invalid: {prompt_id}'s destinations are unchanged, so the "
                f"{label} mutation did not land")
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
    ap.add_argument("--registry", type=pathlib.Path, default=REGISTRY_DEFAULT,
                    help="approved registry whose evidence_contract digests the corpus must match")
    args = ap.parse_args()
    for label, path in (("--base", args.base), ("--work", args.work), ("--bodies", args.bodies)):
        if not path.is_dir():
            die(f"{label} is not a directory: {path}")
    base, work, bodies, registry = args.base, args.work, args.bodies, args.registry
    digests = registry_digests(registry)
    print(f"corpus gate: {len(digests)} registry digests loaded from {registry}")
    read_bodies(bodies, registry)
    print(f"corpus gate: all {len(digests)} bodies match their recorded evidence_contract digest\n")

    print("=== SF10-03 — QA-120 class map (validate_qa_closure_bodies) ===")
    case("installed build reports a defect on the real body", base, None, qa_errors,
         ["QA_PASS_BODY_CLASS_MAP"], bodies_dir=bodies, registry=registry)
    case("repaired build reads the real HTML body", work, None, qa_errors, [], bodies_dir=bodies, registry=registry)
    case("repaired build also reads the pipe rendering", work, repipe_class_map, qa_errors, [],
         bodies_dir=bodies, registry=registry)
    case("repaired build still rejects a wrong receiver", work, break_class_map_receiver, qa_errors,
         ["QA_PASS_BODY_CLASS_MAP"], bodies_dir=bodies, registry=registry)
    case("repaired build still rejects a wrong page id", work, break_class_map_page_id, qa_errors,
         ["QA_PASS_BODY_CLASS_MAP"], bodies_dir=bodies, registry=registry)

    print("\n=== SF10-06 — handoff obligation (validate_prompt_bodies) ===")
    case("installed build reports GCFPE-MGMT-10", base, None, handoff_errors,
         ["PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10"], bodies_dir=bodies, registry=registry)
    case("repaired build clears the corpus, GCFPE-MGMT-10 and PR-50 included",
         work, None, handoff_errors, [], bodies_dir=bodies, registry=registry)
    case("repaired build catches a dropped receiver (PR-30 -> PR-35)", work,
         drop_receiver("PR-30", "PR-35"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:PR-30:PR-35"], bodies_dir=bodies, registry=registry)
    case("repaired build catches GCFPE-MGMT-10 dropping PR-10", work,
         drop_receiver("GCFPE-MGMT-10", "PR-10"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10"], bodies_dir=bodies, registry=registry)

    print("\n=== SF10-06 — the registry's handoff literal, kept alongside the receiver check ===")
    print("  The approved registry requires NEXT_PROMPT_HANDOFF on 53 of its 55 rows and exempts")
    print("  exactly GCFPE-MGMT-10 and PR-50. The clean-corpus case above passes while both of")
    print("  those bodies lack the token, which is the exemption working; the case below proves")
    print("  the requirement still bites everywhere else. The installed build is not contrasted")
    print("  here: it also catches a dropped literal on PR-30, because PR-30 has a non-terminal")
    print("  public branch. The two builds differ only on GCFPE-MGMT-10, which is the case above.")
    case("repaired build catches a dropped handoff literal (PR-30)", work,
         drop_literal("PR-30"), handoff_errors, ["PROMPT_HANDOFF_LITERAL:PR-30"],
         bodies_dir=bodies, registry=registry)

    print("\n=== SF10-06 — receiver ids match as complete tokens ===")
    print("  QA-10 is a prefix of QA-100, the one such collision among the 55 ids. MGR-10 routes")
    print("  to QA-10 and names it once; swapping that token for QA-100 leaves the substring")
    print("  present, so a substring test would pass and boundary matching must not.")
    case("repaired build catches a prefix-collision receiver (MGR-10 -> QA-10)", work,
         collide_receiver_prefix("MGR-10", "QA-10", "QA-100"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:MGR-10:QA-10"], bodies_dir=bodies, registry=registry)

    print("\n=== SF10-06 — `_` is an identifier character too ===")
    print("  Review asked whether `_` belongs in the boundary class. It does, and the corpus")
    print("  proves it rather than a hypothetical: `PR_RETURN_PHASE` values are written")
    print("  `PR-30_PREPUBLICATION` and `PR-30_POSTPUBLICATION`, and OPS-20 writes")
    print("  `NOT_PRODUCED_BY_OPS-20` -- 54 underscore-adjacent prompt-id occurrences in all.")
    print("  Those are enum tokens, not routing mentions. ESC-40 is the subject because it is")
    print("  real on both halves: it declares PR-30 as a receiver AND already carries six")
    print("  `PR-30_` enum tokens beside its five complete mentions. Burying those five leaves")
    print("  a body that discusses `PR-30_PREPUBLICATION` constantly and never names PR-30 --")
    print("  the exact shape of the hazard, not an invented one. Adding `_` to the class flips")
    print("  none of the 166 declared receiver checks on the clean corpus, so this closes a")
    print("  reachable hole without moving a single current verdict.")
    case("repaired build catches a receiver buried in an enum token (ESC-40 -> PR-30)", work,
         bury_receiver_in_enum_token("ESC-40", "PR-30", "_PREPUBLICATION"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:ESC-40:PR-30"], bodies_dir=bodies, registry=registry)

    print("\n=== SF10-06 — malformed route data fails closed through the structured path ===")
    print("  The container was validated; the elements were not. Review found the gap and")
    print("  understated it: an int element is silently absent from EXPECTED_MEMBERS and")
    print("  skipped without a word, and BOTH a dict and a list element raise")
    print("  `TypeError: unhashable type` from the membership test -- which aborts body")
    print("  validation entirely rather than reporting a contract defect. That is the same")
    print("  crash-instead-of-verdict shape as the installed build's fixture-suite failure.")
    print("  All three now surface as MALFORMED_DESTINATIONS, which is what the code already")
    print("  promised. The subject is a real ESC-40 public row, not a synthetic contract.")
    for bad, label in ((7, "a non-string scalar"), ({"prompt": "PR-30"}, "an unhashable dict"),
                       (["PR-30"], "an unhashable list")):
        case(f"repaired build reports MALFORMED_DESTINATIONS for {label}", work,
             corrupt_destination_element("ESC-40", bad, label), handoff_errors,
             ["PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS"],
             bodies_dir=bodies, registry=registry)

    print("  Null and absent are rejected too, and for a reason the shape states: a")
    print("  non-terminal public row's whole meaning is that the invocation continues")
    print("  somewhere, so declaring no route at all is malformed. The old guard read")
    print("  `destinations is not None and not isinstance(..., list)`, so both slipped")
    print("  through and the loop iterated nothing -- silence where a verdict belonged.")
    print("  The contract-level STATE_DESTINATION check already required a list here, so")
    print("  the lax body-level guard also disagreed with the stricter one in the same")
    print("  file. Measured on the real contract first: all 208 non-terminal public rows")
    print("  carry a non-empty list, so requiring one costs nothing. An EMPTY list is")
    print("  deliberately NOT flagged, because STATE_DESTINATION does not flag it either")
    print("  and this check must not be quietly stricter than the rule it mirrors.")
    for mode, label in (("null", "a null destinations value"), ("absent", "an absent destinations key")):
        case(f"repaired build reports MALFORMED_DESTINATIONS for {label}", work,
             blank_destinations("ESC-40", mode, label), handoff_errors,
             ["PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS"],
             bodies_dir=bodies, registry=registry)

    print("\n=== SF10-06 — an unknown destination string is malformed, not a symbol ===")
    print("  The contract declares five non-prompt destinations -- NATHAN_TERMINAL_RETURN (54")
    print("  rows), ORIGINAL_NATIVE_STAGE (39), ACTUAL_OWNER_TERMINAL_RETURN (18),")
    print("  NATHAN_MANUAL_MERGE_ASSERTION (2), NATHAN_PROCEED (1) -- counted from the contract,")
    print("  not recalled. Skipping everything merely absent from EXPECTED_MEMBERS made a typo")
    print("  indistinguishable from a symbol: `PR-300` was ignored exactly as NATHAN_PROCEED is,")
    print("  and the receiver that row meant to name was never checked. With the roster named in")
    print("  SYMBOLIC_DESTINATIONS, anything else fails closed.")
    case("repaired build reports MALFORMED_DESTINATIONS for an unknown destination (ESC-40)", work,
         typo_destination("ESC-40", "PR-300", "a near-miss destination"), handoff_errors,
         ["PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS"],
         bodies_dir=bodies, registry=registry)
    print("  And the five declared symbols must still be skipped rather than flagged -- the")
    print("  clean-corpus case above is that control: all 42 symbolic destinations on")
    print("  non-terminal public rows pass through it without an error.")

    print("\n=== SF10-06 — the predicate's remaining limit, asserted rather than hidden ===")
    print("  The check asserts that each declared receiver is NAMED in the body. It does not")
    print("  bind that name to the operative handoff, so retargeting PR-30's last mention of")
    print("  PR-35 to PR-40 -- while its earlier mentions stay -- is NOT caught. The case")
    print("  below asserts that blind spot so it cannot be mistaken for coverage.")
    print("  Review asked for the stronger check: parse the operative handoff and validate")
    print("  its receiver. It is not implementable against this input, and the reason is")
    print("  categorical rather than a tuning problem. Measured over the 55 bodies: all 68")
    print("  NEXT_PROMPT_HANDOFF occurrences are PROSE, and zero are inside a fenced block.")
    print("  The bodies are prompts -- they instruct a runtime to EMIT a handoff block; the")
    print("  block does not exist until the prompt runs, and this validator never sees a run.")
    print("  There is no operative binding in the artifact to parse. An earlier note here")
    print("  justified the limit by a 17-of-166 false-failure count from one scoped variant;")
    print("  that was a symptom, and this is the cause.")
    case("retargeting the last mention is NOT caught (known limit)", work,
         swap_operative_receiver("PR-30", "PR-35", "PR-40"), handoff_errors, [], bodies_dir=bodies, registry=registry)

    print(f"\n{'ALL CASES AS EXPECTED' if FAIL == 0 else f'{FAIL} CASE(S) NOT AS EXPECTED'}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
