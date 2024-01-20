import json
import os
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str


# Specify the path to your JSON file
# json_file_path = 'path/to/your/data.json'

# Get the current directory of the Python script
script_dir = os.path.dirname(__file__)

# Specify the relative path to your JSON file
json_file_path = os.path.join(script_dir, "data.json")

# Open the file and load the JSON data
with open(json_file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Print the deserialized data
print(json_data)

# Deserialize the JSON array into a list of Person objects
people = [Person(**person_data) for person_data in json_data]

# Print the deserialized Person objects
for person in people:
    print(f"Name: {person.name}, Age: {person.age}, City: {person.city}")
