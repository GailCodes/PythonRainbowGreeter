import random
import json
import time
import argparse
from colorama import Fore, init


GREETINGS_FILENAME = "greetings.json"
COLORS = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]


def main():
    # Get greetings from file
    greetings = read_file(GREETINGS_FILENAME)

    ###############################
    # Command line argument logic #    
    ###############################
    args = create_command_line_arguments()
    
    if args.list:
        print_list(greetings)
        
    elif args.show is not None:
        index_to_show = args.show
        
        if is_index_in_list_range(greetings, index_to_show):
            print_rainbow_text(greetings[index_to_show])
        
    elif args.add:
        add_greeting(args.add, greetings)

    elif args.remove is not None:
        remove_greeting(args.remove, greetings)
        write_file(GREETINGS_FILENAME, greetings)
        print_list(greetings)
        
    else:
        # Get random greeting from the list of greetings
        selected_greeting = greetings[random.randint(0, len(greetings) - 1)]
        print_rainbow_text(selected_greeting)


def create_command_line_arguments():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--list", action="store_true", help="List all greetings")
    args_parser.add_argument("--show", type=int, help="Show a specific greeting by index")
    args_parser.add_argument("--add", type=str, help="Add a new greeting")
    args_parser.add_argument("--remove", type=int, help="Remove a greeting by index")

    return args_parser.parse_args()
    

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The greetings file does not exist")
        exit()
        

def write_file(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Oops! There was an error saving the file: {e}")
        exit()

        
def add_greeting(new_greeting, greetings):
    # Add the new greeting to the current list of greetings and save to the file
    greetings.append(new_greeting)
    write_file(GREETINGS_FILENAME, greetings)
    print(f"New greeting: \"{args.add}\" has been added!")
        

def remove_greeting(index_to_remove, greetings):
    # Remove the greeting with the selected index        
    if is_index_in_list_range(greetings, index_to_remove):
        removed_greeting = greetings.pop(index_to_remove)

        print(f"Successfully removed greeting {index_to_remove}: \"{removed_greeting}\"")


def is_index_in_list_range(lst, index):
    if 0 <= index < len(lst):
        return True
    else:
        print("Oops! Looks like that greeting index is incorrect.")
        return False
        
        
def print_list(lst):
    for i in range(len(lst)):
            # Show all list in order, preceded by the index
            print(f"{i}: \"{lst[i]}\"")
        

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


if __name__ == "__main__":
    main()