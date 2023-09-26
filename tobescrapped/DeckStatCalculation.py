from Deck import Deck


class DeckStatCalculations:
    def __init__(self, deck: Deck):
        """
        Initializes a new object with a given input deck.

        Args:
            deck (Deck): The input deck for which stats will be calculated.
        """
        self.deck = deck

    def calculate_total_stat(self, stat_name: str) -> int:
        """
        Calculates the sum total of a given 'stat_name' attribute across all Cards in this object's input Deck.

        Args:
            stat_name (str): The name of the stat to sum up. Must be a valid key in each card's 'stats' dict.

        Returns:
            int: The sum total of the specified stat.
        """
        return sum(card.stats[stat_name] for card in self.deck.cards)