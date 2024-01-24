# import pytest
import src.demo_service as demoservice  # Replace 'your_module' with the actual name of your module

# import unittest.mock as mock
# https://docs.python.org/3/library/unittest.mock.html
from unittest.mock import patch, MagicMock

from typing import Any, List, Dict

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


@patch("src.demo_service.get_user_from_db")
def test_get_user_from_db_mock_user(mock_get_user_from_db: MagicMock) -> None:
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name: str | None  = demoservice.get_user_from_db(1)
    assert user_name == "Mocked Alice"


# def test_get_user_from_db_existing_user() -> None:
#     result: Any = demoservice.get_users_from_service()
#     assert result is not None

def test_get_users_from_service() -> None:
    result: List[Dict[str, Any]] = demoservice.get_users_from_service()
    
    # Check that the result is a non-empty list
    assert isinstance(result, list)
    assert result

    # Check that each item in the list is a dictionary with expected keys
    for user in result:
        assert isinstance(user, dict)
        assert set(user.keys()) == {'id', 'name', 'email', 'username', 'address', 'phone', 'website', 'company'}

    # You can add more specific checks based on your actual API response structure

    # Example: Check that the first user has a non-empty 'name'
    first_user = result[0] if result else None
    assert first_user and first_user['name']