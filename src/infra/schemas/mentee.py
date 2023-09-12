from pydantic import BaseModel


class MenteeViewSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    company: str
