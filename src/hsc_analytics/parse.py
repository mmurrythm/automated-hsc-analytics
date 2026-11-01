from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import re
from bs4 import BeautifulSoup

LABELS = {
    "college_name": [r"institution name", r"college name", r"institute name"],
    "eiin": [r"\beiin\b"],
    "registered": [r"total registered", r"registered candidates", r"total candidates registered"],
    "appeared": [r"total appeared", r"appeared candidates", r"present candidates"],
    "passed": [r"total passed", r"passed candidates"],
    "failed": [r"total failed", r"failed candidates"],
    "gpa5_count": [r"gpa[- ]?5", r"grade point average 5"],
}

def _clean_int(value):
    if value is None: return None
    digits = re.sub(r"[^0-9]", "", str(value))
    return int(digits) if digits else None

def parse_html_file(path: Path) -> dict:
    html = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "lxml")
    text = " ".join(soup.stripped_strings)
    row = {
        "source_file": str(path),
        "retrieved_at": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
        "source_url": None,
        "parse_status": "needs_review",
        "parser_note": "Generic label parser; validate against each board's actual report layout."
    }
    stem = path.stem.split("_")
    if len(stem) >= 2:
        row["board_code"], row["eiin"] = stem[0], _clean_int(stem[1])
    for field, patterns in LABELS.items():
        if field == "eiin" and row.get("eiin"): continue
        for label in patterns:
            match = re.search(label + r"\s*[:\-]?\s*([A-Za-z0-9][A-Za-z0-9 ,./()&_-]{0,80})", text, re.I)
            if match:
                value = match.group(1).strip()
                row[field] = value if field == "college_name" else _clean_int(value)
                break
    if row.get("appeared") is not None and row.get("passed") is not None:
        row["parse_status"] = "parsed_partial"
    return row
