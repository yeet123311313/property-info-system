#!/usr/bin/env python
"""
Complete script to start both Wave server and app
"""
import subprocess
import sys
import time
import os
from pathlib import Path
import signal

def main():
    # Paths
    base_dir = Path(__file__).parent
    server_exe = base_dir / "wave-server" / "wave-0.26.3-windows-amd64" / "waved.exe"
    server_dir = server_exe.parent
    app_file = base_dir / "app.py"
    
    if not server_exe.exists():
        print("Wave server not found! Please run: python setup_wave.py")
        return
    
    print("=" * 60)
    print("Starting H2O Wave Property Information Sheet")
    print("=" * 60)
    
    # Start the Wave server
    print(f"\n1. Starting Wave server...")
    print(f"   Server directory: {server_dir}")
    
    server_process = subprocess.Popen(
        [str(server_exe)],
        cwd=str(server_dir),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == 'win32' else 0
    )
    
    print("   Wave server started!")
    print("   Waiting for server to be ready...")
    time.sleep(3)
    
    # Start the Wave app
    print(f"\n2. Starting the app...")
    print(f"   App file: {app_file}")
    
    try:
        app_process = subprocess.Popen(
            [sys.executable, '-m', 'h2o_wave', 'run', str(app_file)],
            cwd=str(base_dir)
        )
        
        print("\n" + "=" * 60)
        print("✓ App is running!")
        print("=" * 60)
        print("\nOpen your browser and navigate to:")
        print("  → http://localhost:10101/info-sheet")
        print("\nPress Ctrl+C to stop both server and app")
        print("=" * 60 + "\n")
        
        # Wait for the app process
        app_process.wait()
        
    except KeyboardInterrupt:
        print("\n\nStopping...")
    finally:
        # Clean up
        if 'app_process' in locals():
            app_process.terminate()
        server_process.terminate()
        print("Stopped.")

if __name__ == "__main__":
    main()
