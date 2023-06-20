from collections import Counter
from Card import Card, MyCards
from Deck import Deck

if __name__ == "__main__":
    my_cards_collection = MyCards()

    try:
        card01 = Card(
            "オーロラスカイ",
            "日野下花帆",
            "R",
            {"smile": 1225, "pure": 1525, "cool": 925, "mental": 123, "bp": 100},
            {"style_type": "パフォーマー", "mood": "ハッピー"},
            {},
        )
        card02 = Card(
            "Rose Garden",
            "林野さやか",
            "UR",
            {"smile": 1430, "pure": 2480, "cool": 2280, "mental": 113, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "メロウ"},
            {},
        )

        card03 = Card(
            "オーロラスカイ",
            "林野さやか",
            "R",
            {"smile": 1225, "pure": 1025, "cool": 1425, "mental": 123, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "メロウ"},
            {},
        )

        card04 = Card(
            "オーロラスカイ",
            "大沢瑠璃乃",
            "R",
            {"smile": 1525, "pure": 1125, "cool": 725, "mental": 153, "bp": 100},
            {"style_type": "トリックスター", "mood": "ニュートラル"},
            {},
        )

        card05 = Card(
            "チェリーピクニック",
            "乙宗梢",
            "UR",
            {"smile": 2030, "pure": 2730, "cool": 930, "mental": 163, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "ハッピー"},
            {},
        )

        card06 = Card(
            "水彩世界",
            "乙宗梢",
            "SR",
            {"smile": 1930, "pure": 2130, "cool": 1130, "mental": 173, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "ハッピー"},
            {},
        )

        card07 = Card(
            "オーロラスカイ",
            "乙宗梢",
            "R",
            {"smile": 1525, "pure": 1225, "cool": 925, "mental": 123, "bp": 100},
            {"style_type": "チアリーダー", "mood": "ハッピー"},
            {},
        )

        card08 = Card(
            "Rose Garden",
            "夕霧綴理",
            "SR",
            {"smile": 1230, "pure": 2130, "cool": 2030, "mental": 193, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "メロウ"},
            {},
        )

        card09 = Card(
            "AWOKE",
            "夕霧綴理",
            "SR",
            {"smile": 2130, "pure": 1030, "cool": 1930, "mental": 183, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "メロウ"},
            {},
        )

        card10 = Card(
            "オーロラスカイ",
            "夕霧綴理",
            "R",
            {"smile": 1225, "pure": 925, "cool": 1525, "mental": 123, "bp": 100},
            {"style_type": "ムードメーカー", "mood": "メロウ"},
            {},
        )

        card11 = Card(
            "オーロラスカイ",
            "藤島慈",
            "R",
            {"smile": 1125, "pure": 1525, "cool": 925, "mental": 133, "bp": 100},
            {"style_type": "チアリーダー", "mood": "ニュートラル"},
            {},
        )
    except ValueError as e:
        print(e)

    my_cards_collection.add_card(card01)
    my_cards_collection.add_card(card02)
    my_cards_collection.add_card(card03)
    my_cards_collection.add_card(card04)
    my_cards_collection.add_card(card05)
    my_cards_collection.add_card(card06)
    my_cards_collection.add_card(card07)
    my_cards_collection.add_card(card08)
    my_cards_collection.add_card(card09)
    my_cards_collection.add_card(card10)
    my_cards_collection.add_card(card11)

    # print(my_cards_collection.get_card_by_index(0).name)
    my_cards_collection.export_cards("mycards.json")

    my_deck = Deck()
    my_deck.add_card(card02)
    my_deck.add_card(card02)
    my_deck.remove_card(card02)
    my_deck.remove_card(card02)
    my_deck.remove_card(card03)

    character_counts = []
    for card in my_deck.cards:
        character_counts.append(card.character)

    counts = Counter(character_counts)

    print(counts)

    # Get all the names of cards in our collection and print them out.
    # print(my_cards_collection.get_card_names())
    # print(my_cards_collection.get_card_by_index(0).training.level)
    # my_cards_collection.get_card_by_index(0).training.level = 100
    # print(my_cards_collection.get_card_by_index(0).training.level)
