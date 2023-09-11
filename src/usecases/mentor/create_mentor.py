from src.entities import Mentor


class CreateMentor:
    def __init__(self, mentor_repository):
        self.mentor_repository = mentor_repository

    def execute(self, first_name, last_name, email):
        repository = self.mentor_repository
        mentor = Mentor(first_name, last_name, email)
        repository.add(mentor)
