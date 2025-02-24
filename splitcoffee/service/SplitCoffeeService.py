import logging
from typing import List

from splitcoffee.model.MenuItem import MenuItem
from splitcoffee.model.Person import Person
from splitcoffee.model.SplitCoffeeState import SplitCoffeeState


class SplitCoffeeService:

    split_state: dict[str, SplitCoffeeState]
    current_day_num: int = 0
    def __init__(self):
        pass

    # Determines who is next in line to pay
    def determine_payment_person(self, people: dict[str,Person], order : dict[str, MenuItem]) -> str:
        # Basically we find the person with the lowest debt.
        # Among the people who are actually present.
        sub_split_state = {name: self.split_state[name] for name in order.keys()}
        # Optional: Write a check to make sure they are in split_state, it shouldn't happen because apply_credits adds before this.

        lowest_debt = max(sub_split_state, key=lambda key: sub_split_state.get(key).debt)
        max_many = {key for key, state_item in sub_split_state.items() if state_item.debt == sub_split_state[lowest_debt].debt}
        logging.debug(f"Max Many: {max_many})")

        if len(max_many) > 1:
            lowest_debt = min(sub_split_state, key=lambda key: sub_split_state[key].time_last_paid)
            logging.debug(f"lowest debt: {lowest_debt}")
        return lowest_debt

    def charge_person(self, order_total: float, person_name: str):
        # This applies the debt to a person.
        # Keep track of a counter and anytime it hits 365 reset it to 0
        # Also if two people have the same last week paid pick one at random and move on.
        coffee_state = self.split_state.get(person_name)
        logging.debug(f"order_total {order_total}")
        coffee_state.debt -= order_total
        coffee_state.time_last_paid = self.current_day_num
        self.current_day_num += 1
        if self.current_day_num > 365:
            self.current_day_num = 0

    @classmethod
    def get_order_total(cls, order: dict[str, MenuItem]) -> float:
        total :float = sum(item.price for item in order.values())
        return round(total,2)

    def apply_credits(self, order: dict[str, MenuItem]) -> None:
        # Apply Credits
        for name, item in order.items():
            self.split_state[name].debt = round(item.price + self.split_state.get(name).debt, 2)

        # Determine Payment Person
    def initialize_state(self, people: List[str]):
        self.split_state = {name : SplitCoffeeState(name) for name in people}

# if the state is name: price
# for item in orders get order key and order item.price
# get state[key] += item.price
# Tracking Highest...
# if previous_highest == state[key] ## Tie case
# if previous_highest < state[key] then state[key] is new highest
# if previous_highest > state[key] nothing happens.

# algorithms_availablea
# async algorithms_availablea
# async algorithms_availablea
# async a
