import unittest
import sys
import os

# Add the directory containing LLLL_cards.py to the system path
package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(package_dir)

from LLLL_cards import LLLLCard, LLLLDeck

class LLLLCardTests(unittest.TestCase):
    def setUp(self):
        self.card = LLLLCard(1, "Card Name", "Character Name", "Rare", 100, 80, 90, 120, 100)

    def test_id(self):
        self.assertEqual(self.card.id, 1)

    def test_name(self):
        self.assertEqual(self.card.name, "Card Name")

    def test_character(self):
        self.assertEqual(self.card.character, "Character Name")

    def test_rarity(self):
        self.assertEqual(self.card.rarity, "Rare")

    def test_smile(self):
        self.assertEqual(self.card.smile, 100)

    def test_pure(self):
        self.assertEqual(self.card.pure, 80)

    def test_cool(self):
        self.assertEqual(self.card.cool, 90)

    def test_mental(self):
        self.assertEqual(self.card.mental, 120)

    def test_bp(self):
        self.assertEqual(self.card.bp, 100)
        
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