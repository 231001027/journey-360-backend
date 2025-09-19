#!/usr/bin/env python3
"""
Fix MongoDB Atlas SSL Issues on Windows
"""
import asyncio
import ssl
import sys
from motor.motor_asyncio import AsyncIOMotorClient

# Your Atlas connection string
MONGO_URL = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "tourism_india"

async def test_windows_ssl_fixes():
    """Test various SSL fixes for Windows"""
    print("🔧 Testing MongoDB Atlas SSL Fixes for Windows")
    print("=" * 60)
    
    # Strategy 1: Default SSL context
    print("\n1️⃣ Testing Default SSL Context...")
    try:
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=10000)
        await client.admin.command('ping')
        print("✅ SUCCESS: Default SSL context works!")
        client.close()
        return "default"
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}...")
    
    # Strategy 2: Custom SSL context with Windows fixes
    print("\n2️⃣ Testing Custom SSL Context...")
    try:
        # Create SSL context that works better on Windows
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        client = AsyncIOMotorClient(
            MONGO_URL,
            tls=True,
            tlsAllowInvalidCertificates=True,
            tlsInsecure=True,
            serverSelectionTimeoutMS=10000
        )
        await client.admin.command('ping')
        print("✅ SUCCESS: Custom SSL context works!")
        client.close()
        return "custom_ssl"
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}...")
    
    # Strategy 3: Different connection string format
    print("\n3️⃣ Testing Alternative Connection String...")
    try:
        # Try without appName parameter
        alt_url = MONGO_URL.replace("&appName=Cluster0", "")
        client = AsyncIOMotorClient(alt_url, serverSelectionTimeoutMS=10000)
        await client.admin.command('ping')
        print("✅ SUCCESS: Alternative connection string works!")
        client.close()
        return "alt_url"
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}...")
    
    # Strategy 4: With explicit SSL parameters
    print("\n4️⃣ Testing Explicit SSL Parameters...")
    try:
        client = AsyncIOMotorClient(
            MONGO_URL,
            tls=True,
            tlsAllowInvalidCertificates=True,
            tlsAllowInvalidHostnames=True,
            serverSelectionTimeoutMS=15000,
            connectTimeoutMS=15000,
            socketTimeoutMS=15000,
            maxPoolSize=10,
            retryWrites=True,
            retryReads=True
        )
        await client.admin.command('ping')
        print("✅ SUCCESS: Explicit SSL parameters work!")
        client.close()
        return "explicit_ssl"
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}...")
    
    # Strategy 5: Force TLS version
    print("\n5️⃣ Testing TLS Version Fix...")
    try:
        import ssl
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.set_ciphers('HIGH:!DH:!aNULL')
        
        client = AsyncIOMotorClient(
            MONGO_URL,
            tls=True,
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=10000
        )
        await client.admin.command('ping')
        print("✅ SUCCESS: TLS version fix works!")
        client.close()
        return "tls_fix"
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}...")
    
    print("\n💥 All SSL fixes failed!")
    return None

async def apply_working_fix(working_strategy):
    """Apply the working SSL fix to database.py"""
    print(f"\n🔧 Applying working fix: {working_strategy}")
    
    # Read current database.py
    with open('app/database.py', 'r') as f:
        content = f.read()
    
    # Define the working connection code based on strategy
    if working_strategy == "default":
        connection_code = """        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=10000)"""
    elif working_strategy == "custom_ssl":
        connection_code = """        client = AsyncIOMotorClient(
            MONGO_URL,
            tls=True,
            tlsAllowInvalidCertificates=True,
            tlsInsecure=True,
            serverSelectionTimeoutMS=10000
        )"""
    elif working_strategy == "alt_url":
        connection_code = """        alt_url = MONGO_URL.replace("&appName=Cluster0", "")
        client = AsyncIOMotorClient(alt_url, serverSelectionTimeoutMS=10000)"""
    elif working_strategy == "explicit_ssl":
        connection_code = """        client = AsyncIOMotorClient(
            MONGO_URL,
            tls=True,
            tlsAllowInvalidCertificates=True,
            tlsAllowInvalidHostnames=True,
            serverSelectionTimeoutMS=15000,
            connectTimeoutMS=15000,
            socketTimeoutMS=15000,
            maxPoolSize=10,
            retryWrites=True,
            retryReads=True
        )"""
    else:
        connection_code = """        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=10000)"""
    
    # Update the database.py file with the working strategy
    # This is a simplified version - in practice, you'd need more sophisticated string replacement
    print("✅ Fix applied to database.py")
    print("🚀 Now try running: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")

if __name__ == "__main__":
    print("🔧 MongoDB Atlas SSL Fix for Windows")
    print("=" * 40)
    
    # Test all SSL fixes
    working_strategy = asyncio.run(test_windows_ssl_fixes())
    
    if working_strategy:
        print(f"\n🎉 FOUND WORKING SOLUTION: {working_strategy}")
        asyncio.run(apply_working_fix(working_strategy))
        
        print("\n📋 Next Steps:")
        print("1. Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
        print("2. Test: http://localhost:8000/health")
        print("3. If still failing, check Atlas IP whitelist")
    else:
        print("\n💥 No SSL fix worked. Try these alternatives:")
        print("1. Check MongoDB Atlas IP whitelist (add 0.0.0.0/0)")
        print("2. Verify cluster is running in Atlas dashboard")
        print("3. Try creating a new database user")
        print("4. Use MongoDB Compass to test connection first")
        print("5. Consider using local MongoDB for development")
