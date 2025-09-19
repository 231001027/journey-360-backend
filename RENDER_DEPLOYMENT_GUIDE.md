# 🚀 Render Deployment Guide - Journey 360 Backend

## Why Render?
- ✅ More reliable than Railway
- ✅ Better Python support
- ✅ Free tier available
- ✅ Easy MongoDB integration
- ✅ Automatic deployments from GitHub

## Step-by-Step Deployment

### 1. Go to Render Dashboard
- Visit: https://render.com
- Sign up with your GitHub account
- Connect your repository: `231001027/journey-360-backend`

### 2. Create Web Service
- Click "New +" → "Web Service"
- Connect GitHub repository
- Select: `231001027/journey-360-backend`

### 3. Configure Service
- **Name:** `journey-360-backend`
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **Plan:** Free (or Hobby for $7/month)

### 4. Add MongoDB Database
- Click "New +" → "PostgreSQL" (or MongoDB if available)
- Name: `journey-360-db`
- Connect to your web service

### 5. Set Environment Variables
- Go to your web service settings
- Add these environment variables:
  ```
  MONGO_URL=mongodb://localhost:27017
  NODE_ENV=production
  PORT=10000
  ```

### 6. Deploy!
- Click "Create Web Service"
- Wait for deployment (2-3 minutes)
- Get your public URL

## Expected Results:
- ✅ Backend running on Render
- ✅ Public URL generated
- ✅ MongoDB connected
- ✅ Frontend can connect

## Timeline: 5-10 minutes total!

## Next Steps:
1. Get your Render URL
2. Update frontend `api.ts` with Render URL
3. Test frontend-backend connection
4. Your app is live! 🎉
