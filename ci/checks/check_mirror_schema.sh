#!/usr/bin/env python3
import json,sys,hashlib,os
req=["artifact_key","discovered_physical_path","produced_at_utc","proof_anchor","role","sha256","size_bytes"]
seen1=set(); seen2=set(); prev=None; ok=True
with open("artifacts/evidence_index.jsonl","r",encoding="utf-8") as f:
  for i,line in enumerate(f,1):
    line=line.rstrip("\n"); 
    if not line: print(f"EMPTY:{i}",file=sys.stderr); ok=False; continue
    try: o=json.loads(line)
    except Exception as e: print(f"JSON:{i}:{e}",file=sys.stderr); ok=False; continue
    if list(o.keys())!=req: print(f"KEYS:{i}:{list(o.keys())}",file=sys.stderr); ok=False
    if not isinstance(o["size_bytes"],int): print(f"TYPE:size_bytes:{i}",file=sys.stderr); ok=False
    if not (isinstance(o["sha256"],str) and len(o["sha256"])==64): print(f"TYPE:sha256:{i}",file=sys.stderr); ok=False
    if o["proof_anchor"]!=o["discovered_physical_path"]: print(f"PATH_EQ:{i}",file=sys.stderr); ok=False
    k1=(o["artifact_key"],o["discovered_physical_path"])
    k2=(o["proof_anchor"],o["sha256"])
    if k1 in seen1: print(f"DUP_PRIMARY:{i}:{k1}",file=sys.stderr); ok=False
    if k2 in seen2: print(f"DUP_SECONDARY:{i}:{k2}",file=sys.stderr); ok=False
    seen1.add(k1); seen2.add(k2)
    if prev and (o["artifact_key"],o["discovered_physical_path"]) < prev:
      print(f"SORT:{i}:{(o['artifact_key'],o['discovered_physical_path'])} < {prev}",file=sys.stderr); ok=False
    prev=(o["artifact_key"],o["discovered_physical_path"])
sys.exit(0 if ok else 1)
