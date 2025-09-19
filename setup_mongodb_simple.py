#!/usr/bin/env python3
"""
Simple MongoDB Setup Guide
"""
import os

def show_mongodb_setup():
    """Show MongoDB setup options"""
    print("🔧 MongoDB Setup Options")
    print("=" * 50)
    
    print("\n📋 Option 1: Install MongoDB Community Edition (Recommended)")
    print("1. Go to: https://www.mongodb.com/try/download/community")
    print("2. Download MongoDB Community Server")
    print("3. Install with default settings")
    print("4. Start MongoDB service")
    print("5. Restart your backend")
    
    print("\n📋 Option 2: Use Docker (if available)")
    print("1. Install Docker Desktop")
    print("2. Run: docker run -d -p 27017:27017 --name mongodb mongo:latest")
    print("3. Restart your backend")
    
    print("\n📋 Option 3: Continue with Mock Data")
    print("Your backend is already working with mock data!")
    print("You can develop and test without MongoDB for now.")
    
    print("\n🎯 Current Status:")
    print("✅ Backend running on http://127.0.0.1:8001")
    print("✅ API endpoints working")
    print("⚠️  Using mock data (no database)")
    
    print("\n🚀 Quick Test:")
    print("Visit: http://127.0.0.1:8001/docs")
    print("This shows your API documentation!")

if __name__ == "__main__":
    show_mongodb_setup()
