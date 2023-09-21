from src.entities import Availability
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

    def find_by_id(self, availability_id):
        session = self.session
        availability = session.query(AvailabilityModel).filter(
            AvailabilityModel.id == availability_id).first()
        return availability

    def find_by_mentor_id(self, mentor_id):
        session = self.session
        availabilities = []
        result = session.query(AvailabilityModel).filter(
            AvailabilityModel.mentor_id == mentor_id).all()
        for item in result:
            availabilities.append(Availability(
                item.mentor_id, item.week_day, item.from_time, item.to_time, item.id))
        return availabilities
