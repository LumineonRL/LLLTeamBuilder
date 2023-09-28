from mobile_game_abstracts import Character, Card, Deck
from dataclasses import dataclass

@dataclass
class LLLLCharacter(Character):
    name: str

@dataclass
class LLLLCard(Card):
    @dataclass
    class LLLLCardMetadata(Card.CardMetadata):
        name: str
        character: Character   
 
    @dataclass
    class LLLLStats(Card.Stat):
        smile: int
        pure: int
        cool: int
        mental: int
        bp: int
    
    _id: int
    metadata: LLLLCardMetadata
    stats: LLLLStats
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, new_id: int) -> None:
        assert isinstance(new_id, int) and new_id > 0,\
            "Card ID must be a positive integer."
        self._id = new_id

@dataclass(order=True, frozen=False)
class LLLLDeck(Deck):
    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        
    def remove_card(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)