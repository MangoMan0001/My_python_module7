#!/usr/bin/env python3
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    最強の魔法戦士カードの抽象クラス
    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 defense: int,
                 mana: int,
                 health: int):
        """
        クリーチャー初期化
        攻撃力と体力のパラメータを持つ
        """

        self.validate(attack, health)
        super().__init__(name, cost, rarity)
        self.info['attack'] = attack
        self.info['defense'] = defense
        self.info['mana'] = mana
        self.info['health'] = health
        self.info['type'] = "elite"

    def play(self, game_state: dict) -> dict:
        """
        プレイしたカードの情報が出力される
        """

        return {'card_played': self.info['name'],
                'mana_used': self.info['cost'],
                'effect': 'Elite Creature summoned to battlefield'}

    def attack(self, target) -> dict:
        """
        攻撃メソッド
        """

        return {'attacker': self.info['name'],
                'target': target,
                'damage': self.info['attack'],
                'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> dict:
        """
        防御抽象メソッド
        """

        # -ダメージを食らって生きてるか
        health = self.info['health']
        defense = self.info['defense']
        if defense <= incoming_damage:
            health -= (incoming_damage - defense)
        if 0 < health:
            result = True
        else:
            result = False
        self.info['health'] = health
        return {'defender': self.info['name'],
                'damage_taken': incoming_damage,
                'damage_blocked': self.info['defense'],
                'still_alive': result}

    def get_combat_stats(self) -> dict:
        """
        戦闘状況を返す
        """

        return {'health': self.info.get('health'),
                'attack': self.info.get('attack'),
                'status':
                'alive' if self.info.get('health', 0) > 0 else 'dead'}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        魔法詠唱メソッド
        """

        self.info['mana'] -= 4
        return {'caster': self.info['name'],
                'spell': spell_name,
                'targets': targets,
                'mana_used': 4}

    def channel_mana(self, amount: int) -> dict:
        """
        マナ回復メソッド
        """

        self.info['mana'] += amount
        return {'channeled': amount,
                'total_mana': self.info['mana']}

    def get_magic_stats(self) -> dict:
        """
        魔法情報取得メソッド
        """

        return {}

    def validate(self, attack: int, helth: int) -> None:
        """
        attackとhealthが正の整数であることを検証する
        """

        values = [attack, helth]
        for value in values:
            if value < 1:
                raise ValueError(f"{value} "
                                 f"is not a positive integer ({value})")


if __name__ == "__main__":
    pass
