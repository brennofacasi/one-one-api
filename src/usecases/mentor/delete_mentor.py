from src.usecases.ports import MentorRepository
from src.usecases.mentor.errors import NotFoundMentorError


class DeleteMentor:
    def __init__(self, mentor_repository: MentorRepository):
        self.mentor_repository = mentor_repository

    def execute(self, mentor_id):
        repository = self.mentor_repository
        if repository.find_by_id(mentor_id) is None:
            raise NotFoundMentorError

        repository.delete(mentor_id)
