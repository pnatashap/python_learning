import pytest
from task01 import continued_fraction

@pytest.mark.parametrize(
    "frac, expected", [("239/30", [7, 1, 29]), ("0/2", [0]), ("1/0", [None]), ("415/93", [4, 2, 6, 7])]
)
def test_hw4(frac, expected):
    assert continued_fraction(*map(int, frac.split("/"))) == expected
