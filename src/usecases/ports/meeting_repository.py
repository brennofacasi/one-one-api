from abc import ABC, abstractmethod


class MeetingRepository(ABC):
    @abstractmethod
    def add(self, meeting):
        raise (NotImplementedError)

    @abstractmethod
    def find_by_id(self, meeting_id):
        raise (NotImplementedError)
