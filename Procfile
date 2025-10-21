# Procfile for Railway deployment
# This tells Railway how to start your app

# Start the Wave server in the background and then run the Wave app
web: ./wave-server/wave-0.26.3-windows-amd64/waved & sleep 2 && python -m h2o_wave run app.py --port $PORT
