# 🚀 GitHub + Railway Deployment Guide

## ✅ Step 1: Git Repository Ready!

Your backend code is now committed to Git and ready for GitHub!

**Files committed:** 33 files, 2210 lines of code
**Commit message:** "Journey 360 Backend - Ready for Railway deployment"

## 📋 Next Steps:

### Step 2: Create GitHub Repository

1. **Go to GitHub.com**
   - Visit: https://github.com
   - Sign up/Login to your account

2. **Create New Repository**
   - Click "New repository" (green button)
   - Repository name: `journey-360-backend`
   - Description: `Journey 360 Tourism App Backend`
   - Make it **Public** (for easier Railway deployment)
   - Don't initialize with README (we already have files)
   - Click "Create repository"

3. **Get Repository URL**
   - Copy the repository URL (e.g., `https://github.com/yourusername/journey-360-backend.git`)

### Step 3: Push to GitHub

Run these commands in your backend directory:

```bash
# Add remote repository (replace with your actual GitHub URL)
git remote add origin https://github.com/yourusername/journey-360-backend.git

# Push to GitHub
git push -u origin master
```

### Step 4: Deploy to Railway

1. **Go to Railway.app**
   - Visit: https://railway.app
   - Sign up/Login with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your GitHub

3. **Select Repository**
   - Choose your `journey-360-backend` repository
   - Railway will detect it's a Python project

4. **Configure Deployment**
   - **Root Directory:** Leave empty (or set to `/` if needed)
   - **Build Command:** Railway will auto-detect Dockerfile
   - **Start Command:** Railway will use the Dockerfile CMD

5. **Add MongoDB Database**
   - In Railway dashboard, click "+ New"
   - Select "Database" → "MongoDB"
   - Railway will automatically provide `MONGO_URL` environment variable

6. **Deploy**
   - Click "Deploy"
   - Wait for build to complete (usually 2-5 minutes)

### Step 5: Get Your Railway URL

After successful deployment:
- Railway will provide a URL like: `https://journey-360-backend-production.up.railway.app`
- Copy this URL for your frontend

### Step 6: Update Frontend

Update your frontend API configuration:

```typescript
// In project/src/lib/api.ts
export function getApiBaseUrl(): string {
  // Replace with your actual Railway URL
  return 'https://journey-360-backend-production.up.railway.app';
}
```

### Step 7: Test Your Deployment

1. **Test Health Endpoint**
   - Visit: `https://your-railway-url.up.railway.app/health`
   - Should return: `{"status":"ok"}`

2. **Test Destinations**
   - Visit: `https://your-railway-url.up.railway.app/destinations`
   - Should return tourism destinations data

3. **Test from Mobile App**
   - Update frontend API URL
   - Test login functionality

## 🎉 Expected Results

After successful deployment:
- ✅ Backend running on Railway
- ✅ MongoDB database connected
- ✅ Global HTTPS URL
- ✅ No local runtime issues
- ✅ Mobile app can connect
- ✅ Tourism data available

## 🆘 Troubleshooting

**If deployment fails:**
1. Check Railway logs in dashboard
2. Verify Dockerfile is correct
3. Ensure all dependencies in requirements.txt
4. Check environment variables

**If database connection fails:**
1. Verify MongoDB is added to Railway project
2. Check MONGO_URL environment variable
3. Ensure database is running

## 📞 Support

- Railway Docs: https://docs.railway.app
- GitHub Docs: https://docs.github.com
- Your backend is ready - just follow these steps!
