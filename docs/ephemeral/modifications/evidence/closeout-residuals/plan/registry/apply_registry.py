#!/usr/bin/env python3
"""PLAN repair r1: apply the closeout-residuals registry changes to a scratch copy (never the repository).

Line-anchored, after the parent's evidence/e1_registry_apply.py: every op names its row and an exact line,
which must occur the expected number of times, or the script stops. No YAML is re-dumped.

Source: the LIVE working-tree registry (it must equal the planning baseline 8b4e46ed... and the HEAD blob).
A guard whose value is TBD stops the build unless --allow-tbd is given; then the TBD entry is omitted, the report
says so, and ALL_CHECKS_OK is false. --tbd K52 treats a filled guard as TBD (the refusal test). --fill-k52 PATTERN
builds with that value instead (a candidate trial; outputs get the --suffix given).

Round 2 (P-61, P-62): the report also asserts that RS-40 carries G-K39 and no G-K40, and that each of the 21
ITEM-29 rows requires W-4 (G-K24 on 20 rows; PR-40's parent G25B). TMPDIR must be absolute (the patch round trip).

Usage: PYTHONDONTWRITEBYTECODE=1 TMPDIR=<scratch>/plan/tmp python3 apply_registry.py [--allow-tbd] [--tbd K52]
       [--fill-k52 PATTERN --suffix .k52]
Writes registry.new<suffix>.md, report<suffix>.json and registry<suffix>.diff next to this script.
"""
import argparse, hashlib, json, os, subprocess, sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/user/glow-hdengine-v2"
REL = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
SCR = os.path.dirname(os.path.dirname(HERE))  # .../scratchpad/plan
INSTALLED = [p for p in (os.path.join("/root/.claude/skills/synced", d, "amthor-workspace-governance-audit")
                         for d in os.listdir("/root/.claude/skills/synced")) if os.path.isdir(p)]
FINAL_AUDIT = SCR + "/r1/skills/final/amthor-workspace-governance-audit"
DERIVER = SCR + "/r1/skills/final/glow-graph-contract/scripts/registry_deriver.py"
if not os.path.isfile(DERIVER):
    DERIVER = SCR + "/trial/glow-graph-contract/scripts/registry_deriver.py"
sys.path.insert(0, HERE)
sys.path.insert(0, HERE + "/wga_scripts")  # a byte-identical copy of the installed governance-audit scripts
from audit_workspace_governance import load_data  # noqa: E402
import yaml  # noqa: E402
import guards as G  # noqa: E402

BASE_SHA = "8b4e46ed2dc24442e3dadc416dfe4c810a048788bf03c799808927a54c2677d4"
LISTS = ("required_literals", "forbidden_literals", "required_regex", "forbidden_regex")


def q(s):
    return "'" + s.replace("'", "''") + "'"


def qn(s):
    try:
        if yaml.safe_load("k: " + s) == {"k": s}:
            return s
    except Exception:
        pass
    return q(s)


def entry(value, rid):
    return [f"    - value: {q(value)}", f"      rule_id: {rid}"]


class Reg:
    def __init__(self, text):
        self.lines = text.split("\n")

    def row_range(self, key):
        s = [i for i, l in enumerate(self.lines) if l == f"- prompt_key: {key}"]
        assert len(s) == 1, (key, s)
        s = s[0]
        e = next(i for i in range(s + 1, len(self.lines)) if self.lines[i].startswith("- prompt_key: ") or
                 self.lines[i] == "global_literals:")
        return s, e

    def find(self, key, anchor):
        s, e = self.row_range(key)
        hits = [i for i in range(s, e) if self.lines[i] == anchor]
        assert len(hits) == 1, (key, anchor, hits)
        return hits[0]

    def find_prefix(self, key, prefix):
        s, e = self.row_range(key)
        hits = [i for i in range(s, e) if self.lines[i].startswith(prefix)]
        assert len(hits) == 1, (key, prefix, hits)
        return hits[0]

    def replace(self, key, anchor, new):
        i = self.find(key, anchor)
        self.lines[i:i + 1] = new if isinstance(new, list) else [new]

    def delete_pair(self, key, l1, l2):
        i = self.find(key, l1)
        assert self.lines[i + 1] == l2, (key, self.lines[i + 1])
        del self.lines[i:i + 2]

    def list_end(self, key, header):
        i = self.find(key, header)
        ind = len(header) - len(header.lstrip())
        j = i + 1
        while j < len(self.lines):
            l = self.lines[j]
            lead = len(l) - len(l.lstrip())
            if l.strip() == "" or lead < ind or (lead == ind and not l.lstrip().startswith("- ")):
                break
            j += 1
        return j

    def append_list(self, key, header, new):
        j = self.list_end(key, header)
        self.lines[j:j] = new

    def text(self):
        return "\n".join(self.lines)


def rows_of(keys, sel):
    return list(keys) if sel == G.ALL55 else list(sel)


def value_for(value, row):
    return value[row] if isinstance(value, dict) else value


def active_guards(allow_tbd, fill, force_tbd=()):
    out, omitted = [], []
    for g in G.GUARDS:
        gid, rules, part, kind, value, rid, sel = g
        if gid in force_tbd:
            value = G.TBD
            g = (gid, rules, part, kind, value, rid, sel)
        if value == G.TBD:
            if fill is not None and gid == "K52":
                out.append((gid, rules, part, kind, fill, rid, sel))
                continue
            if not allow_tbd:
                raise SystemExit(f"BUILD REFUSED: guard G-{gid} ({', '.join(rules)}) is TBD; fill its pattern in guards.py "
                                 f"(dry-run candidate for K52: {G.CL30_A2_CANDIDATE!r}) or pass --allow-tbd for a draft without it")
            omitted.append(f"G-{gid} {', '.join(rules)} on {', '.join(sel)}: TBD, omitted from this draft")
            continue
        out.append(g)
    return out, omitted


def apply(src, old, guards):
    keys = [r["prompt_key"] for r in old["prompts"]]
    R = Reg(src)
    counts = Counter()
    # ---- PART-10: lane notion_parent_id/title and row expected_parent_id/title --------------------
    idmap = {o: n for o, _, n, _, _, _ in G.PARENT_MAP}
    titlemap = {ot: nt for _, ot, _, nt, _, _ in G.PARENT_MAP}
    bodyline = [i for i, l in enumerate(R.lines) if l == "prompts:"]
    assert len(bodyline) == 1
    lanes_start = R.lines.index("lanes:")
    for i, l in enumerate(R.lines):
        for key, ind, section in (("notion_parent_id", "  ", "lane"), ("notion_parent_title", "  ", "lane"),
                                  ("expected_parent_id", "  ", "row"), ("expected_parent_title", "  ", "row")):
            pre = f"{ind}{key}: "
            if not l.startswith(pre):
                continue
            in_lanes = lanes_start < i < bodyline[0]
            assert in_lanes == (section == "lane"), (i, l)
            v = l[len(pre):]
            m = idmap if key.endswith("_id") else titlemap
            assert v in m, (i, l)
            R.lines[i] = pre + (m[v] if key.endswith("_id") else qn(m[v]))
            counts[(key, v)] += 1
    for o, ot, n, nt, lane_n, row_n in G.PARENT_MAP:
        assert counts[("notion_parent_id", o)] == lane_n and counts[("expected_parent_id", o)] == row_n, o
        assert counts[("notion_parent_title", ot)] == lane_n, ot
    # ---- PART-17: release-line guards, in place on all 55 rows (P-16 suffix) ------------------------
    for k in keys:
        for label, rid in G.RELEASE_LABELS:
            old_v = G.OLD_HDR + label + G.OLD_END
            new_v = G.NEW_HDR + label + G.NEW_END
            R.replace(k, f"    - value: {q(old_v)}", f"    - value: {q(new_v)}")
            counts["PART-17 replaced in place"] += 1
    # ---- PART-18: the required 'Decide it during work' leaves the 8 rows (its forbidden twin is K51) --
    for k in G.CLAT8:
        R.delete_pair(k, f"    - value: {q(G.CLAT_REQ[0])}", f"      rule_id: {G.CLAT_REQ[1]}")
        counts["PART-18 required removed"] += 1
    # ---- new guards, appended to each row's list in guard order --------------------------------------
    for gid, _, _, kind, value, rid, sel in guards:
        for k in rows_of(keys, sel):
            assert k in keys, (gid, k)
            if isinstance(value, dict) and k not in value:
                raise SystemExit(f"G-{gid} has no value for row {k}")
            R.append_list(k, f"    {kind}:", entry(value_for(value, k), rid))
            counts["guard entries added"] += 1
    # ---- non-assertion fields ------------------------------------------------------------------------
    R.append_list("CL-40", "    allowed:", ["    - " + qn(G.CL40_ALLOWED_NEW)])  # PART-06, ruling 5 Q1 (A)
    R.replace("PR-40", "  - " + G.PR40_INPUT_OLD, "  - " + qn(G.PR40_INPUT_NEW))   # LPR-40-4 (P-01 site)
    w4 = R.find_prefix("PR-40", "  - " + G.PR40_INPUT_W4_PREFIX)
    assert R.lines[w4 - 1] == "  - " + G.PR40_INPUT_AFTER, R.lines[w4 - 1]
    R.lines[w4:w4] = ["  - " + qn(G.PR40_INPUT_RECV)]                               # LPR-40-5 (P-01 sentence)
    return R.text(), counts


ids = lambda l: [((x["value"], x.get("rule_id")) if isinstance(x, dict) else (x, None)) for x in l or []]


def semdiff(old, new, guards):
    rep = {}
    keys = [r["prompt_key"] for r in old["prompts"]]
    rep["top_level_keys_changed"] = sorted(k for k in set(old) | set(new) if k not in ("prompts", "lanes") and old.get(k) != new.get(k))
    idmap = {o: n for o, _, n, _, _, _ in G.PARENT_MAP}
    tmap = {ot: nt for _, ot, _, nt, _, _ in G.PARENT_MAP}
    lane_ok = len(old["lanes"]) == len(new["lanes"]) == 16
    for a, b in zip(old["lanes"], new["lanes"]):
        exp = dict(a, notion_parent_id=idmap[a["notion_parent_id"]], notion_parent_title=tmap[a["notion_parent_title"]])
        lane_ok &= (b == exp)
    rep["lanes_only_parent_changed_by_map"] = lane_ok
    O = {r["prompt_key"]: r for r in old["prompts"]}
    N = {r["prompt_key"]: r for r in new["prompts"]}
    rep["rows"] = len(N)
    rep["rows_kept_in_set_and_order"] = list(O) == list(N) == keys and len(keys) == 55
    exp_add = {k: [] for k in keys}
    exp_rm = {k: [] for k in keys}
    for k in keys:
        for label, rid in G.RELEASE_LABELS:
            exp_rm[k].append(("forbidden_regex", (G.OLD_HDR + label + G.OLD_END, rid)))
            exp_add[k].append(("forbidden_regex", (G.NEW_HDR + label + G.NEW_END, rid)))
    for k in G.CLAT8:
        exp_rm[k].append(("required_regex", G.CLAT_REQ))
    for gid, _, _, kind, value, rid, sel in guards:
        for k in rows_of(keys, sel):
            exp_add[k].append((kind, (value_for(value, k), rid)))
    bad, fields, order_bad, per_row = [], {}, [], {}
    for k in keys:
        a, b = O[k], N[k]
        f = sorted(x for x in set(a) | set(b) if x != "audit_assertions" and a.get(x) != b.get(x))
        if f:
            fields[k] = f
        add, rm = [], []
        for l in LISTS:
            x, y = ids(a["audit_assertions"].get(l)), ids(b["audit_assertions"].get(l))
            cx, cy = Counter(x), Counter(y)
            add += [(l, e) for e in (cy - cx).elements()]
            rm += [(l, e) for e in (cx - cy).elements()]
            if [e for e in y if e in x] != [e for e in x if e in y]:
                order_bad.append((k, l))
            if len(set(y)) != len(y):
                bad.append((k, "duplicate assertion", l))
        if sorted(add) != sorted(exp_add[k]) or sorted(rm) != sorted(exp_rm[k]):
            bad.append(k)
        n_rel = 3
        per_row[k] = {"before": sum(len(a["audit_assertions"].get(l) or []) for l in LISTS),
                      "after": sum(len(b["audit_assertions"].get(l) or []) for l in LISTS),
                      "new_guard_entries": len(add) - n_rel, "release_replaced_in_place": n_rel,
                      "removed": len(rm) - n_rel}
    rep["rows_with_unexpected_assertion_diff"] = bad
    rep["kept_order_violations"] = order_bad
    rep["per_row_assertions"] = per_row
    exp_fields = {}
    for k in keys:
        exp_fields[k] = ["expected_parent_id"] + (["expected_parent_title"] if "expected_parent_title" in O[k] else [])
    exp_fields["CL-40"] = sorted(exp_fields["CL-40"] + ["mutations"])
    exp_fields["PR-40"] = sorted(exp_fields["PR-40"] + ["inputs"])
    exp_fields = {k: sorted(v) for k, v in exp_fields.items()}
    rep["non_assertion_fields_as_expected"] = fields == exp_fields
    rep["parents"] = all(N[k]["expected_parent_id"] == idmap[O[k]["expected_parent_id"]] and
                         N[k].get("expected_parent_title") == (tmap[O[k]["expected_parent_title"]] if "expected_parent_title" in O[k] else None)
                         for k in keys)
    rep["parent_value_counts"] = {"lane_ids": sum(1 for l in new["lanes"] if l["notion_parent_id"] in idmap.values()),
                                  "row_ids": sum(1 for r in new["prompts"] if r["expected_parent_id"] in idmap.values()),
                                  "lane_titles": sum(1 for l in new["lanes"] if l["notion_parent_title"] in tmap.values()),
                                  "row_titles": sum(1 for r in new["prompts"] if r.get("expected_parent_title") in tmap.values()),
                                  "old_ids_left": sum(1 for x in list(new["lanes"]) + list(new["prompts"])
                                                      for f in ("notion_parent_id", "expected_parent_id") if x.get(f) in idmap)}
    rep["CL-40 mutations.allowed added"] = [x for x in N["CL-40"]["mutations"]["allowed"] if x not in O["CL-40"]["mutations"]["allowed"]]
    rep["CL-40 mutations.forbidden unchanged"] = N["CL-40"]["mutations"]["forbidden"] == O["CL-40"]["mutations"]["forbidden"]
    pi_o, pi_n = O["PR-40"]["inputs"], N["PR-40"]["inputs"]
    rep["PR-40 inputs"] = {"before": len(pi_o), "after": len(pi_n),
                           "removed": [x for x in pi_o if x not in pi_n], "added": [x for x in pi_n if x not in pi_o]}
    i_recv = pi_n.index(G.PR40_INPUT_RECV) if G.PR40_INPUT_RECV in pi_n else -1
    rep["values_roundtrip"] = (N["CL-40"]["mutations"]["allowed"][-1] == G.CL40_ALLOWED_NEW and
                               G.PR40_INPUT_NEW in pi_n and G.PR40_INPUT_OLD not in pi_n and i_recv > 0 and
                               pi_n[i_recv - 1] == G.PR40_INPUT_AFTER and pi_n[i_recv + 1].startswith(G.PR40_INPUT_W4_PREFIX) and
                               [x for x in pi_n if x != G.PR40_INPUT_RECV] ==
                               [G.PR40_INPUT_NEW if x == G.PR40_INPUT_OLD else x for x in pi_o])
    tot = lambda Rg: sum(len(r["audit_assertions"].get(l) or []) for r in Rg["prompts"] for l in LISTS)
    rep["assertions_total"] = [tot(old), tot(new)]
    rep["rows_per_guard"] = {}
    for gid, _, _, kind, value, rid, sel in guards:
        placed = [k for k in keys if (not isinstance(value, dict) or k in value)
                  and (value_for(value, k), rid) in ids(N[k]["audit_assertions"].get(kind))]
        rep["rows_per_guard"]["G-" + gid] = [len(placed), sorted(placed) == sorted(rows_of(keys, sel))]
    rep["release_guards_new"] = sum(1 for r in new["prompts"] for label, rid in G.RELEASE_LABELS
                                    if (G.NEW_HDR + label + G.NEW_END, rid) in ids(r["audit_assertions"]["forbidden_regex"]))
    rep["release_guards_old_left"] = sum(1 for r in new["prompts"] for v, _ in ids(r["audit_assertions"]["forbidden_regex"])
                                         if v.startswith(r"\A(?:[ \t]*\n)*") or v.endswith(G.OLD_END) and v.startswith(G.NEW_HDR))
    rep["clat"] = {k: {"required_decide": any(v == "Decide it during work" for v, _ in ids(N[k]["audit_assertions"]["required_regex"])),
                       "forbidden_decide": any(v == "Decide it during work" for v, _ in ids(N[k]["audit_assertions"]["forbidden_regex"])),
                       "material_required": any("Material" in v for v, _ in ids(N[k]["audit_assertions"]["required_regex"]))}
                   for k in ["PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "RS-10", "RS-20", "DOC-10", "DOC-20", "IA-30"]}
    # P-62: RS-40 carries the forbidden G-K39 (the retired storage sentence) and no required R-A5 text (G-K40 stays off)
    _rs40 = {l: [v for v, _ in ids(N["RS-40"]["audit_assertions"].get(l))] for l in LISTS}
    rep["RS-40 carries G-K39 and no G-K40"] = (_rs40["forbidden_regex"].count(G.A5_FORBID) == 1 and
                                               not any(v in (G.A5_NEW, G.A5_MGMT) for l in LISTS for v in _rs40[l]))
    # P-61: the required W-4 on all 21 ITEM-29 rows: G-K24 on 20, and PR-40's kept parent G25B
    rep["W-4 required on the 21 ITEM-29 rows"] = {
        k: [v for v, _ in ids(N[k]["audit_assertions"].get("required_regex")) if v in (G.W4_REQ, G.G25B_REQ)]
        for k in G.A7ALL}
    rep["W-4 required on the 21 ITEM-29 rows ok"] = all(
        v == ([G.G25B_REQ] if k == "PR-40" else [G.W4_REQ]) for k, v in rep["W-4 required on the 21 ITEM-29 rows"].items()) \
        and len(rep["W-4 required on the 21 ITEM-29 rows"]) == 21
    return rep


def yaml_rows(text):
    """Parse each row's own YAML chunk separately and compare it with the loader's row."""
    block = text[text.index("```yaml\n") + 8:]
    block = block[:block.index("\n```")]
    lines = block.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("- prompt_key: ")]
    end = next(i for i, l in enumerate(lines) if l == "global_literals:")
    out = []
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else end
        chunk = "\n".join(lines[s:e])
        try:
            parsed = yaml.safe_load(chunk)
            out.append((parsed[0]["prompt_key"], parsed[0]))
        except Exception as ex:  # noqa: BLE001
            out.append((None, repr(ex)))
    return out


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--allow-tbd", action="store_true")
    ap.add_argument("--fill-k52")
    ap.add_argument("--suffix", default="")
    ap.add_argument("--tbd", action="append", default=[], help="treat this guard id (e.g. K52) as TBD: the refusal test")
    a = ap.parse_args()
    guards, omitted = active_guards(a.allow_tbd, a.fill_k52, set(a.tbd))
    live = open(os.path.join(REPO, REL), "rb").read()
    head = subprocess.run(["git", "-C", REPO, "show", "HEAD:" + REL], capture_output=True, check=True).stdout
    base = open(HERE + "/registry.head.md", "rb").read()
    src = {"live_sha256": hashlib.sha256(live).hexdigest(), "head_blob_sha256": hashlib.sha256(head).hexdigest(),
           "draft_head_copy_sha256": hashlib.sha256(base).hexdigest(), "live_bytes": len(live)}
    assert src["live_sha256"] == BASE_SHA == src["head_blob_sha256"] == src["draft_head_copy_sha256"], src
    old = load_data(os.path.join(REPO, REL))
    new_text, counts = apply(live.decode("utf-8"), old, guards)
    out_md = HERE + f"/registry.new{a.suffix}.md"
    open(out_md, "w", encoding="utf-8").write(new_text)
    new = load_data(out_md)
    rep = {"source": src, "omitted_tbd": omitted}
    rep.update(semdiff(old, new, guards))
    rep["op_counts"] = {str(k): v for k, v in counts.items() if not isinstance(k, tuple)}
    rep["parent_counts"] = {f"{k[0]}:{k[1]}": v for k, v in counts.items() if isinstance(k, tuple)}
    # structure: the installed validator (byte-identical copy) and the r1 final governance-audit copy
    inst = INSTALLED[0] + "/scripts"
    same = {f: hashlib.sha256(open(os.path.join(inst, f), "rb").read()).hexdigest() ==
            hashlib.sha256(open(os.path.join(HERE, "wga_scripts", f), "rb").read()).hexdigest()
            for f in sorted(os.listdir(inst)) if f.endswith(".py")}
    rep["wga_copy_identical_to_installed"] = same
    checks = {}
    for name, d in (("installed-copy", HERE + "/wga_scripts"), ("r1-final", FINAL_AUDIT + "/scripts")):
        r = run([sys.executable, d + "/validate_project_prompt_registry.py", out_md])
        checks[name] = {"exit": r.returncode, "stdout": json.loads(r.stdout) if r.stdout.strip() else None,
                        "stderr": r.stderr.strip()[-400:]}
    rep["structure_check"] = checks
    # per-row YAML parse
    yr = yaml_rows(new_text)
    rows_new = {r["prompt_key"]: r for r in new["prompts"]}
    rep["yaml_per_row"] = {"rows_parsed": sum(1 for k, _ in yr if k), "errors": [v for k, v in yr if not k],
                           "equal_to_loader": all(k and rows_new.get(k) == v for k, v in yr)}
    # registry deriver drift (graph parts in the repository, and the r1 reindexed parts if present)
    drift = {}
    for pname, pdir in (("repo docs/graph/parts", REPO + "/docs/graph/parts"),
                        ("r1 parts_reindexed", SCR + "/r1/skills/parts_reindexed")):
        if not os.path.isdir(os.path.join(pdir, "prompts")):
            continue
        for aname, aroot in (("installed", INSTALLED[0]), ("r1-final", FINAL_AUDIT)):
            for rname, rpath in (("head", os.path.join(REPO, REL)), ("new", out_md)):
                r = run([sys.executable, DERIVER, aroot, rpath, pdir])
                drift[f"{pname} | audit {aname} | {rname}"] = {"exit": r.returncode,
                                                               "out": json.loads(r.stdout) if r.stdout.strip().startswith("{") else r.stdout[-300:],
                                                               "stderr": r.stderr[-300:]}
    rep["deriver"] = {"script": DERIVER, "sha256": hashlib.sha256(open(DERIVER, "rb").read()).hexdigest(), "runs": drift}
    # unified diff against the live file (repository-relative labels), and a patch round trip in scratch
    diff_path = HERE + f"/registry{a.suffix}.diff"
    d = subprocess.run(["diff", "-u", "--label", "a/" + REL, "--label", "b/" + REL, os.path.join(REPO, REL), out_md],
                       capture_output=True, text=True)
    open(diff_path, "w", encoding="utf-8").write(d.stdout)
    tmpd = os.environ.get("TMPDIR", SCR + "/tmp")
    trial = os.path.join(tmpd, "registry.patch-trial.md")
    open(trial, "wb").write(live)
    p = subprocess.run(["patch", "-s", "-o", trial + ".out", trial, diff_path], capture_output=True, text=True)
    rep["diff"] = {"path": diff_path, "exit_diff": d.returncode, "lines": d.stdout.count("\n"),
                   "patch_roundtrip_equal": p.returncode == 0 and open(trial + ".out", "rb").read() == new_text.encode("utf-8"),
                   "patch_stderr": p.stderr[-300:]}
    for f in (trial, trial + ".out"):
        if os.path.exists(f):
            os.remove(f)
    rep["new_path"] = out_md
    rep["new_lines"] = new_text.count("\n")
    rep["new_sha256"] = hashlib.sha256(new_text.encode("utf-8")).hexdigest()
    rep["diff_sha256"] = hashlib.sha256(open(diff_path, "rb").read()).hexdigest()
    drift_ok = all(v["exit"] == 0 and not v["out"].get("drift") for v in drift.values() if isinstance(v["out"], dict))
    ok = (not omitted and not rep["top_level_keys_changed"] and rep["lanes_only_parent_changed_by_map"]
          and rep["rows_kept_in_set_and_order"] and not rep["rows_with_unexpected_assertion_diff"]
          and not rep["kept_order_violations"] and rep["non_assertion_fields_as_expected"] and rep["parents"]
          and rep["values_roundtrip"] and rep["release_guards_new"] == 165 and rep["release_guards_old_left"] == 0
          and all(v["exit"] == 0 and v["stdout"] == {"valid": True, "problems": []} for v in checks.values())
          and rep["yaml_per_row"]["rows_parsed"] == 55 and rep["yaml_per_row"]["equal_to_loader"]
          and drift_ok and rep["diff"]["patch_roundtrip_equal"] and rep["RS-40 carries G-K39 and no G-K40"]
          and rep["W-4 required on the 21 ITEM-29 rows ok"]
          and all(v[1] for v in rep["rows_per_guard"].values()))
    rep["ALL_CHECKS_OK"] = ok
    rep["ALL_CHECKS_OK_EXCEPT_TBD"] = ok or (bool(omitted) and (not rep["top_level_keys_changed"]) and all(
        [rep["lanes_only_parent_changed_by_map"], rep["rows_kept_in_set_and_order"], not rep["rows_with_unexpected_assertion_diff"],
         not rep["kept_order_violations"], rep["non_assertion_fields_as_expected"], rep["parents"], rep["values_roundtrip"],
         rep["release_guards_new"] == 165, rep["release_guards_old_left"] == 0, drift_ok, rep["diff"]["patch_roundtrip_equal"],
         rep["yaml_per_row"]["rows_parsed"] == 55, rep["yaml_per_row"]["equal_to_loader"], rep["RS-40 carries G-K39 and no G-K40"],
         rep["W-4 required on the 21 ITEM-29 rows ok"],
         all(v["exit"] == 0 and v["stdout"] == {"valid": True, "problems": []} for v in checks.values()),
         all(v[1] for v in rep["rows_per_guard"].values())]))
    json.dump(rep, open(HERE + f"/report{a.suffix}.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in rep.items() if k not in ("per_row_assertions", "deriver")}, indent=1, ensure_ascii=False))
    print(json.dumps({"deriver": {k: (v["exit"], v["out"].get("drift") if isinstance(v["out"], dict) else v["out"])
                                  for k, v in drift.items()}}, indent=1))


if __name__ == "__main__":
    main()
