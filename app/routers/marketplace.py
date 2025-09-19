from fastapi import APIRouter, HTTPException
from ..database import get_database

router = APIRouter()


@router.get("/homestays")
async def list_homestays():
    """Get all homestays"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        homestays = await database.homestays.find({"is_available": True}).to_list(length=None)
        
        # Convert ObjectId to string for JSON serialization
        for homestay in homestays:
            homestay["_id"] = str(homestay["_id"])
        
        return homestays
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/guides")
async def list_guides():
    """Get all available guides"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        guides = await database.guides.find({"availability": True}).to_list(length=None)
        
        # Convert ObjectId to string for JSON serialization
        for guide in guides:
            guide["_id"] = str(guide["_id"])
        
        return guides
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/handicrafts")
async def list_handicrafts():
    """Get all available handicrafts"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        handicrafts = await database.handicrafts.find({"is_available": True}).to_list(length=None)
        
        # Convert ObjectId to string for JSON serialization
        for handicraft in handicrafts:
            handicraft["_id"] = str(handicraft["_id"])
        
        return handicrafts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


