from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def pass_data(cls, path):
        raise NotImplementedError
