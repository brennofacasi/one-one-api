from datetime import datetime


class EditMentor:
    def __init__(self, mentor_repository):
        self.mentor_repository = mentor_repository

    def execute(self, mentor):
        repository = self.mentor_repository

        mentor.updated_at = datetime.now()
        repository.update(mentor)
