# MongoDB Atlas SSL Connection Issues on Windows

## 🔍 Problem Diagnosis
You're experiencing `SSL handshake failed: tlsv1 alert internal error` when connecting to MongoDB Atlas from Windows. This is a known compatibility issue.

## 🔧 Solutions (Try in Order)

### Solution 1: Fix Atlas Network Access (Most Common Fix)
1. Go to [MongoDB Atlas Dashboard](https://cloud.mongodb.com)
2. Click on your cluster → "Network Access"
3. Click "Add IP Address"
4. Add `0.0.0.0/0` (allows all IPs) or your specific IP
5. Save changes and wait 2-3 minutes

### Solution 2: Verify Cluster Status
1. In Atlas dashboard, check if your cluster is running
2. If it's paused, click "Resume"
3. Wait for cluster to be fully ready

### Solution 3: Create New Database User
1. In Atlas dashboard → "Database Access"
2. Click "Add New Database User"
3. Create user with "Read and write to any database" permissions
4. Update connection string with new credentials

### Solution 4: Use Different Connection String Format
Try these alternative connection strings:

```python
# Option 1: Without appName
MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority"

# Option 2: With different parameters
MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?ssl=true&retryWrites=true&w=majority"

# Option 3: Simple format
MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india"
```

### Solution 5: Use MongoDB Compass (Test Connection)
1. Download [MongoDB Compass](https://www.mongodb.com/products/compass)
2. Test your connection string in Compass first
3. If Compass works, the issue is with Python drivers
4. If Compass fails, the issue is with Atlas configuration

## 🚀 Quick Development Solution

If Atlas continues to fail, use local MongoDB for development:

```bash
# Install MongoDB Community Edition
# Download from: https://www.mongodb.com/try/download/community

# Or use Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest

# Update database.py to use local connection
MONGO_URL = "mongodb://localhost:27017"
```

## 📋 Next Steps
1. Try Solution 1 (Network Access) first - this fixes 90% of cases
2. If still failing, try Solution 5 (MongoDB Compass) to isolate the issue
3. For immediate development, use local MongoDB (Solution 5)
4. Once working, you can switch back to Atlas for production

## 🔍 Additional Debugging
- Check Windows Firewall settings
- Try from a different network (mobile hotspot)
- Verify your internet connection can reach MongoDB Atlas
- Check if your organization blocks certain ports/protocols
