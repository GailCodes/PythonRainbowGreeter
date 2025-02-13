from src.file_handling import write_file
from src.constants import GREETINGS_FILENAME
from src.display import print_list

def add_greeting(new_greeting, greetings):
    # Add the new greeting to the current list of greetings and save to the file
    greetings.append(new_greeting)
    write_file(GREETINGS_FILENAME, greetings)
    print(f"New greeting: \"{new_greeting}\" has been added!")
        

def remove_greeting(index_to_remove, greetings):
    # Remove the greeting with the selected index        
    if is_index_in_list_range(greetings, index_to_remove):
        removed_greeting = greetings.pop(index_to_remove)
        write_file(GREETINGS_FILENAME, greetings)
        print(f"Successfully removed greeting {index_to_remove}: \"{removed_greeting}\"")

        # Show updated list of greetings after removal
        print_list(greetings)


def is_index_in_list_range(lst, index):
    if 0 <= index < len(lst):
        return True
    else:
        print("Oops! Looks like that greeting index is incorrect.")
        return False