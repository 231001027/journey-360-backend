from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os
from typing import Optional

# MongoDB configuration - Railway deployment

# Use MongoDB Atlas for production
DATABASE_NAME = "tourism_india"

# Atlas connection string - use environment variable for security
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Atlas connection (uncomment and use in Railway environment variables)
# MONGO_URL = "mongodb+srv://231001027_db_user:tourism_user@cluster0.rkmshaj.mongodb.net/tourism_india?retryWrites=true&w=majority&appName=Cluster0"

# Global database connection
client: Optional[AsyncIOMotorClient] = None
database = None

async def connect_to_mongo():
    """Create database connection to MongoDB"""
    global client, database
    
    try:
        print("🔄 Connecting to MongoDB...")
        
        # Connect to local MongoDB
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
        database = client[DATABASE_NAME]
        
        # Test the connection
        await client.admin.command('ping')
        print(f"✅ Connected to MongoDB successfully!")
        print(f"📊 Database: {DATABASE_NAME}")
        
        # Create indexes for better performance
        await create_indexes()
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        print("🔄 Falling back to mock mode...")
        
        # Fallback to mock mode
        client = None
        database = None
        print("⚠️  Using mock data for development")
        print("💡 To connect MongoDB: run 'python start_mongodb.py'")

async def close_mongo_connection():
    """Close database connection"""
    global client
    if client:
        client.close()
        print("🔌 Disconnected from MongoDB")

async def create_indexes():
    """Create database indexes for better performance"""
    if database is None:
        return
        
    try:
        # Users collection indexes
        await database.users.create_index("email", unique=True)
        await database.users.create_index("role")
        
        # Destinations collection indexes
        await database.destinations.create_index("name")
        await database.destinations.create_index("state")
        
        # Bookings collection indexes
        await database.bookings.create_index("user_id")
        await database.bookings.create_index("status")
        await database.bookings.create_index("created_at")
        
        # Reviews collection indexes
        await database.reviews.create_index("destination_id")
        await database.reviews.create_index("user_id")
        
        print("📊 Database indexes created successfully")
        
    except Exception as e:
        print(f"⚠️ Warning: Could not create indexes: {e}")

def get_database():
    """Get database instance"""
    return database
