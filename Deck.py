from Card import Card
from typing import List
from collections import Counter

class Deck:    
    def __init__(self) -> None:
        INITIAL_CARDS = [Card("オーロラスカイ", "日野下花帆", "R", 1225, 1525, 925, 123, 100, "パフォーマー", "ハッピー"),
                Card("オーロラスカイ", "林野さやか", "R", 1225, 1025, 1425, 123, 100, "ムードメーカー", "メロウ"),
                Card("オーロラスカイ", "大沢瑠璃乃", "R", 1525, 1125, 725, 153, 100, "トリックスター", "ニュートラル"),
                Card("オーロラスカイ", "乙宗梢", "R", 1525, 1225, 925, 123, 100, "チアリーダー", "ハッピー"),
                Card("オーロラスカイ", "夕霧綴理", "R", 1225, 925, 1525, 123, 100, "ムードメーカー", "メロウ"),
                Card("オーロラスカイ", "藤島慈", "R", 1125, 1525, 925, 133, 100, "チアリーダー", "ニュートラル")]
        
        self.cards = []
        for card in INITIAL_CARDS:
            self.cards.append(card)
            
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
                raise Exception(f"{char} not found. You may have tried to delete all instances of a character from your deck.")
            
    def _check_max_chars(self) -> None:
        for char in self._character_counts.keys():
            if self._character_counts[char] > 3:
                raise Exception(f"More than 3 cards for {char} found. You may have tried to add a 4th card of a character to your deck..")
        
                
            