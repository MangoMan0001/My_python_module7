#!/usr/bin/env python3
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    """
    ゲームエンジンDEMO
    """

    engine = GameEngine()

    engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())

    report = engine.simulate_turn()
    for key, value in report.items():
        print(f"{key}: {value}")
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
