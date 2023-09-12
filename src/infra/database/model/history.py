from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,  DateTime, Enum, ForeignKey
from . import Base
from src.entities.status import Status


class HistoryModel(Base):
    ''' History Database Model '''
    __tablename__ = 'history'

    meeting_id = Column(String, ForeignKey('meeting.id'), nullable=False)
    status = Column(Enum(Status), nullable=False)
    motive = Column(String)
    created_at = Column(DateTime, default=datetime.now(), primary_key=True)

    meeting = relationship('MeetingModel', back_populates='history')

    def __repr__(self) -> str:
        return f'History(id={self.meeting_id!r}, date={self.status!r})'
