#!/usr/bin/env python3
from tools.card_generator import CardGenerator
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    """
    カードゲームDEMO
    デッキシステムDEMO
    """

    print()
    print("=== DataDeck Deck Builder ===")
    print()

    try:
        # 1.カードジェネレータ作成
        generator = CardGenerator()

        # 2.カードを作成
        card_data = []
        spell = generator.get_spell('Lightning Bolt')
        assert spell is not None
        card_data.append(SpellCard(*spell.values()))

        artifact = generator.get_artifact('Mana Crystal')
        assert artifact is not None
        card_data.append(ArtifactCard(*artifact.values()))

        creature = generator.get_creature('Fire Dragon')
        assert creature is not None
        card_data.append(CreatureCard(*creature.values()))

        # 2.デッキ作成
        print("Building deck with different card types...")
        deck = Deck()
        for card in card_data:
            deck.add_card(card)
        print(deck.get_deck_stats())
        print()

        # 3.「私のターン、ドロー!」
        print("Drawing and playing cards:")
        print()

        hand = deck.draw_card()
        print(f"Drew: {hand.info['name']} ({hand.info['type']})")
        print(f"Play result: {hand.play({})}")
        print()

        hand = deck.draw_card()
        print(f"Drew: {hand.info['name']} ({hand.info['type']})")
        print(f"Play result: {hand.play({})}")
        print()

        hand = deck.draw_card()
        print(f"Drew: {hand.info['name']} ({hand.info['type']})")
        print(f"Play result: {hand.play({})}")
        print()

        print("Polymorphism in action: Same interface, "
              "different card behaviors!")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
