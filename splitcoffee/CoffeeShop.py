import errno
import json
import logging
import os.path
import pathlib

from splitcoffee.model.Menu import Menu
from splitcoffee.model.MenuItem import MenuItem
from splitcoffee.model.Person import Person
from splitcoffee.service.SplitCoffeeService import SplitCoffeeService


class CoffeeShop:

    #resources folder constant path
    RESOURCES_PATH = pathlib.Path(__file__).parent / "resources"
    menu: Menu = None
    people: dict[str, Person]
    order: dict[str, MenuItem] = {}
    split_service: SplitCoffeeService

    def __init__(self):
        logging.info(CoffeeShop.RESOURCES_PATH)
        self.menu = Menu()
        self.split_service = SplitCoffeeService()


    # loads the menu items from the menu_items.json
    def load_menu(self, menu_file_path):
        file_path = os.path.join(CoffeeShop.RESOURCES_PATH, menu_file_path)
        if os.path.isfile(file_path):
            logging.debug(f" Menu File exists: Loading menu from {file_path}")
            with open(file_path, 'r') as menu:
                menu_data = json.load(menu)
                self.menu = Menu()
                self.menu.from_list(menu_data)
                logging.debug(f"Loaded Menu : {self.menu}")
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        if not self.menu.menu_items:
            raise ValueError("Menu cannot be empty")

    # Loads the people data from people.json
    def load_people(self, people_file_path):
        file = os.path.join(CoffeeShop.RESOURCES_PATH, people_file_path)
        if os.path.isfile(file):
            logging.debug(f" People File exists: Loading people data from {file}")
            with open(file, 'r') as people:
                people_data = json.load(people)
                self.people = {person["name"]: Person(person) for person in people_data}
                logging.debug(f"Loaded People: {self.people}")
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
        if not self.people:
            raise ValueError("People cannot be empty")

        self.split_service.initialize_state(list(self.people.keys()))

    #Loops through each of the people in the coffee shop and collects their order into a list called order
    def take_orders(self) -> None:
        self.order = {name : person.get_order(self.menu) for name, person in self.people.items()}
        logging.debug(f"Order: {self.order}")

    def present_bill(self) -> (str, float):
        self.split_service.apply_credits(self.order)
        logging.debug(f"State: {str(self.split_service.split_state)}")
        name = self.split_service.determine_payment_person(self.people, self.order)
        logging.debug(f"Charging : {name}")
        order_total = self.split_service.get_order_total(self.order)
        logging.debug(f"Order Total: {order_total}")
        self.split_service.charge_person(order_total, name)
        logging.debug(f"Person debt Update: {name}: {self.split_service.split_state[name].debt:.2f}")
        return name, order_total

