import time
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


# pytest -m slow test/test_calculator.py -v
@pytest.mark.skip()
def test_very_slow() -> None:
    time.sleep(5)
    result: float = calculator.add(2, 3)
    assert result == 5


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-4, 2, -8),
        (2.5, 4, 10.0),
        (-2, -2.5, 5.0),
        # Add more test cases as needed
    ],
)
def test_many_multiply(x: float, y: float, expected_result: float) -> None:
    assert calculator.multiply(x, y) == expected_result
