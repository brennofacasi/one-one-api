from abc import ABC, abstractmethod


class SlotRepository(ABC):
    @abstractmethod
    def add(self, slot):
        raise NotImplementedError

    @abstractmethod
    def delete(self, slot_id):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, slot_id):
        raise NotImplementedError

    @abstractmethod
    def find_by_mentor_id(self, mentor_id):
        raise NotImplementedError

    @abstractmethod
    def find_by_meeting_id(self, meeting_id):
        raise NotImplementedError
