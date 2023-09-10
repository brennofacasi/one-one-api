from abc import ABC, abstractmethod


class MinuteRepository(ABC):
    @abstractmethod
    def add(self, minute):
        raise (NotImplementedError)

    @abstractmethod
    def find_by_meeting_id(self, meeting_id):
        raise (NotImplementedError)
