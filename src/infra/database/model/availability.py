from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, Time, Integer, ForeignKey

from . import Base
from src.entities import Availability


class AvailabilityModel(Base):
    """ Availability Database Model """
    __tablename__ = "availability"

    id = Column("id", Integer, primary_key=True)
    mentor_id = Column(Integer, ForeignKey("mentor.id"), nullable=False)
    week_day = Column(Integer, nullable=False)
    from_time = Column(Time, nullable=False)
    to_time = Column(Time, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    mentor = relationship(
        "MentorModel", back_populates="availability", foreign_keys=[mentor_id])

    def __init__(self, availability: Availability,
                 created_at: Union[DateTime, None] = None, updated_at: Union[DateTime, None] = None):

        self.id = availability.id
        self.mentor_id = availability.mentor_id
        self.week_day = availability.week_day
        self.from_time = availability.from_time
        self.to_time = availability.to_time

        if created_at:
            self.created_at = created_at

        if updated_at:
            self.updated_at = updated_at