#!/usr/bin/env python3
"""Apply the pre-registered acceptance gates to readings produced by score_ladder.py.

usage:
  evaluate_ladder.py acceptance-v7.json PART_A_RUN1.json PART_A_RUN2.json PART_B.json
  evaluate_ladder.py acceptance-hd-v2.json CASES_RUN1.json [CASES_RUN2.json] [JOBS.json]
Readings are matched to cases by label, and a missing or extra reading stops the evaluation."""
import json
import sys

LEVELS = ["low", "medium", "high", "extra high", "max"]


def load(path):
    return json.load(open(path, encoding="utf-8")) if path and path != "-" else None


def aligned(cases, results, what):
    if results is None:
        return None
    labels = [c["label"] for c in cases]
    got = [r.get("label") for r in results]
    if got != labels:
        sys.exit(f"refused: {what} readings do not match the cases by label and order: {got} != {labels}")
    return results


def check(case, r):
    if "error" in r:
        return False, ["not read: " + r["error"]]
    miss = []
    if case.get("expect_level") and r["level"] not in case["expect_level"]:
        miss.append(f"level {r['level']} not in {case['expect_level']}")
    if case.get("expect_ultracode") is not None and r["ultracode"] != case["expect_ultracode"]:
        miss.append(f"ultracode {'on' if r['ultracode'] else 'off'} (P {r['p_ultracode']:.2f}), expected {'on' if case['expect_ultracode'] else 'off'}")
    if case.get("expect_model") and r["model"] != case["expect_model"]:
        miss.append(f"model {r['model']} (P Fable {r['model_probabilities']['Fable 5.1']:.2f}), expected {case['expect_model']}")
    return not miss, miss


def line(r):
    if "error" in r:
        return f"not read ({r['error']})"
    return (f"{r['cell']} | effort {r['effort_score']:.2f} {r['level_probabilities']} | P(ultra) {r['p_ultracode']:.2f}"
            f" | P(Fable) {r['model_probabilities']['Fable 5.1']:.2f}")


def main():
    acc = load(sys.argv[1])
    hd = acc["version"].startswith("hd")
    cases = acc["part_a"]
    a1 = aligned(cases, load(sys.argv[2]), "run 1")
    a2 = aligned(cases, load(sys.argv[3]) if len(sys.argv) > 3 else None, "run 2")
    extra = load(sys.argv[4]) if len(sys.argv) > 4 else None

    print(f"== {acc['version']} cases, run 1")
    passed, misses = 0, {}
    for c, r in zip(cases, a1):
        ok, miss = check(c, r)
        passed += ok
        misses[c["label"]] = miss
        print(f"{'PASS' if ok else 'FAIL'} {c['label']}: {line(r)}" + (f" | MISS: {'; '.join(miss)}" if miss else ""))
    n = len(cases)
    gates = {}
    if hd:
        gates["A"] = passed == n
        print(f"Gate A: {passed}/{n} cases pass (need {n}) -> {'PASS' if gates['A'] else 'FAIL'}")
    else:
        ultra_on = [(c, r) for c, r in zip(cases, a1) if c.get("expect_ultracode") is True]
        fable = [(c, r) for c, r in zip(cases, a1) if c.get("expect_model") == "Fable 5.1"]
        ultra_ok = all("error" not in r and r["ultracode"] for c, r in ultra_on)
        fable_ok = all("error" not in r and r["model"] == "Fable 5.1" for c, r in fable)
        gates["A"] = passed >= n - 1 and ultra_ok and fable_ok
        print(f"Gate A: {passed}/{n} cases pass (need {n - 1}); ultracode-on cases all on: {ultra_ok} "
              f"({', '.join(c['label'].split()[0] for c, r in ultra_on)}); Fable cases all Fable: {fable_ok} "
              f"({', '.join(c['label'].split()[0] for c, r in fable)}) -> {'PASS' if gates['A'] else 'FAIL'}")

    if a2:
        def maxdiff(get):
            d = [abs(get(x) - get(y)) for x, y in zip(a1, a2) if "error" not in x and "error" not in y]
            return round(max(d), 2) if d else None
        same = sum(1 for x, y in zip(a1, a2) if x.get("cell") == y.get("cell"))
        p2 = sum(check(c, r)[0] for c, r in zip(cases, a2))
        print(f"Part C (noise, reported): same cell on {same}/{n}; max |d effort score| {maxdiff(lambda r: r['effort_score'])}; "
              f"max |d P(ultracode)| {maxdiff(lambda r: r['p_ultracode'])}; max |d P(Fable)| {maxdiff(lambda r: r['model_probabilities']['Fable 5.1'])}; "
              f"run 2 cases passing: {p2}/{n}")

    if hd and extra is not None:
        jobs = acc["jobs"]
        aligned(jobs, extra, "jobs")
        print("== Jobs J0 to J6 (reported)")
        for j, r in zip(jobs, extra):
            print(f"  {j['label']}: {line(r)}")

    if not hd and extra is not None:
        bc = acc["part_b"]
        b = aligned(bc, extra, "part B")
        ok_rows = [(c, r) for c, r in zip(bc, b) if "error" not in r]
        exact = sum(1 for c, r in ok_rows if r["level"] in c["pick_level_exact_set"])
        within = sum(1 for c, r in ok_rows if abs(LEVELS.index(r["level"]) - LEVELS.index(c["pick_level"])) <= 1
                     or r["level"] in c["pick_level_exact_set"])
        model_all = sum(1 for c, r in ok_rows if r["model"] == c["pick_model"])
        fable_picks = [(c, r) for c, r in zip(bc, b) if c["pick_model"] == "Fable 5.1"]
        opus_picks = [(c, r) for c, r in zip(bc, b) if c["pick_model"] == "Opus 5.5"]
        fable_hit = sum(1 for c, r in fable_picks if "error" not in r and r["model"] == "Fable 5.1")
        opus_hit = sum(1 for c, r in opus_picks if "error" not in r and r["model"] == "Opus 5.5")
        gated = [(c, r) for c, r in zip(bc, b) if c["ultracode_gated"]]
        off_ok = sum(1 for c, r in gated if "error" not in r and not r["ultracode"])
        print(f"== Part B: {len(bc)} recorded texts with Nathan's picks")
        for c, r in zip(bc, b):
            tag = "gated-off" if c["ultracode_gated"] else ("override" if c["override_of_v6"] else "reported")
            print(f"  [{tag:9}] {c['label'][:58]:58} pick {c['pick_cell']:24} | v7 {line(r)}")
        gates["B_effort"] = exact >= 24 and within >= 30
        gates["B_model"] = model_all >= 26 and fable_hit >= 6 and opus_hit >= 18
        gates["B_ultracode"] = off_ok >= 19
        print(f"Gate B_effort: exact {exact}/31 (need 24), within one level {within}/31 (need 30) -> {'PASS' if gates['B_effort'] else 'FAIL'}")
        print(f"Gate B_model: same model {model_all}/31 (need 26); Fable picks {fable_hit}/{len(fable_picks)} (need 6); "
              f"Opus picks {opus_hit}/{len(opus_picks)} (need 18) -> {'PASS' if gates['B_model'] else 'FAIL'}")
        print(f"Gate B_ultracode: off on {off_ok}/{len(gated)} gated texts (need 19) -> {'PASS' if gates['B_ultracode'] else 'FAIL'}")
        print("Reported, not gated: ultracode on the other texts")
        for c, r in zip(bc, b):
            if not c["ultracode_gated"]:
                print(f"  {c['label'][:58]:58} pick {c['pick_cell']:24} | P(ultra) {r.get('p_ultracode')} | {'on' if r.get('ultracode') else 'off'}")
        print("Reported, not gated: the 9 texts where Nathan overrode the v6 reading")
        for c, r in zip(bc, b):
            if c["override_of_v6"]:
                print(f"  {c['label'][:58]:58} v6 {c['v6_cell']:24} pick {c['pick_cell']:24} v7 {r.get('cell', 'not read')}")

    accepted = all(gates.values()) and ("B_effort" in gates or hd)
    print("OVERALL:", "ACCEPTED" if accepted else "NOT ACCEPTED", gates)


if __name__ == "__main__":
    main()
