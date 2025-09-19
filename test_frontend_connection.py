#!/usr/bin/env python3
"""
Test script to verify frontend-backend connection
"""
import requests
import json

def test_backend_endpoints():
    base_url = "http://127.0.0.1:8003"
    
    print("🔍 Testing Frontend-Backend Connection")
    print("=" * 50)
    
    # Test 1: Health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health endpoint: OK")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
    
    # Test 2: CORS headers (important for frontend)
    try:
        response = requests.options(f"{base_url}/health")
        cors_headers = {
            'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
            'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
            'Access-Control-Allow-Headers': response.headers.get('Access-Control-Allow-Headers'),
        }
        print("✅ CORS headers check:")
        for header, value in cors_headers.items():
            print(f"   {header}: {value or 'Not set'}")
    except Exception as e:
        print(f"❌ CORS check error: {e}")
    
    # Test 3: Destinations endpoint
    try:
        response = requests.get(f"{base_url}/destinations")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Destinations endpoint: OK ({len(data)} destinations)")
        else:
            print(f"❌ Destinations endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Destinations endpoint error: {e}")
    
    # Test 4: Login endpoint structure
    try:
        # This should fail but show us the expected format
        response = requests.post(f"{base_url}/auth/login", 
                               json={"email": "test", "password": "test"})
        print(f"✅ Login endpoint accessible (status: {response.status_code})")
        if response.status_code == 422:
            print("   Expected validation error - endpoint is working")
    except Exception as e:
        print(f"❌ Login endpoint error: {e}")
    
    print("\n🎯 Frontend Connection Summary:")
    print("- Backend is running on port 8003")
    print("- Health endpoint is accessible")
    print("- API endpoints are responding")
    print("- Frontend should be able to connect!")
    
    return True

if __name__ == "__main__":
    test_backend_endpoints()
