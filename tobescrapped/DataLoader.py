from abc import ABC, abstractmethod
from typing import List, Dict, Any
import json
from Card import Card


class JsonDataLoader(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read_json(self) -> dict:
        raise NotImplementedError("read_json() method not implemented.")

    @abstractmethod
    def write_json(self, data: dict):
        raise NotImplementedError("write_json() method not implemented.")


class JsonCardDataLoader(JsonDataLoader):
    def read_json(self) -> List[Card]:
        with open(self.file_path, "r", encoding="utf-8") as file:
            raw_card_list = json.load(file)
            card_object_list = self._convert_card_dict_to_card_object(raw_card_list)

            return card_object_list

    def write_json(self, data: List[Card]):
        cards = [self._convert_card_object_to_card_dict(card) for card in data]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(cards, file, indent=4, ensure_ascii=False)
            
    def _convert_card_object_to_card_dict(self, card: Card) -> dict:
        return {
            "id": card.id,
            "name": card.name,
            "character": card.character,
            "rarity": card.rarity,
            "stats": {
                "smile": card.smile,
                "pure": card.pure,
                "cool": card.cool,
                "mental": card.mental,
                "bp": card.bp,
            },
            "mood": {
                "style_type": card.style_type,
                "mood_type": card.mood_type
            },
            "training": {
                "level": card.level,
                "uncaps": card.uncaps,
                "appeal_level": card.appeal_level,
                "skill_level": card.skill_level,
            },
        }
            
    def _convert_card_dict_to_card_object(self, raw_card_data: Dict[str, Any]) -> List[Card]:
        cards = [
            Card(
                id=d['id'],
                name=d['name'],
                character=d['character'],
                rarity=d['rarity'],
                smile=d["stats"]["smile"],
                pure=d["stats"]["pure"],
                cool=d["stats"]["cool"],
                mental=d["stats"]["mental"],
                bp=d["stats"]["bp"],
                style_type=d["mood"]["style_type"],
                mood_type=d["mood"]["mood_type"]
                )
                for d in raw_card_data
            ]

        return cards
            
if __name__ == "__main__":
    INITIAL_CARDS = [
        Card(
            id=1,
            name="オーロラスカイ",
            character="日野下花帆",
            rarity="R",
            smile=1225,
            pure=1525,
            cool=925,
            mental=123,
            bp=100,
            style_type="パフォーマー",
            mood_type="ハッピー",
        ),
        Card(
            id=2,
            name="オーロラスカイ",
            character="林野さやか",
            rarity="R",
            smile=1225,
            pure=1025,
            cool=1425,
            mental=123,
            bp=100,
            style_type="ムードメーカー",
            mood_type="メロウ",
        ),
        Card(
            id=3,
            name="オーロラスカイ",
            character="大沢瑠璃乃",
            rarity="R",
            smile=1525,
            pure=1125,
            cool=725,
            mental=153,
            bp=100,
            style_type="トリックスター",
            mood_type="ニュートラル",
        ),
        Card(
            id=4,
            name="オーロラスカイ",
            character="乙宗梢",
            rarity="R",
            smile=1525,
            pure=1225,
            cool=925,
            mental=123,
            bp=100,
            style_type="チアリーダー",
            mood_type="ハッピー",
        ),
        Card(
            id=5,
            name="オーロラスカイ",
            character="夕霧綴理",
            rarity="R",
            smile=1225,
            pure=925,
            cool=1525,
            mental=123,
            bp=100,
            style_type="ムードメーカー",
            mood_type="メロウ",
        ),
        Card(
            id=6,
            name="オーロラスカイ",
            character="藤島慈",
            rarity="R",
            smile=1125,
            pure=1525,
            cool=925,
            mental=133,
            bp=100,
            style_type="チアリーダー",
            mood_type="ニュートラル",
        ),
    ]
    
    print(INITIAL_CARDS[5].name)
    
    card_loader = JsonCardDataLoader("Data/initial_cards.json")
    card_loader.write_json(INITIAL_CARDS)
    
    #load_test = card_loader.read_json()
    
    #print([card.smile for card in load_test])
    
    



