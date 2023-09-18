from pydantic import BaseModel
from datetime import datetime
from typing import List


class MeetingSchema(BaseModel):
    mentor_id: int
    mentee_id: int
    slot_id: int
    kind: str


class MeetingViewSchema(BaseModel):
    id: str
    mentor: object
    mentee_id: str
    slot: object
    kind: str
    created_at: datetime
    updated_at: datetime


class MeetingSearchById(BaseModel):
    id: str


def show_meetings(meetings: List[MeetingViewSchema], mentee_repository):
    result = []
    for meeting in meetings:
        mentee = mentee_repository.find_by_id(meeting.mentee_id)
        result.append({
            "id": meeting.id,
            "mentor": {
                "first_name": meeting.mentor.first_name,
                "last_name": meeting.mentor.last_name,
            },
            "mentee": mentee,
            "slot": {
                "start_time": meeting.slot.start_time,
                "end_time": meeting.slot.end_time,
            },
            "kind": meeting.kind,
            "created_at": meeting.created_at,
            "updated_at": meeting.updated_at
        })
    return result
