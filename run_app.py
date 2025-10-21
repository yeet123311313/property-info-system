#!/usr/bin/env python
"""
Start the Wave app (assumes server is running)
"""
import subprocess
import sys
from pathlib import Path

app_path = Path(__file__).parent / "app.py"

print("\nStarting Wave app...")
print(f"App file: {app_path}")
print("\nOnce started, open your browser to:")
print("  http://localhost:10101/info-sheet")
print("\nPress Ctrl+C to stop.\n")
print("=" * 60)

subprocess.run([sys.executable, '-m', 'h2o_wave', 'run', str(app_path)])
