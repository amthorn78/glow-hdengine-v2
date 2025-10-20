# ==== ARCH_CAPTURE_START (auto: architecture capture + structural guards) ====
EPIC_ID_ENV="${EPIC_ID:-${CARD:-UNSPECIFIED_EPIC}}"

# 1) Capture a timestamped architecture snapshot
if [ ! -x scripts/architecture_capture.sh ]; then
  echo "ERROR: scripts/architecture_capture.sh missing or not executable" >&2
  exit 1
fi
echo "[arch] capture: EPIC_ID=${EPIC_ID_ENV}"
scripts/architecture_capture.sh "${EPIC_ID_ENV}"

# 2) Run structural guard suite (must pass)
LATEST_ARCH="$(ls -1d _arch/* 2>/dev/null | sort | tail -1 || true)"
if command -v pytest >/dev/null 2>&1; then
  echo "[arch] running structural guards (pytest tests/arch)"
  pytest -q tests/arch
else
  echo "ERROR: pytest not found; structural guards required at close." >&2
  exit 1
fi

# 3) Append a short note to the closeout log if available
if [ -n "${CLOSE_MD:-}" ] && [ -f "${CLOSE_MD}" ]; then
  {
    echo "- Architecture snapshot: ${LATEST_ARCH:-_arch/(not found)}"
    echo "- Arch guards: PASS (tests/arch)"
  } >> "${CLOSE_MD}"
fi
echo "[arch] ${LATEST_ARCH:-_arch/(not found)}"
# ==== ARCH_CAPTURE_END ====
