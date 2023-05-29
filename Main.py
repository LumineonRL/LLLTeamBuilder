from Card import MyCards

if __name__ == "__main__":
    my_cards_collection = MyCards()

    try:
        my_cards_collection.add_card(
            "オーロラスカイ", "日野下花帆", "R", 1225, 1525, 925, 123, 100, "パフォーマー", "ハッピー"
        )
    except Exception as e:
        print(e)
    # Get all the names of cards in our collection and print them out.
    # print(my_cards_collection.get_card_names())
    print(my_cards_collection.get_card_by_index(0).training.level)
    my_cards_collection.get_card_by_index(0).training.level = 100
    print(my_cards_collection.get_card_by_index(0).training.level)
