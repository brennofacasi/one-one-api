from pydantic import BaseModel
from datetime import datetime
from src.entities import Status


class MeetingSchema(BaseModel):
    date: datetime
    mentor_id: int
    mentee_id: int
    duration: int
    kind: Status


class MeetingViewSchema(BaseModel):
    id: str
    date: datetime
    mentor_id: int
    mentee_id: int
    duration: int
    kind: str
    created_at: datetime
    updated_at: datetime
