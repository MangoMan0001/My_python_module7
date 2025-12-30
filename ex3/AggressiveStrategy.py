#!/usr/bin/env python3
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    """
    大胆な戦略
    「やっちゃえバーサーカー」
    """

    def execute_turn(self, hand: list[Card], battlefield: list) -> dict:
        """
        ターンを進める
        """

        played_c = []
        played_s = []
        mana = battlefield[0]
        i = 0
        while i <= mana:
            if mana < i:
                break
            for k, card in enumerate(hand):
                if card.info['cost'] == i:
                    if card.info['type'] == 'creature':
                        played_c.append(hand.pop(k))
                    elif card.info['type'] == 'spell':
                        played_s.append(hand.pop(k))
                    else:
                        continue
                    mana -= i
                    i -= 1
                    break
            i += 1

        mana_used = battlefield[0] - mana
        target = 'Enemy Player'
        damage = 0
        if len(played_c):
            damage += sum(card.info.get('attack') for card in played_c)
        damage += 6 * len(played_s)
        played = played_c + played_s
        names = []
        for card in played:
            names.append(card.info['name'])
        if damage == 0:
            action = {'cards_played': [],
                      'mana_used': mana_used,
                      'damage_dealt': damage}
        else:
            action = {'cards_played': [names],
                      'mana_used': mana_used,
                      'targets_attacked': target,
                      'damage_dealt': damage}

        return action

    def get_strategy_name(self) -> str:
        """
        戦略名を返す
        """

        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Player > クリーチャーの順に選択する
        """

        if 'Enemy Player' in available_targets:
            return ['Enemy Player']
        return available_targets


if __name__ == "__main__":
    pass
