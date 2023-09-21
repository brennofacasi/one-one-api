from src.entities import Availability
from src.usecases.ports import AvailabilityRepository

from typing import List


class CreateAvailabilities:
    def __init__(self, availability_repository: AvailabilityRepository):
        self.availability_repository = availability_repository

    def execute(self, availabilities: List[Availability]):
        repository = self.availability_repository
        repository.add_many(availabilities)
