from abc import ABC, abstractmethod


class SlotRepository(ABC):
    @abstractmethod
    def add(self, slot):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, slot_id):
        raise NotImplementedError

    @abstractmethod
    def find_by_mentor_id(self, mentor_id):
        raise NotImplementedError

    @abstractmethod
    def set_available_by_id(self, slot_id):
        raise NotImplementedError

    @abstractmethod
    def set_unavailable_by_id(self, slot_id):
        raise NotImplementedError
