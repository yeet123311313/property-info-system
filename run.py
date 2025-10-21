#!/usr/bin/env python
"""
Simple script to run H2O Wave app
This will start the Wave server and the app together
"""
import subprocess
import sys
import time
import os
from pathlib import Path

def main():
    print("Starting H2O Wave Property Information Sheet App...")
    print("=" * 60)
    
    # Start the app using h2o_wave's built-in server
    app_path = Path(__file__).parent / "app.py"
    
    try:
        # Use h2o_wave.cli to run the app
        from h2o_wave import cli
        
        print("\nStarting Wave app...")
        print(f"App file: {app_path}")
        print("\nOnce started, open your browser to:")
        print("  http://localhost:10101/info-sheet")
        print("\nPress Ctrl+C to stop the server.\n")
        print("=" * 60)
        
        # Run the wave app
        sys.argv = ['wave', 'run', str(app_path)]
        cli.main()
        
    except KeyboardInterrupt:
        print("\n\nShutting down...")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTrying alternative method...")
        
        # Alternative: Start with wave command if installed
        try:
            subprocess.run(['wave', 'run', str(app_path)])
        except FileNotFoundError:
            print("\nWave CLI not found. Installing...")
            print("Please wait...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'h2o-wave'])
            print("\nNow starting the app...")
            subprocess.run(['wave', 'run', str(app_path)])

if __name__ == '__main__':
    main()
