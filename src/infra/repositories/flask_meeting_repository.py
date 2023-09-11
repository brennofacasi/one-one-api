from src.usecases.ports import MeetingRepository
from src.infra.database import Session
from src.infra.database.model import MeetingModel


class FlaskMeetingRepository(MeetingRepository):
    def __init__(self):
        self.session = Session()

    def add(self, meeting):
        meeting_model = MeetingModel(
            meeting.date, meeting.mentor, meeting.mentee, meeting.duration, meeting.kind)
        self.session.add(meeting_model)
        self.session.commit()
        return {
            "message": "Meeting added successfully."
        }

    def find_by_id(self, meeting_id):
        # TO DO - Implement Find by Id
        return super().find_by_id(meeting_id)
