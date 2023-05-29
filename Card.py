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
    ) -> None:
        self.name = name
        self.character = character
        self.rarity = rarity
        self.stats = self.Stats(smile, pure, cool, mental, bp)
        self.mood = self.Mood(type, mood)
        self.training = self.Training()

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
        def __init__(
            self,
            level: int = 1,
            uncaps: int = 1,
            appeal_level: int = 1,
            skill_level: int = 1,
        ):
            self.level = level
            self.uncaps = uncaps
            self.appeal_level = appeal_level
            self.skill_level = skill_level
        

            


class MyCards:
    def __init__(self):
        self.cards = []

    def add_card(
        self,
        name: str,
        character: str,
        rarity: str,
        s: int,
        p: int,
        c: int,
        m: int,
        b: int,
        mood_type: str,
        mood_mood: str,
    ) -> None:
        card = Card(name, character, rarity, s, p, c, m, b, mood_type, mood_mood)
        self.cards.append(card)

    def get_card_by_index(self, index) -> Card:
        return self.cards[index]
