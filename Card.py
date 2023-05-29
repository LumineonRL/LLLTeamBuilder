import json


class Card:
    def __init__(
        self,
        name: str,
        character: str,
        rarity: str,
        smile: int,
        pure: int,
        cool: int,
        mental: int,
        bp: int,
        type: str,
        mood: str,
        level: int = 1,
        uncaps: int = 1,
        appeal_level: int = 1,
        skill_level: int = 1,
    ) -> None:
        self.name = name
        self.character = character
        self.rarity = rarity
        self.stats = self.Stats(smile, pure, cool, mental, bp)
        self.mood = self.Mood(type, mood)
        self.training = self.Training(level, uncaps, appeal_level, skill_level)

    class Stats:
        def __init__(
            self, smile: int, pure: int, cool: int, mental: int, bp: int
        ) -> None:
            self.smile = smile
            self.pure = pure
            self.cool = cool
            self.mental = mental
            self.bp = bp

    class Mood:
        def __init__(self, type: str, mood: str) -> None:
            self.type = type
            self.mood = mood

    class Training:
        def __init__(self, level, uncaps, appeal_level, skill_level):
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

        with open(filename, "w") as f_out:
            json.dump(data, f_out, default=lambda x: x.__dict__)

    def import_cards(self, filename: str) -> None:
        with open(filename, "r") as f_in:
            file = json.load(f_in)

        cards = []

        for data in file:
            stats = data["stats"]
            mood = data["mood"]
            training = data["training"]
            card = Card(
                data["name"],
                data["character"],
                data["rarity"],
                stats["smile"],
                stats["pure"],
                stats["cool"],
                stats["mental"],
                stats["bp"],
                mood["type"],
                mood["mood"],
                training["level"],
                training["uncaps"],
                training["appeal_level"],
                training["skill_level"],
            )
            cards.append(card)

        self.cards = cards
