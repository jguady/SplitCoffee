import random

import pytest

from splitcoffee.model.Person import Person


def test_person_file_read_create(person_data, persons):
    for exp_per, act_per in zip(person_data, persons.values()):
        assert act_per.name == exp_per["name"]
        assert act_per.favorite_drink == exp_per["favorite_drink"]
        assert act_per.consistency_rate == exp_per["consistency_rate"]


def test_person_set_consistency():
    person = Person({"name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95})
    person.consistency_rate = 0.1
    assert person.consistency_rate == 0.1


def test_person_set_name():
    person = Person({"name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95})
    person.name = "Scott"
    assert person.name == "Scott"


def test_person_set_favorite_drink():
    person = Person({"name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95})
    person.favorite_drink = "Cappuccino"
    assert person.favorite_drink == "Cappuccino"


def test_get_order_favorite(persons, menu):
    random.seed(42)
    # build a dict of Names: MenuItems to make an order
    orders = {person.name: person.get_order(menu) for person in persons.values()}
    person = persons["Jay"]
    order = persons["Jay"].get_order(menu)
    assert person.favorite_drink == orders[person.name].name or person.ordered_random

def test_get_order_random(persons, menu):
    random.seed(42)
    person : Person = persons["Jim"]
    person.consistency_rate = 0.0
    order = person.get_order(menu)
    assert person.ordered_random == True
    assert person.favorite_drink != order.name

def test_get_order_no_menu(persons):
    with pytest.raises(TypeError) as err:
        order = persons["Jim"].get_order(None)
    assert "Menu cannot be None" in str(err.value)


