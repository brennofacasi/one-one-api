from datetime import datetime, timezone
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,  DateTime, Integer, ForeignKey

from . import Base
from src.entities import Meeting


class MeetingModel(Base):
    """ Meeting Database Model """
    __tablename__ = "meeting"

    id = Column("id", String, primary_key=True)
    mentor_id = Column(Integer, ForeignKey("mentor.id"), nullable=False)
    mentee_id = Column(Integer, nullable=False)
    kind = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime)

    mentor = relationship("MentorModel", back_populates="meeting")
    slot = relationship("SlotModel", back_populates="meeting", uselist=False)

    history = relationship(
        "HistoryModel", back_populates="meeting")
    minute = relationship(
        "MinuteModel", back_populates="meeting")

    def __init__(self, meeting: Meeting, created_at: Union[DateTime, None] = None,
                 updated_at: Union[DateTime, None] = None):
        self.mentor_id = meeting.mentor_id
        self.mentee_id = meeting.mentee_id
        self.kind = meeting.kind
        self.id = meeting.id

        if created_at:
            self.created_at = created_at

        if updated_at:
            self.updated_at = updated_at
