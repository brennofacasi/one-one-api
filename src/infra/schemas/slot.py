from datetime import datetime
from pydantic import BaseModel


class SlotSchema(BaseModel):
    mentor_id: int
    meeting_id: str
    start_time: datetime
    end_time: datetime
    is_available: bool


class SlotSearchById(BaseModel):
    id: int
