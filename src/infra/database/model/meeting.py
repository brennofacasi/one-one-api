from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,  DateTime, Integer, ForeignKey
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

    history = relationship('HistoryModel', back_populates='meeting')
    minute = relationship('MinuteModel', back_populates='meeting')

    def __repr__(self) -> str:
        return f'Meeting(id={self.id!r}, date={self.date!r})'

    def __init__(self, date: DateTime, mentor_id: int, mentee_id: int, duration: int, kind: str, updated_at: Union[DateTime, None] = None):
        self.date = date
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id
        self.duration = duration
        self.kind = kind

        if updated_at:
            self.updated_at = updated_at
