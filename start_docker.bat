@echo off
echo 🐳 Starting Backend with Docker...
echo.

echo 📦 Building Docker containers...
docker-compose build

echo.
echo 🚀 Starting services...
docker-compose up

echo.
echo ✅ Backend is running at http://localhost:8001
echo 📱 Your frontend can now connect to the backend!
pause
