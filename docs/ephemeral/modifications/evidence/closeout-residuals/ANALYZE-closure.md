# ANALYZE closure — MODIFICATION-20260923-closeout-residuals

`PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/closure.py <ID>` over `docs/graph/parts` at
`main` `77d98dd`, for each of the 48 prompts this Modification touches, pasted as printed. Every run exited 0.

```
CF-C-10  -- closure over 55 graph parts

  upstream                       4  CF-C-20, CF-E-10, CF-PO-10, MGR-10
  downstream                     4  CF-C-10, CF-C-20, CF-E-10, CF-PO-10
  state_sharers                 19  CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CF-PO-10, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, MGR-10, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
```

```
CF-C-20  -- closure over 55 graph parts

  upstream                       1  CF-C-10
  downstream                     2  CF-C-10, CF-C-30
  state_sharers                 21  CF-C-10, CF-C-40, CF-E-10, CF-E-20, CF-E-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
```

```
CF-C-30  -- closure over 55 graph parts

  upstream                       2  CF-C-20, CF-C-40
  downstream                     2  CF-C-40, IA-10
  state_sharers                  2  CF-E-30, IA-30
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CF-C-20, CF-C-40, CF-E-30, IA-10, IA-30
```

```
CF-C-40  -- closure over 55 graph parts

  upstream                       1  CF-C-30
  downstream                     1  CF-C-30
  state_sharers                  3  CF-C-20, CF-E-20, CF-E-40
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 4
  CF-C-20, CF-C-30, CF-E-20, CF-E-40
```

```
CF-E-10  -- closure over 55 graph parts

  upstream                       4  CF-C-10, CF-E-20, CF-PO-10, MGR-10
  downstream                     4  CF-C-10, CF-E-10, CF-E-20, CF-PO-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CF-PO-10, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, MGR-10, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
```

```
CF-E-20  -- closure over 55 graph parts

  upstream                       1  CF-E-10
  downstream                     2  CF-E-10, CF-E-30
  state_sharers                 21  CF-C-10, CF-C-20, CF-C-40, CF-E-10, CF-E-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-C-40, CF-E-10, CF-E-30, CF-E-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
```

```
CF-E-30  -- closure over 55 graph parts

  upstream                       2  CF-E-20, CF-E-40
  downstream                     2  CF-E-40, IA-10
  state_sharers                  2  CF-C-30, IA-30
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CF-C-30, CF-E-20, CF-E-40, IA-10, IA-30
```

```
CF-E-40  -- closure over 55 graph parts

  upstream                       1  CF-E-30
  downstream                     1  CF-E-30
  state_sharers                  3  CF-C-20, CF-C-40, CF-E-20
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 4
  CF-C-20, CF-C-40, CF-E-20, CF-E-30
```

```
CL-20  -- closure over 55 graph parts

  upstream                       2  CL-C-10, CL-E-10
  downstream                     5  CL-30, CL-40, CL-E-20, CL-E-30, CL-E-40
  state_sharers                  0  -
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 7
  CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40
```

```
CL-30  -- closure over 55 graph parts

  upstream                       1  CL-20
  downstream                     1  CL-40
  state_sharers                  0  -
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 2
  CL-20, CL-40
```

```
CL-40  -- closure over 55 graph parts

  upstream                       4  CL-20, CL-30, CL-E-40, MGR-10
  downstream                     1  CL-40
  state_sharers                  7  CL-E-20, DOC-20, ESC-25, OPS-20, QA-100, QA-110, UTIL-10
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 12
  CL-20, CL-30, CL-40, CL-E-20, CL-E-40, DOC-20, ESC-25, MGR-10, OPS-20, QA-100, QA-110, UTIL-10
```

```
CL-C-10  -- closure over 55 graph parts

  upstream                       1  QA-120
  downstream                     2  CL-20, ESC-30
  state_sharers                  1  CL-E-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 4
  CL-20, CL-E-10, ESC-30, QA-120
```

```
CL-E-10  -- closure over 55 graph parts

  upstream                       1  QA-120
  downstream                     3  CL-20, CL-E-20, ESC-30
  state_sharers                  1  CL-C-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 5
  CL-20, CL-C-10, CL-E-20, ESC-30, QA-120
```

```
CL-E-20  -- closure over 55 graph parts

  upstream                       4  CL-20, CL-E-10, CL-E-30, CL-E-40
  downstream                     2  CL-E-20, CL-E-30
  state_sharers                 21  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, UTIL-10
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 26
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-20, CL-40, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, UTIL-10
```

```
CL-E-30  -- closure over 55 graph parts

  upstream                       2  CL-20, CL-E-20
  downstream                     2  CL-E-20, CL-E-40
  state_sharers                  5  ESC-40, OPS-30, PR-40, QA-110, QA-70
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 8
  CL-20, CL-E-20, CL-E-40, ESC-40, OPS-30, PR-40, QA-110, QA-70
```

```
CL-E-40  -- closure over 55 graph parts

  upstream                       2  CL-20, CL-E-30
  downstream                     2  CL-40, CL-E-20
  state_sharers                  0  -
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 4
  CL-20, CL-40, CL-E-20, CL-E-30
```

```
DOC-10  -- closure over 55 graph parts

  upstream                       1  DOC-20
  downstream                     3  DOC-10, PR-20, RS-10
  state_sharers                 20  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10
```

```
DOC-20  -- closure over 55 graph parts

  upstream                       0  -
  downstream                     4  DOC-10, PR-40, QA-10, RS-10
  state_sharers                 23  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-110, QA-20, QA-50, QA-60, UTIL-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 25
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-10, QA-100, QA-110, QA-20, QA-50, QA-60, RS-10, UTIL-10
```

```
ESC-10  -- closure over 55 graph parts

  upstream                       3  QA-110, QA-120, QA-90
  downstream                     1  ESC-30
  state_sharers                  0  -
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 4
  ESC-30, QA-110, QA-120, QA-90
```

```
ESC-25  -- closure over 55 graph parts

  upstream                       4  ESC-30, OPS-10, OPS-20, OPS-30
  downstream                     1  ESC-30
  state_sharers                 21  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, UTIL-10
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, UTIL-10
```

```
ESC-30  -- closure over 55 graph parts

  upstream                       6  CL-C-10, CL-E-10, ESC-10, ESC-25, ESC-40, QA-10
  downstream                     2  ESC-25, ESC-40
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 24
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-C-10, CL-E-10, CL-E-20, DOC-10, DOC-20, ESC-10, ESC-25, ESC-40, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-10, QA-100, QA-20, QA-50, QA-60
```

```
ESC-40  -- closure over 55 graph parts

  upstream                       1  ESC-30
  downstream                     3  ESC-30, PR-30, PR-35
  state_sharers                  3  CL-E-30, QA-70, RS-20
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 6
  CL-E-30, ESC-30, PR-30, PR-35, QA-70, RS-20
```

```
GCFPE-MGMT-10  -- closure over 55 graph parts

  upstream                       0  -
  downstream                     1  PR-10
  state_sharers                  0  -
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 1
  PR-10
```

```
IA-30  -- closure over 55 graph parts

  upstream                       4  IA-10, IA-20, IA-40, IA-50
  downstream                     2  IA-40, PR-10
  state_sharers                  6  CF-C-30, CF-E-30, IA-40, PR-30, PR-35, RS-40
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  CF-C-30, CF-E-30, IA-10, IA-20, IA-40, IA-50, PR-10, PR-30, PR-35, RS-40
```

```
OPS-10  -- closure over 55 graph parts

  upstream                       1  OPS-30
  downstream                     3  ESC-25, OPS-20, RS-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 21
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-20, OPS-30, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, RS-10
```

```
OPS-20  -- closure over 55 graph parts

  upstream                       1  OPS-10
  downstream                     3  ESC-25, OPS-30, RS-10
  state_sharers                 22  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, QA-90, UTIL-10
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 24
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-30, PR-10, PR-20, QA-100, QA-20, QA-50, QA-60, QA-90, RS-10, UTIL-10
```

```
OPS-30  -- closure over 55 graph parts

  upstream                       1  OPS-20
  downstream                     3  ESC-25, OPS-10, RS-10
  state_sharers                  4  CL-E-30, PR-40, QA-110, RS-20
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 8
  CL-E-30, ESC-25, OPS-10, OPS-20, PR-40, QA-110, RS-10, RS-20
```

```
PR-10  -- closure over 55 graph parts

  upstream                       3  GCFPE-MGMT-10, IA-30, PR-40
  downstream                     3  PR-10, PR-20, RS-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-20, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 24
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, GCFPE-MGMT-10, IA-10, IA-20, IA-30, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10
```

```
PR-20  -- closure over 55 graph parts

  upstream                       3  DOC-10, PR-10, PR-40
  downstream                     2  PR-20, RS-10
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, QA-100, QA-20, QA-50, QA-60
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_PROCEED, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, PR-40, QA-100, QA-20, QA-50, QA-60, RS-10
```

```
PR-30  -- closure over 55 graph parts

  upstream                       3  ESC-40, RS-20, RS-40
  downstream                     3  PR-30, PR-35, RS-20
  state_sharers                  3  IA-30, PR-35, RS-40
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 6
  ESC-40, IA-30, PR-30, PR-35, RS-20, RS-40
```

```
PR-35  -- closure over 55 graph parts

  upstream                       4  ESC-40, PR-30, RS-20, RS-40
  downstream                     3  PR-35, PR-40, RS-20
  state_sharers                  3  IA-30, PR-30, RS-40
  boundaries (NOT consumers)     2  NATHAN_MANUAL_MERGE_ASSERTION, NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 7
  ESC-40, IA-30, PR-30, PR-35, PR-40, RS-20, RS-40
```

```
PR-40  -- closure over 55 graph parts

  upstream                       3  DOC-20, PR-35, RS-40
  downstream                     3  PR-10, PR-20, RS-10
  state_sharers                  6  CL-E-30, DOC-10, DOC-20, OPS-30, QA-110, RS-20
  boundaries (NOT consumers)     3  ACTUAL_OWNER_TERMINAL_RETURN, NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 11
  CL-E-30, DOC-10, DOC-20, OPS-30, PR-10, PR-20, PR-35, QA-110, RS-10, RS-20, RS-40
```

```
PR-50  -- closure over 55 graph parts

  upstream                       0  -
  downstream                     0  -
  state_sharers                  0  -
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 0
  -
```

```
QA-10  -- closure over 55 graph parts

  upstream                       3  DOC-20, MGR-10, QA-20
  downstream                     2  ESC-30, QA-20
  state_sharers                  0  -
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 4
  DOC-20, ESC-30, MGR-10, QA-20
```

```
QA-100  -- closure over 55 graph parts

  upstream                       2  QA-110, QA-90
  downstream                     1  QA-110
  state_sharers                 22  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-20, QA-50, QA-60, QA-90, UTIL-10
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 23
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-40, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-110, QA-20, QA-50, QA-60, QA-90, UTIL-10
```

```
QA-110  -- closure over 55 graph parts

  upstream                       3  QA-100, QA-120, QA-90
  downstream                     4  ESC-10, QA-100, QA-120, QA-90
  state_sharers                  7  CL-40, CL-E-30, DOC-20, OPS-30, PR-40, QA-90, UTIL-10
  boundaries (NOT consumers)     2  ACTUAL_OWNER_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  CL-40, CL-E-30, DOC-20, ESC-10, OPS-30, PR-40, QA-100, QA-120, QA-90, UTIL-10
```

```
QA-120  -- closure over 55 graph parts

  upstream                       1  QA-110
  downstream                     5  CL-C-10, CL-E-10, ESC-10, QA-110, QA-90
  state_sharers                  0  -
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 5
  CL-C-10, CL-E-10, ESC-10, QA-110, QA-90
```

```
QA-20  -- closure over 55 graph parts

  upstream                       1  QA-10
  downstream                     2  QA-10, QA-50
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-50, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 20
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-10, QA-100, QA-50, QA-60
```

```
QA-50  -- closure over 55 graph parts

  upstream                       1  QA-20
  downstream                     4  QA-60, QA-70, QA-80, QA-90
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-60
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-60, QA-70, QA-80, QA-90
```

```
QA-60  -- closure over 55 graph parts

  upstream                       1  QA-50
  downstream                     3  QA-70, QA-80, QA-90
  state_sharers                 19  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 22
  CF-C-10, CF-C-20, CF-E-10, CF-E-20, CL-E-20, DOC-10, DOC-20, ESC-25, ESC-30, IA-10, IA-20, IA-60, OPS-10, OPS-20, PR-10, PR-20, QA-100, QA-20, QA-50, QA-70, QA-80, QA-90
```

```
QA-70  -- closure over 55 graph parts

  upstream                       3  QA-50, QA-60, QA-80
  downstream                     2  QA-80, QA-90
  state_sharers                  3  CL-E-30, ESC-40, RS-20
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 7
  CL-E-30, ESC-40, QA-50, QA-60, QA-80, QA-90, RS-20
```

```
QA-80  -- closure over 55 graph parts

  upstream                       3  QA-50, QA-60, QA-70
  downstream                     1  QA-70
  state_sharers                  1  IA-40
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 4
  IA-40, QA-50, QA-60, QA-70
```

```
QA-90  -- closure over 55 graph parts

  upstream                       5  QA-110, QA-120, QA-50, QA-60, QA-70
  downstream                     3  ESC-10, QA-100, QA-110
  state_sharers                  3  OPS-20, QA-100, QA-110
  boundaries (NOT consumers)     1  NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 8
  ESC-10, OPS-20, QA-100, QA-110, QA-120, QA-50, QA-60, QA-70
```

```
RS-10  -- closure over 55 graph parts

  upstream                       8  DOC-10, DOC-20, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-40
  downstream                     1  RS-20
  state_sharers                  1  RS-30
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 10
  DOC-10, DOC-20, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-40, RS-20, RS-30
```

```
RS-20  -- closure over 55 graph parts

  upstream                       5  PR-30, PR-35, RS-10, RS-30, RS-40
  downstream                     4  PR-30, PR-35, RS-30, RS-40
  state_sharers                  4  ESC-40, OPS-30, PR-40, QA-70
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 9
  ESC-40, OPS-30, PR-30, PR-35, PR-40, QA-70, RS-10, RS-30, RS-40
```

```
RS-30  -- closure over 55 graph parts

  upstream                       1  RS-20
  downstream                     1  RS-20
  state_sharers                  1  RS-10
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 2
  RS-10, RS-20
```

```
RS-40  -- closure over 55 graph parts

  upstream                       1  RS-20
  downstream                     4  PR-30, PR-35, PR-40, RS-20
  state_sharers                  3  IA-30, PR-30, PR-35
  boundaries (NOT consumers)     2  NATHAN_MANUAL_MERGE_ASSERTION, NATHAN_TERMINAL_RETURN

  radius a Tier 1 gate must cover: 5
  IA-30, PR-30, PR-35, PR-40, RS-20
```

```
UTIL-10  -- closure over 55 graph parts

  upstream                       0  -
  downstream                     0  -
  state_sharers                  7  CL-40, CL-E-20, DOC-20, ESC-25, OPS-20, QA-100, QA-110
  boundaries (NOT consumers)     2  NATHAN_TERMINAL_RETURN, ORIGINAL_NATIVE_STAGE

  radius a Tier 1 gate must cover: 7
  CL-40, CL-E-20, DOC-20, ESC-25, OPS-20, QA-100, QA-110
```
