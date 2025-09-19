#!/usr/bin/env python3
"""
Setup script for MongoDB database
This script will:
1. Install required dependencies
2. Start MongoDB (if not running)
3. Seed the database with initial data
"""

import subprocess
import sys
import asyncio
import os
from pathlib import Path

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_mongodb_running():
    """Check if MongoDB is running"""
    try:
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        print("✅ MongoDB is running")
        return True
    except Exception:
        print("❌ MongoDB is not running")
        return False

def start_mongodb():
    """Start MongoDB service (Windows)"""
    print("🚀 Starting MongoDB...")
    try:
        # Try to start MongoDB service on Windows
        subprocess.run(["net", "start", "MongoDB"], check=True, capture_output=True)
        print("✅ MongoDB service started")
        return True
    except subprocess.CalledProcessError:
        print("⚠️ Could not start MongoDB service automatically")
        print("Please start MongoDB manually:")
        print("1. Open Command Prompt as Administrator")
        print("2. Run: net start MongoDB")
        print("3. Or start MongoDB Compass/Shell")
        return False

async def seed_database():
    """Seed the database with initial data"""
    print("🌱 Seeding database...")
    try:
        from app.seed_data import seed_all_data
        await seed_all_data()
        return True
    except Exception as e:
        print(f"❌ Failed to seed database: {e}")
        return False

def main():
    """Main setup function"""
    print("🏗️ Setting up Tourism India Database")
    print("=" * 50)
    
    # Change to backend directory
    backend_dir = Path(__file__).parent
    os.chdir(backend_dir)
    
    # Step 1: Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        return False
    
    # Step 2: Check MongoDB
    if not check_mongodb_running():
        if not start_mongodb():
            print("❌ Setup failed - MongoDB not available")
            return False
    
    # Step 3: Seed database
    if not asyncio.run(seed_database()):
        print("❌ Setup failed at database seeding")
        return False
    
    print("\n🎉 Database setup completed successfully!")
    print("\nNext steps:")
    print("1. Start the backend server: python -m uvicorn app.main:app --reload")
    print("2. Start the frontend: npx expo start")
    print("3. Test the API endpoints")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
