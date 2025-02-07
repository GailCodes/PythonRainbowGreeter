import random
import json
import time
import argparse
from colorama import Fore, init


COLORS = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]


def main():
    # Get greetings from file
    greetings = readFile("greetings.json")
    
    command_line_arguments = createCommandLineArguments()

    if command_line_arguments.list_all:
        print(greetings)
    else:
        # Get random greeting from the list of greetings
        selected_greeting = greetings[random.randint(0, len(greetings) - 1)]

        printRainbowText(selected_greeting)

        # Print a newline so terminal doesn't look weird
        print("\n", end="")


def createCommandLineArguments():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--list-all", action="store_true", help="List all phrases")
    args_parser.add_argument("--add", action="store_true", help="Add a phrase")
    args_parser.add_argument("--remove", action="store_true", help="Remove a phrase")

    return args_parser.parse_args()
    

def readFile(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The greetings file does not exist")
        exit


def printRainbowText(text):
    # Initialize colorama
    init(autoreset=True)

    # Print the greeting with a rainbow effect
    for i, char in enumerate(text):
        color = COLORS[i % len(COLORS)]
        print(color + char, end="", flush=True)
        time.sleep(0.03)


if __name__ == "__main__":
    main()