#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Get PORT from environment variable or use default
    port = os.environ.get('PORT', '8000')
    
    # Ensure port is a valid integer
    try:
        port = int(port)
    except ValueError:
        print(f"Invalid PORT value: {port}, using default 8000")
        port = 8000
    
    print(f"Starting server on port {port}")
    print(f"Environment variables: PORT={os.environ.get('PORT', 'NOT SET')}")
    
    # Start uvicorn server
    cmd = [
        sys.executable, '-m', 'uvicorn', 
        'app.main:app', 
        '--host', '0.0.0.0', 
        '--port', str(port)
    ]
    
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
