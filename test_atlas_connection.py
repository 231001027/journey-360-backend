#!/usr/bin/env python3
"""
Test MongoDB Atlas Connection
"""
from pymongo import MongoClient
import os

def test_atlas_connection():
    """Test MongoDB Atlas connection"""
    
    print("🚀 Testing MongoDB Atlas Connection")
    print("=" * 40)
    
    # Get connection string from environment or user input
    mongo_url = os.getenv("MONGO_URL")
    
    if not mongo_url:
        print("❌ MONGO_URL not set")
        print("\n📋 To set it:")
        print("1. Get your Atlas connection string from MongoDB Atlas dashboard")
        print("2. Set environment variable:")
        print("   set MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/")
        print("\nOr enter it now:")
        mongo_url = input("Enter your Atlas connection string: ").strip()
    
    if not mongo_url:
        print("❌ No connection string provided")
        return False
    
    print(f"🔗 Testing connection...")
    print(f"📍 URL: {mongo_url[:50]}...")
    
    try:
        # Test connection
        client = MongoClient(mongo_url, serverSelectionTimeoutMS=10000)
        
        # Ping the database
        client.admin.command('ping')
        print("✅ Connection successful!")
        
        # Test database access
        db = client["tourism_india"]
        collections = db.list_collection_names()
        print(f"📊 Database 'tourism_india' accessible")
        print(f"📁 Collections: {collections}")
        
        # Test creating a document
        test_collection = db["connection_test"]
        test_doc = {
            "test": "atlas_connection",
            "status": "success",
            "timestamp": "2025-01-18"
        }
        result = test_collection.insert_one(test_doc)
        print(f"✅ Test document created with ID: {result.inserted_id}")
        
        # Clean up
        test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        client.close()
        print(f"\n🎉 SUCCESS! MongoDB Atlas connected!")
        print(f"✅ Use this connection string: {mongo_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print(f"\n🔧 Troubleshooting:")
        print(f"1. Check if connection string is correct")
        print(f"2. Verify cluster is running in Atlas")
        print(f"3. Check IP whitelist (0.0.0.0/0 for all IPs)")
        print(f"4. Verify username/password")
        return False

def main():
    success = test_atlas_connection()
    
    if success:
        print(f"\n🎯 NEXT STEPS:")
        print(f"1. Set environment variable:")
        print(f"   set MONGO_URL=your_atlas_connection_string")
        print(f"2. Start your backend:")
        print(f"   python -m uvicorn app.main:app --reload")
        print(f"3. Test your API:")
        print(f"   curl http://localhost:8000/health")

if __name__ == "__main__":
    main()
