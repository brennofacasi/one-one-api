from abc import ABC, abstractmethod


class HistoryRepository(ABC):
    @abstractmethod
    def add(self, history):
        raise NotImplementedError

    @abstractmethod
    def find_by_meeting_id(self, meeting_id):
        raise NotImplementedError
