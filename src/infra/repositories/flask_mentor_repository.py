from src.usecases.ports import MentorRepository
from src.infra.database import Session
from src.infra.database.model import MentorModel


class FlaskMentorRepository(MentorRepository):
    def __init__(self):
        self.session = Session()

    def add(self, mentor):
        session = self.session
        mentor_model = MentorModel(mentor)
        session.add(mentor_model)
        session.commit()

    def get_all(self):
        # TO DO - Implement
        return super().get_all()

    def find_by_email(self, email):
        session = self.session
        mentor = session.query(MentorModel).filter(
            MentorModel.email == email).first()
        return mentor
