# Deploying to Railway

This guide will help you deploy your Property Information System to Railway so you can have unique URLs for each property to link in your CRM.

## What You'll Get

After deployment, you'll have:
- A home page at `https://your-app.railway.app/` that lists all properties
- Unique URLs for each property like `https://your-app.railway.app/property/abc-123-def-456`
- Auto-save functionality - all changes are saved automatically to a database
- Persistent storage using SQLite

## Prerequisites

1. A [Railway account](https://railway.app/) (free tier available)
2. [Git](https://git-scm.com/) installed on your computer
3. This project folder

## Step-by-Step Deployment

### 1. Initialize Git Repository (if not already done)

Open a terminal in your project folder and run:

```bash
git init
git add .
git commit -m "Initial commit - Property Information System"
```

### 2. Create a Railway Project

1. Go to [railway.app](https://railway.app/) and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. If prompted, connect your GitHub account
5. You'll need to push your code to GitHub first (see Step 3)

### 3. Push to GitHub

1. Create a new repository on [GitHub](https://github.com/new)
2. Name it something like `property-info-system`
3. Don't initialize with README (you already have files)
4. Copy the commands GitHub shows you, something like:

```bash
git remote add origin https://github.com/YOUR-USERNAME/property-info-system.git
git branch -M main
git push -u origin main
```

### 4. Deploy on Railway

1. Back in Railway, click **"Deploy from GitHub repo"**
2. Select your `property-info-system` repository
3. Railway will automatically detect the configuration from `railway.json`
4. Click **"Deploy"**

### 5. Configure Environment (Optional)

Railway will automatically assign a port. The app is configured to work with Railway's environment.

### 6. Add a Custom Domain (Optional)

1. In your Railway project, go to **Settings**
2. Under **Domains**, click **"Generate Domain"**
3. Railway will give you a URL like `your-app.railway.app`
4. You can also add a custom domain if you own one

### 7. Monitor Deployment

1. Click on **"Deployments"** to see the build logs
2. Wait for the deployment to complete (usually 2-5 minutes)
3. Once it says **"Success"**, click on the generated URL

## Using Your Deployed App

### Creating Properties

1. Visit your Railway URL (e.g., `https://your-app.railway.app/`)
2. Click **"+ Create New Property"**
3. You'll be redirected to a unique URL like `/property/abc-123-def-456`
4. Fill in the property information
5. All changes are auto-saved

### Linking in Your CRM

1. Copy the property URL (e.g., `https://your-app.railway.app/property/abc-123-def-456`)
2. Paste it into your CRM as a custom field or note
3. Each property has a permanent,unique URL you can share

### Managing Properties

- **Home page**: Lists all your properties with quick links
- **View/Edit**: Click any property to view or edit
- **Auto-save**: Changes save automatically as you type

## Database Persistence

The app uses SQLite to store data. On Railway:

- Data is stored in `properties.db` in your project
- **Important**: Railway's filesystem is ephemeral (resets on redeploy)
- For production, consider upgrading to use Railway's PostgreSQL addon

### Upgrading to PostgreSQL (Recommended for Production)

1. In Railway, click **"New"** → **"Database"** → **"PostgreSQL"**
2. Update `database.py` to use PostgreSQL instead of SQLite
3. Railway will automatically provide connection credentials via environment variables

## Troubleshooting

### Build Fails

- Check the build logs in Railway's **Deployments** tab
- Ensure all files are committed to Git
- Verify `requirements.txt` includes all dependencies

### App Won't Start

- Check that `start_railway.sh` has execute permissions
- Review the deployment logs for error messages
- Ensure Wave server downloaded correctly

### Data Not Saving

- Check that the app has write permissions
- For production, switch to PostgreSQL database
- Verify the database file exists in logs

## Local Testing Before Deployment

Test the deployment setup locally:

```bash
bash start_railway.sh
```

Visit `http://localhost:10101/` to verify everything works.

## Updating Your Deployed App

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

Railway will automatically detect the changes and redeploy.

## Cost Estimate

- **Railway Free Tier**: $5 credit per month (enough for small usage)
- **Hobby Plan**: $5/month for more resources
- Your app should fit comfortably in the free tier for moderate use

## Support

If you encounter issues:
1. Check Railway's deployment logs
2. Review the app logs in Railway dashboard
3. Verify all environment variables are set correctly

## Next Steps

- Add authentication if you want to restrict access
- Upgrade to PostgreSQL for persistent storage
- Add export functionality (CSV/PDF)
- Integrate with your CRM's API for two-way sync
