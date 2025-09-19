#!/usr/bin/env python3
"""
Test Local MongoDB Connection
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "tourism_india"

async def test_local_mongodb():
    """Test local MongoDB connection"""
    print("🔧 Testing Local MongoDB Connection")
    print("=" * 40)
    
    try:
        print("📡 Connecting to local MongoDB...")
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
        
        # Test connection
        await client.admin.command('ping')
        print("✅ SUCCESS! Connected to local MongoDB!")
        
        # Test database operations
        db = client[DATABASE_NAME]
        collections = await db.list_collection_names()
        print(f"📊 Database: {DATABASE_NAME}")
        print(f"📋 Collections: {collections}")
        
        # Test write operation
        test_collection = db.test_connection
        result = await test_collection.insert_one({
            "test": "local_connection_successful", 
            "environment": "development",
            "timestamp": "now"
        })
        print(f"✍️ Write test successful! Document ID: {result.inserted_id}")
        
        # Clean up
        await test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        client.close()
        print("🔌 Connection closed successfully")
        
        print("\n🎉 READY TO START BACKEND!")
        print("Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n🔧 To fix this:")
        print("1. Install MongoDB: https://www.mongodb.com/try/download/community")
        print("2. Or use Docker: docker run -d -p 27017:27017 --name mongodb mongo:latest")
        print("3. Make sure MongoDB service is running")
        return False

if __name__ == "__main__":
    print("🚀 Testing Local MongoDB for Development")
    print("=" * 50)
    
    success = asyncio.run(test_local_mongodb())
    
    if success:
        print("\n🎉 LOCAL MONGODB IS WORKING!")
        print("You can now start your backend server.")
    else:
        print("\n❌ LOCAL MONGODB NOT AVAILABLE")
        print("Please install and start MongoDB first.")
