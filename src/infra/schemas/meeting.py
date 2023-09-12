from pydantic import BaseModel
from datetime import datetime


class MeetingSchema(BaseModel):
    date: datetime
    mentor: int
    mentee: int
    duration: int
    kind: str


class MeetingViewSchema(BaseModel):
    id: str
    date: datetime
    mentor_id: int
    mentee_id: int
    duration: int
    kind: str
    created_at: datetime
    updated_at: datetime
