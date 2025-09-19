# 🐳 Docker Deployment to Railway

## Quick Deployment Steps

### Method 1: Railway Web Dashboard (Recommended)

1. **Go to Railway.app**
   - Visit: https://railway.app
   - Sign up/Login with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"

3. **Connect Your Repository**
   - Connect your GitHub account
   - Select your repository
   - Choose the `project/backend` folder

4. **Add MongoDB Database**
   - In Railway dashboard, click "+ New"
   - Select "Database" → "MongoDB"
   - Railway will automatically provide `MONGO_URL`

5. **Deploy**
   - Railway will automatically detect Dockerfile
   - Click "Deploy" and wait for build

### Method 2: Railway CLI (Alternative)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Add MongoDB
railway add mongodb

# Deploy with Docker
railway up
```

## Environment Variables

Railway automatically provides:
- `MONGO_URL` - MongoDB connection string
- `PORT` - Server port (Railway sets this)

## Your Backend Structure

```
project/backend/
├── Dockerfile          # Docker configuration
├── railway.toml        # Railway configuration
├── requirements.txt    # Python dependencies
├── app/
│   ├── main.py        # FastAPI app
│   ├── database.py    # MongoDB connection
│   ├── models.py      # Data models
│   └── routers/       # API endpoints
└── ...
```

## After Deployment

1. **Get Railway URL**
   - Check Railway dashboard
   - Copy the HTTPS URL (e.g., `https://your-app-name.up.railway.app`)

2. **Update Frontend**
   - Update `project/src/lib/api.ts`
   - Replace localhost URLs with Railway URL

3. **Test Connection**
   - Visit `https://your-app-name.up.railway.app/health`
   - Should return `{"status":"ok"}`

## Benefits of Docker Deployment

✅ **Consistent Environment**
- Same environment everywhere
- No local setup issues
- Works on any platform

✅ **Easy Scaling**
- Railway handles scaling
- Automatic load balancing
- High availability

✅ **Zero Configuration**
- Docker handles dependencies
- Railway handles hosting
- MongoDB included

## Cost
- **Free tier**: $5 credit monthly
- **Perfect for development**
- **No credit card required**
