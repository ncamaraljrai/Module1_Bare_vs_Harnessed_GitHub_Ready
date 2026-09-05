#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path("DIAGNOSTIC_LOG.md")
text = path.read_text(encoding="utf-8")

count = text.count("RECORD")
if count:
    print(f"FAIL: {count} RECORD placeholder(s) remain in {path}")
    sys.exit(1)

required = [
    "| Bare |",
    "| Harnessed |",
    "| Ablated |",
    "Layer attribution",
    "Ablation impact statement",
]

missing = [item for item in required if item not in text]
if missing:
    print("FAIL: missing required sections:", ", ".join(missing))
    sys.exit(1)

print("PASS: diagnostic log has no RECORD placeholders and required sections are present.")
