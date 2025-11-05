# Writers Auth Boundary (EPIC-008)

- Scheme: `Authorization: Bearer`
- Scope: `admin:write`
- 401: `{"ok":false,"schema":"v1","code":"unauthorized","error":"authorization required"}`
- 403: `{"ok":false,"schema":"v1","code":"forbidden","error":"insufficient scope"}`
