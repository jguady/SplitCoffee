import typing
import random

from splitcoffee.model.Menu import Menu
from splitcoffee.model.MenuItem import MenuItem


class Person:
    name: str
    favorite_drink: str
    consistency_rate: float
    ordered_random: bool = False

    def __init__(self, data: dict = None) -> None:
        for key, _ in typing.get_type_hints(self).items():
            if key == "ordered_random":
                self.ordered_random = False
            else:
                setattr(self, key, data[key])


    def __str__(self):
        return f"Person(name={self.name}, favorite_drink={self.favorite_drink}, consistency_rate={self.consistency_rate})"
    def __repr__(self):
        return str(self)

    def get_order(self, menu: Menu) -> MenuItem:
        if not menu:
            raise TypeError("Menu cannot be None")
        # simulate people's ability to not order the same drink every day after lunch
        # random.random generates 0..1 value and consistency rate is also 0..1
        # if the random is greater than the persons will to order the same drink they will order a different drink
        if (random.random() > self.consistency_rate) or not menu[self.favorite_drink]:
            self.ordered_random = True
            drink_name = random.choice(list(menu.menu_items))
            return menu.menu_items[drink_name]
        else:
            self.ordered_random = False
            return menu[self.favorite_drink]

