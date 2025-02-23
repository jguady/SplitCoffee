import errno
import logging
import os.path
import pathlib
import json
import typing

from splitcoffee.model.Menu import Menu
from splitcoffee.model.MenuItem import MenuItem
from splitcoffee.model.Person import Person


class CoffeeShop:

    #resources folder constant path
    RESOURCES_PATH = pathlib.Path(__file__).parent / "resources"
    menu: Menu
    people: dict[str, Person]
    order: typing.List[MenuItem] = []

    def __init__(self, menu_file_path : str =RESOURCES_PATH / "menu_items.json", person_file_path : str =RESOURCES_PATH / "people.json" ):
        logging.info(CoffeeShop.RESOURCES_PATH)
        self.menu = Menu()

    # loads the menu items from the menu_items.json
    def load_menu(self, menu_file_path):
        file_path = os.path.join(CoffeeShop.RESOURCES_PATH, menu_file_path)
        if os.path.isfile(file_path):
            logging.info(f" Menu File exists: Loading menu from {file_path}")
            with open(file_path, 'r') as menu:
                # self.menu = json.load(menu, object_hook=lambda d: SimpleNamespace(**d))
                menu_data = json.load(menu)
                menu = Menu()
                menu.from_list(menu_data)
                logging.debug(self.menu)

        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)

    # Loads the people data from people.json
    def load_people(self, people_file_path):
        file = os.path.join(CoffeeShop.RESOURCES_PATH, people_file_path)
        if os.path.isfile(file):
            logging.info(f" People File exists: Loading people data from {file}")
            with open(file, 'r') as people:
                people_data = json.load(people)
                self.people = {person.name: Person(person) for person in people_data}
                logging.debug(self.people)
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)

    #Loops through each of the people in the coffee shop and collects their order into a list called order
    def take_orders(self) -> None:
        self.order : typing.List[*MenuItem] = []

        for name, person in self.people.items():
            self.order.append(person.get_order(self.menu))


