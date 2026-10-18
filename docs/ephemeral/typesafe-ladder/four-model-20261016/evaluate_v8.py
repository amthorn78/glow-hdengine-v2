#!/usr/bin/env python3
"""Apply the pre-registered acceptance gates to readings produced by score_v8.py.

usage:
  evaluate_v8.py acceptance-v8.json PART_A_RUN1.json PART_A_RUN2.json PART_B.json
  evaluate_v8.py acceptance-hd-v3.json CASES_RUN1.json [CASES_RUN2.json] [JOBS.json]
Readings are matched to cases by label and order; a missing or extra reading stops the evaluation.
Exit status 0 when every gate passes, 1 otherwise."""
import json
import sys

RUNGS = ["low", "medium", "high", "extra high", "max", "ultracode"]
MODELS = ["Fable 5.1", "Opus 5.5", "Sonnet 5.5", "Haiku 5.5"]


def load(path):
    return json.load(open(path, encoding="utf-8")) if path and path != "-" else None


def aligned(cases, results, what):
    if results is None:
        return None
    labels, got = [c["label"] for c in cases], [r.get("label") for r in results]
    if got != labels:
        sys.exit(f"refused: {what} readings do not match the cases by label and order: {got} != {labels}")
    return results


def check(case, r):
    if "error" in r:
        return False, ["not read: " + r["error"]]
    miss = []
    if case.get("expect_rung") and r["rung"] not in case["expect_rung"]:
        miss.append(f"rung {r['rung']} (score {r['score']:.2f}) not in {case['expect_rung']}")
    if case.get("expect_model") and r["model"] not in case["expect_model"]:
        miss.append(f"model {r['model']} ({', '.join(f'{m} {p:.2f}' for m, p in r['model_probabilities'].items())}) not in {case['expect_model']}")
    return not miss, miss


def table(cases, run1, run2=None):
    for c, r in zip(cases, run1):
        ok, miss = check(c, r)
        cell = r.get("cell", "not read")
        line = f"  {'pass' if ok else 'FAIL'}  {c['label']}: {cell}"
        if "error" not in r:
            line += f" (score {r['score']:.2f}; " + ", ".join(f"{m} {p:.2f}" for m, p in r["model_probabilities"].items()) + ")"
        if run2 is not None:
            r2 = run2[cases.index(c)]
            line += f"; run 2 {'same' if r2.get('cell') == cell else r2.get('cell', 'not read')}"
        print(line + ("; " + "; ".join(miss) if miss else ""))


def noise(run1, run2):
    ds, dm, changed = 0.0, {m: 0.0 for m in MODELS}, 0
    for a, b in zip(run1, run2):
        if "error" in a or "error" in b:
            continue
        ds = max(ds, abs(a["score"] - b["score"]))
        for m in MODELS:
            dm[m] = max(dm[m], abs(a["model_probabilities"][m] - b["model_probabilities"][m]))
        changed += a["cell"] != b["cell"]
    print(f"  Part C (reported): cells changed on {changed} of {len(run1)}; largest change in effort score {ds:.2f}; "
          + ", ".join(f"P({m}) {v:.2f}" for m, v in dm.items()))


def glow(acc, a1, a2, b):
    cases = acc["part_a"]
    a1, a2 = aligned(cases, a1, "Part A run 1"), aligned(cases, a2, "Part A run 2")
    by = {c["label"]: (c, r) for c, r in zip(cases, a1)}
    met = sum(check(c, r)[0] for c, r in zip(cases, a1))
    fable_ok = all(by[l][1].get("model") == "Fable 5.1" for l in by if l.split()[0] in ("A5", "A6", "A9"))
    haiku_n = sum(by[l][1].get("model") == "Haiku 5.5" for l in by if l.split()[0] in ("A1", "A13", "A14"))
    sonnet_n = sum(by[l][1].get("model") == "Sonnet 5.5" for l in by if l.split()[0] in ("A15", "A16"))
    gate_a = met >= 14 and fable_ok and haiku_n >= 2 and sonnet_n >= 1
    print(f"Part A run 1: {met} of {len(cases)} meet every expectation (need 14); A5, A6, A9 Fable 5.1: {fable_ok}; "
          f"Haiku 5.5 on {haiku_n} of A1, A13, A14 (need 2); Sonnet 5.5 on {sonnet_n} of A15, A16 (need 1). Gate A {'PASS' if gate_a else 'FAIL'}")
    table(cases, a1, a2)
    if a2 is not None:
        noise(a1, a2)
    gates = [gate_a]
    if b is not None:
        bc = acc["part_b"]
        b = aligned(bc, b, "Part B")
        read = [r for r in b if "error" not in r]
        if len(read) != len(b):
            print(f"Part B: {len(b) - len(read)} texts not read; gates B fail")
            return False
        eq = sum(r["rung"] == c["pick_rung"] for c, r in zip(bc, b))
        near = sum(abs(RUNGS.index(r["rung"]) - RUNGS.index(c["pick_rung"])) <= 1 for c, r in zip(bc, b))
        gate_be = eq >= 24 and near >= 30
        fab = [(c, r) for c, r in zip(bc, b) if c["pick_model"] == "Fable 5.1"]
        opu = [(c, r) for c, r in zip(bc, b) if c["pick_model"] == "Opus 5.5"]
        fab_ok = sum(r["model"] == "Fable 5.1" for _, r in fab)
        opu_ok = sum(r["model"] in ("Opus 5.5", "Sonnet 5.5") for _, r in opu)
        haiku_b = sum(r["model"] == "Haiku 5.5" for r in b)
        gate_bm = fab_ok >= 6 and opu_ok >= 18 and haiku_b <= 1
        print(f"B_effort: rung equal to the pick on {eq} of {len(bc)} (need 24), within one rung on {near} (need 30): {'PASS' if gate_be else 'FAIL'}")
        print(f"B_model: Fable 5.1 picks read Fable 5.1 on {fab_ok} of {len(fab)} (need 6); Opus 5.5 picks read Opus 5.5 or Sonnet 5.5 on "
              f"{opu_ok} of {len(opu)} (need 18); Haiku 5.5 on {haiku_b} of {len(b)} (at most 1): {'PASS' if gate_bm else 'FAIL'}")
        son = sum(r["model"] == "Sonnet 5.5" for _, r in opu)
        print(f"B_report: of the {len(opu)} Opus 5.5 picks, {son} read Sonnet 5.5 and {sum(r['model'] == 'Opus 5.5' for _, r in opu)} read Opus 5.5")
        for c, r in zip(bc, b):
            print(f"  {c['label']}: pick {c['pick_cell']}; v6 {c['v6_cell']}; v8 {r['cell']}" + ("; override of v6" if c["override_of_v6"] else ""))
        gates += [gate_be, gate_bm]
    else:
        print("Part B: not supplied; gates B not evaluated")
        gates.append(False)
    return all(gates)


def hd(acc, r1, r2, jobs):
    cases = acc["cases"]
    r1, r2 = aligned(cases, r1, "cases run 1"), aligned(cases, r2, "cases run 2")
    met = sum(check(c, r)[0] for c, r in zip(cases, r1))
    ha7 = [r for c, r in zip(cases, r1) if c["label"].startswith("HA7")][0].get("model") == "Haiku 5.5"
    ok = met == len(cases) and ha7
    print(f"Cases run 1: {met} of {len(cases)} meet every expectation (need all); HA7 Haiku 5.5: {ha7}. {'PASS' if ok else 'FAIL'}")
    table(cases, r1, r2)
    if r2 is not None:
        noise(r1, r2)
    if jobs is not None:
        print("Jobs (reported, not gated):")
        for j in jobs:
            print(f"  {j.get('label')}: {j.get('cell', 'not read')}" + (f" (score {j['score']:.2f})" if "score" in j else ""))
    return ok


def main():
    acc = load(sys.argv[1])
    rest = [load(p) for p in sys.argv[2:]] + [None] * 3
    ok = glow(acc, *rest[:3]) if acc["version"] in ("v8", "v8.1") else hd(acc, *rest[:3])
    print(f"\nOverall: {'ACCEPTED' if ok else 'NOT ACCEPTED'} ({acc['version']})")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
