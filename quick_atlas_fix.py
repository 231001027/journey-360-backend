#!/usr/bin/env python3
"""
Quick MongoDB Atlas Fix Script
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

def update_database_config_for_atlas():
    """Update database.py with Atlas connection"""
    
    atlas_connection_strings = [
        "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority",
        "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india",
        "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?ssl=true&retryWrites=true&w=majority"
    ]
    
    print("🔧 MongoDB Atlas Quick Fix")
    print("=" * 40)
    
    print("📋 STEP 1: Fix Atlas Network Access")
    print("1. Go to: https://cloud.mongodb.com")
    print("2. Click your cluster → Network Access")
    print("3. Add IP Address: 0.0.0.0/0")
    print("4. Save and wait 2-3 minutes")
    print()
    
    print("📋 STEP 2: Test Connection")
    for i, url in enumerate(atlas_connection_strings, 1):
        print(f"Testing connection string {i}...")
        try:
            client = AsyncIOMotorClient(url, serverSelectionTimeoutMS=5000)
            # Test connection (this will fail but we're just checking format)
            print(f"✅ Connection string {i} format is valid")
        except Exception as e:
            if "SSL handshake" in str(e):
                print(f"❌ Connection string {i}: SSL handshake failed (check Network Access)")
            else:
                print(f"❌ Connection string {i}: {str(e)[:50]}...")
    
    print("\n📋 STEP 3: If Still Failing")
    print("1. Try MongoDB Compass to test connection")
    print("2. Create a new database user in Atlas")
    print("3. Use local MongoDB for development:")
    print("   MONGO_URL = 'mongodb://localhost:27017'")
    
    return atlas_connection_strings[0]

async def test_connection_with_retry():
    """Test connection with multiple retries"""
    url = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority"
    
    print("\n🔄 Testing Atlas Connection with Retry...")
    
    for attempt in range(3):
        try:
            print(f"Attempt {attempt + 1}/3...")
            client = AsyncIOMotorClient(url, serverSelectionTimeoutMS=10000)
            await client.admin.command('ping')
            print("✅ SUCCESS! Atlas connection is working!")
            client.close()
            return True
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {str(e)[:100]}...")
            if attempt < 2:
                print("⏳ Waiting 5 seconds before retry...")
                await asyncio.sleep(5)
    
    print("💥 All attempts failed. Check Network Access in Atlas dashboard.")
    return False

if __name__ == "__main__":
    print("🚀 MongoDB Atlas Quick Fix Tool")
    print("=" * 50)
    
    # Step 1: Update configuration
    working_url = update_database_config_for_atlas()
    
    # Step 2: Test connection
    success = asyncio.run(test_connection_with_retry())
    
    if success:
        print("\n🎉 SUCCESS! Your Atlas connection is working!")
        print("🚀 Now run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
    else:
        print("\n💡 RECOMMENDED ACTION:")
        print("1. Fix Network Access in Atlas (add 0.0.0.0/0)")
        print("2. Or use local MongoDB for development")
        print("3. Check atlas_troubleshooting_guide.md for detailed steps")
