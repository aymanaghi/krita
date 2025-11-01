#!/usr/bin/env python3
"""
export-layers.py
Exports all layers in the current Krita document to PNGs.
"""
from krita import *
import os

app = Krita.instance()
doc = app.activeDocument()

if not doc:
    print("⚠️ No document open.")
else:
    out_dir = os.path.expanduser("~/KritaExports")
    os.makedirs(out_dir, exist_ok=True)
    for node in doc.topLevelNodes():
        name = node.name().replace(" ", "_")
        path = os.path.join(out_dir, f"{name}.png")
        doc.exportImage(path, InfoObject())
        print(f"✅ Exported {name}.png")
    print("🎨 All layers exported successfully.")
