#!/bin/bash
set -e

echo "Setting up H2O Wave on Render..."

# Download Wave server for Linux
WAVE_VERSION="0.26.3"
WAVE_ARCHIVE="wave-${WAVE_VERSION}-linux-amd64.tar.gz"
WAVE_URL="https://github.com/h2oai/wave/releases/download/v${WAVE_VERSION}/${WAVE_ARCHIVE}"

echo "Downloading Wave server..."
wget -q "$WAVE_URL"
tar -xzf "$WAVE_ARCHIVE"
rm "$WAVE_ARCHIVE"

echo "Starting Wave server..."
cd "wave-${WAVE_VERSION}-linux-amd64"
./waved &
WAVED_PID=$!

echo "Waiting for Wave server to start..."
sleep 5

cd ..
echo "Starting Wave app..."
python -m h2o_wave run app.py &
APP_PID=$!

# Keep the script running
wait $WAVED_PID $APP_PID
