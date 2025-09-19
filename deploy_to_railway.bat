@echo off
echo 🚂 Deploying Journey 360 Backend to Railway
echo ==========================================

echo 📦 Installing Railway CLI...
npm install -g @railway/cli

echo.
echo 🔐 Logging into Railway...
railway login

echo.
echo 🏗️ Initializing Railway project...
railway init

echo.
echo 🗄️ Adding MongoDB database...
railway add mongodb

echo.
echo 🚀 Deploying to Railway...
railway up

echo.
echo ✅ Deployment complete!
echo 📱 Update your frontend API URL to the Railway URL
echo 📖 Check RAILWAY_DEPLOYMENT.md for next steps

pause
