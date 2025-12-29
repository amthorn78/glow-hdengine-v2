#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

REQ_KEYS = ["engine_tag","build_commit","invocation_tag","invocation_sha256","emitter_sha256","release_id"]

def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def sh(cmd: list[str]) -> tuple[int, bytes, bytes]:
    p = subprocess.run(cmd, capture_output=True)
    return p.returncode, p.stdout or b"", p.stderr or b""

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()

def norm_headers(raw: bytes) -> str:
    txt = raw.decode("utf-8", errors="replace").replace("\r\n", "\n")
    out_lines = []
    for ln in txt.split("\n"):
        if ":" in ln:
            k, v = ln.split(":", 1)
            out_lines.append(k.lower() + ":" + v)
        else:
            out_lines.append(ln)
    return "\n".join(out_lines).strip() + "\n"

def parse_status_code(hdr_txt: str) -> int | None:
    for ln in hdr_txt.splitlines():
        if ln.startswith("http/"):
            m = re.search(r"\s(\d{3})\s", ln)
            if m:
                return int(m.group(1))
            break
    return None

def header_value(hdr_txt: str, name_lower: str) -> str | None:
    prefix = name_lower.lower() + ":"
    for ln in hdr_txt.splitlines():
        if ln.lower().startswith(prefix):
            return ln.split(":", 1)[1].strip()
    return None

def curl_headers(url: str, method: str, auth_header: str, extra_headers: list[str],
                 connect_timeout: int, max_time: int, out_path: Path) -> int:
    cmd = [
        "curl","-sS","-D","-","-o","/dev/null","-X",method,
        "--connect-timeout",str(connect_timeout),
        "--max-time",str(max_time),
        "--retry","0",
        "-H",auth_header,
    ]
    for h in extra_headers:
        cmd += ["-H", h]
    cmd.append(url)

    rc, out, err = sh(cmd)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if rc != 0:
        out_path.write_text(norm_headers(out + b"\n" + err), encoding="utf-8")
        return rc
    out_path.write_text(norm_headers(out), encoding="utf-8")
    return 0

def curl_body(url: str, auth_header: str, connect_timeout: int, max_time: int, out_path: Path) -> int:
    cmd = [
        "curl","-sS",
        "--connect-timeout",str(connect_timeout),
        "--max-time",str(max_time),
        "--retry","0",
        "-H",auth_header,
        url,
    ]
    rc, out, err = sh(cmd)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if rc != 0:
        out_path.write_bytes(out + b"\n" + err)
        return rc
    out_path.write_bytes(out)
    return 0

def read_text_optional(p: Path) -> str | None:
    try:
        if p.exists():
            return p.read_text(encoding="utf-8").strip()
    except Exception:
        return None
    return None

def read_json_optional(p: Path) -> dict | None:
    try:
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    return None

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--auth-header-env", required=True)
    ap.add_argument("--connect-timeout", type=int, default=5)
    ap.add_argument("--max-time", type=int, default=30)
    args = ap.parse_args()

    auth_header = os.getenv(args.auth_header_env, "")
    if not auth_header:
        return 2

    base = args.base_url.rstrip("/")
    url = base + "/internal/version"
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    headers_get = out_dir / "headers_get.txt"
    headers_head = out_dir / "headers_head.txt"
    cond_inm = out_dir / "cond_if_none_match_headers.txt"
    cond_ims = out_dir / "cond_if_modified_since_headers.txt"
    alias_inm = out_dir / "headers_cond_if_none_match.txt"
    alias_ims = out_dir / "headers_cond_if_modified_since.txt"

    body1 = out_dir / "body_get.json"
    body_sha = out_dir / "body_get.sha256"
    body2 = out_dir / "body_get_run2.json"
    two_run = out_dir / "two_run_identity.log"

    rc = curl_headers(url, "GET", auth_header, [], args.connect_timeout, args.max_time, headers_get)
    if rc != 0:
        return 3
    rc = curl_headers(url, "HEAD", auth_header, [], args.connect_timeout, args.max_time, headers_head)
    if rc != 0:
        return 3

    rc = curl_headers(url, "GET", auth_header, ['If-None-Match: "0"'], args.connect_timeout, args.max_time, cond_inm)
    if rc != 0:
        return 3
    rc = curl_headers(url, "GET", auth_header, ["If-Modified-Since: Thu, 01 Jan 1970 00:00:00 GMT"], args.connect_timeout, args.max_time, cond_ims)
    if rc != 0:
        return 3

    alias_inm.write_text(cond_inm.read_text(encoding="utf-8"), encoding="utf-8")
    alias_ims.write_text(cond_ims.read_text(encoding="utf-8"), encoding="utf-8")

    rc = curl_body(url, auth_header, args.connect_timeout, args.max_time, body1)
    if rc != 0:
        return 3
    sha1 = sha256_file(body1)
    body_sha.write_text(sha1 + "\n", encoding="utf-8")

    rc = curl_body(url, auth_header, args.connect_timeout, args.max_time, body2)
    if rc != 0:
        return 3
    sha2 = sha256_file(body2)
    identical = (sha1 == sha2)
    body2.unlink(missing_ok=True)

    checks = []

    def add_check(ok: bool, label: str, source: str = "", expected: str | None = None, got: str | None = None):
        c = {"ok": bool(ok), "label": label}
        if source:
            c["source"] = source
        if expected is not None and got is not None:
            c["expected"] = expected
            c["got"] = got
        checks.append(c)

    def load_hdr(p: Path) -> str:
        return p.read_text(encoding="utf-8")

    hg = load_hdr(headers_get)
    hh = load_hdr(headers_head)
    hinm = load_hdr(cond_inm)
    hims = load_hdr(cond_ims)

    for name in ["etag", "last-modified"]:
        add_check(header_value(hg, name) is None, f"no_{name}_get", "headers_get.txt", "absent", "present" if header_value(hg, name) else "absent")
        add_check(header_value(hh, name) is None, f"no_{name}_head", "headers_head.txt", "absent", "present" if header_value(hh, name) else "absent")

    cc = header_value(hg, "cache-control") or ""
    add_check("no-store" in cc.lower(), "cache_control_no_store", "headers_get.txt", "contains no-store", cc or "(missing)")

    ctype_get = header_value(hg, "content-type") or ""
    add_check(("application/json" in ctype_get.lower()) and ("charset=utf-8" in ctype_get.lower()),
              "ctype_json_utf8_get", "headers_get.txt", "application/json; charset=utf-8", ctype_get or "(missing)")

    ctype_head = header_value(hh, "content-type") or ""
    add_check(ctype_head == ctype_get, "head_content_type_matches_get", "headers_head.txt", ctype_get or "(missing)", ctype_head or "(missing)")

    clen = header_value(hh, "content-length")
    if clen is not None and clen.isdigit():
        got_len = int(clen)
        body_len = len(body1.read_bytes())
        add_check(got_len == body_len, "head_content_length_matches_body_bytes", "headers_head.txt", str(body_len), str(got_len))

    for pth, txt in [("cond_if_none_match_headers.txt", hinm), ("cond_if_modified_since_headers.txt", hims)]:
        sc = parse_status_code(txt)
        add_check(sc == 200, "conditionals_ignored_still_200", pth, "200", str(sc) if sc is not None else "(unparsed)")

    body_bytes = body1.read_bytes()
    add_check(body_bytes.endswith(b"\n"), "body_lf_terminated", "body_get.json", "endswith LF", "endswith LF" if body_bytes.endswith(b"\n") else "missing LF")

    body_obj = None
    try:
        body_obj = json.loads(body_bytes.decode("utf-8"))
    except Exception as e:
        add_check(False, "body_json_parse_ok", "body_get.json", "valid JSON", f"parse_error: {e}")
    if isinstance(body_obj, dict):
        keys = list(body_obj.keys())
        add_check(keys == REQ_KEYS, "body_keys_fixed_order", "body_get.json", " ".join(REQ_KEYS), " ".join(keys))

    release_expected = read_text_optional(Path("artifacts/math/release_id.txt"))
    if isinstance(body_obj, dict) and release_expected is not None:
        add_check(body_obj.get("release_id") == release_expected, "release_id_matches_artifacts_math_release_id", "artifacts/math/release_id.txt", release_expected, str(body_obj.get("release_id")))

    manifest = read_json_optional(Path("artifacts/math/freeze_pack_manifest.json"))
    if isinstance(body_obj, dict) and isinstance(manifest, dict):
        for k in ["release_id","invocation_tag","invocation_sha256","emitter_sha256"]:
            if k in manifest:
                add_check(str(body_obj.get(k)) == str(manifest.get(k)), f"{k}_matches_freeze_pack_manifest", "artifacts/math/freeze_pack_manifest.json", str(manifest.get(k)), str(body_obj.get(k)))

    overall_pass = identical and all(c.get("ok") for c in checks)

    lines = []
    lines.append(f"captured_at_utc: {utc_now()}")
    lines.append(f"two_run_identity.identical: {str(identical).lower()}")
    lines.append(f"two_run_identity.sha256_run1: {sha1}")
    lines.append(f"two_run_identity.sha256_run2: {sha2}")
    lines.append(f"coupling.overall_pass: {str(overall_pass).lower()}")
    lines.append("coupling.checks:")
    for c in checks:
        lines.append(f"- ok={c.get('ok')} label={c.get('label','')} source={c.get('source','')}")
        if "expected" in c and "got" in c:
            lines.append(f"  expected={c['expected']}")
            lines.append(f"  got={c['got']}")
    lines.append("rails_reference: SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod (open rails) + determinism pins")
    lines.append("determinism_pins_reference: audit/gates/determinism/env_pins.log")
    two_run.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if not overall_pass:
        return 10
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
