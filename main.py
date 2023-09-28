from LLLL_cards import LLLLCharacter, LLLLCard

def main():
    # Create a character
    character = LLLLCharacter(name="John")
    print(f"Character name: {character.name}")

    # Create a card metadata
    card_metadata = LLLLCard.LLLLCardMetadata(name="Card 1", character=character)
    print(f"Card metadata: {card_metadata.name}, Character: {card_metadata.character.name}")

    # Create card stats
    card_stats = LLLLCard.LLLLStats(smile=80, pure=90, cool=85, mental=75, bp=200)
    print(f"Card stats: Smile: {card_stats.smile}, Pure: {card_stats.pure}, Cool: {card_stats.cool}, Mental: {card_stats.mental}, BP: {card_stats.bp}")

    # Create a card
    card = LLLLCard(_id=1, metadata=card_metadata, stats=card_stats)
    print(f"Card ID: {card.id}")

    # Update card ID
    card.id = 2
    print(f"Updated Card ID: {card.id}")
    
if __name__ == "__main__":
    main()