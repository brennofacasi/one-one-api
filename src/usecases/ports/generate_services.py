from abc import ABC, abstractmethod


class GenerateServices(ABC):

    @abstractmethod
    def id(self):
        raise NotImplementedError
