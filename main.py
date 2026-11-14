#!/usr/bin/env python3
"""make.fun entry: writes the bundled text to /output/entry.png. Deterministic, no network."""
import os, shutil
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), "/output/entry.png")
print("entry.png written")
