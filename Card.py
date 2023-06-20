import json


class Card:
    def __init__(
        self,
        name: str,
        character: str,
        rarity: str,
        stats_dict: dict,
        mood_dict: dict,
        training_dict: dict,
    ) -> None:
        self.name = name
        self.character = character
        self.rarity = rarity
        self.stats = self.Stats(**stats_dict)
        self.mood = self.Mood(**mood_dict)
        self.training = self.Training(**training_dict)

    class Stats:
        def __init__(
            self,
            smile: int = 0,
            pure: int = 0,
            cool: int = 0,
            mental: int = 0,
            bp: int = 0,
        ) -> None:
            if not all(
                isinstance(x, int) and x >= 0 for x in [smile, pure, cool, mental, bp]
            ):
                raise ValueError("Stat parameters should be non-negative integers")

            self.smile = smile
            self.pure = pure
            self.cool = cool
            self.mental = mental
            self.bp = bp

    class Mood:
        def __init__(self, style_type: str = "パフォーマー", mood: str = "ハッピー") -> None:
            self.style_type = style_type
            self.mood = mood

    class Training:
        def __init__(
            self,
            level: int = 1,
            uncaps: int = 0,
            appeal_level: int = 1,
            skill_level: int = 1,
        ) -> None:
            # TODO - Break into seperate methods for each parameter.
            # Will probably make skill into a separate class once I understand this better,
            # so I'm holding off for now.
            if not all(
                isinstance(x, int) and x >= 1
                for x in [level, appeal_level, skill_level]
            ):
                raise ValueError("Stat parameters should be non-negative integers")

            if not all(isinstance(x, int) and x >= 0 and x <= 5 for x in [uncaps]):
                raise ValueError("Stat parameters should be non-negative integers")

            self.level = level
            self.uncaps = uncaps
            self.appeal_level = appeal_level
            self.skill_level = skill_level


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
