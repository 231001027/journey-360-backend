# 🚂 Railway CLI Deployment (Alternative Method)

Since the web dashboard is having Railpack issues, let's use Railway CLI instead.

## Step-by-Step CLI Deployment:

### 1. Install Railway CLI
```bash
npm install -g @railway/cli
```

### 2. Login to Railway
```bash
railway login
```

### 3. Initialize Project
```bash
railway init
```
- Select "Empty Project"
- Name it "journey-360-backend"

### 4. Add MongoDB Database
```bash
railway add mongodb
```

### 5. Deploy Your Code
```bash
railway up
```

### 6. Get Your URL
```bash
railway domain
```

## Alternative: Try Different Railway Settings

If CLI doesn't work, try these settings in Railway web dashboard:

1. **Go to your Railway project settings**
2. **Change build settings:**
   - **Build Command:** `echo "Using Dockerfile"`
   - **Start Command:** `python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`

3. **Environment Variables:**
   - Add `PYTHON_VERSION=3.10`
   - Add `PORT=8000`

## Troubleshooting:

If still failing, try:
1. **Delete the current Railway project**
2. **Create a new one**
3. **Use different settings**

The issue might be with the project configuration itself.
