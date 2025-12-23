import builtins
import importlib
import sys
from wsgiref.validate import assert_

import pytest


@pytest.fixture
def blackjack_module(monkeypatch):
    inputs = iter([
        '0',  # Tétet input
        'm',  # Húz vagy megáll
        'n'   # új játék
    ])
    monkeypatch.setattr(builtins, 'input', lambda prompt='': next(inputs))
    module = importlib.import_module('blackjack')
    yield module
    sys.modules.pop('blackjack', None)


def test_carddata_constructor_raises(blackjack_module):
    CardData = blackjack_module.CardData
    with pytest.raises(RuntimeError):
        CardData()


@pytest.mark.parametrize("rank, value", [
    ("Ketto", 2), ("Harom", 3), ("Tiz", 10), ("Bubi", 10), ("Asz", 11)
])
def test_carddata_get_value_valid(blackjack_module, rank, value):
    CardData = blackjack_module.CardData
    assert CardData.get_value(rank) == value

def test_carddata_get_value_invalid(blackjack_module):
    CardData = blackjack_module.CardData
    with pytest.raises(ValueError):
        CardData.get_value('invalid')

def test_card_valid_and_str(blackjack_module):
    Card = blackjack_module.Card
    c = Card('Kor', 'Ketto')
    assert c.color == 'Kor'
    assert c.rank == 'Ketto'
    assert str(c) == 'Ketto - Kor'

@pytest.mark.parametrize('bad_color', ['K', '12', 'AB'])
def test_card_invalid_color(blackjack_module, bad_color):
    Card = blackjack_module.Card
    with pytest.raises(ValueError):
        Card(bad_color, 'Ketto')

@pytest.mark.parametrize('bad_rank', ['A', 'Z', ''])
def test_card_invalid_rank(blackjack_module, bad_rank):
    Card = blackjack_module.Card
    with pytest.raises(ValueError):
        Card('Kor', bad_rank)

def test_deck_init_length(blackjack_module):
    Deck = blackjack_module.Deck
    deck = Deck()
    exptected_length = len(blackjack_module.CardData.colors) * len(blackjack_module.CardData.ranks)
    assert len(deck) == exptected_length

def test_deck_mix_calls_shuffle(monkeypatch, blackjack_module):
    Deck = blackjack_module.Deck
    calls = []
    monkeypatch.setattr(blackjack_module, name='shuffle', lambda lst: calls.append(True))
    deck = Deck()
    deck.mix()
    assert calls

def test_deck_div_and_append(blackjack_module):
    Deck = blackjack_module.Deck
    deck = Deck()
    top = deck[-1]
    popped = deck.div()
    assert popped == top
    assert len(deck) == len(blackjack_module.CardData.colors) * len(blackjack_module.CardData.ranks) - 1
    deck.append(popped)
    assert deck[-1] == popped
    with pytest.raises(TypeError):
        deck.append('not_a_card')

def test_hand_append_and_ace_adjustment(blackjack_module):
    Hand = blackjack_module.Hand
    Card = blackjack_module.Card
    hand = Hand()
    ace1 = Card("Karo", "Asz")
    ace2 = Card("Treff", "Asz")
    hand.append(ace1)
    hand.append(ace2)
    assert hand.value == 22
    assert hand.ace == 2
    hand.set_aces()
    assert hand.value == 12
    assert hand.ace == 1

def test_chips_initial_and_sum_setter(blackjack_module):
    Chips = blackjack_module.Chips
    chips = Chips()
    assert chips.sum == 100
    chips.sum = 200
    assert chips.sum == 200
    with pytest.raises(ValueError):
        chips.sum = 0

def test_chips_bet_setter_and_win_loose(blackjack_module):
    Chips = blackjack_module.Chips
    chips = Chips()
    chips.bet = 10
    assert chips.bet == 10
    with pytest.raises(ValueError):
        chips.bet = -1
    with pytest.raises(ValueError):
        chips.bet = 200
    chips.bet = 20
    chips.win_bet()
    assert chips.sum == 120
    chips.loose_bet()
    assert chips.sum == 100

def test_betting_sets_bet(monkeypatch, blackjack_module):
    Rules = blackjack_module.Rules
    Chips = blackjack_module.Chips
    chips = Chips(sum=50)
    monkeypatch.setattr(builtins, name='input', lambda prompt='': '15')
    Rules.betting(chips)
    assert chips.bet == 15

def test_draw_appends_and_updates(blackjack_module):
    Rules = blackjack_module.Rules
    Hand = blackjack_module.Hand
    class StubDeck:
        def __init__(self):
            self.called = False
        def div(self):
            self.called = True
            return blackjack_module.Card('Pikk', 'Negy')
    hand = Hand()
    deck = StubDeck()
    Rules.draw(deck, hand)
    assert deck.called
    assert hand.value == blackjack_module.CardData.get_value('Negy')

def run_logic(player_value, dealer_value, card_rank, expected_message):
    player = Hand()
    player.value = player_value
    player.ace = 0
    dealer = Hand()
    dealer.value = dealer_value
    dealer.ace = 0
    chips = Chips()
    chips.bet = 10
    class StubDeck:
        def __init__(self):
            self.card = blackjack_module.Card('Kor', card_rank)

        def div(self):
            return self.card

    deck = StubDeck()
    if player.value > 21:
        Rules.player_loose(chips)
    else:
        while dealer.value < 17:
            Rules.draw(deck, dealer)

        if dealer.value > 21:
            Rules.dealer_loose(chips)
        elif dealer.value > player.value:
            Rules.dealer_win(chips)
        elif dealer.value < player.value:
            Rules.player_win(chips)
        else:
            Rules.equals()
    out = capsys.readouterr().out
    assert expected_message in out
    assert chips.sum == 100 + expected_sum

run_logic(player_value=10, dealer_value=15, card_rank='Nyolc',
          expected_message='Az osztó elúszott!', expected_sum=0)

run_logic(player_value=5, dealer_value=15, card_rank='Négy',
          expected_message='Az osztó nyert!', expected_sum=-10)

run_logic(player_value=20, dealer_value=10, card_rank='Négy',
          expected_message='A játékos nyert!', expected_sum=10)

run_logic(player_value=20, dealer_value=15, card_rank='Öt',
          expected_message='Az állás döntetlen!', expected_sum=0)









