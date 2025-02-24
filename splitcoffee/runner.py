import argparse
import logging

from splitcoffee.cli import main

if __name__ == "__main__":  # pragma: no cover
    # Create arg parser
    parser = argparse.ArgumentParser(description='Split coffee into smaller chunks')

    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")

    # Add Arguments below
    parser.add_argument("-m", "--menu", type=str, help="Menu Prices JSON File")

    parser.add_argument("-p", "--people", type=str, help="People Joining for lunch")

    # parse
    args = parser.parse_args()

    # Call Cli Main

    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    main(args, loglevel)