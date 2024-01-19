# pip install pytest
# pytest C:\Logiciels\GitHub\python-sandbox\pytest_calculator1.py
from calculator1 import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4


def test_anotherNegative():
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

