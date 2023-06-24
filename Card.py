from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List
from collections import Counter
from DataLoader import JsonCardDataLoader

@dataclass
class Stats:
    smile: int = 0
    pure: int = 0
    cool: int = 0
    mental: int = 0
    bp: int = 0


@dataclass
class Mood:
    style_type: str = "パフォーマー"
    mood_type: str = "ハッピー"


@dataclass
class Training:
    level: int = 1
    uncaps: int = 0
    appeal_level: int = 1
    skill_level: int = 1


@dataclass
class Card(Stats, Mood, Training):
    _id: int = 0
    name: str = ""
    character: str = ""
    rarity: str = ""
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, new_id: int):
        assert isinstance(new_id, int) and new_id > 0,\
            "Card ID must be a positive integer."
        self._id = new_id
        
class CardLoader:

      @staticmethod  
      def create_card_from_id(card_id:int)-> Card :
          card_data=JsonCardDataLoader.get_card_data()
          
          if not card_data or not isinstance(card_data,list):
              raise ValueError('Invalid data format')
              
          for c in card_data:
              if 'id' in c and c['id']==card_id:
                  # Create a dictionary that maps keys to values from the found object. 
                  # This will ignore any additional fields present.
                  fields_dict={k:v for k,v in c.items() if hasattr(Card,k)}
                  
                  return Card(**fields_dict)

          raise ValueError(f"No matching cards with provided id {card_id}")


@dataclass(order=True, frozen=False)
class Deck(ABC):
    cards: List[Card]

    @abstractmethod
    def add_card(self, card: Card) -> None:
        pass

    @abstractmethod
    def remove_card(self, card: Card) -> None:
        pass


def _initial_cards() -> List[Card]:
    pass
    #initial_cards = JsonCardDataLoader("Data/initial_cards.json")
    #return initial_cards.read_json()


@dataclass(frozen=False)
class InitialDeck(Deck):
    cards: List[Card] = field(default_factory=_initial_cards)

    @abstractmethod
    def add_card(self, card: Card) -> None:
        pass

    @abstractmethod
    def remove_card(self, card: Card) -> None:
        pass


def _default_character_names() -> List[str]:
    return ["日野下花帆", "林野さやか", "大沢瑠璃乃", "乙宗梢", "夕霧綴理", "藤島慈"]


@dataclass(frozen=True)
class Characters:
    name: List[str] = field(default_factory=_default_character_names)


def _initialize_character_counts() -> Counter:
    return Counter()


@dataclass
class UserDeck(InitialDeck):
    _character_counts: Counter = field(default_factory=_initialize_character_counts)
    _max_cards_per_character: int = 3

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

        self._check_validity()

    def remove_card(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)

        self._check_validity()

    def _check_validity(self) -> bool:
        deck_characters = []

        for card in self.cards:
            deck_characters.append(card.character)

        self._character_counts = Counter(deck_characters)

        self._check_all_chars()
        self._check_max_chars()

    def _check_all_chars(self) -> None:
        CHARACTERS = Characters().name

        for char in CHARACTERS:
            if char not in self._character_counts.keys():
                raise ValueError(
                    f"{char} not found. You may have tried to delete all instances of a character from your deck."
                )

    def _check_max_chars(self) -> None:
        for char, count in self._character_counts.items():
            if count > self._max_cards_per_character:
                raise ValueError(
                    f"More than 3 cards for {char} found. You may have tried to add a 4th card of a character to your deck."
                )

    def calculate_stat(self, stat: str) -> int:
        return sum(getattr(card, stat) for card in self.cards if stat in vars(Stats))
