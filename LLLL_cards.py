from mobile_game_abstracts import Card
from dataclasses import dataclass

@dataclass
class LLLLCard(Card):
    name: str
    character: str
    rarity: str
    smile: int
    pure: int
    cool: int
    mental: int
    bp: int
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, new_id: int):
        assert isinstance(new_id, int) and new_id > 0,\
            "Card ID must be a positive integer."
        self._id = new_id