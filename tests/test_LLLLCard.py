import unittest
import sys
import os

# Add the directory containing LLLL_cards.py to the system path
package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(package_dir)

from LLLL_cards import LLLLCharacter, LLLLCard, LLLLDeck

class TestCharacter(unittest.TestCase):
    def test_character_name(self):
        character = LLLLCharacter(name="John")
        self.assertEqual(character.name, "John")

# WIP
class TestCard(unittest.TestCase):
    def setUp(self):
        self.character = LLLLCharacter(name="John")
        self.metadata = LLLLCard.LLLLCardMetadata(name="Card 1", character=self.character)
        self.stats = LLLLCard.LLLLStats(smile=80, pure=90, cool=85, mental=75, bp=200)
        self.card = LLLLCard(_id=1, metadata=self.metadata, stats=self.stats)

    def test_card_id(self):
        self.assertEqual(self.card.id, 1)

    def test_card_metadata(self):
        self.assertEqual(self.card.metadata.name, "Card 1")
        self.assertEqual(self.card.metadata.character.name, "John")

    def test_card_stats(self):
        self.assertEqual(self.card.stats.smile, 80)
        self.assertEqual(self.card.stats.pure, 90)
        self.assertEqual(self.card.stats.cool, 85)
        self.assertEqual(self.card.stats.mental, 75)
        self.assertEqual(self.card.stats.bp, 200)

    def test_set_card_id(self):
        self.card.id = 2
        self.assertEqual(self.card.id, 2)

    def test_set_card_id_invalid(self):
        with self.assertRaises(AssertionError):
            self.card.id = -1
        
class DeckTests(unittest.TestCase):
    def test_add_card(self):
        deck = LLLLDeck([])
        card1 = LLLLCard(1, "Card Name", "Character Name", "Rare", 100, 80, 90, 120, 100)
        card2 = LLLLCard(2, "Card Name", "Character Name", "Rare", 100, 80, 90, 120, 100)

        deck.add_card(card1)
        deck.add_card(card2)

        self.assertEqual(deck.cards, [card1, card2])

    def test_remove_card(self):
        card1 = LLLLCard(1, "Card Name", "Character Name", "Rare", 100, 80, 90, 120, 100)
        card2 = LLLLCard(2, "Card Name", "Character Name", "Rare", 100, 80, 90, 120, 100)
        card3 = LLLLCard(3, "Card Name", "Character Name", "Rare", 100, 80, 90, 120, 100)
        deck = LLLLDeck([card1, card2, card3])

        deck.remove_card(card2)

        self.assertEqual(deck.cards, [card1, card3])
       
if __name__ == '__main__':
    unittest.main()