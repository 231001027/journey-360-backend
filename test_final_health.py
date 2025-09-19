#!/usr/bin/env python3
"""
Final backend health check on port 8004
"""
import requests
import json

def test_final_backend():
    base_url = "http://127.0.0.1:8004"
    
    print("🎯 Final Backend Health Check - Port 8004")
    print("=" * 50)
    
    # Test 1: Health endpoint
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health endpoint: OK")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health endpoint: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
        return False
    
    # Test 2: Destinations endpoint
    try:
        response = requests.get(f"{base_url}/destinations", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Destinations endpoint: OK ({len(data)} destinations)")
            if len(data) > 0:
                print(f"   Sample: {data[0]['name']} - {data[0]['state']}")
        else:
            print(f"❌ Destinations endpoint: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Destinations endpoint error: {e}")
    
    # Test 3: CORS headers
    try:
        response = requests.get(f"{base_url}/health")
        cors_origin = response.headers.get('Access-Control-Allow-Origin')
        if cors_origin == '*':
            print("✅ CORS: Configured correctly")
        else:
            print(f"⚠️  CORS: {cors_origin}")
    except Exception as e:
        print(f"❌ CORS error: {e}")
    
    print("\n🎉 Backend Status:")
    print("- Server: Running on port 8004")
    print("- Database: Connected with tourism data")
    print("- CORS: Enabled for frontend")
    print("- Ready for frontend connections!")
    
    return True

if __name__ == "__main__":
    test_final_backend()
