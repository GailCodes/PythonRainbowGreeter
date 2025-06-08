import os
import sys
import json
import shutil
from pathlib import Path

def get_data_path(filename):
    if getattr(sys, 'frozen', False): # Check if is being run as a compiled binary (pyinstaller app)
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
        template_path = os.path.join(base_path, filename)
        
        # Writable location in user's config directory
        app_data_dir = os.path.join(Path.home(), ".python-rainbow-greeter")
        os.makedirs(app_data_dir, exist_ok=True)
        writable_path = os.path.join(app_data_dir, filename)
        
        # Copy template if writable file doesn't exist
        if not os.path.exists(writable_path):
            try:
                shutil.copyfile(template_path, writable_path)
            except FileNotFoundError:
                # If template doesn't exist, create default file
                with open(writable_path, 'w') as f:
                    json.dump(["Hello World!", "Hola Mundo!", "Bonjour le Monde!"], f)
        
        return writable_path
    else:
        # Running in normal Python environment
        return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), filename)

# Define the path to greetings.json
GREETINGS_FILENAME = get_data_path("greetings.json")