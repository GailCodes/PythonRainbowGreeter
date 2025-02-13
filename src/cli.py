import argparse

def create_command_line_arguments():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--list", action="store_true", help="List all greetings")
    args_parser.add_argument("--show", type=int, help="Show a specific greeting by index")
    args_parser.add_argument("--add", type=str, help="Add a new greeting")
    args_parser.add_argument("--remove", type=int, help="Remove a greeting by index")

    return args_parser.parse_args()