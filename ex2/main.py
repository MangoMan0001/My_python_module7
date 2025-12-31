#!/usr/bin/env python3
from ex2.EliteCard import EliteCard


def main() -> None:
    """
    最強エリートモンスター作成DEMO
    """

    try:
        print()
        print("=== DataDeck Ability System ===")
        print()

        # 1.エリートカードの要素紹介
        print("EliteCard capabilities:\n"
              "- Card: ['play', 'get_card_info', 'is_playable']\n"
              "- Combatable: ['attack', 'defend', 'get_combat_stats']\n"
              "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
        print()

        # 2.アーケインウォリアーの作成と召喚
        arcane_warrior = EliteCard('Arcane Warrior', 7, 'Unique', 5, 3, 8, 10)
        print("Playing Arcane Warrior (Elite Card):")
        print()

        # 3.戦闘処理
        print("Combat phase:")
        print(f"Attack result: {arcane_warrior.attack('Enemy')}")
        print(f"Defense result: {arcane_warrior.defend(2)}")
        print()

        # 4.魔法処理
        targets = ['Enemy1', 'Enemy2']
        print("Magic phase:")
        print(f"Spell cast: {arcane_warrior.cast_spell('Fireball', targets)}")
        print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
        print()

        print("Multiple interface implementation successful!")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
