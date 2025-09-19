#!/usr/bin/env python3
"""
Setup Local MongoDB for Development
"""
import subprocess
import sys

def install_mongodb():
    """Install MongoDB Community Edition"""
    print("🚀 Setting up Local MongoDB for Development")
    print("=" * 50)
    
    print("📋 Steps to install MongoDB:")
    print("1. Download MongoDB Community Edition from:")
    print("   https://www.mongodb.com/try/download/community")
    print("2. Install with default settings")
    print("3. Start MongoDB service")
    print("4. Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
    
    # Alternative: Use Docker if available
    print("\n🐳 Alternative: Use Docker MongoDB")
    print("Run: docker run -d -p 27017:27017 --name mongodb mongo:latest")
    
    return True

if __name__ == "__main__":
    install_mongodb()
