class Team:
    def __init__(self, cards: list[Card]) -> None:
        if len(cards) != 9 :
            raise ValueError("A team must have exactly 9 cards")
        else : 
            self.cards = cards
    def total_smile(self)->int :
      return sum(card.stats.smile for card in self.cards)