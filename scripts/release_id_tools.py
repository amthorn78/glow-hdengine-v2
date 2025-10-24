#!/usr/bin/env python3
import argparse, hashlib, json, os, sys

def lowerhex64(s): return isinstance(s,str) and len(s)==64 and all(c in "0123456789abcdef" for c in s)
def read_bytes(p): 
    with open(p,"rb") as f: return f.read()

def validate_manifest(obj):
    issues=[]
    if not isinstance(obj,dict) or not isinstance(obj.get("entries"),list):
        return {"ok":False,"issues":["manifest must be an object with `entries` array"]}
    for i,ent in enumerate(obj["entries"]):
        if not isinstance(ent,dict): issues.append(f"entries[{i}] not an object"); continue
        p,h,z = ent.get("path"), ent.get("sha256"), ent.get("size")
        if not isinstance(p,str) or not p: issues.append(f"entries[{i}].path invalid")
        if not lowerhex64(h or ""):       issues.append(f"entries[{i}].sha256 invalid")
        if not isinstance(z,int) or z<0:  issues.append(f"entries[{i}].size invalid")
    return {"ok": not issues, "issues": issues}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", default="artifacts/math")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    # 1) freeze-pack copy
    b = read_bytes(args.manifest)
    open(os.path.join(args.out,"freeze_pack_manifest.json"),"wb").write(b)

    # 2) release_id + two-run equality
    rid  = hashlib.sha256(b).hexdigest()
    open(os.path.join(args.out,"release_id.txt"),"w",encoding="utf-8").write(rid+"\n")
    b2   = read_bytes(args.manifest)
    rid2 = hashlib.sha256(b2).hexdigest()
    open(os.path.join(args.out,"release_id_recompute.log"),"w",encoding="utf-8").write(
        rid+"\n"+rid2+"\n"+("EQUAL\n" if rid==rid2 else "MISMATCH\n"))

    # 3) schema check + checksums audit
    try:
        obj = json.loads(b.decode("utf-8"))
        rep = validate_manifest(obj)
        audit=[]
        for ent in obj.get("entries",[]):
            p,h,z = ent["path"], ent["sha256"], ent["size"]
            if not os.path.exists(p):
                audit.append(f"MISSING {p}")
                continue
            fb = read_bytes(p); sh = hashlib.sha256(fb).hexdigest(); sz = len(fb)
            audit.append("PASS "+p if (sh==h and sz==z) else f"BAD {p} expected {h}:{z} got {sh}:{sz}")
    except Exception as e:
        rep={"ok":False,"issues":[f"json parse error: {e}"]}; audit=["MISSING entries (manifest unreadable)"]
    open(os.path.join(args.out,"manifest_schema_report.json"),"w",encoding="utf-8").write(
        json.dumps(rep,separators=(",",":"),ensure_ascii=False)+"\n")
    open(os.path.join(args.out,"checksums_audit.log"),"w",encoding="utf-8").write(
        "\n".join(audit or ["EMPTY"])+"\n")

if __name__=="__main__":
    sys.exit(main())
