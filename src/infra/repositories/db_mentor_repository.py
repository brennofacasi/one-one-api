from src.usecases.ports import MentorRepository
from src.infra.database import Session
from src.infra.database.model import MentorModel


class DBMentorRepository(MentorRepository):
    def __init__(self):
        self.session = Session()

    def add(self, mentor):
        session = self.session
        mentor_model = MentorModel(mentor)
        session.add(mentor_model)
        session.commit()

    def delete(self, mentor_id):
        session = self.session
        session.query(MentorModel).filter(
            MentorModel.id == mentor_id).delete()
        session.commit()

    def get_all(self):
        session = self.session
        mentors = session.query(MentorModel).all()
        return mentors

    def find_by_email(self, email):
        session = self.session
        mentor = session.query(MentorModel).filter(
            MentorModel.email == email).first()
        return mentor

    def find_by_id(self, mentor_id):
        session = self.session
        mentor = session.query(MentorModel).filter(
            MentorModel.id == mentor_id).first()
        return mentor
