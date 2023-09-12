from src.usecases.ports import MeetingRepository
from src.infra.database import Session
from src.infra.database.model import MeetingModel


class DBMeetingRepository(MeetingRepository):
    def __init__(self):
        self.session = Session()

    def add(self, meeting):
        session = self.session
        meeting_model = MeetingModel(meeting)
        session.add(meeting_model)
        session.commit()

    def find_by_id(self, meeting_id):
        # TO DO - Implement Find by Id
        return super().find_by_id(meeting_id)
