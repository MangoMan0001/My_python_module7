#!/usr/bin/env python3
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Game orchestrator
    """

    def __init__(self):
        """
        初期化
        """

        self.factory: CardFactory
        self.strategy: GameStrategy
        self.battlefield = [5]
        self.turns = 0
        self.total_damage = 0

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        工場と戦略を適用
        """

        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """
        ターンをシミュレート
        """

        print()
        print("=== DataDeck Game Engine ===")
        print()

        # 1.ステータス表示
        print("Configuring Fantasy Card Game...")
        status = self.get_engine_status()
        for key, value in status.items():
            print(f"{key}: {value}")
        print()

        # 2.手札作成
        print("Simulating aggressive turn...")
        cards = 3
        hand = self.factory.create_themed_deck(cards)['deck']
        strhand = []
        for card in hand:
            strhand.append(f"{card.info['name']} ({card.info['cost']})")
        print(f"Hand: {strhand}")
        print()

        # 3.ターン処理
        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        action = self.strategy.execute_turn(hand, self.battlefield)
        self.total_damage += action['damage_dealt']
        print(f"Actions: {action}")
        self.turns += 1
        print()

        return {'Game Report':
                {'turns_simulated': self.turns,
                 'strategy_used': self.strategy.get_strategy_name(),
                 'total_damage': self.total_damage,
                 'cards_created': cards}}

    def get_engine_status(self) -> dict:
        """
        ステータスを返す
        """

        return {'Factory': self.factory.__class__.__name__,
                'Strategy': self.strategy.get_strategy_name(),
                'Available types': self.factory.get_supported_types()}


if __name__ == "__main__":
    pass
