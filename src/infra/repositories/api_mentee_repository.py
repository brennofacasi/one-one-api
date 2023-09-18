import os
import requests
from dotenv import load_dotenv

from src.infra.schemas import show_mentees
from src.entities import Mentee
from src.usecases.ports import MenteeRepository

load_dotenv()


class ApiMenteeRepository(MenteeRepository):
    def __init__(self):
        res = requests.get(os.getenv("USERS_API"))
        data = res.json()
        self.users = data["users"]

    def get_all(self):
        result = []
        for user in self.users:
            mentee = Mentee(user["firstName"], user["lastName"],
                            user["email"], user["company"]["name"], user["id"])
            result.append(mentee)
        return show_mentees(result)

    def find_by_email(self, email):
        mentees = self.get_all()
        for mentee in mentees:
            if mentee["email"] == email:
                return mentee

    def find_by_id(self, mentee_id):
        mentees = self.get_all()
        for mentee in mentees:
            if mentee["id"] == mentee_id:
                return mentee
