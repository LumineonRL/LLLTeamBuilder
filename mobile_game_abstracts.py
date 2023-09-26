from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Card(ABC):
    _id: int

    @abstractmethod
    def id(self) -> int:
        pass

    @abstractmethod
    def id(self, new_id: int):
        pass