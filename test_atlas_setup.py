#!/usr/bin/env python3
"""
Test MongoDB Atlas Setup
"""
from pymongo import MongoClient
import sys

def test_atlas_setup():
    """Test MongoDB Atlas connection with user input"""
    
    print("🚀 MongoDB Atlas Connection Test")
    print("=" * 40)
    
    print("📋 Please provide your Atlas connection details:")
    print("(You can get these from MongoDB Atlas dashboard)")
    print()
    
    # Get connection details from user
    username = input("Database Username: ").strip()
    password = input("Database Password: ").strip()
    cluster_url = input("Cluster URL (e.g., cluster0.xxxxx.mongodb.net): ").strip()
    
    if not all([username, password, cluster_url]):
        print("❌ All fields are required!")
        return False
    
    # Build connection string
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority"
    
    print(f"\n🔗 Testing connection...")
    print(f"📍 Connection string: {connection_string[:50]}...")
    
    try:
        # Test connection
        client = MongoClient(connection_string, serverSelectionTimeoutMS=10000)
        
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
            "test": "atlas_setup",
            "status": "success",
            "app": "tourism_india",
            "timestamp": "2025-01-18"
        }
        result = test_collection.insert_one(test_doc)
        print(f"✅ Test document created with ID: {result.inserted_id}")
        
        # Clean up
        test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        client.close()
        print(f"\n🎉 SUCCESS! MongoDB Atlas is ready!")
        
        # Show the connection string for environment variable
        print(f"\n🎯 Use this connection string:")
        print(f"MONGO_URL={connection_string}")
        
        return connection_string
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print(f"\n🔧 Troubleshooting:")
        print(f"1. Check username/password")
        print(f"2. Verify cluster is running")
        print(f"3. Check IP whitelist (should include 0.0.0.0/0)")
        print(f"4. Verify cluster URL is correct")
        return False

def main():
    connection_string = test_atlas_setup()
    
    if connection_string:
        print(f"\n🎯 NEXT STEPS:")
        print(f"1. Set environment variable:")
        print(f"   set MONGO_URL={connection_string}")
        print(f"2. Start your backend:")
        print(f"   python -m uvicorn app.main:app --reload")
        print(f"3. Test your API:")
        print(f"   curl http://localhost:8000/health")

if __name__ == "__main__":
    main()
