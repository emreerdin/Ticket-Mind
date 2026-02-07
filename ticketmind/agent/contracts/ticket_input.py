from pydantic import BaseModel
import uuid
import datetime
from typing import Any

class TicketInput(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    subject: str
    body: str
    status: str
    created_at: datetime.datetime