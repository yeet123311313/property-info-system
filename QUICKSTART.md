# Property Information System - Quick Start

## What's New?

Your app now supports **multiple properties with unique URLs**! Perfect for linking in your CRM.

## How It Works

### 1. Home Page (`/`)
- Lists all your properties
- Click "+ Create New Property" to add a new one
- Each property gets a unique UUID

### 2. Property Pages (`/property/{id}`)
- Each property has a permanent, unique URL
- Example: `http://localhost:10101/property/abc-123-def-456`
- Auto-saves as you type
- Link these URLs in your CRM!

### 3. Database Storage
- All data stored in `properties.db` (SQLite)
- Automatic saving on every field change
- Persistent across restarts

## Local Usage

1. Make sure Wave server is running (should already be running on port 10101)
2. Start the app: `python -m h2o_wave run app.py`
3. Visit: `http://localhost:10101/`
4. Create properties and copy their URLs

## Railway Deployment

Follow the step-by-step guide in `DEPLOY.md` to:
1. Push your code to GitHub
2. Deploy to Railway (free tier available)
3. Get a public URL like `https://your-app.railway.app`
4. Link property URLs in your CRM

## Features

✅ **Unique URLs** - Every property gets its own permanent link  
✅ **Auto-save** - Changes save automatically as you type  
✅ **CRM Integration** - Copy property URLs to your CRM  
✅ **List View** - See all properties at a glance  
✅ **No Data Loss** - SQLite database persistence  
✅ **Railway Ready** - Deploy in minutes  

## Next: Deploy to Railway

See `DEPLOY.md` for complete deployment instructions!
