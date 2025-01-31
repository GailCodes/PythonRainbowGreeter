import random
import json

greetings = None

try:
    with open("greetings.json", "r") as file:
        greetings = json.load(file)
except FileNotFoundError:
    print("The greetings file does not exist")
    exit


# Print the greeting
print(greetings[random.randint(0, len(greetings) - 1)])
