from __future__ import annotations
from adapter.retry_after import parse_retry_after_ms
from flask import Blueprint, Response, request
from adapter.etag_core import reader_response
from adapter.etag_core import writer_headers
from engine.stable.sercanon import serialize
import hashlib

bp = Blueprint("reader", __name__)

def _emit_demo_public_bytes_and_hash() -> tuple[bytes, str]:
    # Minimal success envelope (schema-legal, numeric-free)
    env = {
        "reader_version": "v1",
        "eligible": False,
        "categories": [],
        "meta": {"engine_tag": "dev", "invocation_tag": "local-smoke"},
        "release_id": "0"*64,
    }
    # Preimage = env without idempotence_hash
    pre_b = serialize(env)                 # bytes, single LF (canonical)
    h = hashlib.sha256(pre_b).hexdigest()  # lowercase hex
    env["idempotence_hash"] = h
    public_bytes = serialize(env)          # final literal bytes (LF-terminated)
    return public_bytes, h

@bp.route("/reader", methods=["GET", "HEAD"])
def reader():
    public_bytes, id_hash = _emit_demo_public_bytes_and_hash()
    status, headers, body = reader_response(
        public_bytes=public_bytes,
        id_hash_hex=id_hash,
        if_none_match=request.headers.get("If-None-Match"),
        method=request.method,
    )
    return Response(body, status=status, headers=headers, mimetype="application/json; charset=utf-8")

def _error_response(status:int, code:str, message:str, retry_after_value:str|None=None):
    # Build Reader v1 error envelope (no ETag; Cache-Control: no-store)
    env = {"reader_version":"v1", "error":{"code":code, "message":message}}
    ms = parse_retry_after_ms(retry_after_value)
    if ms is not None:
        env["error"]["retry_after_ms"] = ms
    body = serialize(env)
    headers = writer_headers()
    return Response(body, status=status, headers=headers, mimetype="application/json")

@bp.get("/_test/429_seconds")
def _test_429_seconds():
    sec = request.args.get("sec","5")
    resp = _error_response(429, "RateLimited", "TooManyRequests", retry_after_value=sec)
    resp.headers["Retry-After"] = sec
    return resp

@bp.get("/_test/429_date")
def _test_429_date():
    # delta seconds in the future (default 5)
    import datetime as _dt
    from email.utils import format_datetime as _fmt
    delta = int(request.args.get("delta","5"))
    when = _dt.datetime.now(_dt.timezone.utc) + _dt.timedelta(seconds=delta)
    httpdate = _fmt(when)
    resp = _error_response(429, "RateLimited", "TooManyRequests", retry_after_value=httpdate)
    resp.headers["Retry-After"] = httpdate
    return resp