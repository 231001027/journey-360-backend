from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List


router = APIRouter()


class Message(BaseModel):
    id: str
    text: str
    isUser: bool
    timestamp: datetime


class ChatRequest(BaseModel):
    messages: List[Message]
    language: str = "en"


@router.post("/chat")
def chat(req: ChatRequest):
    canned_responses = [
        "Based on your location, I can see you're near Hundru Falls! It's a spectacular 322-feet waterfall. Would you like me to share some local legends about this place?",
        "For emergency assistance, I've noted your location. The nearest police station is 2.3 km away. Emergency helpline: 100. Do you need immediate help?",
        "The weather today is perfect for sightseeing - 24°C with clear skies. I recommend visiting the Rock Garden in Ranchi. Shall I create a route for you?",
        "I can connect you with a certified local guide who speaks English and Hindi. Should I book for you?",
    ]
    idx = (len(req.messages) or 1) % len(canned_responses)
    return {
        "reply": canned_responses[idx],
        "language": req.language,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


