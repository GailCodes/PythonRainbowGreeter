import json
import sys
from src.constants import GREETINGS_FILENAME

def read_file(filename=GREETINGS_FILENAME):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The greetings file does not exist")
        sys.exit(1)
    except json.JSONDecodeError:
        print("The greetings file is corrupted")
        sys.exit(1)

def write_file(data, filename=GREETINGS_FILENAME):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Oops! There was an error saving the file: {e}")
        sys.exit(1)