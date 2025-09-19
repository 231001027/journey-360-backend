#!/usr/bin/env python3
"""
Test MongoDB Connection
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def test_mongodb():
    """Test if MongoDB is running"""
    print("🔧 Testing MongoDB Connection")
    print("=" * 40)
    
    try:
        print("📡 Connecting to MongoDB on localhost:27017...")
        client = AsyncIOMotorClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
        
        # Test connection
        await client.admin.command('ping')
        print("✅ MongoDB is running and accessible!")
        
        # Test database operations
        db = client.tourism_india
        collections = await db.list_collection_names()
        print(f"📊 Database: tourism_india")
        print(f"📋 Collections: {collections}")
        
        client.close()
        print("🔌 Connection closed successfully")
        
        print("\n🎉 MongoDB is ready!")
        print("✅ You can now restart your backend to connect to MongoDB")
        
        return True
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        print("\n🔧 To fix this:")
        print("1. Make sure MongoDB service is running")
        print("2. Check if MongoDB is listening on port 27017")
        print("3. Try starting MongoDB manually")
        return False

if __name__ == "__main__":
    asyncio.run(test_mongodb())
