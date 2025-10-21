#!/usr/bin/env bash
# start_wave.sh - download (if needed) and start h2o Wave server, then run the app
# Usage: bash start_wave.sh

set -e

WAVE_DIR="wave-server"
WAVE_BIN="$WAVE_DIR/waved"

# If waved not present, download a prebuilt Wave server (linux-amd64). For Windows, use the .bat script.
if [ ! -f "$WAVE_BIN" ]; then
  echo "Wave server not found in $WAVE_DIR. Downloading..."
  mkdir -p "$WAVE_DIR"
  # Try to download latest linux server (if running WSL or Linux)
  WAVE_URL="https://github.com/h2oai/wave/releases/latest/download/wave-linux-amd64.tar.gz"
  curl -L "$WAVE_URL" -o "$WAVE_DIR/wave.tar.gz"
  tar -xzf "$WAVE_DIR/wave.tar.gz" -C "$WAVE_DIR"
  chmod +x "$WAVE_BIN" || true
  rm "$WAVE_DIR/wave.tar.gz"
fi

# Start waved in background
"$WAVE_BIN" &
WAVE_PID=$!
echo "Started wave server (pid=$WAVE_PID). Waiting 1s for startup..."
sleep 1

# Run the wave app using wave CLI if available, otherwise use Python
if command -v wave &> /dev/null; then
  echo "Using wave cli to run app.py"
  wave run app.py
else
  echo "wave cli not found. Running python -m h2o_wave but this requires h2o-wave package and server running."
  python -m h2o_wave run app.py
fi

# On script exit, kill the background waved
trap "echo Killing wave server $WAVE_PID; kill $WAVE_PID || true" EXIT
