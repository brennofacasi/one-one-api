from src.usecases.ports import MeetingRepository
from src.infra.database import Session
from src.infra.database.model import MeetingModel, SlotModel


class DBMeetingRepository(MeetingRepository):
    def __init__(self):
        self.session = Session()

    def add(self, meeting):
        session = self.session
        meeting_model = MeetingModel(meeting)
        meeting_model.slot = SlotModel(meeting.slot)
        session.add(meeting_model)
        session.commit()

    def update(self, meeting_id, data):
        # TO DO: Implement update method
        raise NotImplementedError

    def delete(self, meeting_id):
        session = self.session
        session.query(MeetingModel).filter(
            MeetingModel.id == meeting_id).delete()
        session.commit()

    def find_by_id(self, meeting_id):
        session = self.session
        meeting = session.query(MeetingModel).filter(
            MeetingModel.id == meeting_id).first()
        return meeting

    def get_all(self):
        session = self.session
        meetings = session.query(MeetingModel).join(
            MeetingModel.mentor).join(MeetingModel.slot).order_by(SlotModel.start_time.asc()).all()
        return meetings
