from datetime import datetime, timezone
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, Integer

from . import Base
from src.entities import Mentor


class MentorModel(Base):
    """ Mentor Database Model """
    __tablename__ = "mentor"

    id = Column("id", Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime)

    meeting = relationship("MeetingModel", back_populates="mentor")
    slot = relationship("SlotModel", back_populates="mentor")
    availability = relationship("AvailabilityModel", back_populates="mentor")

    def __init__(self, mentor: Mentor, updated_at: Union[DateTime, None] = None):
        self.id = mentor.id
        self.first_name = mentor.first_name
        self.last_name = mentor.last_name
        self.email = mentor.email

        if updated_at:
            self.updated_at = updated_at
