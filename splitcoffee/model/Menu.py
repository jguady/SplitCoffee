# import typing
from typing import List

from splitcoffee.model.MenuItem import MenuItem


class Menu:

    menu_items: dict[str,MenuItem] = {}

    # Useful if data is in { "name": "Espresso", "price": 2.5 },
    def from_list(self, mi: List):
        self.menu_items = {menu_item["name"] : MenuItem(**menu_item) for menu_item in mi}

    # Useful if data is in "Espresso": { "price": 2.5 } format
    def from_dict(self, mi: dict):
        self.menu_items = mi

    def __str__(self):
        return str(self.menu_items)

    def __getitem__(self, item):
        return self.menu_items[item]

