#!/usr/bin/env python3
"""
Test MongoDB Atlas Connection
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Atlas connection string
MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "tourism_india"

async def test_connection():
    """Test MongoDB Atlas connection"""
    print("🚀 Testing MongoDB Atlas Connection")
    print("=" * 40)
    
    try:
        # Create client
        client = AsyncIOMotorClient(MONGO_URL)
        database = client[DATABASE_NAME]
        
        # Test connection
        print("📡 Testing connection...")
        await client.admin.command('ping')
        print("✅ Connection successful!")
        
        # Test database access
        print("📊 Testing database access...")
        collections = await database.list_collection_names()
        print(f"✅ Database '{DATABASE_NAME}' accessible!")
        print(f"📋 Collections: {collections}")
        
        # Test write operation
        print("✍️ Testing write operation...")
        test_collection = database.test_connection
        result = await test_collection.insert_one({"test": "connection", "timestamp": "now"})
        print(f"✅ Write operation successful! Document ID: {result.inserted_id}")
        
        # Clean up test document
        await test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        # Close connection
        client.close()
        print("🔌 Connection closed")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_connection())
    if success:
        print("\n🎉 MongoDB Atlas connection test PASSED!")
    else:
        print("\n💥 MongoDB Atlas connection test FAILED!")
