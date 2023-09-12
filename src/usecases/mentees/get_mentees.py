class GetMentees:
    def __init__(self, mentees_repository):
        self.mentees_repository = mentees_repository

    def execute(self):
        repository = self.mentees_repository
        return repository.get_all()
