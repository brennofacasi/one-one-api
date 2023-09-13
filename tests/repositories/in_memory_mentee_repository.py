import json
import os
from src.usecases.ports import MenteeRepository


class InMemoryMenteeRepository(MenteeRepository):
    def __init__(self):
        dirPath = os.path.dirname(__file__)
        dbPath = os.path.join(dirPath, 'fake_mentee_database.json')
        db = open(dbPath)
        data = json.load(db)
        self.mentees = data
        db.close()

    def get_all(self):
        return self.mentees

    def find_by_email(self, email):
        for mentee in self.mentees:
            if mentee.email == email:
                return mentee

    def find_by_id(self, id):
        for mentee in self.mentees:
            if mentee['id'] == id:
                return mentee
