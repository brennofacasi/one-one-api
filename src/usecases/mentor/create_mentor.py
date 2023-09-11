from src.entities import Mentor
from .errors import DuplicateMentorError


class CreateMentor:
    def __init__(self, mentor_repository):
        self.mentor_repository = mentor_repository

    def execute(self, mentor):
        repository = self.mentor_repository

        if repository.find_by_email(mentor.email) != None:
            raise DuplicateMentorError()

        mentor = Mentor(mentor.first_name, mentor.last_name, mentor.email)
        repository.add(mentor)
