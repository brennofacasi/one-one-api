from abc import ABC, abstractmethod


class AvailabilityRepository(ABC):
    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_mentor_id(self):
        raise NotImplementedError
