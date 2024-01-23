# import pytest
import src.demo_service as demoservice  # Replace 'your_module' with the actual name of your module

# Fixture to provide a sample database for testing
# @pytest.fixture
# def sample_database():
#     return {1: "Alice", 2: "Bob", 3: "Charlie"}

# Test the get_user_from_db function
def test_get_user_from_db_existing_user() -> None:
    result: str | None = demoservice.get_user_from_db(1)
    assert result == "Alice"
    

def test_get_user_from_db_nonexistent_user() -> None:
    result: str | None = demoservice.get_user_from_db(4)
    assert result is None
