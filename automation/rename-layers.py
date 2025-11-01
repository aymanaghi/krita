#!/usr/bin/env python3
"""
rename-layers.py
Renames layers to a clean lowercase format.
"""
from krita import *

app = Krita.instance()
doc = app.activeDocument()

if not doc:
    print("⚠️ No open document.")
else:
    for node in doc.topLevelNodes():
        old_name = node.name()
        new_name = old_name.lower().replace(" ", "_")
        node.setName(new_name)
        print(f"🧩 {old_name} → {new_name}")
    print("✅ All layers renamed cleanly.")
