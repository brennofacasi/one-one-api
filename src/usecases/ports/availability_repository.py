from abc import ABC, abstractmethod


class AvailabilityRepository(ABC):
    @abstractmethod
    def add(self, availability):
        raise NotImplementedError

    @abstractmethod
    def add_many(self, availabilities):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, availability_id):
        raise NotImplementedError

    @abstractmethod
    def delete(self, availability_id):
        raise NotImplementedError

    @abstractmethod
    def find_by_mentor_id(self, mentor_id):
        raise NotImplementedError
