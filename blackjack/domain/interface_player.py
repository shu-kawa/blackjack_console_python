from abc import ABC, abstractmethod

class IPlayer(ABC):
    @abstractmethod
    def add_card(self, card):
        pass

    @abstractmethod
    def clear_hand(self):
        pass

    @abstractmethod
    def hand_value(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def hand(self):
        pass

    @property
    @abstractmethod
    def money(self):
        pass

    @property
    @abstractmethod
    def bet(self):
        pass

    @bet.setter
    @abstractmethod
    def bet(self, value):
        pass
