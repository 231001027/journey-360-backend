#!/usr/bin/env python3
"""
Start MongoDB using Docker (Quick Setup)
"""
import subprocess
import sys
import time
import os

def start_mongodb_docker():
    """Start MongoDB using Docker"""
    print("🚀 Starting MongoDB with Docker")
    print("=" * 40)
    
    try:
        # Check if Docker is available
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Docker is not installed or not running")
            print("📋 Alternative: Install MongoDB Community Edition")
            print("   Download from: https://www.mongodb.com/try/download/community")
            return False
        
        print("✅ Docker is available")
        
        # Check if MongoDB container already exists
        result = subprocess.run(['docker', 'ps', '-a', '--filter', 'name=mongodb'], capture_output=True, text=True)
        
        if 'mongodb' in result.stdout:
            print("🔄 MongoDB container exists, starting it...")
            subprocess.run(['docker', 'start', 'mongodb'])
        else:
            print("🆕 Creating new MongoDB container...")
            subprocess.run([
                'docker', 'run', '-d', 
                '--name', 'mongodb',
                '-p', '27017:27017',
                'mongo:latest'
            ])
        
        print("⏳ Waiting for MongoDB to start...")
        time.sleep(5)
        
        print("✅ MongoDB should now be running on localhost:27017")
        print("🔄 Restart your backend server to connect to MongoDB")
        
        return True
        
    except Exception as e:
        print(f"❌ Error starting MongoDB: {e}")
        return False

def test_mongodb_connection():
    """Test MongoDB connection"""
    print("\n🔧 Testing MongoDB Connection")
    print("=" * 30)
    
    try:
        from motor.motor_asyncio import AsyncIOMotorClient
        import asyncio
        
        async def test():
            client = AsyncIOMotorClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
            await client.admin.command('ping')
            print("✅ MongoDB connection successful!")
            client.close()
            return True
        
        return asyncio.run(test())
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    print("🔧 MongoDB Setup for Tourism App")
    print("=" * 50)
    
    success = start_mongodb_docker()
    
    if success:
        print("\n📋 Next Steps:")
        print("1. Stop your current backend (Ctrl+C)")
        print("2. Update database.py to connect to MongoDB")
        print("3. Restart backend: python -m uvicorn app.main:app --host 127.0.0.1 --port 8001")
        print("4. Test connection")
    else:
        print("\n💡 Alternative Setup:")
        print("1. Install MongoDB Community Edition")
        print("2. Start MongoDB service")
        print("3. Restart backend")
