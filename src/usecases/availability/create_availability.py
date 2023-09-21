from src.entities import Availability
from src.usecases.ports import AvailabilityRepository


class CreateAvailability:
    def __init__(self, availability_repository: AvailabilityRepository):
        self.availability_repository = availability_repository

    def execute(self, availability: Availability):
        repository = self.availability_repository
        repository.add(availability)
