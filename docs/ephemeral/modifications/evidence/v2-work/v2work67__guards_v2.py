"""The v2 registry guards, with every §12 decision applied."""
PID = (r"(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|"
       r"the next prompt|the destination prompt|a main-ecosystem prompt)")
HDR = r"\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?"
HDR_END = r"(?:\*\*|__|`)?[ \t]*:"
STEP5 = ["CF-C-10", "CF-C-20", "CF-C-30", "CF-C-40", "CF-E-10", "CF-E-20", "CF-E-30", "CF-E-40", "CF-PO-10", "MGR-10"]
LAT10 = ["PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "RS-10", "RS-20", "DOC-10", "DOC-20", "IA-30"]
ASK4 = ["QA-60", "QA-80", "RS-10", "RS-30"]
# id, list, value, rule_id, rows, homes (required only)
GUARDS = [
 ("G01", "forbidden_regex", "CONTROL_NOTION", "CTR-001", "ALL55", None),
 ("G02", "forbidden_regex", r"(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b", "CTR-001", "ALL55", None),
 ("G03", "forbidden_regex", "Notion and repository persistence", "CTR-001", ["QA-10"], None),
 ("G04", "forbidden_regex", "Notion-resident artifact", "CTR-001", STEP5, None),
 ("G05", "required_regex", r"never\s+carries\s+the\s+only\s+copy", "CTR-002", "NPH53", ["C-ART"]),
 ("G06", "forbidden_regex", r"NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)", "TOP-001", "NPH53", None),
 ("G07", "required_regex", r"The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.", "TOP-001", "NPH53", ["C-PLACE", "C-PLACE ASK OK? variant"]),
 ("G08", "forbidden_regex", r"\bends? `ASK OK\?`", "CTR-002", ASK4, None),
 ("G08A", "required_regex", r"`ASK OK\?` is the line immediately before the block\.", "TOP-001", ASK4, ["C-PLACE ASK OK? variant"]),
 ("G09", "required_regex", r"An\s+\*?In-flight decisions\*?\s+section", "CTR-002", ["PR-30", "PR-35", "RS-40"], ["C-DEC"]),
 ("G10", "required_regex", "Decide it during work", "CTR-002", LAT10, ["C-LAT"]),
 ("G11", "required_regex", r"\*{0,2}Material\*{0,2} means a change to the Epic-level commitment", "CTR-002", LAT10, ["C-LAT"]),
 ("G12", "forbidden_regex", HDR + r"Prompt [Vv]ersion" + HDR_END, "SRC-001", "ALL55", None),
 ("G13", "forbidden_regex", HDR + r"Ecosystem release" + HDR_END, "INV-003", "ALL55", None),
 ("G14", "forbidden_regex", HDR + r"Set" + HDR_END, "SRC-001", "ALL55", None),
 ("G15", "forbidden_regex", r"Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session", "CTR-001", "MAIN54", None),
 ("G16", "required_regex", "they do not share a session", "CTR-002", ["PR-30", "PR-35", "RS-40"], ["C-SESSION"]),
 ("G17", "required_regex", r"never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30", "CTR-002", ["PR-30", "PR-35", "RS-40"], ["C-SESSION"]),
 ("G18", "required_regex", r"never\s+as\s+a\s+subagent\s+of\s+another\s+session", "CTR-002", "MAIN54", ["C-TOP"]),
 ("G19", "forbidden_regex", r"(?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?" + PID + r"(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b", "CTR-001", "MAIN54", None),
 ("G20", "forbidden_regex", r"(?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?" + PID, "CTR-001", "MAIN54", None),
 ("G21", "forbidden_regex", r"(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b", "CTR-001", "MAIN54", None),
 ("G22", "forbidden_regex", "launched as a new session", "CTR-001", ["PR-35", "RS-40"], None),
 ("G23", "required_regex", r"[Ss]ubscribe to the pull request", "CTR-002", ["PR-35", "RS-40"], ["C-SUB"]),
 ("G24", "required_regex", "stay subscribed and do not poll", "CTR-002", ["PR-35", "RS-40"], ["C-DISPATCH"]),
 ("G25", "required_regex", "The observed merge event is the fact PR-40 is entered on", "CTR-002", ["PR-35", "RS-40"], ["C-DISPATCH"]),
 ("G26", "forbidden_regex", "original Proceed and a suitable actual authorized implementation vehicle", "CTR-001", ["PR-40"], None),
 ("G27", "required_regex", r"accepts\s+a\s+`?PR_WORK_UNIT_LINEAGE_REVIEW`?\s+whose\s+result\s+is\s+`?REJECT", "CTR-002", ["PR-20"], ["C-PR20-ENTRY"]),
]
# Candidate for the gap §12 leaves on PR-40 (Unsettled): not in GUARDS
G25_PR40_CANDIDATE = ("G25P", "required_regex", "PR-40 is entered on the observed merge event", "CTR-002", ["PR-40"], ["W-4 PR-40 entry"])
