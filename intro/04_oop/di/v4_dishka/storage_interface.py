from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def save(self, avatar_name: str):
        pass
