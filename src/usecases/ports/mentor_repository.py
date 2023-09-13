from abc import ABC, abstractmethod


class MentorRepository(ABC):
    @abstractmethod
    def add(self, mentor):
        raise (NotImplementedError)

    @abstractmethod
    def get_all(self):
        raise (NotImplementedError)

    @abstractmethod
    def find_by_email(self, email):
        raise (NotImplementedError)

    @abstractmethod
    def find_by_id(self, id):
        raise (NotImplementedError)
