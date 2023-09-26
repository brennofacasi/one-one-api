from src.usecases.ports import SlotRepository
from src.infra.database.model import SlotModel
from src.infra.database import Session


class DBSlotRepository(SlotRepository):
    def __init__(self):
        self.session = Session()

    def add(self, slot):
        session = self.session
        slot_model = SlotModel(slot)
        session.add(slot_model)
        session.commit()

    def delete(self, slod_it):
        session = self.session
        session.query(SlotModel).filter(
            SlotModel.id == slod_it).delete()
        session.commit()

    def find_by_id(self, slot_id):
        session = self.session
        slot = session.query(SlotModel).filter(
            SlotModel.id == slot_id).first()
        return slot

    def find_by_mentor_id(self, mentor_id):
        session = self.session
        slots = session.query(SlotModel).filter(
            SlotModel.mentor_id == mentor_id).all()
        return slots

    def find_by_meeting_id(self, meeting_id):
        session = self.session
        slots = session.query(SlotModel).filter(
            SlotModel.meeting_id == meeting_id).all()
        return slots
