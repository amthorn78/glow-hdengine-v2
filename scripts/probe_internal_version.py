#!/usr/bin/env python3
import argparse, json, time
from datetime import datetime
from urllib.parse import urljoin
from urllib.request import Request, urlopen
def norm(h): return {k.lower(): v.strip() for k,v in h.items()}
def jdump(p,obj): open(p,"w",encoding="utf-8").write(json.dumps(obj,separators=(",",":"),ensure_ascii=False)+"\n")
def fetch(url, method="GET", headers=None, timeout=10):
    req = Request(url, method=method, headers=headers or {}); import time as T
    t0=T.time()
    try:
        with urlopen(req, timeout=timeout) as resp:
            body=resp.read(); dt=T.time()-t0; 
            return resp.getcode(), norm(resp.headers), len(body), dt, None
    except Exception as e:
        dt=T.time()-t0; return None, {}, 0, dt, str(e)
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--base-url",required=True); ap.add_argument("--out",default="artifacts"); a=ap.parse_args()
    import os; os.makedirs(f"{a.out}/headers",exist_ok=True); os.makedirs(f"{a.out}/prod",exist_ok=True)
    base=a.base_url.rstrip('/')+'/'; target=urljoin(base,"internal/version")
    for name,method,hdr in [
        ("internal_version_200.json","GET",{"Accept":"application/json"}),
        ("internal_version_head.json","HEAD",{"Accept":"application/json"}),
        ("internal_version_if_none_match.json","GET",{"If-None-Match":'"deadbeef"'}),
        ("internal_version_override_denied.json","GET",{"X-Identity-Override":"engine_tag=foo;build_commit=deadbeef"}),
    ]:
        code,h,cl,dt,err=fetch(target,method,hdr); jdump(f"{a.out}/headers/{name}",{"status":code,"headers":h,"len":cl,"err":err})
    log=f"{a.out}/prod/latency_sample.jsonl"
    for _ in range(288):
        code,h,cl,dt,err=fetch(target,"GET",{"Accept":"application/json"})
        rec={"ts":datetime.utcnow().isoformat()+"Z","status":code,"latency_s":round(dt,4),"content_length":h.get("content-length"),"error":err}
        open(log,"a",encoding="utf-8").write(json.dumps(rec,separators=(",",":"),ensure_ascii=False)+"\n"); time.sleep(300)
