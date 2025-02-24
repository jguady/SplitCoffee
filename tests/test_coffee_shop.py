import json

import pytest

from splitcoffee.CoffeeShop import CoffeeShop


@pytest.fixture
def loaded_coffee_shop(persons,menu):
    coffee_shop = CoffeeShop()
    coffee_shop.__setattr__("people", persons)
    coffee_shop.__setattr__("menu", menu)
    return coffee_shop

@pytest.fixture
def file_loaded_coffee_shop(tmp_path, person_data, menu_data):
    coffee_shop = CoffeeShop()
    # load people
    file_path = tmp_path / "people.json"
    file_path.write_text(json.dumps(person_data))

    coffee_shop.load_people(tmp_path / "people.json")
    #load menu
    file_path = tmp_path / "menu_items.json"
    file_path.write_text(json.dumps(menu_data))

    coffee_shop.load_menu(tmp_path / "menu_items.json")
    return coffee_shop

def test_coffee_shop():
    coffee_shop = CoffeeShop()
    assert coffee_shop is not None


def test_load_people(tmp_path, person_data):
    coffee_shop = CoffeeShop()
    file_path = tmp_path / "people.json"
    file_path.write_text(json.dumps(person_data))

    coffee_shop.load_people(tmp_path / "people.json")

    for index, key in enumerate(coffee_shop.people.keys()):
        assert key == person_data[index]["name"]

def test_load_menu(tmp_path, menu_data):
    coffee_shop = CoffeeShop()
    file_path = tmp_path / "menu_items.json"
    file_path.write_text(json.dumps(menu_data))

    coffee_shop.load_menu(tmp_path / "menu_items.json")

    for index, key in enumerate(coffee_shop.menu.menu_items.keys()):
        assert key == menu_data[index]["name"]

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


def test_present_bill(file_loaded_coffee_shop):
    #Setup the state
    coffee_shop = file_loaded_coffee_shop

    #Act
    coffee_shop.take_orders()
    name, amount = coffee_shop.present_bill()

    #Expected name?

    #exepcted amount
    total: float = sum(item.price for item in coffee_shop.order.values())
    assert name in coffee_shop.people.keys()
    assert total == amount
    #Verify the return values and internal state match expected results.

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
