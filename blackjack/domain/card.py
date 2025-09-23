import random

class Card:
    SUITS = ['♠', '♥', '♦', '♣']
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    VALUES = {str(n): n for n in range(2, 11)}
    VALUES.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        return Card.VALUES[str(self.rank)]

    def __str__(self):
        return f"{self.suit}{self.rank}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None
