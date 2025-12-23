import pytest

from teszteles.multiply_numbers import multiply

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-1, 5, -5),
        (-2, -2, 4)
    ]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected