import builtins
import importlib
import pytest
import sys


@pytest.fixture
def blackjack_module(moneykpatch, monkeypatch=None):
    inputs = iter([
        '0', # Tet es input
        'm', # Huz vagy megall
        'n' # uj jatek
    ])
    monkeypatch.setattr(builtins, name='input', lambda prompt='' : next(inputs))
    module = importlib.import_module('blackjack')
    yield module
    sys.modules.pop("blackjack", None)

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


