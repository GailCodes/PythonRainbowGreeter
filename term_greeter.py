import random
import json
import time
from colorama import Fore, init


# Initialize colorama
init(autoreset=True)

greetings = None
colors = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]


def main():
    # Get greetings from file
    greetings = readFile("greetings.json")

    # Get random greeting from the list of greetings
    selected_greeting = greetings[random.randint(0, len(greetings) - 1)]


    printRainbowText(selected_greeting)


    # Print a newline so terminal doesn't look weird
    print("\n", end="")


def readFile(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The greetings file does not exist")
        exit


def printRainbowText(text):
    # Print the greeting with a rainbow effect
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(color + char, end="", flush=True)
        time.sleep(0.03)

if __name__ == "__main__":
    main()