from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Define the Message model
class Message(BaseModel):
    sender: str
    text: str
    timestamp: datetime
    message_type: str
    question_id: Optional[str] = None

# Define the Conversation model
class Conversation(BaseModel):
    conversation_id: str
    scenario_type: str
    resident_id: str
    resident_name: str
    event_type: str
    reporting_agent_id: str
    reporting_agent: str
    messages: List[Message]
    summary: str
    created_at: datetime
    updated_at: datetime
