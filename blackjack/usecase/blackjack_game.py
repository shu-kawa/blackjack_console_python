from blackjack.domain.card import Deck
from blackjack.domain.player import Player
from blackjack.interface.console import ConsoleOutput

class BlackjackGame:

    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.dealer = Player("Dealer")
        self.output = ConsoleOutput()

    def initial_deal(self):
        for player in self.players:
            player.clear_hand()
            player.add_card(self.deck.draw())
            player.add_card(self.deck.draw())
        self.dealer.clear_hand()
        self.dealer.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

    def player_turn(self, player):
        self.output.write(f"あなたの手札: {[str(card) for card in player.hand]} (合計: {player.hand_value()})")
        self.output.write(f"ディーラーの見えているカード: {self.dealer.hand[0]}")

        while True:
            if player.hand_value() == 21:
                self.output.write("ブラックジャック！")
                break
            action = input("ヒットしますか？スタンドしますか？ (h/s): ").lower()
            if action == 'h':
                card = self.deck.draw()
                player.add_card(card)
                self.output.write(f"カード: {card} を引きました。あなたの手札: {[str(c) for c in player.hand]} (合計: {player.hand_value()})")
                if player.hand_value() > 21:
                    self.output.write("バーストしました。あなたの負けです。")
                    return False
            elif action == 's':
                break
            else:
                self.output.write("h か s を入力してください。")
        return True

    def dealer_turn(self):
        print(f"ディーラーの手札: {[str(card) for card in self.dealer.hand]} (合計: {self.dealer.hand_value()})")
        while self.dealer.hand_value() < 17:
            card = self.deck.draw()
            self.dealer.add_card(card)
            print(f"ディーラーはカード: {card} を引きました。手札: {[str(c) for c in self.dealer.hand]} (合計: {self.dealer.hand_value()})")
        if self.dealer.hand_value() > 21:
            print("ディーラーがバーストしました。あなたの勝ちです！")
            return False
        return True

    def judge(self, player):
        player_total = player.hand_value()
        dealer_total = self.dealer.hand_value()
        print(f"あなたの合計: {player_total}、ディーラーの合計: {dealer_total}")
        if player_total > dealer_total:
            print("あなたの勝ちです！")
        elif player_total < dealer_total:
            print("あなたの負けです。")
        else:
            print("引き分けです。")
