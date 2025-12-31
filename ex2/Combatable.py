#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    戦闘インターフェース
    """

    @abstractmethod
    def attack(self, target) -> dict:
        """
        攻撃抽象メソッド
        """

        pass

    def defend(self, incoming_damage: int) -> dict:
        """
        防御抽象メソッド
        """

        pass

    def get_combat_stats(self) -> dict:
        """
        戦闘状況を返す
        """

        pass


if __name__ == "__main__":
    pass
