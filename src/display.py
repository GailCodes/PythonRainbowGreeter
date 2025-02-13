import random
import time
from colorama import Fore, init

COLORS = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def print_list(list):
    for i in range(len(list)):
            # Show all list in order, preceded by the index
            print(f"{i}: \"{list[i]}\"")
        

def print_rainbow_text(text):
    # Initialize colorama
    init(autoreset=True)

    # Print the greeting with a rainbow effect
    for i, char in enumerate(text):
        color = COLORS[i % len(COLORS)]
        print(color + char, end="", flush=True)
        time.sleep(0.03)
    
    # Print a newline so terminal doesn't look weird
    print("\n", end="")