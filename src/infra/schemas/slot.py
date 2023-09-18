from datetime import datetime
from pydantic import BaseModel


class SlotSchema(BaseModel):
    mentor_id: int
    start_time: datetime
    end_time: datetime
    is_available: bool


class SlotSearchById(BaseModel):
    id: int
