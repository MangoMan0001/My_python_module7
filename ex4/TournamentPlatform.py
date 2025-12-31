#!/usr/bin/env python3
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    トーナメントマネージャー
    """

    def __init__(self):
        """
        初期化
        """

        self.cards = {}
        self.matchs = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        カードの登録、ID返す
        """

        id = card.info['name']

        self.cards[id] = card
        return id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        IDで呼ばれたカード同士でマッチ
        リザルトを返す
        """

        # 攻撃力の高い方が勝ち
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card2.info['attack'] < card1.info['attack']:
            card1.update_wins(1)
            card2.update_losses(1)
            winner = card1
            loser = card2
        elif card1.info['attack'] < card2.info['attack']:
            card2.update_wins(1)
            card1.update_losses(1)
            winner = card2
            loser = card1
        else:
            return {'winner': 'draw',
                    'loser': 'draw',
                    'winner_rating': 'draw',
                    'loser_rating': 'draw'}
        self.matchs += 1

        return {'winner': winner.info['name'],
                'loser': loser.info['name'],
                'winner_rating': winner.calculate_rating(),
                'loser_rating': loser.calculate_rating()}

    def get_leaderboard(self) -> list:
        """
        リーダーボードを返す
        """

        def get_rating(card: TournamentCard) -> int:
            """
            渡されたカードのレートを返す
            """
            return card.calculate_rating()

        leaderboard = []
        sorted_card = sorted(self.cards.values(), key=get_rating, reverse=True)
        for i, card in enumerate(sorted_card):
            for key, value in card.get_rank_info().items():
                board = f"{i}. {card.info['name']} - {key}{value}"
            leaderboard.append(board)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        """
        レポートを返す
        """

        rat_list = []
        for card in self.cards.values():
            rat_list.append(card.calculate_rating())
        avg = sum(rat_list) / len(rat_list)
        return {'total_cards': len(self.cards),
                'matches_played': self.matchs,
                'avg_rating': avg,
                'platform_status': 'active'}


if __name__ == "__main__":
    pass
