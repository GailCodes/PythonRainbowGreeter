import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to greetings.json in the root directory
GREETINGS_FILENAME = os.path.join(ROOT_DIR, "greetings.json")