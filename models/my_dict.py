from typing import TypedDict

class MyDict(TypedDict):
    key1: str
    key2: int
    key3: float

my_dict = MyDict(key1="value1", key2=2, key3=3.0)
