from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,  DateTime, Integer, ForeignKey
from . import Base


class Meeting(Base):
    ''' Meeting Database Model '''
    __tablename__ = 'meeting'

    id = Column('id', String, primary_key=True)
    date = Column(DateTime, nullable=False)
    mentor_id = Column(Integer, ForeignKey('mentor.id'), nullable=False)
    mentee_id = Column(Integer, nullable=False)
    duration = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    # mentor = relationship('Mentor')
    history = relationship('History')
    minute = relationship('Minute')

    def __repr__(self) -> str:
        return f'Meeting(id={self.id!r}, date={self.date!r})'
