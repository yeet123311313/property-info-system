Run instructions - H2O Wave app

Quick steps (bash / WSL):

1) Create and activate virtualenv (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Start the Wave server and app with the helper script:
```bash
bash start_wave.sh
```

If you prefer manual steps:

- Download Wave for your OS from https://github.com/h2oai/wave/releases and extract it into a folder named `wave-server` next to `app.py`.
- Start the Wave server (example):
```bash
./wave-server/waved &
```
- In another terminal, run the app:
```bash
wave run app.py
# or
python -m h2o_wave run app.py
```

Windows (cmd/powershell):

- Download `waved.exe` from the Wave releases and put it in `wave-server`.
- Run `start_wave.bat` or manually:
```powershell
Start-Process -FilePath .\wave-server\waved.exe
# In new terminal
wave run app.py
# or
python -m h2o_wave run app.py
```

Notes:
- If `wave` CLI is not installed, `python -m h2o_wave run app.py` is a fallback but requires the `h2o-wave` package installed in the active Python environment.
- The helper scripts attempt to download a Linux server automatically for non-Windows environments. For Windows, download is manual.

If you want, I can attempt to start the server here and run the app to verify — tell me if you'd like me to try (may be blocked by environment).