#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Railway typically uses port 8000, so let's use that directly
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
