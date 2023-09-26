
from .errors import AvailabilityNotFoundError


class DeleteAvailability:
    def __init__(self, availability_repository):
        self.availability_repository = availability_repository

    def execute(self, availability_id):
        repository = self.availability_repository

        if repository.find_by_id(availability_id) is None:
            raise AvailabilityNotFoundError

        repository.delete(availability_id)
