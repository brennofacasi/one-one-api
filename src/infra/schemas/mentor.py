from datetime import datetime
from pydantic import BaseModel


class MentorSchema(BaseModel):
    first_name: str
    last_name: str
    email: str


class MentorViewSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime
