import argparse
import logging

from splitcoffee.cli import main

if __name__ == "__main__": 
    # Create arg parser
    parser = argparse.ArgumentParser(description='Split coffee into smaller chunks')

    # Add Arguments below
    parser.add_argument(
        "-v",
        "--verbose",
        help="increases logging level to DEBUG",
        action="store_true")

    # parse
    args = parser.parse_args()

    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    main(args, loglevel)