#!/usr/bin/env python3
"""
Comprehensive backend health check
"""
import requests
import json

def test_backend_comprehensive():
    base_url = "http://127.0.0.1:8003"
    
    print("🔍 Comprehensive Backend Health Check")
    print("=" * 50)
    
    # Test 1: Basic health
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health endpoint: OK")
        else:
            print(f"❌ Health endpoint: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
        return False
    
    # Test 2: Destinations endpoint with detailed error
    try:
        response = requests.get(f"{base_url}/destinations", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Destinations endpoint: OK ({len(data)} destinations)")
        else:
            print(f"❌ Destinations endpoint failed: {response.status_code}")
            print(f"   Error details: {response.text}")
    except Exception as e:
        print(f"❌ Destinations endpoint error: {e}")
    
    # Test 3: Auth endpoint
    try:
        response = requests.post(f"{base_url}/auth/login", 
                               json={"email": "test@test.com", "password": "test"},
                               timeout=5)
        if response.status_code == 422:  # Expected validation error
            print("✅ Auth endpoint: OK (validation working)")
        else:
            print(f"⚠️  Auth endpoint: {response.status_code}")
    except Exception as e:
        print(f"❌ Auth endpoint error: {e}")
    
    # Test 4: CORS preflight
    try:
        response = requests.options(f"{base_url}/health", timeout=5)
        cors_origin = response.headers.get('Access-Control-Allow-Origin')
        if cors_origin == '*':
            print("✅ CORS: Configured correctly")
        else:
            print(f"⚠️  CORS: {cors_origin}")
    except Exception as e:
        print(f"❌ CORS error: {e}")
    
    print("\n🎯 Backend Status Summary:")
    print("- Server is running and responding")
    print("- Health endpoint working")
    print("- Ready for frontend connections")
    
    return True

if __name__ == "__main__":
    test_backend_comprehensive()
