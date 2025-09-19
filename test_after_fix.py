#!/usr/bin/env python3
"""
Test MongoDB Atlas Connection After Network Access Fix
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority"
DATABASE_NAME = "tourism_india"

async def test_connection():
    """Test Atlas connection after Network Access fix"""
    print("🔧 Testing MongoDB Atlas After Network Access Fix")
    print("=" * 60)
    
    try:
        print("📡 Connecting to Atlas...")
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=10000)
        
        # Test connection
        await client.admin.command('ping')
        print("✅ SUCCESS! Connected to MongoDB Atlas!")
        
        # Test database operations
        db = client[DATABASE_NAME]
        collections = await db.list_collection_names()
        print(f"📊 Database: {DATABASE_NAME}")
        print(f"📋 Collections: {collections}")
        
        client.close()
        print("🔌 Connection closed successfully")
        
        print("\n🎉 READY TO START BACKEND!")
        print("Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n🔧 If still failing:")
        print("1. Double-check Network Access in Atlas (0.0.0.0/0)")
        print("2. Wait 5-10 minutes for changes to propagate")
        print("3. Try creating a new database user")
        print("4. Use local MongoDB for development")
        return False

if __name__ == "__main__":
    asyncio.run(test_connection())
