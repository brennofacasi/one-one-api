from src.entities import Meeting


class CreateMeeting:
    def __init__(self, meeting_repository):
        self.meeting_repository = meeting_repository

    def execute(self, mentor, mentee, date, duration, kind, id):
        repository = self.meeting_repository
        meeting = Meeting(mentor, mentee, date, duration, kind, id)
        repository.add(meeting)
