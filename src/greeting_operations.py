from src.file_handling import write_file
from src.display import print_list

def add_greeting(new_greeting, greetings):
    greetings.append(new_greeting)
    write_file(greetings)  
    print(f"New greeting: \"{new_greeting}\" has been added!")

def remove_greeting(index_to_remove, greetings):
    if is_index_in_list_range(greetings, index_to_remove):
        removed_greeting = greetings.pop(index_to_remove)
        write_file(greetings)  
        print(f"Successfully removed greeting {index_to_remove}: \"{removed_greeting}\"")
        # Show updated list of greetings after removal
        print_list(greetings)

def is_index_in_list_range(lst, index):
    """Check if index is valid for the given list"""
    if 0 <= index < len(lst):
        return True
    else:
        print("Oops! That greeting does not exist.")
        return False