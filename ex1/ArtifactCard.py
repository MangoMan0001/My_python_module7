#!/usr/bin/env python3
from ex0.Card import Card


class ArtifactCard(Card):
    """
    アーティファクトカードクラス
    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        """
        アーティファクトカードの初期化
        """

        super().__init__(name, cost, rarity)
        self.info['durability'] = durability
        self.info['effect'] = effect
        self.info['type'] = "artifact"

    def play(self, game_state: dict) -> dict:
        """
        アーティファクト効果処理
        """

        return {'card_played': self.info['name'],
                'mana_used': self.info['cost'],
                'effect': 'Permanent: +1 mana per turn'}

    def activate_ability(self) -> dict:
        """
        持続効果処理
        """

        return {}


if __name__ == "__main__":
    pass
