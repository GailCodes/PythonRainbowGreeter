import random
import json
import time
from colorama import Fore, init


# Initialize colorama
init(autoreset=True)

greetings = None
colors = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]


# Get greetings from file
try:
    with open("greetings.json", "r") as file:
        greetings = json.load(file)
except FileNotFoundError:
    print("The greetings file does not exist")
    exit


# Get random greeting from the list of greetings
selected_greeting = greetings[random.randint(0, len(greetings) - 1)]


# Print the greeting with a rainbow effect
for i, char in enumerate(selected_greeting):
    color = colors[i % len(colors)]
    print(color + char, end="", flush=True)
    time.sleep(0.03)


# Print a newline so terminal doesn't look weird
print("\n", end="")

