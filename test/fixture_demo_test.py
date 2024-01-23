import pytest

@pytest.fixture
def example_fixture() -> int:
    return 15

def test_with_fixture(example_fixture: int) -> None:
      assert example_fixture == 15
