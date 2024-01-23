from typing import Dict, Optional

database: Dict[int, str] = {1: "Alice", 2: "Bob", 3: "Charlie"}


def get_user_from_db(user_id: int) -> Optional[str]:
    return database.get(user_id)
