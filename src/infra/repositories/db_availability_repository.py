from src.usecases.ports import AvailabilityRepository
from src.infra.database.model import AvailabilityModel
from src.infra.database import Session


class DBAvailabilityRepository(AvailabilityRepository):
    def __init__(self):
        self.session = Session()

    def add(self, availability):
        session = self.session
        availability_model = AvailabilityModel(availability)
        session.add(availability_model)
        session.commit()

    def add_many(self, availabilities):
        session = self.session
        availabilities_model = []

        for availability in availabilities:
            availabilities_model.append(AvailabilityModel(availability))

        session.add_all(availabilities_model)
        session.commit()

    def get_all(self):
        session = self.session
        availabilities = session.query(AvailabilityModel).all()
        return availabilities

    def find_by_id(self, availability_id):
        session = self.session
        availability = session.query(AvailabilityModel).filter(
            AvailabilityModel.id == availability_id).first()
        return availability

    def delete(self, availability_id):
        session = self.session
        session.query(AvailabilityModel).filter(
            AvailabilityModel.id == availability_id).delete()
        session.commit()

    def find_by_mentor_id(self, mentor_id):
        session = self.session
        availabilities = session.query(AvailabilityModel).filter(
            AvailabilityModel.mentor_id == mentor_id).order_by(AvailabilityModel.week_day.asc()).all()
        return availabilities
