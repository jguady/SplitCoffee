import logging
import os.path
import sys
from time import sleep

from splitcoffee.CoffeeShop import CoffeeShop

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    ## Main Loop ##
    coffeeshop = CoffeeShop()

    coffeeshop.load_menu(os.path.join("menu_items.json"))
    coffeeshop.load_people(os.path.join("people.json"))
    while True:
        try:
            coffeeshop.take_orders()
            print("Taking everyone's order for today and calculating the total")
            print("==============ORDERS============")
            for name,order in coffeeshop.order.items():
                sleep(.4)
                print(f"{name} order={order.name} price=${order.price:.2f} debt=${coffeeshop.split_service.split_state[name].debt:.2f} total=${(order.price + coffeeshop.split_service.split_state[name].debt):.2f}")

            name, amount = coffeeshop.present_bill()
            print("==============TOTAL=============")
            sleep(.4)
            print(f"{name} paid ${amount:.2f} for coffee today.")
            user_input = input("Press Enter to continue...\nEnter Q to quit\n")
            if user_input.lower().strip() == 'q':
                sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)




