#!/usr/bin/env python3
"""The successor-page map of MODIFICATION-20261027-gcfpe-backlog-open-items (W7 tooling.successor_page_map, C-1).

EXECUTE writes the one real map, once, at
    docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/successor-pages-102726.1.json
as each successor page is duplicated and moved. Every PLAN tool that needs a successor page id, URL, title or
revision pin imports `load()` from this file and reads that map; none types an id.

    successor_map_102726.py standin <members-tsv> <out>
        write the PLAN dry run's STAND-IN map: each SUCCESSOR's page id is its own 100926.1 page id, CL-05's is the
        102626.2 candidate page 4054590a05eb8155b301e2cb6dec31d5, PE's is its 100926.1 page. The map carries
        "stand_in": true, and every receipt built from it says so.
    successor_map_102726.py check <map> <members-tsv> [--stand-in-ok]
        the W7 checks; a stand-in map is refused unless --stand-in-ok.
    successor_map_102726.py selftest <members-tsv> <scratch>
        each check fires on its injected regression.

The checks (W7 successor_page_map.checks; C-1): 56 members exactly; GCFPE-MGMT-10 is the only KEPT member and
keeps its 100926.1 page; CL-05 is the only ADDED member, duplicated from the candidate page; the other 54 are
SUCCESSOR, each with its 100926.1 page as predecessor and a distinct new page id (a stand-in map alone may reuse
the predecessor id); every title is the 100926.1 title stem plus ' — 102726.1' (KEPT: its 100926.1 title); PE's
predecessor is 3f44590a05eb81f98b76c83465dc1960. Writes only the path it is given. Run with
PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

RELEASE, VERSION = "GCFPE-20261027.1", "102726.1"
OLD_RELEASE, OLD_VERSION = "GCFPE-20261009.1", "100926.1"
BASELINE = "GCFPE-20261009.1 / 100926.1 / 55"
KEPT = {"GCFPE-MGMT-10"}
ADDED = "CL-05"
CL05_CANDIDATE = "4054590a05eb8155b301e2cb6dec31d5"
CL05_TITLE = "CL-05 — Prepare and Publish the Close Mutation Set — 102726.1"
CL05_PARENT_STAND_IN = "3db4590a05eb81d59059eb6b95ed5fcf"  # the HDE Change Flow hub (C-9, C-19; stand-in only)
PE_TITLE = "PE Metaprompt 102726.1"
PE_PREDECESSOR = "3f44590a05eb81f98b76c83465dc1960"
DASH = " — "
HEX32 = re.compile(r"^[0-9a-f]{32}$")
REAL_MAP_PATH = ("docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/"
                 "successor-pages-102726.1.json")
MEMBER_KEYS = {"disposition", "reason", "page_id", "title", "predecessor_page_id", "duplicated_from", "parent_id",
               "created_last_edited_at"}
# C-22: the map's PE row carries its title and its revision pin as well as its ids
PE_KEYS = {"page_id", "predecessor_page_id", "title", "created_last_edited_at"}


def members_tsv(path: str) -> dict:
    """id -> (100926.1 page id, 100926.1 title, lane) from members-100926.1.tsv."""
    out = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            pid, page, title, lane = line.split("\t")
            out[pid] = (page, title, lane)
    assert len(out) == 55, f"members tsv: {len(out)} rows, not 55"
    return out


def stem(title: str, version: str) -> str:
    suffix = DASH + version
    assert title.endswith(suffix), f"title does not end with {suffix!r}: {title!r}"
    return title[: -len(suffix)]


def url(page_id: str) -> str:
    return f"https://app.notion.com/p/{page_id}?pvs=204"


def standin(tsv: str, out: str) -> int:
    base = members_tsv(tsv)
    members = {}
    for pid, (page, title, _lane) in sorted(base.items()):
        if pid in KEPT:
            members[pid] = {"disposition": "KEPT", "reason": "STAND-IN: its 100926.1 body names no member page but "
                            "its own (W7-D10)", "page_id": page, "title": title, "predecessor_page_id": None,
                            "duplicated_from": None, "parent_id": None, "created_last_edited_at": None}
        else:
            members[pid] = {"disposition": "SUCCESSOR", "reason": "STAND-IN: C-1 cascade (PF04 §9.1.6)",
                            "page_id": page, "title": stem(title, OLD_VERSION) + DASH + VERSION,
                            "predecessor_page_id": page, "duplicated_from": page, "parent_id": None,
                            "created_last_edited_at": None}
    members[ADDED] = {"disposition": "ADDED", "reason": "STAND-IN: DN-2 (b), PART-13", "page_id": CL05_CANDIDATE,
                      "title": CL05_TITLE, "predecessor_page_id": None, "duplicated_from": CL05_CANDIDATE,
                      "parent_id": CL05_PARENT_STAND_IN, "created_last_edited_at": None}
    doc = {"stand_in": True,
           "stand_in_note": "PLAN dry run only: each successor page id is its predecessor's; CL-05's is the candidate "
                            "page. EXECUTE writes the real map at " + REAL_MAP_PATH,
           "release": RELEASE, "version_family": VERSION, "baseline": BASELINE,
           "members": dict(sorted(members.items())),
           "pe": {"page_id": PE_PREDECESSOR, "predecessor_page_id": PE_PREDECESSOR, "title": PE_TITLE,
                  "created_last_edited_at": None}}
    Path(out).write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"written": out, "stand_in": True, "members": len(members)}))
    return 0


def errors(doc: dict, base: dict, stand_in_ok: bool) -> list[str]:
    errs = []
    si = doc.get("stand_in") is True
    if si and not stand_in_ok:
        errs.append("STAND_IN_MAP_REFUSED")
    if (doc.get("release"), doc.get("version_family"), doc.get("baseline")) != (RELEASE, VERSION, BASELINE):
        errs.append("RELEASE_HEAD")
    m = doc.get("members") or {}
    if set(m) != set(base) | {ADDED}:
        errs.append(f"MEMBER_SET:{len(m)}")
    ids = []
    for pid, row in sorted(m.items()):
        if set(row) != MEMBER_KEYS:
            errs.append(f"KEYS:{pid}")
            continue
        if not HEX32.match(str(row["page_id"])):
            errs.append(f"PAGE_ID_FORM:{pid}")
        if not str(row.get("reason") or "").strip():
            errs.append(f"NO_REASON:{pid}")
        ids.append(row["page_id"])
        disp = row["disposition"]
        if pid in KEPT:
            if disp != "KEPT" or row["page_id"] != base[pid][0] or row["title"] != base[pid][1]:
                errs.append(f"KEPT_ROW:{pid}")
        elif pid == ADDED:
            if disp != "ADDED" or row["duplicated_from"] != CL05_CANDIDATE or row["predecessor_page_id"] is not None \
                    or row["title"] != CL05_TITLE:
                errs.append(f"ADDED_ROW:{pid}")
        elif pid in base:
            if disp != "SUCCESSOR":
                errs.append(f"DISPOSITION:{pid}:{disp}")
            if row["predecessor_page_id"] != base[pid][0]:
                errs.append(f"PREDECESSOR:{pid}")
            if row["title"] != stem(base[pid][1], OLD_VERSION) + DASH + VERSION:
                errs.append(f"TITLE:{pid}")
            if row["page_id"] == base[pid][0] and not si:
                errs.append(f"SUCCESSOR_NOT_NEW:{pid}")
        if not si:
            for key in ("parent_id",):
                if not HEX32.match(str(row[key])):
                    errs.append(f"{key.upper()}_FORM:{pid}")
            if not row["created_last_edited_at"]:
                errs.append(f"NO_REVISION_PIN:{pid}")
    if len(ids) != len(set(ids)):
        errs.append("DUPLICATE_PAGE_ID")
    pe = doc.get("pe") or {}
    if pe.get("predecessor_page_id") != PE_PREDECESSOR or not HEX32.match(str(pe.get("page_id"))):
        errs.append("PE")
    if set(pe) != PE_KEYS:
        errs.append("PE_KEYS")
    elif pe["title"] != PE_TITLE:
        errs.append("PE_TITLE")
    if not si and pe.get("page_id") == PE_PREDECESSOR:
        errs.append("PE_NOT_NEW")
    if not si and not pe.get("created_last_edited_at"):
        errs.append("PE_NO_REVISION_PIN")
    # C-19: the sole added member's parent fills the contract's staged_parent_id, so even a stand-in map carries one
    if ADDED in m and set(m[ADDED]) == MEMBER_KEYS and not HEX32.match(str(m[ADDED]["parent_id"])):
        errs.append(f"PARENT_ID_FORM:{ADDED}")
    return errs


def load(path: str, tsv: str, stand_in_ok: bool) -> dict:
    """The checked map. Raises SystemExit on any check failure."""
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    errs = errors(doc, members_tsv(tsv), stand_in_ok)
    if errs:
        raise SystemExit(f"successor map refused: {errs}")
    return doc


def check(path: str, tsv: str, *flags: str) -> int:
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    errs = errors(doc, members_tsv(tsv), "--stand-in-ok" in flags)
    print(json.dumps({"map_ok": not errs, "stand_in_used": doc.get("stand_in") is True, "errors": errs}))
    return 0 if not errs else 1


def selftest(tsv: str, scratch: str) -> int:
    d = Path(scratch)
    d.mkdir(parents=True, exist_ok=True)
    p = d / "standin-map.json"
    standin(tsv, str(p))
    base = members_tsv(tsv)
    good = json.loads(p.read_text(encoding="utf-8"))
    rows = {"clean_standin_passes": errors(good, base, True) == [],
            "standin_refused_without_flag": "STAND_IN_MAP_REFUSED" in errors(good, base, False)}

    def inj(fn) -> list[str]:
        doc = copy.deepcopy(good)
        fn(doc)
        return errors(doc, base, True)

    rows["rejects_missing_member"] = bool(inj(lambda o: o["members"].pop("QA-10")))
    rows["rejects_second_kept"] = bool(inj(lambda o: o["members"]["PR-10"].__setitem__("disposition", "KEPT")))
    rows["rejects_wrong_predecessor"] = bool(inj(lambda o: o["members"]["PR-10"].__setitem__(
        "predecessor_page_id", "0" * 32)))
    rows["rejects_old_title"] = bool(inj(lambda o: o["members"]["PR-10"].__setitem__(
        "title", base["PR-10"][1])))
    rows["rejects_cl05_not_from_candidate"] = bool(inj(lambda o: o["members"]["CL-05"].__setitem__(
        "duplicated_from", "1" * 32)))
    rows["rejects_duplicate_page_id"] = bool(inj(lambda o: o["members"]["PR-20"].__setitem__(
        "page_id", o["members"]["PR-10"]["page_id"])))
    rows["rejects_typed_page_id_form"] = bool(inj(lambda o: o["members"]["PR-10"].__setitem__("page_id", "PR-10")))
    rows["rejects_pe_without_title"] = "PE_KEYS" in inj(lambda o: o["pe"].pop("title"))
    rows["rejects_pe_wrong_title"] = "PE_TITLE" in inj(lambda o: o["pe"].__setitem__("title", "PE Metaprompt 100926.1"))
    rows["rejects_pe_without_revision_key"] = "PE_KEYS" in inj(lambda o: o["pe"].pop("created_last_edited_at"))
    rows["rejects_cl05_without_parent"] = f"PARENT_ID_FORM:{ADDED}" in inj(lambda o: o["members"][ADDED].__setitem__(
        "parent_id", None))
    real = copy.deepcopy(good)
    real.pop("stand_in")
    rows["real_map_rejects_pe_without_revision_pin"] = "PE_NO_REVISION_PIN" in errors(real, base, False)
    rows["real_map_rejects_reused_predecessor_ids"] = any(e.startswith("SUCCESSOR_NOT_NEW") for e in
                                                          errors(real, base, False))
    ok = all(rows.values())
    print(json.dumps({"mode": "selftest", "rows": rows, "selftest_ok": ok}))
    return 0 if ok else 1


COMMANDS = {"standin": standin, "check": check, "selftest": selftest}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]](*sys.argv[2:]))
