from blackjack.domain.interface_player import IPlayer

class Player(IPlayer):
    def __init__(self, name, money=100):
        self._name = name
        self._hand = []
        self._money = money
        self._bet = 0

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        return self._hand

    @property
    def money(self):
        return self._money

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        self._bet = value

    def add_card(self, card):
        self._hand.append(card)

    def clear_hand(self):
        self._hand = []

    def hand_value(self):
        value = sum(card.value() for card in self._hand)
        ace_count = sum(1 for card in self._hand if card.rank == 'A')
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value
