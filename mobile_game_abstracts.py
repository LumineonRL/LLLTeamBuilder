from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class Character(ABC):
    name: str

@dataclass
class Card(ABC):
    @dataclass
    class CardMetadata(ABC):
        name: str
        character: Character
    
    @dataclass
    class Stat(ABC):
        pass
    
    _id: int
    metadata: CardMetadata
    stats: Stat

    # Implementation should use @property
    @abstractmethod
    def id(self) -> int:
        pass
    
    # Implementation should use @id.setter
    @abstractmethod
    def id(self, new_id: int) -> None:
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
