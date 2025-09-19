#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Get PORT from environment variable or use default
    port = os.environ.get('PORT', '8000')
    
    print(f"Starting server on port {port}")
    
    # Start uvicorn server
    cmd = [
        sys.executable, '-m', 'uvicorn', 
        'app.main:app', 
        '--host', '0.0.0.0', 
        '--port', port
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
