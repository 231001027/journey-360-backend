#!/usr/bin/env python3
"""
Test MongoDB Atlas with Updated Drivers
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# Your Atlas connection string
MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "tourism_india"

async def test_updated_drivers():
    """Test with updated MongoDB drivers"""
    print("🚀 Testing MongoDB Atlas with Updated Drivers")
    print("=" * 50)
    
    try:
        # Try with the latest drivers
        print("📡 Testing connection with updated drivers...")
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=10000)
        
        # Test connection
        await client.admin.command('ping')
        print("✅ SUCCESS! Connection works with updated drivers!")
        
        # Test database operations
        db = client[DATABASE_NAME]
        collections = await db.list_collection_names()
        print(f"📊 Database: {DATABASE_NAME}")
        print(f"📋 Collections: {collections}")
        
        # Test write operation
        test_collection = db.test_connection
        result = await test_collection.insert_one({"test": "updated_drivers", "status": "success"})
        print(f"✍️ Write test successful! Document ID: {result.inserted_id}")
        
        # Clean up
        await test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        client.close()
        print("🔌 Connection closed")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_updated_drivers())
    
    if success:
        print("\n🎉 MongoDB Atlas connection is working!")
        print("🚀 You can now start the backend server:")
        print("   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
    else:
        print("\n💥 Connection still failing. Check:")
        print("1. MongoDB Atlas cluster is running")
        print("2. IP whitelist includes your IP (0.0.0.0/0 for all)")
        print("3. Username/password are correct")
        print("4. Try creating a new cluster")
