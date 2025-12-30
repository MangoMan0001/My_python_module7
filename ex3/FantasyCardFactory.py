#!/usr/bin/env python3
import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """
    カード工場
    """

    def __init__(self):
        """
        初期化
        """

        self.cretures = ['dragon', 'goblin']
        self.spells = ['lightning_bolt', 'fireball', 'ice shard']
        self.art = ['mana_ring', 'ring_of_wisdom', 'staff_of_elements']

    def create_creature(self, name_or_power) -> Card:
        """
        ファンタジークリーチャー作成
        """

        data = {'dragon': ["Fire Dragon", 5, "Legendary", 7, 5],
                'goblin': ["Goblin Warrior", 2, "Common", 2, 1]}
        return CreatureCard(*data[name_or_power])

    def create_spell(self, name_or_power) -> Card:
        """
        ファンタジー魔法作成
        """

        data = {"lightning_bolt": ["Lightning Bolt", 3, "Common", "damage"],
                "fireball": ["Fireball", 4, "Uncommon", "damage"],
                "ice shard": ["Ice Shard", 2, "Common", "damage"]}
        return SpellCard(*data[name_or_power])

    def create_artifact(self, name_or_power) -> Card:
        """
        ファンタジーアーティファクト作成
        """

        data = {"mana_ring": ["Mana Crystal", 2, "Common", 5,
                              "Permanent: +1 mana per turn"],
                "ring_of_wisdom": ["Ring of Wisdom", 4, "Rare", 4,
                                   "Permanent: Draw an extra card each turn"],
                "staff_of_elements": ["Staff of Elements", 6, "Legendary",  7,
                                      "Permanent: +1 spell damage"]}
        return ArtifactCard(*data[name_or_power])

    def create_themed_deck(self, size: int) -> dict:
        """
        ファンタジーテーマデッキの作成
        """

        types = ['creature', 'spell', 'art']
        creatures = self.cretures
        spells = self.spells
        art = self.art
        deck = []
        for i in range(size):
            type = random.choice(types)
            if type == 'creature':
                deck.append(self.create_creature(random.choice(creatures)))
            elif type == 'spell':
                deck.append(self.create_spell(random.choice(spells)))
            else:
                deck.append(self.create_artifact(random.choice(art)))
        return {'deck': deck}

    def get_supported_types(self) -> dict:
        """
        サポートされているタイプを取得
        """

        return {'creatures': self.cretures,
                'spells': self.spells,
                'artifacts': self.art}


if __name__ == "__main__":
    pass
