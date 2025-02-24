import logging
import os.path
import sys

from splitcoffee.CoffeeShop import CoffeeShop


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
q - exits the program

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
        print('\n')
        user_input = input("Enter command: ")

        if user_input.lower().strip() == 'q':
            sys.exit(0)
        if user_input.lower().strip() == 'd':
            coffee = CoffeeShop()
        if user_input.lower().strip() == 'help':
            print_commands()

        if user_input.lower().strip() == 'start':
            print("Press Ctrl+C to stop.")
            coffeeshop.load_menu(os.path.join("menu_items.json"))
            coffeeshop.load_people(os.path.join("people.json"))
            while True:
                try:
                    coffeeshop.take_orders()
                    print("Please wait while we make the drinks and total the order")
                    # for i in range(len(coffeeshop.order.items())):
                    #     # sleep(3)
                    #     print("Order's ready!!")

                    name, amount = coffeeshop.present_bill()
                    print(f"{name} was charged for {amount} dollars")
                    user_input = input("Press Enter to continue...\nType s and Press enter to stop\n")
                    if user_input.lower().strip() == 's':
                        print("Reminder: you'll still need to type q to quit")
                        break
                    if user_input.lower().strip() == 'q':
                        sys.exit(0)
                except KeyboardInterrupt:
                    sys.exit(0)

        logging.debug(f"You entered: {user_input}")



