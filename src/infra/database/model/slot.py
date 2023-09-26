from datetime import datetime, timezone
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column,  DateTime, Integer, ForeignKey, UniqueConstraint, String

from . import Base
from src.entities import Slot


class SlotModel(Base):
    """ Slot Database Model """
    __tablename__ = "slot"

    id = Column("id", Integer, primary_key=True)
    mentor_id = Column(Integer, ForeignKey("mentor.id"), nullable=False)
    meeting_id = Column(String, ForeignKey("meeting.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime)

    mentor = relationship("MentorModel", foreign_keys=[
                          mentor_id], back_populates="slot")
    meeting = relationship("MeetingModel", foreign_keys=[
                           meeting_id], back_populates="slot")

    __table_args__ = (UniqueConstraint('mentor_id', 'start_time', 'end_time'),)

    def __init__(self, slot: Slot, created_at: Union[DateTime, None] = None,
                 updated_at: Union[DateTime, None] = None):

        self.mentor_id = slot.mentor_id
        self.meeting_id = slot.meeting_id
        self.start_time = slot.start_time
        self.end_time = slot.end_time
        self.id = slot.id

        if created_at:
            self.created_at = created_at

        if updated_at:
            self.updated_at = updated_at
