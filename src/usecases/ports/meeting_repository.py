from abc import ABC, abstractmethod
from src.entities import Meeting


class MeetingRepository(ABC):
    @abstractmethod
    def add(self, meeting: Meeting):
        raise NotImplementedError

    @abstractmethod
    def delete(self, meeting_id):
        raise NotImplementedError

    @abstractmethod
    def update(self, meeting_id, data):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, meeting_id):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
