#!/usr/bin/env python3
"""
Fix MongoDB Atlas with Your Specific IP Address
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# Your IP address
YOUR_IP = "49.37.195.149"

MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority"
DATABASE_NAME = "tourism_india"

async def test_connection_with_your_ip():
    """Test Atlas connection after adding your IP"""
    print("🔧 Testing MongoDB Atlas with Your IP Address")
    print("=" * 50)
    print(f"📍 Your IP: {YOUR_IP}")
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
        
        client.close()
        print("🔌 Connection closed successfully")
        
        print("\n🎉 READY TO START BACKEND!")
        print("Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def show_atlas_setup_instructions():
    """Show detailed Atlas setup instructions"""
    print("\n📋 STEP-BY-STEP ATLAS SETUP:")
    print("=" * 40)
    print("1. Go to: https://cloud.mongodb.com")
    print("2. Sign in to your account")
    print("3. Click on your cluster (Cluster0)")
    print("4. Click 'Network Access' in the left sidebar")
    print("5. Click 'Add IP Address'")
    print(f"6. Add your IP: {YOUR_IP}/32")
    print("7. Click 'Confirm'")
    print("8. Wait 2-3 minutes for changes to take effect")
    print("\n💡 Alternative: Add 0.0.0.0/0 for all IPs (less secure but works)")

if __name__ == "__main__":
    print("🚀 MongoDB Atlas Fix with Your IP Address")
    print("=" * 50)
    
    # Show setup instructions
    show_atlas_setup_instructions()
    
    print(f"\n🔄 Testing connection...")
    success = asyncio.run(test_connection_with_your_ip())
    
    if success:
        print("\n🎉 CONNECTION SUCCESSFUL!")
        print("Your Atlas setup is working correctly!")
    else:
        print("\n❌ CONNECTION FAILED")
        print("Please follow the setup instructions above to add your IP to Atlas Network Access")
        print(f"Your IP address: {YOUR_IP}/32")
        print("\nAfter adding your IP, wait 2-3 minutes and run this script again.")
