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

    def delete(self, meeting_id):
        session = self.session
        session.query(MeetingModel).filter(
            MeetingModel.id == meeting_id).delete()
        session.commit()

    def find_by_id(self, id):
        session = self.session
        meeting = session.query(MeetingModel).filter(
            MeetingModel.id == id).first()
        return meeting

    def get_all(self):
        session = self.session
        meetings = session.query(MeetingModel).join(
            MeetingModel.mentor).order_by(MeetingModel.created_at.asc()).all()
        return meetings
