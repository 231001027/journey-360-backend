from fastapi import APIRouter, HTTPException, status, Depends
from datetime import timedelta
from ..models import UserCreate, UserResponse, LoginRequest, Token, User
from ..auth import (
    authenticate_user, 
    create_access_token, 
    get_password_hash, 
    get_current_active_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from ..database import get_database

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserCreate):
    """Register a new user"""
    database = get_database()
    if not database:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    # Check if user already exists
    existing_user = await database.users.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    user_dict = user_data.dict()
    user_dict["hashed_password"] = hashed_password
    del user_dict["password"]
    
    # Insert user into database
    result = await database.users.insert_one(user_dict)
    
    # Fetch the created user
    created_user = await database.users.find_one({"_id": result.inserted_id})
    return UserResponse(**created_user)

@router.post("/login", response_model=Token)
async def login_user(login_data: LoginRequest):
    """Login user and return access token"""
    user = await authenticate_user(login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user role matches requested role
    if user.role != login_data.role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Access denied. User role is {user.role}, but {login_data.role} was requested"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}, 
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """Get current user information"""
    return UserResponse(**current_user.dict())

@router.post("/logout")
async def logout_user():
    """Logout user (client should discard token)"""
    return {"message": "Successfully logged out"}

# Dummy login endpoint for testing (matches frontend dummy credentials)
@router.post("/dummy-login", response_model=Token)
async def dummy_login(login_data: LoginRequest):
    """Dummy login for testing with hardcoded credentials"""
    dummy_credentials = {
        "tourist@example.com": {"password": "tourist123", "role": "tourist"},
        "guide@example.com": {"password": "guide123", "role": "guide"},
        "business@example.com": {"password": "business123", "role": "business"},
        "admin@example.com": {"password": "admin123", "role": "admin"},
    }
    
    if login_data.email not in dummy_credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email"
        )
    
    creds = dummy_credentials[login_data.email]
    if (login_data.password != creds["password"] or 
        login_data.role != creds["role"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": login_data.email, "role": login_data.role}, 
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
