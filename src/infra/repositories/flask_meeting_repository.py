from src.usecases.ports import MeetingRepository
from src.infra.database import Session


class FlaskMeetingRepository(MeetingRepository):
    def __init__(self):
        self.session = Session()

    def add(self, meeting):
        self.session.add(meeting)
        self.session.commit()
        return {
            "message": "Meeting added successfully."
        }

    def find_by_id(self, meeting_id):
        return super().find_by_id(meeting_id)
