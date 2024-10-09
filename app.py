from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from models import Conversation

# MongoDB connection string

# Database and collection names
DATABASE_NAME = "AI_event_report"
COLLECTION_NAME = "conversations"

# Create FastAPI app instance
app = FastAPI()

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGODB_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

@app.get("/conversations/", response_model=List[Conversation])
async def get_conversations(resident_id: str, event_type: str):
    try:
        # Create the MongoDB query based on the resident_id and event_type
        query = {"resident_id": resident_id, "event_type": event_type}
        
        # Fetch documents from the collection (limit to 100 documents for performance)
        conversations = await collection.find(query).to_list(100)
        
        # If no documents are found, raise an HTTP 404 error
        if not conversations:
            raise HTTPException(status_code=404, detail="No conversations found")
        
        return conversations
    
    except Exception as e:
        # Handle any exceptions and return a 500 error
        raise HTTPException(status_code=500, detail=str(e))

