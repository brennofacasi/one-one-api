from src.usecases.ports import MeetingRepository


class InMemoryMeetingRepository(MeetingRepository):
    def __init__(self):
        self.meetings = []

    def add(self, meeting):
        self.meetings.append(meeting)

    def delete(self, meeting_id):
        for meeting in self.meetings:
            if meeting.id == meeting_id:
                self.meetings.remove(meeting)

    def find_by_id(self, meeting_id):
        for meeting in self.meetings:
            if meeting.id == meeting_id:
                return meeting

    def get_all(self):
        return self.meetings

    def update(self, meeting_id, data):
        return super().update(meeting_id, data)
