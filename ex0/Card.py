#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Card(ABC):
    """
    カードテンプレート
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        カードの初期値
        """

        self.info = {'name': name,
                     'cost': cost,
                     'rarity': rarity}

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        プレイしたカードの情報が出力される
        """

        pass

    def get_card_info(self) -> dict:
        """
        カードの情報を返す
        返す情報: name, cost, rarity, type, attack
        """

        return self.info

    def is_playable(self, available_mana: int) -> bool:
        """
        プレイできるか（カードを使えるか）を検証
        召喚にマナが足りるかどうかでbool値を返す
        """

        if self.info['cost'] <= available_mana:
            return True
        return False


if __name__ == "__main__":
    pass
