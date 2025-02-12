import random
import json
import time
import argparse
from colorama import Fore, init

GREETINGS_FILENAME = "greetings.json"
COLORS = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]


def main():
    # Get greetings from file
    greetings = readFile(GREETINGS_FILENAME)
    
    command_line_arguments = createCommandLineArguments()

    ###############################
    # Command line argument logic #    
    ###############################
    
    if command_line_arguments.list:
        printList(greetings)
        
    elif command_line_arguments.show != None:
        index_to_show = command_line_arguments.show
        
        if isIndexInListRange(index_to_show):
            printRainbowText(greetings[index_to_show])
            
        
    elif command_line_arguments.add:
        new_greeting = command_line_arguments.add
        
        # Add the new greeting to the current list of greetings and save to the file
        greetings.append(new_greeting)
        writeFile(GREETINGS_FILENAME, greetings)
        print(f"New greeting: \"{command_line_arguments.add}\" has been added!")

    elif command_line_arguments.remove != None:
        index_to_remove = command_line_arguments.remove
        
        if isIndexInListRange(greetings, index_to_remove):
            removed_greeting = greetings.pop(index_to_remove)

            print(f"Successfully remove greeting {index_to_remove}: \"{removed_greeting}\"")
            writeFile(GREETINGS_FILENAME, greetings)
            printList(greetings)
        
    else:
        # Get random greeting from the list of greetings
        selected_greeting = greetings[random.randint(0, len(greetings) - 1)]

        printRainbowText(selected_greeting)


def createCommandLineArguments():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--list", action="store_true", help="List all greetings")
    args_parser.add_argument("--show", type=int, help="Show a specific greeting by index")
    args_parser.add_argument("--add", type=str, help="Add a new greeting")
    args_parser.add_argument("--remove", type=int, help="Remove a greeting by index")

    return args_parser.parse_args()
    

def readFile(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The greetings file does not exist")
        exit()
        

def writeFile(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Oops! There was an error saving the file: {e}")
        exit()
        

def isIndexInListRange(list, index):
    if 0 <= index < len(list):
        return True
    else:
        print("Oops! Looks like that greeting index is incorrect.")
        
        
def printList(list):
    for i in range(len(list)):
            # Show all list in order, preceded by the index
            print(f"{i}: \"{list[i]}\"")
        

def printRainbowText(text):
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