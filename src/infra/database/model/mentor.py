from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, Integer
from . import Base


class Mentor(Base):
    ''' Mentor Database Model '''
    __tablename__ = 'mentor'

    id = Column('id', Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    meeting = relationship('Meeting')

    def __repr__(self) -> str:
        return f'Mentor(id={self.id!r}, name={self.first_name!r}, email={self.email!r})'
