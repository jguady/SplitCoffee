import copy
from typing import List

import pytest

from splitcoffee.model.MenuItem import MenuItem
from splitcoffee.model.SplitCoffeeState import SplitCoffeeState
from splitcoffee.service.SplitCoffeeService import SplitCoffeeService


@pytest.fixture
def split_state_data():
    return {
        "Bob": SplitCoffeeState(person_name="Bob", debt= -15.00, time_last_paid= 0),
        "Amanda": SplitCoffeeState(person_name="Amanda", debt= 5.00, time_last_paid= 0)
    }

@pytest.fixture
def split_state_data_tie():
    return {
        "Bob": SplitCoffeeState(person_name="Bob", debt= -15.00, time_last_paid= 1),
        "Amanda": SplitCoffeeState(person_name="Amanda", debt= -15.00, time_last_paid= 0)
    }

@pytest.fixture
def menu_items() -> List[MenuItem]:
    items: List[MenuItem] = [MenuItem("Drip", 1.5), MenuItem("Espresso", 2.5)]
    return items

@pytest.fixture
def orders(menu_items: List[MenuItem]):
    return dict(zip(["Bob", "Amanda"], menu_items))

def test__determine_payment_person(split_state_data, orders, persons):
    service = SplitCoffeeService()
    service.split_state = split_state_data

    lowest_expected = get_lowest_expected(split_state_data)

    name = service.determine_payment_person(persons, orders)

    assert name in orders.keys()
    assert split_state_data.get(name) == service.split_state.get(name)
    assert split_state_data.get(lowest_expected) == service.split_state.get(name)
    assert lowest_expected == name

    # alter the state for testing
    service.split_state["Amanda"] = SplitCoffeeState("Amanda",debt= -15.00, time_last_paid= 0)
    #
    second_order_name = service.determine_payment_person(persons, orders)
    assert second_order_name == "Bob"


def test__determine_payment_person_not_present(split_state_data, orders, persons):
    service = SplitCoffeeService()
    service.split_state = copy.deepcopy(split_state_data)

    #Add Additional Person not on order
    service.split_state["Steve"] = SplitCoffeeState(person_name="Steve", debt= 6.00, time_last_paid= 0)

    name = service.determine_payment_person(persons, orders)
    lowest_expected = get_lowest_expected(split_state_data)

    assert name in orders.keys()
    assert name is not "Steve"
    assert service.split_state.get("Steve").debt == 6.00
    assert lowest_expected == name
    assert split_state_data.get(lowest_expected).debt == service.split_state.get(name).debt


    # alter the state for testing
    service.split_state["Amanda"].debt = -16.00
    split_state_data["Amanda"].debt = -16.00
    second_order_name = service.determine_payment_person(persons, orders)
    assert second_order_name == "Bob"
    lowest_expected = get_lowest_expected(split_state_data)

    assert split_state_data.get(lowest_expected).debt == service.split_state.get(second_order_name).debt

def test__determine_payment_person_tie(split_state_data_tie, orders, persons):
    service = SplitCoffeeService()
    service.split_state = copy.deepcopy(split_state_data_tie)

    name = service.determine_payment_person(persons, orders)
    lowest_expected = get_lowest_expected(split_state_data_tie)

    expected_max_many = {key for key, state_item in split_state_data_tie.items() if state_item.debt == split_state_data_tie[lowest_expected].debt}

    if len(expected_max_many) > 1:
        lowest_expected = min(expected_max_many, key=lambda key: split_state_data_tie[key].time_last_paid)

    assert name == "Amanda"
    assert name in orders.keys()
    assert lowest_expected == name
    assert split_state_data_tie.get(lowest_expected).debt == service.split_state.get(name).debt
    assert split_state_data_tie.get(lowest_expected).time_last_paid == service.split_state.get(name).time_last_paid


    service.split_state["Amanda"].time_last_paid = 2
    split_state_data_tie["Amanda"].time_last_paid = 2
    # Modify
    name = service.determine_payment_person(persons, orders)
    lowest_expected = get_lowest_expected(split_state_data_tie)

    expected_max_many = {key for key, state_item in split_state_data_tie.items() if
                         state_item.debt == split_state_data_tie[lowest_expected].debt}

    if len(expected_max_many) > 1:
        lowest_expected = min(expected_max_many, key=lambda key: split_state_data_tie[key].time_last_paid)

    assert name in orders.keys()
    assert lowest_expected == name
    assert split_state_data_tie.get(lowest_expected).debt == service.split_state.get(name).debt
    assert split_state_data_tie.get(lowest_expected).time_last_paid == service.split_state.get(name).time_last_paid


def test_charge_person(split_state_data, persons, orders):
    service = SplitCoffeeService()
    service.split_state = copy.deepcopy(split_state_data)
    total = service.get_order_total(orders)
    person_name = service.determine_payment_person(persons, orders)
    service.charge_person(total, person_name )

    assert service.split_state.get(person_name).debt == (split_state_data.get(person_name).debt - total)
    service.split_state.pop(person_name)
    for key, data in service.split_state.items():
        assert data.debt == split_state_data.get(key).debt

def test_get_order_total(orders):
    service = SplitCoffeeService()
    total = SplitCoffeeService.get_order_total(orders)

    assert total == 4.0

    orders["Steve"] = MenuItem("Mocha", 4.0)
    total = SplitCoffeeService.get_order_total(orders)

    assert total == 8.0

def test__update_state():
    # Create expected state
    service = SplitCoffeeService()
    service.split_state = {
        "Bob": SplitCoffeeState(person_name="Bob", debt=-15.00, time_last_paid=0),
        "Amanda": SplitCoffeeState(person_name="Amanda", debt=5.00, time_last_paid=0)
    }
    items : List[MenuItem] = [ MenuItem("Drip", 1.5), MenuItem("Espresso", 2.5) ]
    orders = {
        "Bob": items[0],
        "Amanda": items[1],
    }

    service.apply_credits(orders)

    assert service.split_state["Bob"].debt == -13.50
    assert service.split_state["Amanda"].debt == 7.5

    # {'Bob': MenuItem(name=Espresso, price=2.5), 'Jim': MenuItem(name=Latte, price=3.75),
    #  'Alice': MenuItem(name=Mocha, price=4.1), 'Jay': MenuItem(name=Mocha, price=4.1),
    #  'Steve': MenuItem(name=Drip, price=1.5), 'Sarah': MenuItem(name=Espresso, price=2.5),
    #  'Michael': MenuItem(name=Latte, price=3.75)}

def test_initialize_state(persons):
    service = SplitCoffeeService()
    service.initialize_state(list(persons.keys()))

    assert service.split_state.keys() == persons.keys()
    for value in service.split_state.values():
        assert value.debt == 0

def get_lowest_expected(split_data: dict[str,SplitCoffeeState]) -> str:
    return max(split_data, key=lambda key: split_data.get(key).debt)