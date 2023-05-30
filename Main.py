from Card import Card, MyCards
from Deck import Deck
import json
from collections import Counter

if __name__ == "__main__":
    my_cards_collection = MyCards()

    try:
        card01 = Card("オーロラスカイ", "日野下花帆", "R", 1225, 1525, 925, 123, 100, "パフォーマー", "ハッピー")
        card02 = Card("Rose Garden", "林野さやか", "UR", 1430, 2480, 2280, 113, 100, "ムードメーカー", "メロウ")
        card03 = Card("オーロラスカイ", "林野さやか", "R", 1225, 1025, 1425, 123, 100, "ムードメーカー", "メロウ")
        card04 = Card("オーロラスカイ", "大沢瑠璃乃", "R", 1525, 1125, 725, 153, 100, "トリックスター", "ニュートラル")
        card05 = Card("チェリーピクニック", "乙宗梢", "UR", 2030, 2730, 930, 163, 100, "ムードメーカー", "ハッピー")
        card06 = Card("水彩世界", "乙宗梢", "SR", 1930, 2130, 1130, 173, 100, "ムードメーカー", "ハッピー")
        card07 = Card("オーロラスカイ", "乙宗梢", "R", 1525, 1225, 925, 123, 100, "チアリーダー", "ハッピー")
        card08 = Card("Rose Garden", "夕霧綴理", "SR", 1230, 2130, 2030, 193, 100, "ムードメーカー", "メロウ")
        card09 = Card("AWOKE", "夕霧綴理", "SR", 2130, 1030, 1930, 183, 100, "ムードメーカー", "メロウ")
        card10 = Card("オーロラスカイ", "夕霧綴理", "R", 1225, 925, 1525, 123, 100, "ムードメーカー", "メロウ")
        card11 = Card("オーロラスカイ", "藤島慈", "R", 1125, 1525, 925, 133, 100, "チアリーダー", "ニュートラル")
    except Exception as e:
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

    #print(my_cards_collection.get_card_by_index(0).name)
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
