# Deploy to Render.com

## Quick Start

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub account
4. Select the `property-info-system` repository
5. Render will auto-detect the `render.yaml` configuration
6. Click "Create Web Service"

## Configuration

Render will automatically:
- Install Python dependencies from `requirements.txt`
- Run `start_render.sh` which:
  - Downloads H2O Wave server
  - Starts the server
  - Runs your app

## After Deployment

Your app will be available at: `https://property-info-system.onrender.com`

Shareable property URLs will work like:
```
https://property-info-system.onrender.com/#property_id=<uuid>
```

## Notes

- Free tier instances spin down after 15 minutes of inactivity
- First load after spin-down will take ~30 seconds
- Database (SQLite) will persist across restarts
