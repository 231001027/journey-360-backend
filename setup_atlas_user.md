# MongoDB Atlas User Setup Guide

## Quick Setup Steps:

### 1. Go to MongoDB Atlas
- Visit: https://cloud.mongodb.com
- Sign in to your account

### 2. Create New Database User
- Click "Database Access" in left sidebar
- Click "Add New Database User"
- **Username:** `journey360_user`
- **Password:** `journey360_pass123`
- **Privileges:** "Read and write to any database"
- Click "Add User"

### 3. Update Network Access
- Click "Network Access" in left sidebar
- Click "Add IP Address"
- Select "Allow access from anywhere" (0.0.0.0/0)
- Click "Confirm"

### 4. Get Connection String
- Click "Database" in left sidebar
- Click "Connect" on your cluster
- Choose "Connect your application"
- Copy the connection string
- Replace `<password>` with your actual password

### 5. Update Backend Configuration
Replace in `app/database.py`:
```python
MONGO_URL = "mongodb+srv://journey360_user:journey360_pass123@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0"
```

### 6. Test Connection
Run: `python test_atlas_connection.py`

### 7. Add to Railway
Add to Railway environment variables:
```
MONGO_URL=mongodb+srv://journey360_user:journey360_pass123@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0
```
