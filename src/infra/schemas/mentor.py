from typing import List
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
    mentors: List[MentorViewSchema]


def show_mentors(mentors: List[MentorViewSchema]):
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
    return result
