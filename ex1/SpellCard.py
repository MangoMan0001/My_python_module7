#!/usr/bin/env python3
from ex0.Card import Card


class SpellCard(Card):
    """
    魔法カードクラス

    ユニーク属性
        エフェクトタイプ

    ユニークメソッド
        resolve_effect(self, target: list) -> dict
    """

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """
        魔法カードの初期化
        """

        super().__init__(name, cost, rarity)
        self.info['effect_type'] = effect_type
        self.info['type'] = "spell"

    def play(self, game_state: dict) -> dict:
        """
        魔法発動処理
        """

        return {'card_played': self.info['name'],
                'mana_used': self.info['cost'],
                'effect': 'Deal 3 damage to target'}

    def resolve_effect(self, targets: list) -> dict:
        """
        呪文メカニクス処理
        """

        return {}


if __name__ == "__main__":
    pass
