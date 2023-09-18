from .errors import DuplicateMentorError


class CreateMentor:
    def __init__(self, mentor_repository):
        self.mentor_repository = mentor_repository

    def execute(self, mentor):
        repository = self.mentor_repository

        if repository.find_by_email(mentor.email) is not None:
            raise DuplicateMentorError()

        repository.add(mentor)
