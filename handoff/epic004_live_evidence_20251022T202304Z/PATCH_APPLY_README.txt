Manual apply (no git):
1) Create new file: engine/serializer/canon.py (see below).
2) Edit engine/presenter/emitter.py to import and use canon.dumps.
3) Edit adapter/http_reader.py to use the shared emitter in _error(...) AND keep the small POST 405 route.
4) Add scripts: scripts/capture_reader_headers.py and scripts/guards/check_forbidden_serializers.sh.
5) Place evidence under _arch/EPIC004_<ts>/ and artifacts/epic004/ as-is (for audit only; not required at runtime).
6) Re-run the header capture in your environment if desired and update artifacts.

Rationale: Keep one shared serializer/emitter; public JSON must be UTF-8, sorted keys, compact, one LF; dev Reader proves A7 transport.
