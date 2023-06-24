from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List
from collections import Counter


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
    name: str = ""
    character: str = ""
    rarity: str = ""

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "character": self.character,
            "rarity": self.rarity,
            "stats": {
                "smile": self.smile,
                "pure": self.pure,
                "cool": self.cool,
                "mental": self.mental,
                "bp": self.bp,
            },
            "mood": {
                "style_type": self.style_type,
                "mood_type": self.mood_type
            },
            "training": {
                "level": self.level,
                "uncaps": self.uncaps,
                "appeal_level": self.appeal_level,
                "skill_level": self.skill_level,
            },
        }


@dataclass(order=True, frozen=False)
class Deck(ABC):
    cards: List[Card]

    @abstractmethod
    def add_card(self, card: Card) -> None:
        pass

    @abstractmethod
    def remove_card(self, card: Card) -> None:
        pass


def _default_cards() -> List[Card]:
    return [
        Card(
            "オーロラスカイ",
            "日野下花帆",
            "R",
            smile=1225,
            pure=1525,
            cool=925,
            mental=123,
            bp=100,
            style_type="パフォーマー",
            mood_type="ハッピー",
        ),
        Card(
            "オーロラスカイ",
            "林野さやか",
            "R",
            smile=1225,
            pure=1025,
            cool=1425,
            mental=123,
            bp=100,
            style_type="ムードメーカー",
            mood_type="メロウ",
        ),
        Card(
            "オーロラスカイ",
            "大沢瑠璃乃",
            "R",
            smile=1525,
            pure=1125,
            cool=725,
            mental=153,
            bp=100,
            style_type="トリックスター",
            mood_type="ニュートラル",
        ),
        Card(
            "オーロラスカイ",
            "乙宗梢",
            "R",
            smile=1525,
            pure=1225,
            cool=925,
            mental=123,
            bp=100,
            style_type="チアリーダー",
            mood_type="ハッピー",
        ),
        Card(
            "オーロラスカイ",
            "夕霧綴理",
            "R",
            smile=1225,
            pure=925,
            cool=1525,
            mental=123,
            bp=100,
            style_type="ムードメーカー",
            mood_type="メロウ",
        ),
        Card(
            "オーロラスカイ",
            "藤島慈",
            "R",
            smile=1125,
            pure=1525,
            cool=925,
            mental=133,
            bp=100,
            style_type="チアリーダー",
            mood_type="ニュートラル",
        ),
    ]


@dataclass(frozen=False)
class InitialDeck(Deck):
    cards: List[Card] = field(default_factory=_default_cards)

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
