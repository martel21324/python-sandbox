import pytest
import src.calculator as calculator


def test_multiply_by_zero() -> None:
    assert calculator.multiply(5, 0) == 0


def test_multiply_by_2() -> None:
    assert calculator.multiply(5, 2) == 10


def test_divide_by_2() -> None:
    result: float = calculator.divide(10, 2)
    assert result == 5


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
