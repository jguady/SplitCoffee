import heapq
import operator
import random
from ftplib import print_line
from heapq import heappush, heappop

import pytest

from splitcoffee.CoffeeShop import CoffeeShop
from splitcoffee.model.MenuItem import MenuItem

@pytest.fixture
def loaded_coffee_shop(persons,menu):
    coffee_shop = CoffeeShop()
    coffee_shop = CoffeeShop()
    coffee_shop.__setattr__("people", persons)
    coffee_shop.__setattr__("menu", menu)
    return coffee_shop

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


# def test_stuff(loaded_coffee_shop):
#     loaded_coffee_shop.take_orders()
#     assert loaded_coffee_shop.order is not []
#     assert type(loaded_coffee_shop.order) == dict
#     orders_a = loaded_coffee_shop.order
#
#
#
#     print()
#     print(orders_a)
#     order_list_a = [(key, orders_a[key].price) for key in orders_a]
#     print(order_list_a)
#     print(order_list_a[1])
#
#     loaded_coffee_shop.take_orders()
#     orders_b = loaded_coffee_shop.order
#
#     assert orders_a != orders_b
#     print()
#     print(orders_b)
#     order_list_b = [(key, orders_b[key].price) for key in orders_b]
#     print(order_list_b)
#     print(order_list_b[1])
#
#     print(list(map(lambda x,y: x[1]+y[1], order_list_a, order_list_b)))







# build a dict of Names: MenuItems to make an order
