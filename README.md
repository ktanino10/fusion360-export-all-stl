# Export All Components as STL – Fusion 360 Script

This is a Python script for Autodesk Fusion 360 that exports **all components in the active design** as individual `.stl` files.  
It's especially useful for 3D printing projects involving many parts (e.g. robotic mechanisms, mechanical models, modular assemblies).

---

## ✅ Features

- Exports all components including subcomponents (via occurrences)
- Files are saved with component names
- Simple, clean Python code using Fusion 360 API
- Easy to customize

---

## 📁 File Structure

```plaintext
fusion360-export-all-stl/
├── ExportAllSTLs.py      ← Main script
├── README.md             ← This documentation
└── LICENSE               ← Recommended: MIT or other open license
