class GetMentorAvailabilities:
    def __init__(self, availabilities_repository):
        self.availabilities_repository = availabilities_repository

    def execute(self, mentor_id):
        repository = self.availabilities_repository
        return repository.find_by_mentor_id(mentor_id)
