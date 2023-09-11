from src.entities import Minute


class CreateMinute:
    def __init__(self, minute_repository):
        self.minute_repository = minute_repository

    def execute(self, meeting, content):
        repository = self.minute_repository
        minute = Minute(meeting, content)
        repository.add(minute)
