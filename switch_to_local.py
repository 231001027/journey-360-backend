#!/usr/bin/env python3
"""
Switch to Local MongoDB for Development
"""
import os

def switch_to_local_mongodb():
    """Switch database configuration to local MongoDB"""
    
    print("🔄 Switching to Local MongoDB for Development")
    print("=" * 50)
    
    # Read current database.py
    with open('app/database.py', 'r') as f:
        content = f.read()
    
    # Update MONGO_URL to local
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('MONGO_URL = "mongodb+srv://'):
            lines[i] = 'MONGO_URL = "mongodb://localhost:27017"'
            break
    
    # Write back
    with open('app/database.py', 'w') as f:
        f.write('\n'.join(lines))
    
    print("✅ Switched to local MongoDB configuration")
    print("\n📋 Next Steps:")
    print("1. Install MongoDB Community Edition:")
    print("   https://www.mongodb.com/try/download/community")
    print("2. Start MongoDB service")
    print("3. Run: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")
    print("\n🔄 To switch back to Atlas later:")
    print("   python quick_atlas_fix.py")

if __name__ == "__main__":
    switch_to_local_mongodb()
