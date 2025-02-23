import random
import pytest

from splitcoffee.CoffeeShop import CoffeeShop
from splitcoffee.model.MenuItem import MenuItem


def test_coffee_shop():
    coffee_shop = CoffeeShop()

def test_coffee_shop_menu_file_not_found():
    with pytest.raises(FileNotFoundError) as FNF:
        coffee_shop = CoffeeShop()
        coffee_shop.load_menu("gibberish")
    assert "No such file or directory" in str(FNF.value)

def test_coffee_shop_person_file_not_found():
    with pytest.raises(FileNotFoundError) as FNF:
        coffee_shop = CoffeeShop()
        coffee_shop.load_menu("teatime")
    assert "No such file or directory" in str(FNF.value)


def test_take_orders(persons, menu):
    jay = persons["Jay"]
    jay.consistency_rate = 0
    coffee_shop = CoffeeShop()
    coffee_shop.__setattr__("people", persons)
    coffee_shop.__setattr__("menu", menu)
    assert coffee_shop.menu is not {}
    assert coffee_shop.menu["Drip"]
    assert coffee_shop.people is not {}
    assert coffee_shop.people["Jay"]

    coffee_shop.take_orders()
    assert coffee_shop.order is not []
    assert type(coffee_shop.order) == dict
    orders = coffee_shop.order

    for person in persons.values():
        assert (person.favorite_drink == orders[person.name].name or person.ordered_random)

# build a dict of Names: MenuItems to make an order
