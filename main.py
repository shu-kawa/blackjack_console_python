
from blackjack.usecase.blackjack_game import BlackjackGame

def main():
    print("ブラックジャックへようこそ！")
    name = input("あなたの名前を入力してください: ")
    print(f"こんにちは、{name}さん。ゲームを開始します。\n")

    # 今は1人プレイ想定。複数人対応時はリストで渡す
    game = BlackjackGame([name])
    game.initial_deal()

    player = game.players[0]
    # プレイヤーのターン
    if not game.player_turn(player):
        return
    # ディーラーのターン
    if not game.dealer_turn():
        return
    # 勝敗判定
    game.judge(player)

if __name__ == "__main__":
    main()
