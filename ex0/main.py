#!/usr/bin/env python3
from tools.card_generator import CardGenerator
from ex0.CreatureCard import CreatureCard


def main() -> None:
    """
    カードゲームDEMO
    """

    print()
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()

    try:
        # 1.カードジェネレータ作成
        generator = CardGenerator()

        # 2.Fire Dragon（クリーチャー）を作成
        creature = generator.get_creature('Fire Dragon')
        assert creature is not None
        fire_dragon = CreatureCard(*creature.values())
        creature = generator.get_creature('Goblin Warrior')
        assert creature is not None
        goblin_warrior = CreatureCard(*creature.values())

        # 3.クリーチャー情報を出力
        print(f"CreatureCard Info:\n{fire_dragon.get_card_info()}")
        print()

        # 4.マナが足りるか確かめて、召喚！
        print("Playing Fire Dragon with 6 mana available:")
        print(f"Playable: {fire_dragon.is_playable(6)}")
        print(f"Play result: {fire_dragon.play({})}")
        print()

        # 5.攻撃！
        print("Fire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
        print()

        # 6.マナ枯渇DEMO
        print("Testing insufficient mana (3 available):")
        print(f"Playable: {fire_dragon.is_playable(3)}")
        print()

        print("Abstract pattern successfully demonstrated!")

    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()
