
import json
from types import SimpleNamespace
from typing import List

import pytest

from splitcoffee.model.Menu import Menu
from splitcoffee.model.MenuItem import MenuItem



def test_load_menu(tmp_path, menu_data):
    menu = Menu()
    file_path = tmp_path / "menu.json"
    file_path.write_text(json.dumps(menu_data))

    with open(file_path, "r") as menu_file:
        loaded_menu = json.loads(menu_file.read())

    menu.from_list(loaded_menu)

    assert menu["Cappuccino"].price == 3.75
    assert menu.menu_items.keys() == { 'Drip', 'Espresso', 'Latte', 'Cappuccino', 'Mocha'}
    for expected, actual in zip(menu_data, menu.menu_items.values()):
        assert actual.name == expected["name"]
        assert actual.price == expected["price"]



