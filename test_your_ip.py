#!/usr/bin/env python3
"""
Test MongoDB Atlas Connection After Adding Your IP
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority"
DATABASE_NAME = "tourism_india"

async def test_connection():
    """Test Atlas connection after adding your IP"""
    print("🔧 Testing MongoDB Atlas Connection")
    print("=" * 50)
    print("📍 Your IP: 49.37.195.149")
    print("=" * 50)
    
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
        
        # Test write operation
        test_collection = db.test_connection
        result = await test_collection.insert_one({
            "test": "connection_successful", 
            "ip": "49.37.195.149",
            "timestamp": "now"
        })
        print(f"✍️ Write test successful! Document ID: {result.inserted_id}")
        
        # Clean up
        await test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        client.close()
        print("🔌 Connection closed successfully")
        
        print("\n🎉 READY TO START BACKEND!")
        print("Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n🔧 If still failing:")
        print("1. Make sure you added 49.37.195.149/32 to Atlas Network Access")
        print("2. Wait 5-10 minutes for changes to propagate")
        print("3. Check if your cluster is running (not paused)")
        print("4. Verify username/password are correct")
        return False

if __name__ == "__main__":
    print("🚀 Testing MongoDB Atlas with Your IP")
    print("Make sure you've added 49.37.195.149/32 to Atlas Network Access!")
    print("=" * 60)
    
    success = asyncio.run(test_connection())
    
    if success:
        print("\n🎉 CONNECTION SUCCESSFUL!")
        print("Your MongoDB Atlas is working correctly!")
        print("You can now start the backend server.")
    else:
        print("\n❌ CONNECTION STILL FAILING")
        print("Please check:")
        print("1. Network Access in Atlas dashboard")
        print("2. Cluster is running (not paused)")
        print("3. Username/password are correct")
        print("4. Wait a few more minutes for changes to take effect")
