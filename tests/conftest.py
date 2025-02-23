import json
from typing import List

import pytest

from splitcoffee.model.Menu import Menu
from splitcoffee.model.Person import Person


@pytest.fixture
def menu_data() -> List:
    return [
        {"name": "Espresso", "price": 2.5},
        {"name": "Drip", "price": 1.50},
        {"name": "Latte", "price": 3.75},
        {"name": "Cappuccino", "price": 3.75},
        {"name": "Mocha", "price": 4.1}
    ]

@pytest.fixture
def menu(tmp_path, menu_data):
    menu = Menu()
    file_path = tmp_path / "menu.json"
    file_path.write_text(json.dumps(menu_data))

    with open(file_path, "r") as menu_file:
        loaded_menu = json.loads(menu_file.read())

    menu.from_list(loaded_menu)

    return menu

@pytest.fixture
def person_data() -> List:
    return [
        {"name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95},
        {"name": "Jim", "favorite_drink": "Latte", "consistency_rate": 0.1},
        {"name": "Alice", "favorite_drink": "Cappuccino", "consistency_rate": 0.8},
        {"name": "Jay", "favorite_drink": "Mocha", "consistency_rate": 0.4},
        {"name": "Steve", "favorite_drink": "Drip", "consistency_rate": 0.8},
        {"name": "Sarah", "favorite_drink": "Espresso", "consistency_rate": 0.92},
        {"name": "Michael", "favorite_drink": "Latte", "consistency_rate": 0.85}
    ]
@pytest.fixture
def persons(tmp_path, person_data) -> dict[str,Person]:

    file_path = tmp_path / "person.json"
    file_path.write_text(json.dumps(person_data))

    with open(file_path, "r") as person_file:
        loaded_person = json.loads(person_file.read())
    persons = {data["name"]: Person(data) for data in loaded_person}
    return persons