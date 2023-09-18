from pydantic import BaseModel
from typing import List


class MenteeViewSchema(BaseModel):
    id: int = 2
    first_name: str = "Mike"
    last_name: str = "Wazowski"
    email: str = "mike@monstersinc.com"
    company: str = "Monsters Inc."


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
