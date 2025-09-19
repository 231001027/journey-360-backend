#!/usr/bin/env python3
"""
Quick Fix Script - Update database connection
"""
import os

def update_database_config():
    """Update database configuration for Atlas"""
    
    # Your Atlas connection string
    atlas_url = "mongodb+srv://231001027_db_user:ilnKCnxkczxfCKej@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0"
    
    # Read current database.py
    with open('app/database.py', 'r') as f:
        content = f.read()
    
    # Update the MONGO_URL
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('MONGO_URL = "mongodb://localhost:27017"'):
            lines[i] = f'MONGO_URL = "{atlas_url}"'
            break
    
    # Write back
    with open('app/database.py', 'w') as f:
        f.write('\n'.join(lines))
    
    print("✅ Database configuration updated for Atlas")
    print("🚀 Now try running: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000")

if __name__ == "__main__":
    update_database_config()
