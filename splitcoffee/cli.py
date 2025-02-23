import logging

from splitcoffee.CoffeeShop import CoffeeShop
from splitcoffee.service.SplitCoffeeService import SplitCoffeeService


def print_welcome():

    print("""
Welcome to splitcoffee cli
Type 'help' to see available commands
Type 'q' to quit the program
    """)

def print_commands():
    print(
"""The available commands are:
start - starts the program with the default settings
help - print this help message
q(uit) - exits the program

    """)
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    """
    Main Entry Point of the application

    :return:
    """
    ## Main Loop ##
    print_welcome()
    coffeeshop = CoffeeShop()


    while True:
        user_input = input("Enter command: ")

        if user_input.lower().strip() == 'q':
            break
        if user_input.lower().strip() == 'd':
            coffee = CoffeeShop()
        if user_input.lower().strip() == 'help':
            print_commands()

        if user_input.lower().strip() == 'start':
            print("The next person to pay is...")
            coffeeshop.load_menu("splitcoffee/resources/menu_items.json")
            coffeeshop.load_people("splitcoffee/resources/people.json")
            coffeeshop.take_orders()

        logging.debug(f"You entered: {user_input}")



