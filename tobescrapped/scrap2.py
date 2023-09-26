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


def create_stats_instance(stats_dict):
    return Card.Stats(**stats_dict)


def set_stats_attribute(instance, stats_instance):
    setattr(instance, "stats", stats_instance)


"""Creating card instance"""
card_data = {
    "name": "Shizuku Osaka",
    "character": "Osaka Shizuku",
    "rarity": "SR",
    "stats_dict": {
        "smile": 3000,
        "pure": 2000,
        "cool": 1000,
        "mental": 500,
        "bp": 15000,
    },
    "mood_dict": {"style_type": "パフォーマー", "mood": "ハッピー"},
    "training_dict": {"level": 5, "uncaps": 5, "appeal_level": 5, "skill_level": 5},
}
card_instance = Card(**card_data)

"""Creating stats instance"""
stats_data = {"smile": 3000, "pure": 2000, "cool": 1000, "mental": 500, "bp": 15000}

stats_instance = create_stats_instance(stats_data)
print(stats_instance)


"""Assigning the created stats instance to attribute of Card class"""
set_stats_attribute(card_instance, stats_instance)

"""Printing all attributes of card instance"""

print(f"Name: {card_instance.name}")
print(f"Character: {card_instance.character}")
print(f"Rarity: {card_instance.rarity}")
print(
    f"\nStats:\nSmile - {card_instance.Stats.smile}\nPure - {card_instance.Stats.pure}\nCool -{ card_instance.Stats.cool}\nMental- { card_instance.Stats.mental}\nBP-   { card_instance.Stats.bp}"
)

print(card_instance.Training.level)

# Right now it seems to just be using the defaults for everything. Edit to make sure it sets correctly.