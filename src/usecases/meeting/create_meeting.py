from src.entities import Meeting


class CreateMeeting:
    def __init__(self, meeting_repository):
        self.meeting_repository = meeting_repository

    def execute(self, meeting):
        repository = self.meeting_repository
        meeting = Meeting(meeting.mentor, meeting.mentee,
                          meeting.date, meeting.duration, meeting.kind)
        repository.add(meeting)
