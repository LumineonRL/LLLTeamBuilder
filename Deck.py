from collections import Counter
from Card import Card


class Deck:
    def __init__(self) -> None:
        INITIAL_CARDS = [
            Card(
                "オーロラスカイ",
                "日野下花帆",
                "R",
                {"smile": 1225, "pure": 1525, "cool": 925, "mental": 123, "bp": 100},
                {"style_type": "パフォーマー", "mood": "ハッピー"},
                {},
            ),
            Card(
                "オーロラスカイ",
                "林野さやか",
                "R",
                {"smile": 1225, "pure": 1025, "cool": 1425, "mental": 123, "bp": 100},
                {"style_type": "ムードメーカー", "mood": "メロウ"},
                {},
            ),
            Card(
                "オーロラスカイ",
                "大沢瑠璃乃",
                "R",
                {"smile": 1525, "pure": 1125, "cool": 725, "mental": 153, "bp": 100},
                {"style_type": "トリックスター", "mood": "ニュートラル"},
                {},
            ),
            Card(
                "オーロラスカイ",
                "乙宗梢",
                "R",
                {"smile": 1525, "pure": 1225, "cool": 925, "mental": 123, "bp": 100},
                {"style_type": "チアリーダー", "mood": "ハッピー"},
                {},
            ),
            Card(
                "オーロラスカイ",
                "夕霧綴理",
                "R",
                {"smile": 1225, "pure": 925, "cool": 1525, "mental": 123, "bp": 100},
                {"style_type": "ムードメーカー", "mood": "メロウ"},
                {},
            ),
            Card(
                "オーロラスカイ",
                "藤島慈",
                "R",
                {"smile": 1125, "pure": 1525, "cool": 925, "mental": 133, "bp": 100},
                {"style_type": "チアリーダー", "mood": "ニュートラル"},
                {},
            ),
        ]

        self.cards = []
        for card in INITIAL_CARDS:
            self.cards.append(card)

        self._character_counts = Counter()

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
        CHARACTERS = ["日野下花帆", "林野さやか", "大沢瑠璃乃", "乙宗梢", "夕霧綴理", "藤島慈"]

        for char in CHARACTERS:
            if char not in self._character_counts.keys():
                raise ValueError(
                    f"{char} not found. You may have tried to delete all instances of a character from your deck."
                )

    def _check_max_chars(self) -> None:
        for char, count in self._character_counts.items():
            if count > 3:
                raise ValueError(
                    f"More than 3 cards for {char} found. You may have tried to add a 4th card of a character to your deck."
                )
