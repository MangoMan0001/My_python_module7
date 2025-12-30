#!/usr/bin/env python3
from abc import ABC, abstractmethod
from ex0.Card import Card


class GameStrategy(ABC):
    """
    ストラテジー基礎クラス
    """

    @abstractmethod
    def execute_turn(self, hand: list[Card], battlefield: list) -> dict:
        """
        ターン実行
        """

        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        戦略名の取得
        """

        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        ターゲットの優先順位づけ
        """

        pass


if __name__ == "__main__":
    pass
