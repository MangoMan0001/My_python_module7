#!/usr/bin/env python3
from ex0.Card import Card


class CreatureCard(Card):
    """
    クリーチャーカード
    攻撃力と体力とタイプの属性を持つ
    戦闘時処理のattack_targetメソッドを持つ
    """

    def __init__(self, creature_data: dict | None):
        """
        クリーチャー独自のパラメータを付与する
        """

        creature_data = creature_data or {}
        name = creature_data["name"]
        cost = creature_data["cost"]
        rarity = creature_data["rarity"]
        attack = creature_data["attack"]
        health = creature_data["health"]

        # -attackとhealthの検証
        self.validate(attack, health)
        super().__init__(name, cost, rarity)
        self.info['attack'] = attack
        self.info['health'] = health
        self.info['type'] = "Creature"

    def play(self, game_state: dict) -> dict:
        """
        クリチャープレイ時処理
        """

        return {'card_played': self.info['name'],
                'mana_used': self.info['cost'],
                'effect': 'Creature summoned to battlefield'}

    def attack_target(self, target: Card) -> dict:
        """
        クリーチャーアタック時処理
        """

        # -ターゲットに体力パラメータがあるかどうか
        if type(target.info.get('health')) is int:
            result = True
        else:
            result = False
        return {'attacker': self.info['name'],
                'target': target.info['name'],
                'damage_dealt': self.info['attack'],
                'combat_resolved': result}

    @staticmethod
    def validate(attack: int, helth: int) -> None:
        """
        attackとhealthが正の整数であることを検証する
        """

        values = [attack, helth]
        for value in values:
            if value < 1:
                raise ValueError(f"{value.__str__} "
                                 f"is not a positive integer ({value})")


if __name__ == "__main__":
    pass
