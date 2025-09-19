#!/usr/bin/env python3
"""
Simple MongoDB Atlas Connection Test
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def test_simple_connection():
    """Test simple MongoDB Atlas connection"""
    print("🚀 Testing Simple MongoDB Atlas Connection")
    print("=" * 50)
    
    # Try different connection string formats
    connection_strings = [
        "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority",
        "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india",
        "mongodb://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net:27017/tourism_india"
    ]
    
    for i, url in enumerate(connection_strings, 1):
        print(f"\n📡 Test {i}: Trying connection string format {i}")
        print(f"URL: {url[:50]}...")
        
        try:
            client = AsyncIOMotorClient(url, serverSelectionTimeoutMS=5000)
            await client.admin.command('ping')
            print("✅ SUCCESS! This connection string works!")
            print(f"🎯 Use this URL in your database.py: {url}")
            
            # Test database operations
            db = client.tourism_india
            collections = await db.list_collection_names()
            print(f"📊 Collections found: {collections}")
            
            client.close()
            return url
            
        except Exception as e:
            print(f"❌ Failed: {str(e)[:100]}...")
            continue
    
    print("\n💥 All connection attempts failed!")
    return None

if __name__ == "__main__":
    working_url = asyncio.run(test_simple_connection())
    if working_url:
        print(f"\n🎉 SUCCESS! Working connection string found!")
    else:
        print(f"\n🔧 Next steps:")
        print("1. Check your Atlas cluster is running")
        print("2. Verify IP whitelist includes your current IP")
        print("3. Check username/password are correct")
        print("4. Try creating a new cluster if issues persist")
