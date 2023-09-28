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
        
class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.character = LLLLCharacter(name="John")
        self.card1 = LLLLCard(
            _id=1,
            metadata=LLLLCard.LLLLCardMetadata(name="Card1", character=self.character),
            stats=LLLLCard.LLLLStats(smile=10, pure=20, cool=30, mental=40, bp=50)
        )
        self.card2 = LLLLCard(
            _id=2,
            metadata=LLLLCard.LLLLCardMetadata(name="Card2", character=self.character),
            stats=LLLLCard.LLLLStats(smile=15, pure=25, cool=35, mental=45, bp=55)
        )
        self.deck = LLLLDeck(cards=[self.card1, self.card2])

    def test_add_card(self):
        card3 = LLLLCard(
            _id=3,
            metadata=LLLLCard.LLLLCardMetadata(name="Card3", character=self.character),
            stats=LLLLCard.LLLLStats(smile=5, pure=15, cool=25, mental=35, bp=45)
        )
        self.deck.add_card(card3)
        self.assertIn(card3, self.deck.cards)

    def test_remove_card(self):
        self.deck.remove_card(self.card1)
        self.assertNotIn(self.card1, self.deck.cards)
        
    def test_add_duplicate_card(self):
        card4 = LLLLCard(
            _id=2,
            metadata=LLLLCard.LLLLCardMetadata(name="Card4", character=self.character),
            stats=LLLLCard.LLLLStats(smile=5, pure=15, cool=25, mental=35, bp=45)
        )
        with self.assertRaises(ValueError):
            self.deck.add_card(card4)
        
       
if __name__ == '__main__':
    unittest.main()