#!/usr/bin/env python3
from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """
    トーナメントプログラム実行関数
    """

    print()
    print("=== DataDeck Tournament Platform ===")
    print()

    # 1.トーナメントオブジェクト作成
    tournament = TournamentPlatform()
    fire_dragon = TournamentCard('Fire Dragon', 5, 'rare', 7)
    ice_wizard = TournamentCard('Ice Wizard', 3, 'rare', 4)
    id1 = tournament.register_card(fire_dragon)
    id2 = tournament.register_card(ice_wizard)
    print("Registering Tournament Cards...")
    print()

    stats = []
    stats.append(fire_dragon.get_tournament_stats())
    stats.append(ice_wizard.get_tournament_stats())
    for stat in stats:
        for key, value in stat.items():
            print(f"{key} {value}")
        print()

    # 2.マッチ実行
    print("Creating tournament match...")
    match_result = tournament.create_match(id1, id2)
    print(match_result)
    print()

    # 3.リーダーボード出力
    print("Tournament Leaderboard:")
    for board in tournament.get_leaderboard():
        print(board)
    print()

    # 4.レポート出力
    print("Platform Report:")
    print(tournament.generate_tournament_report())
    print()

    print("== Tournament Platform Successfully Deployed! ===\n"
          "All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
