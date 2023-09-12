from src.entities import Meeting
from nanoid import generate


class CreateMeeting:
    def __init__(self, meeting_repository):
        self.meeting_repository = meeting_repository

    def execute(self, meeting):
        repository = self.meeting_repository
        id = generate()
        meeting = Meeting(meeting.mentor, meeting.mentee,
                          meeting.date, meeting.duration, meeting.kind, id)
        repository.add(meeting)
        return id
