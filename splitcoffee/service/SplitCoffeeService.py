

import splitcoffee.CoffeeShop
from splitcoffee.model.MenuItem import MenuItem
from splitcoffee.model.Person import Person


class SplitCoffeeService:


    def __init__(self):
        pass


    def determine_payment_person(self, people: dict[str,Person], order : dict[str, MenuItem]) -> str:
        return "John"