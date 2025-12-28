#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Magical(ABC):
    """
    魔法インターフェイス
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        魔法詠唱抽象メソッド
        """

        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        持続魔法抽象メソッド
        """

        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """
        魔法情報取得抽象メソッド
        """

        pass


if __name__ == "__main__":
    pass
