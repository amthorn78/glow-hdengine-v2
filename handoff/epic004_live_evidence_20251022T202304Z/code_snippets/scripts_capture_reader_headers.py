# scripts/capture_reader_headers.py
from __future__ import annotations
import json, urllib.request, hashlib, os
def lower_headers(h): return {k.lower(): h.get(k) for k in h.keys()}
def write_json(path,obj):
    s=json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",",":"))
    open(path,"w",encoding="utf-8").write(s+("\n" if not s.endswith("\n") else ""))
BASE='http://127.0.0.1:5000'; A='fixtures/charts/alice.json'; B='fixtures/charts/bob.json'
id_url=f"{BASE}/api/reader?v=1&a={A}&b={B}&a_tz=UTC&b_tz=UTC"
os.makedirs('artifacts/epic004/headers', exist_ok=True)
os.makedirs('artifacts/epic004/bytes', exist_ok=True)
# identity
r=urllib.request.urlopen(urllib.request.Request(id_url, headers={"Accept-Encoding":"identity"}))
id_body=r.read(); id_hdr=lower_headers(r.headers)
open('artifacts/epic004/bytes/reader_identity.bin','wb').write(id_body)
open('artifacts/epic004/bytes/reader_identity.sha256','w').write(hashlib.sha256(id_body).hexdigest()+"\n")
write_json('artifacts/epic004/headers/reader_200.json', id_hdr)
# gzip (if enabled)
r=urllib.request.urlopen(urllib.request.Request(id_url, headers={"Accept-Encoding":"gzip"}))
gz_body=r.read(); gz_hdr=lower_headers(r.headers)
open('artifacts/epic004/bytes/reader_gzip.bin','wb').write(gz_body)
open('artifacts/epic004/bytes/reader_gzip.sha256','w').write(hashlib.sha256(gz_body).hexdigest()+"\n")
write_json('artifacts/epic004/headers/reader_200_gzip.json', gz_hdr)
# 304 after 200
etag=id_hdr.get("etag","")
try:
    urllib.request.urlopen(urllib.request.Request(id_url, headers={"If-None-Match": etag}))
except urllib.error.HTTPError as e:
    write_json('artifacts/epic004/headers/reader_304.json', lower_headers(e.headers))
# HEAD
r=urllib.request.urlopen(urllib.request.Request(id_url, method="HEAD", headers={"Accept-Encoding":"identity"}))
write_json('artifacts/epic004/headers/reader_head.json', lower_headers(r.headers))
# POST 405 typed JSON
try:
    urllib.request.urlopen(urllib.request.Request(f"{BASE}/api/reader?v=1", method="POST", data=b"{}", headers={"Content-Type":"application/json"}))
except urllib.error.HTTPError as e:
    open('artifacts/epic004/headers/reader_post_405.json','wb').write(e.read())
print("CAPTURE_DONE")
