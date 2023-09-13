from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,  DateTime, Integer, ForeignKey

from src.entities import Meeting
from .base import Base


class MeetingModel(Base):
    ''' Meeting Database Model '''
    __tablename__ = 'meeting'

    id = Column('id', String, primary_key=True)
    date = Column(DateTime, nullable=False)
    mentor_id = Column(Integer, ForeignKey('mentor.id'), nullable=False)
    mentee_id = Column(Integer, nullable=False)
    duration = Column(Integer)
    kind = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    mentor = relationship('MentorModel', back_populates='meeting')
    history = relationship('HistoryModel', back_populates='meeting')
    minute = relationship('MinuteModel', back_populates='meeting')

    def __repr__(self) -> str:
        return f'Meeting(id={self.id!r}, date={self.date!r})'

    def __init__(self, meeting: Meeting, created_at: Union[DateTime, None] = None, updated_at: Union[DateTime, None] = None):
        self.date = meeting.date
        self.mentor_id = meeting.mentor_id
        self.mentee_id = meeting.mentee_id
        self.duration = meeting.duration
        self.kind = meeting.kind
        self.id = meeting.id

        if created_at:
            self.created_at = created_at

        if updated_at:
            self.updated_at = updated_at
