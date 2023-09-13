class GetMeetings:
    def __init__(self, meetings_repository):
        self.meetings_repository = meetings_repository

    def execute(self):
        repository = self.meetings_repository
        return repository.get_all()
