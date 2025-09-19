from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")
        return field_schema

class UserRole(str, Enum):
    TOURIST = "tourist"
    GUIDE = "guide"
    BUSINESS = "business"
    ADMIN = "admin"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

# User Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone: Optional[str] = None
    role: UserRole
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserResponse(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

# Authentication Models
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    role: UserRole

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Destination Models
class DestinationBase(BaseModel):
    name: str
    state: str
    description: str
    attractions: List[str] = []
    popular_places: List[str] = []
    image_url: str
    coordinates: Optional[Dict[str, float]] = None
    best_time_to_visit: Optional[str] = None
    climate: Optional[str] = None

class DestinationCreate(DestinationBase):
    pass

class DestinationUpdate(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    description: Optional[str] = None
    attractions: Optional[List[str]] = None
    popular_places: Optional[List[str]] = None
    image_url: Optional[str] = None
    coordinates: Optional[Dict[str, float]] = None
    best_time_to_visit: Optional[str] = None
    climate: Optional[str] = None

class Destination(DestinationBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Homestay Models
class HomestayBase(BaseModel):
    name: str
    location: str
    description: str
    price_per_night: float
    amenities: List[str] = []
    host_name: str
    host_phone: str
    coordinates: Optional[Dict[str, float]] = None
    images: List[str] = []

class HomestayCreate(HomestayBase):
    pass

class HomestayUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    price_per_night: Optional[float] = None
    amenities: Optional[List[str]] = None
    host_name: Optional[str] = None
    host_phone: Optional[str] = None
    coordinates: Optional[Dict[str, float]] = None
    images: Optional[List[str]] = None

class Homestay(HomestayBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    rating: float = 0.0
    total_reviews: int = 0
    is_available: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Guide Models
class GuideBase(BaseModel):
    name: str
    speciality: str
    languages: List[str] = []
    experience_years: int
    phone: str
    email: EmailStr
    description: str
    price_per_day: float
    availability: bool = True

class GuideCreate(GuideBase):
    pass

class GuideUpdate(BaseModel):
    name: Optional[str] = None
    speciality: Optional[str] = None
    languages: Optional[List[str]] = None
    experience_years: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    description: Optional[str] = None
    price_per_day: Optional[float] = None
    availability: Optional[bool] = None

class Guide(GuideBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    rating: float = 0.0
    total_reviews: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Handicraft Models
class HandicraftBase(BaseModel):
    name: str
    description: str
    price: float
    category: str
    artist_name: str
    artist_phone: str
    images: List[str] = []
    materials_used: List[str] = []

class HandicraftCreate(HandicraftBase):
    pass

class HandicraftUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    artist_name: Optional[str] = None
    artist_phone: Optional[str] = None
    images: Optional[List[str]] = None
    materials_used: Optional[List[str]] = None

class Handicraft(HandicraftBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    is_available: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Itinerary Models
class ItineraryBase(BaseModel):
    title: str
    description: str
    duration_days: int
    places: List[str] = []
    highlights: List[str] = []
    difficulty_level: str = "Easy"
    price_estimate: Optional[float] = None

class ItineraryCreate(ItineraryBase):
    pass

class ItineraryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    duration_days: Optional[int] = None
    places: Optional[List[str]] = None
    highlights: Optional[List[str]] = None
    difficulty_level: Optional[str] = None
    price_estimate: Optional[float] = None

class Itinerary(ItineraryBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    rating: float = 0.0
    total_reviews: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Booking Models
class BookingBase(BaseModel):
    user_id: str
    booking_type: str  # "homestay", "guide", "itinerary"
    item_id: str
    start_date: datetime
    end_date: Optional[datetime] = None
    total_amount: float
    status: BookingStatus = BookingStatus.PENDING

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    status: Optional[BookingStatus] = None

class Booking(BookingBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Review Models
class ReviewBase(BaseModel):
    user_id: str
    item_id: str
    item_type: str  # "destination", "homestay", "guide", "itinerary"
    rating: int = Field(..., ge=1, le=5)
    comment: str
    title: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Chat Models
class Message(BaseModel):
    id: str
    text: str
    isUser: bool
    timestamp: datetime

class ChatRequest(BaseModel):
    messages: List[Message]
    language: str = "en"

class ChatResponse(BaseModel):
    reply: str
    language: str
    timestamp: str
