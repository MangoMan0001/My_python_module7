#!/usr/bin/env python3
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    ランクとトーナメント機能を持つカード
    """

    def __init__(self, name: str, cost: int, rarity: str, attack: int):
        """
        初期化
        """

        super().__init__(name, cost, rarity)
        self.wins = 0
        self.losees = 0
        self.rating = 1000
        self.info['attack'] = attack

    def play(self, game_state: dict) -> dict:
        """
        プレイしたカードの情報が出力される
        """

        return {'card_played': self.info['name'],
                'mana_used': self.info['cost']}

    def attack(self, target) -> dict:
        """
        攻撃メソッド
        """

        return {'attacker': self.info['name'],
                'target': target,
                'damage': self.info['attack']}

    def calculate_rating(self) -> int:
        """
        レートを返す
        """

        return self.rating

    def get_tournament_stats(self) -> dict:
        """
        トーナメント情報を返す
        """

        return {self.info['name']: f"(ID: {self.info['name']}):",
                '- Interfaces': '[Card, Combatable, Rankable]',
                '- Rating': self.calculate_rating(),
                '- Record': f'{self.wins}-{self.losees}'}

    def get_rank_info(self) -> dict:
        """
        ランク情報取得
        """

        return {self.info['name']:
                f"Rating: {self.rating} ({self.wins}-{self.losees})"}

    def update_wins(self, wins: int) -> None:
        """
        勝利更新
        """

        self.wins += wins
        self.rating += wins * 10

    def update_losses(self, losses: int) -> None:
        """
        敗北更新
        """

        self.losees += losses
        self.rating -= losses * 10

    def defend(self, incoming_damage: int) -> dict:
        """TournamentCardは防御計算を行わないため、そのまま返す"""
        return {}

    def get_combat_stats(self) -> dict:
        """TournamentCardでは詳細は不要"""
        return {}


if __name__ == "__main__":
    pass
