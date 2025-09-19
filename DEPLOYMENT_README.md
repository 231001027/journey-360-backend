# Journey 360 Backend - Railway Deployment

## Quick Deploy to Railway

### 🚀 One-Click Deployment

1. **Push this code to GitHub**
2. **Go to [Railway.app](https://railway.app)**
3. **Click "New Project" → "Deploy from GitHub repo"**
4. **Select your repository and `project/backend` folder**
5. **Add MongoDB database**
6. **Deploy!**

### 📁 Project Structure

```
backend/
├── app/
│   ├── main.py           # FastAPI application
│   ├── database.py       # MongoDB connection
│   ├── models.py         # Data models
│   ├── auth.py          # Authentication
│   ├── seed_data.py     # Sample data
│   └── routers/         # API endpoints
│       ├── health.py
│       ├── auth.py
│       ├── destinations.py
│       ├── itineraries.py
│       ├── marketplace.py
│       └── assistant.py
├── Dockerfile           # Docker configuration
├── railway.toml        # Railway settings
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### 🔧 Environment Variables

Railway automatically provides:
- `MONGO_URL` - MongoDB connection string
- `PORT` - Server port

### 🌐 API Endpoints

After deployment, your API will be available at:
- `https://your-app-name.up.railway.app/health`
- `https://your-app-name.up.railway.app/destinations`
- `https://your-app-name.up.railway.app/auth/login`
- And more...

### 📱 Frontend Integration

Update your frontend API configuration to use the Railway URL:

```typescript
// In project/src/lib/api.ts
export function getApiBaseUrl(): string {
  return 'https://your-app-name.up.railway.app';
}
```

### 💰 Cost
- **Free tier**: $5 credit monthly
- **Perfect for development and small apps**
- **No credit card required**

### 🆘 Support
If you encounter any issues:
1. Check Railway logs in the dashboard
2. Verify environment variables
3. Ensure MongoDB is connected
4. Check the health endpoint

---
**Built with ❤️ for Tourism India**
