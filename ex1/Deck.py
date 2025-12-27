#!/usr/bin/env python3
from ex0.Card import Card
from collections import defaultdict


class Deck:
    """
    デッキ管理クラス
    """

    def __init__(self):
        """
        空デッキ作成
        """

        self.deck = []

    def add_card(self, card: Card) -> None:
        """
        デッキにカードを追加する
        """

        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        デッキからカードを削除する
        """


    def shuffle(self) -> None:
        """
        カードをシャッフルする
        """

    def draw_card(self) -> Card:
        """
        カードをドローする
        """

    def get_deck_stats(self) -> dict:
        """
        デッキの情報を取得する
        """

        result = defaultdict(int)
        result = self.deck.copy()
        result['avg_cost'] =
        return self.deck

if __name__ == "__main__":
    pass
