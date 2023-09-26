from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class Card(ABC):
    _id: int

    @abstractmethod
    def id(self) -> int:
        pass

    @abstractmethod
    def id(self, new_id: int):
        pass
    
@dataclass(order=True, frozen=False)
class Deck(ABC):
    cards: List[Card]

    @abstractmethod
    def add_card(self, card: Card) -> None:
        pass

    @abstractmethod
    def remove_card(self, card: Card) -> None:
        pass