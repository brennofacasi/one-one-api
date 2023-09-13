from pydantic import BaseModel
from typing import List


class MenteeViewSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    company: str


def show_mentees(mentees: List[MenteeViewSchema]):
    result = []
    for mentee in mentees:
        result.append({
            "id": mentee.id,
            "first_name": mentee.first_name,
            "last_name": mentee.last_name,
            "email": mentee.email,
            "company": mentee.company,
        })
    return result
