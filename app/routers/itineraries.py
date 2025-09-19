from fastapi import APIRouter, HTTPException
from bson import ObjectId
from ..database import get_database

router = APIRouter()


@router.get("/")
async def list_itineraries():
    """Get all itineraries"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        itineraries = await database.itineraries.find().to_list(length=None)
        
        # Convert ObjectId to string for JSON serialization
        for itinerary in itineraries:
            itinerary["_id"] = str(itinerary["_id"])
        
        return itineraries
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/{itinerary_id}")
async def get_itinerary(itinerary_id: str):
    """Get a specific itinerary by ID"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        # Validate ObjectId format
        if not ObjectId.is_valid(itinerary_id):
            raise HTTPException(status_code=400, detail="Invalid itinerary ID format")
        
        itinerary = await database.itineraries.find_one({"_id": ObjectId(itinerary_id)})
        if not itinerary:
            raise HTTPException(status_code=404, detail="Itinerary not found")
        
        # Convert ObjectId to string
        itinerary["_id"] = str(itinerary["_id"])
        return itinerary
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


