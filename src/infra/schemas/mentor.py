from datetime import datetime
from pydantic import BaseModel


class MentorSchema(BaseModel):
    first_name: str = "Brenno"
    last_name: str = "Cavalcante"
    email: str = "brenno@nouhau.pro"


class MentorViewSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime


class MentorSearchById(BaseModel):
    id: str


class MentorListSchema(BaseModel):
    mentors: list[MentorViewSchema]


class MentorGetAvailableSlotsSchema(BaseModel):
    mentor_id: str = 1
    week_starts: datetime = "2023-09-21T12:00:00Z"
    week_ends: datetime = "2023-09-28T18:00:00Z"
    slot_duration: int = 30


def show_mentors(mentors: list[MentorViewSchema]):
    result = []
    for mentor in mentors:
        result.append({
            "id": mentor.id,
            "first_name": mentor.first_name,
            "last_name": mentor.last_name,
            "email": mentor.email,
            "created_at": mentor.created_at,
            "updated_at": mentor.updated_at,
        })
    return {"mentors": result}


def show_mentor_slots(slots: list[tuple[datetime.time]]):
    result = []
    for slot in slots:
        result.append({
            "start_time": slot[0],
            "end_time": slot[1]
        })
    return {"slots": result}
