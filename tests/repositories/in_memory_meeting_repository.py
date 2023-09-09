from src.usecases.ports.meeting_repository import MeetingRepository


class InMemoryMeetingRepository(MeetingRepository):
    def __init__(self):
        self.meetings = []

    def add(self, meeting):
        self.meetings.append(meeting)

    def find_by_id(self, meeting_id):
        for meeting in self.meetings:
            if meeting.id == meeting_id:
                return meeting
