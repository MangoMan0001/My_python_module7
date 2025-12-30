#!/usr/bin/env python3
from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory (ABC):
    """
    カード工場
    """

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        """
        クリーチャー作成
        """

        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        """
        魔法作成
        """

        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        """
        アーティファクト作成
        """

        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        テーマ付きデッキの作成
        """

        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        サポートされているタイプを取得
        """

        pass


if __name__ == "__main__":
    pass
