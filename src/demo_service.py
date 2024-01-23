import requests
from typing import Dict, List, Optional, Any

database: Dict[int, str] = {1: "Alice", 2: "Bob", 3: "Charlie"}


def get_user_from_db(user_id: int) -> Optional[str]:
    return database.get(user_id)


def get_users_from_service() -> List[Dict[str, Any]]:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError