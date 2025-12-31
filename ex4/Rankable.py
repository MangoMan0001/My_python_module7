#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    ランクシステム抽象クラス
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        ランク計測
        """

        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        勝利数更新
        """

        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        敗北数更新
        """

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        ランク情報取得
        """

        pass


if __name__ == "__main__":
    pass
