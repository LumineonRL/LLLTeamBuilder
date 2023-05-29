from Card import Card, MyCards
import json

if __name__ == "__main__":
    my_cards_collection = MyCards()

    try:
        my_card1 = Card("オーロラスカイ", "日野下花帆", "R", 1225, 1525, 925, 123, 100, "パフォーマー", "ハッピー")
    except Exception as e:
        print(e)
        
    my_cards_collection.add_card(my_card1)
    
    print(my_cards_collection.get_card_by_index(0).name)
    my_cards_collection.export_cards("mycards.json")
    
    my_cards_imported = MyCards()
    my_cards_import = my_cards_imported.import_cards("mycards.json")
    
    
    print(my_cards_imported.get_card_by_index(0).name)
    
    
    # Get all the names of cards in our collection and print them out.
    # print(my_cards_collection.get_card_names())
    # print(my_cards_collection.get_card_by_index(0).training.level)
    # my_cards_collection.get_card_by_index(0).training.level = 100
    # print(my_cards_collection.get_card_by_index(0).training.level)
