from src.file_handling import read_file, write_file 
from src.cli import create_command_line_arguments
from src.greeting_operations import add_greeting, remove_greeting, is_index_in_list_range
from src.display import print_list, print_rainbow_text
from src.constants import GREETINGS_FILENAME

import random

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
        
    else:
        # Get random greeting from the list of greetings
        selected_greeting = greetings[random.randint(0, len(greetings) - 1)]
        print_rainbow_text(selected_greeting)

        
if __name__ == "__main__":
    main()