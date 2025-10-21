#!/usr/bin/env python
"""
Download and setup H2O Wave server
"""
import urllib.request
import tarfile
import os
import sys
from pathlib import Path
import platform

def download_wave_server():
    """Download the Wave server for Windows"""
    wave_version = "0.26.3"
    
    # Determine the correct download URL
    system = platform.system()
    if system == "Windows":
        filename = f"wave-{wave_version}-windows-amd64.tar.gz"
    else:
        print("This script is designed for Windows. Please download Wave manually from:")
        print("https://github.com/h2oai/wave/releases")
        return None
    
    url = f"https://github.com/h2oai/wave/releases/download/v{wave_version}/{filename}"
    
    print(f"Downloading Wave server v{wave_version}...")
    print(f"URL: {url}")
    
    download_path = Path.cwd() / filename
    
    try:
        urllib.request.urlretrieve(url, download_path)
        print(f"Downloaded to: {download_path}")
        
        # Extract the tar.gz file
        print("Extracting...")
        extract_dir = Path.cwd() / "wave-server"
        extract_dir.mkdir(exist_ok=True)
        
        with tarfile.open(download_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_dir)
        
        print(f"Extracted to: {extract_dir}")
        
        # Clean up zip file
        download_path.unlink()
        
        # Find waved.exe
        waved_path = list(extract_dir.rglob("waved.exe"))
        if waved_path:
            print(f"\nWave server ready at: {waved_path[0]}")
            return waved_path[0]
        else:
            print("Could not find waved.exe in extracted files")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    server_path = download_wave_server()
    if server_path:
        print("\n" + "=" * 60)
        print("Setup complete!")
        print("=" * 60)
        print(f"\nTo start the Wave server, run:")
        print(f'  "{server_path}"')
        print(f"\nThen in another terminal, run:")
        print(f"  python run_app.py")
