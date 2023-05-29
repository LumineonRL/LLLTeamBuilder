class Stats:
    def __init__(self, smile: int, pure: int, cool: int, mental: int, bp: int) -> None:
        self.smile = smile
        self.pure = pure
        self.cool = cool
        self.mental = mental
        self.bp = bp


class Mood:
    def __init__(self, type: str, mood: str) -> None:
        self.type = type
        self.mood = mood


class Card:
    def __init__(
        self, name: str, character: str, rarity: str, stats: Stats, mood: Mood
    ) -> None:
        self.name = name
        self.character = character
        self.rarity = rarity
        self.stats = stats
        self.mood = mood


class MyCards:
    def __init__(self):
        self.cards = []

    def add_card(
        self,
        name: str,
        charcater: str,
        rarity: str,
        s: int,
        p: int,
        c: int,
        m: int,
        b: int,
        mood_type: str,
        mood_mood: str,
    ) -> None:
        card_stats = Stats(s, p, c, m, b)
        card_mood = Mood(mood_type, mood_mood)
        card = Card(name, charcater, rarity, card_stats, card_mood)
        self.cards.append(card)

    def get_card_by_index(self, index) -> Card:
        return self.cards[index]


if __name__ == "__main__":
    my_cards_collection = MyCards()
    my_cards_collection.add_card(
        "オーロラスカイ", "日野下花帆", "R", 1225, 1525, 925, 123, 100, "パフォーマー", "ハッピー"
    )
    # Get all the names of cards in our collection and print them out.
    # print(my_cards_collection.get_card_names())
    print(my_cards_collection.get_card_by_index(0).stats.mental)
