from src.entities import Meeting


class CreateMeeting:
    def __init__(self, meeting_repository):
        self.meeting_repository = meeting_repository

    def perform(self, id, mentor, mentee, date, duration, kind):
        repository = self.meeting_repository
        meeting = Meeting(id, mentor, mentee, date, duration, kind)
        repository.add(meeting)
