import json
from dataclasses import dataclass


@dataclass
class Card:
    name: str
    character: str
    rarity: str
    stats_dict: dict
    mood_dict: dict
    training_dict: dict

    @dataclass
    class Stats:
        smile: int = 0
        pure: int = 0
        cool: int = 0
        mental: int = 0
        bp: int = 0

        def __post_init__(self):
            if not all(
                self._is_non_negative_int(x)
                for x in [self.smile, self.pure, self.cool, self.mental, self.bp]
            ):
                raise ValueError("Stat parameters should be non-negative integers")

        @staticmethod
        def _is_non_negative_int(val):
            return isinstance(val, int) and val >= 1

    @dataclass
    class Mood:
        style_type: str = "パフォーマー"
        mood: str = "ハッピー"

    @dataclass
    class Training:
        level: int = 1
        uncaps: int = 0
        appeal_level: int = 1
        skill_level: int = 1

        if not all(
            isinstance(x, int) and x >= 1 for x in [level, appeal_level, skill_level]
        ):
            raise ValueError("Level parameters should be non-negative integers")

        if not all(isinstance(x, int) and x >= 0 and x <= 5 for x in [uncaps]):
            raise ValueError("Stat parameters should be non-negative integers")

    def __post_init__(self):
        # Creating an instance of Stats class from stats dictionary
        stats_instance = self.Stats(**self.stats_dict)
        mood_instance = self.Mood(**self.mood_dict)
        training_instance = self.Training(**self.training_dict)

        # Assigning the created instance to attribute 'stats'
        setattr(self, "stats", stats_instance)
        setattr(self, "mood", mood_instance)
        setattr(self, "training", training_instance)


class MyCards:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)

    def get_card_by_index(self, index) -> Card:
        return self.cards[index]

    def export_cards(self, filename: str) -> None:
        data = []
        for card in self.cards:
            stats = card.stats.__dict__
            mood = card.mood.__dict__
            training = card.training.__dict__

            card_dict = {
                "name": card.name,
                "character": card.character,
                "rarity": card.rarity,
                "stats": stats,
                "mood": mood,
                "training": training,
            }

            data.append(card_dict)

        with open(filename, "w", encoding="utf-8") as write_card_file:
            json.dump(data, write_card_file, default=lambda x: x.__dict__)

    def import_cards(self, filename: str) -> None:
        with open(filename, "r", encoding="utf-8") as read_card_file:
            file = json.load(read_card_file)

        cards = []

        for item in file:
            stats_attr = item["stats"]
            mood_attr = item["mood"]
            training_attr = item["training"]

            card = Card(
                name=item["name"],
                character=item["character"],
                rarity=item["rarity"],
                stats_dict=stats_attr,
                mood_dict=mood_attr,
                training_dict=training_attr,
            )

            cards.append(card)
