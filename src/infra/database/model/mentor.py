from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, UUID, String, DateTime
from . import Base


class Mentor(Base):
    ''' Mentor Database Model '''
    __tablename__ = 'mentor'

    id = Column('id', UUID, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    meeting = relationship('Meeting')

    def __repr__(self) -> str:
        return f'Mentor(id={self.id!r}, name={self.name!r}, email={self.email!r})'
