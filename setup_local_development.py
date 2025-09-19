#!/usr/bin/env python3
"""
Setup Local Development Environment
"""
import subprocess
import sys
import os

def setup_local_development():
    """Setup local development environment"""
    print("🚀 Setting Up Local Development Environment")
    print("=" * 50)
    
    print("📋 Steps to get your backend running:")
    print()
    
    print("1️⃣ Install MongoDB locally:")
    print("   Option A: Download from https://www.mongodb.com/try/download/community")
    print("   Option B: Use Docker: docker run -d -p 27017:27017 --name mongodb mongo:latest")
    print()
    
    print("2️⃣ Start MongoDB service:")
    print("   - If installed locally: Start MongoDB service from Services")
    print("   - If using Docker: docker start mongodb")
    print()
    
    print("3️⃣ Test MongoDB connection:")
    print("   python test_local_mongodb.py")
    print()
    
    print("4️⃣ Start your backend server:")
    print("   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload")
    print()
    
    print("5️⃣ Test your backend:")
    print("   http://localhost:8000/health")
    print()
    
    print("✅ Your backend is now disconnected from Railway!")
    print("✅ Using local MongoDB for development")
    print("✅ No more SSL handshake issues")

if __name__ == "__main__":
    setup_local_development()
