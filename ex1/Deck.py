#!/usr/bin/env python3
from ex0.Card import Card
from collections import Counter
import random
import math


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

        try:
            self.deck.remove(card_name)
            return True
        except Exception:
            return False

    def shuffle(self) -> None:
        """
        カードをシャッフルする
        """

        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        """
        カードをドローする
        """

        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        """
        デッキの情報を取得する
        """

        counts = Counter(card.info['type'] for card in self.deck)
        avg = sum(card.info['cost'] for card in self.deck) / len(self.deck)
        counts['avg_cost'] = math.ceil(avg)
        result = {'total_cards': len(self.deck)} | dict(counts)
        return result


if __name__ == "__main__":
    pass
