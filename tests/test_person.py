
import json
import random
from typing import List

import pytest

from splitcoffee.model.MenuItem import MenuItem
from splitcoffee.model.Person import Person



def test_person_file_read_create(person_data, persons):
    for exp_per, act_per in zip(person_data, persons):
        assert act_per.name == exp_per["name"]
        assert act_per.favorite_drink == exp_per["favorite_drink"]
        assert act_per.consistency_rate == exp_per["consistency_rate"]

def test_person_set_consistency():
    person = Person({ "name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95 })
    person.consistency_rate = 0.1
    assert person.consistency_rate == 0.1

def test_person_set_name():
    person = Person({ "name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95 })
    person.name = "Scott"
    assert person.name == "Scott"

def test_person_set_favorite_drink():
    person = Person({ "name": "Bob", "favorite_drink": "Espresso", "consistency_rate": 0.95 })
    person.favorite_drink = "Cappuccino"
    assert person.favorite_drink == "Cappuccino"

def test_get_order(persons, menu):
    random.seed(42)
    # build a dict of Names: MenuItems to make an order
    orders = { person.name: person.get_order(menu) for person in persons}

    for i,person in enumerate(persons):
        if person.name == "Michael":
            assert person.ordered_random == True
        else:
            assert (persons[i].favorite_drink == orders[person.name].name or persons[i].ordered_random)
