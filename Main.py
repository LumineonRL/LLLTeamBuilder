from Card import MyCards

if __name__ == "__main__":
    my_cards_collection = MyCards()
    my_cards_collection.add_card(
        "オーロラスカイ", "日野下花帆", "R", 1225, 1525, 925, 123, 100, "パフォーマー", "ハッピー"
    )
    # Get all the names of cards in our collection and print them out.
    # print(my_cards_collection.get_card_names())
    print(my_cards_collection.get_card_by_index(0).stats.mental)
    
