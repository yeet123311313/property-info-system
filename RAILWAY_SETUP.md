# Railway Deployment Guide

## Quick Setup Steps

### 1. Prerequisites
- A GitHub account
- A Railway account (sign up at https://railway.app)
- Your code pushed to a GitHub repository

### 2. Push Your Code to GitHub

If you haven't already, initialize git and push your code:

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Property Information System"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 3. Deploy to Railway

1. **Go to Railway Dashboard**
   - Visit https://railway.app/dashboard
   - Click "New Project"

2. **Deploy from GitHub**
   - Select "Deploy from GitHub repo"
   - Connect your GitHub account if not already connected
   - Search for and select your repository
   - Click "Deploy Now"

3. **Wait for Deployment**
   - Railway will automatically detect Python and use Nixpacks to build
   - The build process will:
     - Install Python 3.10
     - Install dependencies from `requirements.txt`
     - Run `start_railway.sh` to start Wave server and app
   - This takes about 2-3 minutes

4. **Generate a Public Domain**
   - Once deployed, click on your service
   - Go to the "Settings" tab
   - Scroll to "Networking" section
   - Click "Generate Domain"
   - You'll get a URL like: `https://your-app.railway.app`

5. **Done!**
   - Your app is now live at the generated URL
   - Each property will have a unique shareable link like:
     `https://your-app.railway.app/#property_id=abc-123-def-456`

## How Unique URLs Work

### On Railway:
- **Base URL**: `https://your-app.railway.app/`
- **Property URL**: `https://your-app.railway.app/#property_id=<uuid>`

### In Your CRM:
1. Open any property in the app
2. Copy the URL shown at the top of the property page
3. Paste it into your CRM as the property link
4. Anyone clicking that link will go directly to that property

### Example:
```
Property A: https://your-app.railway.app/#property_id=123e4567-e89b-12d3-a456-426614174000
Property B: https://your-app.railway.app/#property_id=987f6543-e21c-98d7-b654-426614174111
```

## Database Persistence

The app uses SQLite for data storage. On Railway:
- Data persists between deployments
- Each property has a permanent UUID
- Properties are stored in `properties.db`

**Note**: For production use with high traffic, consider upgrading to PostgreSQL later.

## Environment Variables (Optional)

You can set environment variables in Railway:
1. Go to your service settings
2. Click "Variables" tab
3. Add any needed variables

Current setup doesn't require any environment variables to work.

## Monitoring & Logs

To view logs:
1. Click on your service in Railway
2. Go to "Deployments" tab
3. Click on the active deployment
4. View real-time logs

## Cost

Railway offers:
- **Free Tier**: $5 of usage credit per month (sufficient for testing)
- **Hobby Plan**: $5/month for more resources
- **Pro Plan**: Pay-as-you-go for production apps

This app should stay within free tier limits for moderate usage.

## Troubleshooting

### Deployment Failed
- Check build logs in Railway dashboard
- Ensure `requirements.txt` is present
- Verify `start_railway.sh` has execute permissions

### App Not Loading
- Check deploy logs for errors
- Ensure Wave server started successfully
- Look for port binding issues

### Need Help?
- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.com
