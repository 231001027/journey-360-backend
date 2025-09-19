#!/usr/bin/env python3
"""
Railway startup script - handles PORT environment variable properly
"""
import os
import sys
import uvicorn

def main():
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 8000))
    
    print(f"🚀 Starting Journey 360 Backend on port {port}")
    print(f"📊 Environment: {os.environ.get('NODE_ENV', 'development')}")
    print(f"🗄️ Database URL: {os.environ.get('MONGO_URL', 'mongodb://localhost:27017')}")
    
    # Start the server
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,  # Disable reload in production
        log_level="info"
    )

if __name__ == "__main__":
    main()
