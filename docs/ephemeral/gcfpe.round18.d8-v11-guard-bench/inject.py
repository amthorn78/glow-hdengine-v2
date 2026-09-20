#!/usr/bin/env python3
"""Round 18 bench — inject one prohibited-gate placement and report every guard layer.

    python3 inject.py <pristine-rig> <work-dir> [placement ...]

<pristine-rig> is an unmodified extraction of the two .skill packages, side by side.
It is never written to: each placement is applied to a fresh copy at <work-dir>.
With no placement named, every placement runs.

Each run applies the mutation identically to BOTH contract copies and re-stamps only
the byte pins that any lawful contract edit must re-stamp:
EXPECTED_CANDIDATE_CONTRACT_SHA256, EXPECTED_CANDIDATE_CONTRACT_BYTES, and the
validation profile's candidate_contract.sha256 / byte_count. EXPECTED_ROUTING_SURFACE
is never touched. A JSON round-trip at indent=2, ensure_ascii=False, with one trailing
newline is byte-stable for these contracts, so nothing but the injection changes.
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys

CF = "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
FV = "flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
PROFILE = "flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json"
VALIDATOR = "flowmaster-validate/scripts/validate_gcfpe_20260914.py"

# The prohibited gate D8 forbids: a mandatory post-addendum PF10 comparison.
GATE = ("Before producing, compare the current controlled PF10 against the previously "
        "approved PF10 addendum baseline and HALT_AND_RETURN_TO_NATHAN on divergence.")


def _set(obj, key):
    return lambda d: d["pf10_addendum_contract"].__setitem__(key, GATE)


def _append(key):
    return lambda d: d["pf10_addendum_contract"][key].append(GATE)


def _nested_dotted(d):
    d["pf10_addendum_contract"]["native_outcome_normalization"]["PENDING.X"] = GATE


def _index_collision(d):
    d["pf10_addendum_contract"]["forbidden_fields"] = {"0": GATE}


def _reverse(d):
    d["pf10_addendum_contract"]["forbidden_fields"].reverse()


def _dict_in_list(d):
    d["pf10_addendum_contract"]["forbidden_fields"].append({"branch_id": "x", "rule": GATE})


def _lawful_promotion(d):
    # The real exempt names, from CONTRACT_LIFECYCLE_KEYS. Must stay clean.
    d.update({"selection_status": "SELECTED_PRODUCTION", "status": "SELECTED",
              "promoted_at": "2026-09-20T13:26:10Z", "selected_release": "GCFPE-20260914.1",
              "selected_prompt_version": "091426.1", "selected_member_count": 55,
              "selection_claim": "GCFPE-20260914.1"})


PLACEMENTS = {
    # v10's tenth defeat: a literal dotted key collides with a derived nested path.
    "G1-dotted-producers-RS-20":   _set(None, "producers.RS-20"),
    "G2-dotted-producers-CF-C-30": _set(None, "producers.CF-C-30"),
    "G3-dotted-normalization":     _set(None, "native_outcome_normalization.PENDING"),
    "G4-dotted-nested":            _nested_dotted,
    "G5-bracket-shaped-key":       _set(None, "forbidden_fields[8]"),
    "G6-index-collision":          _index_collision,
    # v10's second defeat: a scalar list element receives no path at all.
    "H1-append-forbidden_fields":  _append("forbidden_fields"),
    "H2-append-never_for":         _append("never_for"),
    "H3-append-required_fields":   _append("required_fields"),
    "H4-append-producer_set":      _append("exact_producer_set"),
    "H5-reverse-forbidden_fields": _reverse,
    "H6-dict-in-list":             _dict_in_list,
    # Controls.
    "CONTROL-ordinary-key":        _set(None, "post_approval_divergence_check"),
    "CONTROL-lawful-promotion":    _lawful_promotion,
}

# What each placement must do to the D8 GUARD LAYERS — not to the four gates.
# Judging on the layers is both stricter and more informative: a gate can go red for
# an unrelated reason (H4 also trips PF10_PRODUCER_SET), and a lawful promotion
# legitimately fails G1's candidate-lifecycle check because this contract is pinned as
# an UNSELECTED_CANDIDATE, which is not a guard finding. The gates are still printed.
EXPECT_GUARD_FIRES = {k for k in PLACEMENTS if k != "CONTROL-lawful-promotion"}


def dumps(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode()


def apply(work, mutate):
    d = json.loads(open(os.path.join(work, CF), "rb").read())
    mutate(d)
    new = dumps(d)
    for rel in (CF, FV):
        open(os.path.join(work, rel), "wb").write(new)
    sha = hashlib.sha256(new).hexdigest()
    p = os.path.join(work, VALIDATOR)
    src = open(p).read()
    src = re.sub(r'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "[0-9a-f]{64}"',
                 'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "%s"' % sha, src)
    src = re.sub(r"EXPECTED_CANDIDATE_CONTRACT_BYTES = \d+",
                 "EXPECTED_CANDIDATE_CONTRACT_BYTES = %d" % len(new), src)
    open(p, "w").write(src)
    pp = os.path.join(work, PROFILE)
    prof = json.load(open(pp))
    prof["candidate_contract"]["sha256"] = sha
    prof["candidate_contract"]["byte_count"] = len(new)
    open(pp, "wb").write(dumps(prof))


def layers(work):
    sdir = os.path.join(work, "flowmaster-validate", "scripts")
    sys.path.insert(0, sdir)
    for stale in [k for k in list(sys.modules) if k.startswith("validate_") or k == "m"]:
        del sys.modules[stale]
    spec = importlib.util.spec_from_file_location("m", os.path.join(work, VALIDATOR))
    m = importlib.util.module_from_spec(spec)
    sys.modules["m"] = m
    spec.loader.exec_module(m)
    sys.path.remove(sdir)
    c = json.load(open(os.path.join(work, CF)))
    surf, rows = m.routing_surface(c)
    out = {
        "pin_changed": surf != m.EXPECTED_ROUTING_SURFACE or rows != m.EXPECTED_ROUTING_SURFACE_ROWS,
        "L2_out_of_surface": m.out_of_surface_pf10_branches(c),
        "L3_key_drift": m.pf10_addendum_contract_key_drift(c),
        "L4_top_level_drift": m.contract_top_level_key_drift(c),
        "L5_lifecycle_shape": m.contract_lifecycle_key_shape(c),
        "overlay": m.unallowed_terminal_pf10_overlay_branches(c),
    }
    if hasattr(m, "addendum_list_value_drift"):          # v11 only
        out["L6_list_value_drift"] = m.addendum_list_value_drift(c)
    return out


def main():
    pristine, work = sys.argv[1], sys.argv[2]
    names = sys.argv[3:] or list(PLACEMENTS)
    here = os.path.dirname(os.path.abspath(__file__))
    failures = []
    for name in names:
        if os.path.isdir(work):
            shutil.rmtree(work)
        shutil.copytree(pristine, work, symlinks=True)
        # Setup and evaluation are judged differently, and conflating them is a silent pass:
        # if apply() raises, nothing was injected and no guard layer ran, so crediting that
        # as fail-closed would let a run print "as expected" having tested nothing.
        harness_error = None
        L = {}
        before = open(os.path.join(work, CF), "rb").read()
        try:
            apply(work, PLACEMENTS[name])
        except Exception as exc:
            harness_error = "apply() raised %s: %s" % (type(exc).__name__, exc)
        else:
            if open(os.path.join(work, CF), "rb").read() == before:
                harness_error = "apply() changed nothing; the placement did not land"
        if harness_error is None:
            try:
                L = layers(work)
            except Exception as exc:                      # HERE a crash IS fail-closed
                L = {"raised": "%s: %s" % (type(exc).__name__, exc)}
        print("=" * 78)
        print("PLACEMENT %s" % name)
        if harness_error:
            # Never a pass. Nothing was tested, so there is no guard result to report.
            print("  HARNESS FAILURE        %s" % harness_error)
            print("  VERDICT *** HARNESS FAILURE - nothing was tested ***")
            failures.append("%s (harness)" % name)
            continue
        gates = subprocess.run(["bash", os.path.join(here, "run_gates.sh"), work],
                               capture_output=True, text=True).stdout.strip()
        green = ("G1 rc=0" in gates and "ok=True errors=[]" in gates
                 and "fixture_suite_ok=True" in gates and "FLOWMASTER_SUITE_PASS" in gates)
        # A raise from the validator IS fail-closed: non-zero exit, nothing admitted.
        fired = bool(L.get("raised")) or bool(L.get("pin_changed")) or any(
            L.get(k) for k in ("L2_out_of_surface", "L3_key_drift", "L4_top_level_drift",
                               "L5_lifecycle_shape", "L6_list_value_drift", "overlay"))
        for k, v in L.items():
            if v not in ([], False):
                print("  %-22s %s" % (k, v))
        if not any(v not in ([], False) for v in L.values()):
            print("  %-22s %s" % ("guard layers", "all silent"))
        for line in gates.splitlines():
            print("  " + line)
        print("  guard fired: %s   all four gates green: %s" % (fired, green))
        if fired != (name in EXPECT_GUARD_FIRES):
            failures.append(name)
            print("  VERDICT *** UNEXPECTED *** expected guard to %s"
                  % ("fire" if name in EXPECT_GUARD_FIRES else "stay silent"))
        else:
            print("  VERDICT as expected")
    print("=" * 78)
    print("placements run: %d  unexpected: %s" % (len(names), failures or "none"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
