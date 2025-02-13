from json import load, dump

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return load(file)
    except FileNotFoundError:
        print("The greetings file does not exist")
        exit()
        

def write_file(filename, data):
    try:
        with open(filename, "w") as file:
            dump(data, file, indent=4)
    except Exception as e:
        print(f"Oops! There was an error saving the file: {e}")
        exit()