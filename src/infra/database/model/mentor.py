from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, Integer

from src.entities import Mentor
from . import Base


class MentorModel(Base):
    ''' Mentor Database Model '''
    __tablename__ = 'mentor'

    id = Column('id', Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    meeting = relationship('MeetingModel')

    def __repr__(self) -> str:
        return f'Mentor(id={self.id!r}, name={self.first_name!r}, email={self.email!r})'

    def __init__(self, mentor: Mentor, updated_at: Union[DateTime, None] = None):
        self.first_name = mentor.first_name
        self.last_name = mentor.last_name
        self.email = mentor.email

        if updated_at:
            self.updated_at = updated_at
