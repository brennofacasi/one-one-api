from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, String, ForeignKey
from . import Base


class Minute(Base):
    ''' Minute Database Model '''
    __tablename__ = 'minute'

    meeting_id = Column(String, ForeignKey('meeting.id'),
                        primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    meeting = relationship('Meeting')

    def __repr__(self) -> str:
        return f'Minute(id={self.meeting_id!r}, date={self.content!r})'
