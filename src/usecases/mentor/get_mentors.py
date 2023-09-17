class GetMentors:
    def __init__(self, mentor_repository):
        self.mentor_repository = mentor_repository

    def execute(self):
        mentor_repository = self.mentor_repository
        return mentor_repository.get_all()
