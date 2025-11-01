# 🧠 Krita Python API — Control the Canvas with Code

Krita ships with a **Python scripting engine** that lets you automate, extend, and even draw with code.

---

## 🧩 Enable Scripting
1. Open Krita → `Settings → Configure Krita → Python Plugin Manager`
2. Check ✅ “Scripter” and “Python Plugin Importer”
3. Restart Krita

---

## ⚙️ Basic Script Structure

```python
from krita import *

app = Krita.instance()
doc = app.activeDocument()
node = doc.activeNode()

print("Active layer:", node.name())
