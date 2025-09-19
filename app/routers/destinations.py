from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from bson import ObjectId
from ..database import get_database
from ..models import Destination

router = APIRouter()


@router.get("/")
async def list_destinations(q: Optional[str] = Query(None)):
    """Get all destinations with optional search"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        if q:
            # Search by name (case-insensitive)
            destinations = await database.destinations.find(
                {"name": {"$regex": q, "$options": "i"}}
            ).to_list(length=None)
        else:
            destinations = await database.destinations.find().to_list(length=None)
        
        # Convert ObjectId to string for JSON serialization
        for dest in destinations:
            dest["_id"] = str(dest["_id"])
        
        return destinations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/{destination_id}")
async def get_destination(destination_id: str):
    """Get a specific destination by ID"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        # Validate ObjectId format
        if not ObjectId.is_valid(destination_id):
            raise HTTPException(status_code=400, detail="Invalid destination ID format")
        
        destination = await database.destinations.find_one({"_id": ObjectId(destination_id)})
        if not destination:
            raise HTTPException(status_code=404, detail="Destination not found")
        
        # Convert ObjectId to string
        destination["_id"] = str(destination["_id"])
        return destination
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.post("/")
async def create_destination(destination: Destination):
    """Create a new destination (Admin only)"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        result = await database.destinations.insert_one(destination.dict())
        created_destination = await database.destinations.find_one({"_id": result.inserted_id})
        created_destination["_id"] = str(created_destination["_id"])
        return created_destination
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


