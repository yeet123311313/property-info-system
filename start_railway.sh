#!/usr/bin/env bash
# Railway startup script

set -e

echo "Starting Property Information System..."

# Download Wave server for Linux (Railway uses Linux)
WAVE_URL="https://github.com/h2oai/wave/releases/download/v0.26.3/wave-0.26.3-linux-amd64.tar.gz"
WAVE_DIR="wave-server"

if [ ! -f "$WAVE_DIR/waved" ]; then
    echo "Downloading Wave server..."
    mkdir -p "$WAVE_DIR"
    curl -L "$WAVE_URL" -o wave.tar.gz
    tar -xzf wave.tar.gz
    mv wave-0.26.3-linux-amd64/* "$WAVE_DIR/"
    chmod +x "$WAVE_DIR/waved"
    rm -rf wave.tar.gz wave-0.26.3-linux-amd64
fi

# Start Wave server in background
echo "Starting Wave server on port 10101..."
"$WAVE_DIR/waved" &
WAVE_PID=$!

# Wait for Wave server to start
sleep 3

# Run the app
echo "Starting Wave app..."
python -m h2o_wave run app.py

# Cleanup on exit
trap "kill $WAVE_PID" EXIT
