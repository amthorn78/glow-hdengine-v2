docs/contracts/reader_v1_public_bytes.md

Title: Reader v1 — Public Bytes Contract
Version: 1.0
Owner: Cyrano (Tech Writer)
Status: Canon (A7 scope)
Cards: CORE-READER-A5 (body invariants), A7 transport
References:

docs/server/reader_v1.md (A7 transport, conditional GET, HEAD)

docs/CLI_commands.md (emits the same public bytes as Reader)


1. Scope and invariants

This page defines the exact public body returned by Reader v1 and printed by the CLI for the same inputs. It does not redefine HTTP transport; see docs/server/reader_v1.md.

Non-negotiables:

UTF-8, no BOM; sort_keys=True, separators=(',',':'), ensure_ascii=False.

Exactly one trailing newline (\n).

Numeric-free for SPA.

One emitter for public bytes; CLI and Reader both call it.

Idempotence hash is computed over the canonical preimage (see §3).


Top-level keys (sorted order induced by sort_keys=True):

["categories","eligible","idempotence_hash","meta","release_id"]

2. Allowed values

categories

Array with exactly one object.

Object fields (only): {"id":"harmony","band":"Cool"|"Open"|"Warm"|"Glow"}.


eligible

Boolean (true or false).


idempotence_hash

Lowercase 64-hex. See §3.


meta

Object reserved for audit/operational fields. The Spec owns its internal shape.


release_id

Lowercase 64-hex (sha256 of the release manifest).



3. Idempotence preimage and hash (worked)

Preimage = the response object without the idempotence_hash field, serialized canonically and LF-terminated, then hashed with sha256.

Example preimage (canonical, LF-terminated):

{"categories":[{"band":"Warm","id":"harmony"}],"eligible":true,"meta":{},"release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}

Compute:

# Save the preimage above (with the final newline) as preimage.json
python - <<'PY'
import json,hashlib,sys
b=open("preimage.json","rb").read()
print(hashlib.sha256(b).hexdigest())
PY
# → 3ec639a4be1385cb74c769a14410a5b38dfb9fab2fef4be2fbada43b7716b07c

So:

idempotence_hash = "3ec639a4be1385cb74c769a14410a5b38dfb9fab2fef4be2fbada43b7716b07c"

4. Canonical body (worked, LF-terminated)

Putting it together (sorted keys, compact, UTF-8, one final \n):

{"categories":[{"band":"Warm","id":"harmony"}],"eligible":true,"idempotence_hash":"3ec639a4be1385cb74c769a14410a5b38dfb9fab2fef4be2fbada43b7716b07c","meta":{},"release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}

Validation:

# exact sha256 over the final bytes (including the trailing newline)
python - <<'PY'
import hashlib
b=open("body.json","rb").read()  # body.json contains the JSON above with the final newline
print(hashlib.sha256(b).hexdigest())
PY
# → 8bbd7de9638aed343ca0a302e70c256749789d043cc80316d677456bdb0410f9

5. ETag over final bytes (worked)

For Reader’s success responses (A7), the ETag is the sha256 of the final LF-terminated bytes (pre-compression):

ETag: "8bbd7de9638aed343ca0a302e70c256749789d043cc80316d677456bdb0410f9"

Notes:

Same ETag for identity, gzip, and br encodings.

Quoted, strong validator.

Conditional GET uses strong comparison; see docs/server/reader_v1.md.


6. Equivalence to CLI and Reader

The CLI prints exactly the bytes in §4 for the same inputs.

Reader v1 returns exactly those bytes in the 200 body.

Both call the same emitter.


7. Quick checks (copy-paste)

# canonical formatting check: one trailing LF, no BOM, no ANSI
python - <<'PY'
import re,sys
b=open("body.json","rb").read()
assert b.endswith(b"\n")
assert not b.startswith(b"\xef\xbb\xbf")
assert not re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]').search(b)
print("CANON_FORMAT_OK")
PY

# idempotence preimage check
python - <<'PY'
import json,hashlib
o=json.load(open("body.json","r",encoding="utf-8"))
pre=dict(o); pre.pop("idempotence_hash",None)
canon=(json.dumps(pre,sort_keys=True,separators=(',',':'),ensure_ascii=False)+"\n").encode()
print("IDEMP_OK" if hashlib.sha256(canon).hexdigest()==o["idempotence_hash"] else "IDEMP_FAIL")
PY

# ETag check (matches §5)
python - <<'PY'
import hashlib
b=open("body.json","rb").read()
print("ETAG_OK" if hashlib.sha256(b).hexdigest()=="8bbd7de9638aed343ca0a302e70c256749789d043cc80316d677456bdb0410f9" else "ETAG_FAIL")
PY

8. Change control

This page is the single contract source for the public body.

Any schema change or additional category requires a Spec update and a doc delta here.

Transport rules live in docs/server/reader_v1.md; do not duplicate them here.


End of contract.