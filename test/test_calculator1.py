# pip install pytest
# pytest C:\Logiciels\GitHub\python-sandbox\pytest_calculator1.py
from calculator1 import square


def test_positive() -> None:
    assert square(2) == 4
    assert square(3) == 9


def test_negative() -> None:
    assert square(-2) == 4


def test_anotherNegative() -> None:
    assert square(-3) == 9


def test_square_zero() -> None:
    assert square(0) == 0

