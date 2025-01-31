# Setup the virtual environment and install dependencies
setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Install dependencies
install-deps:
	. venv/bin/activate && pip install -r requirements.txt

# Update current dependencies
update-deps:
	. venv/bin/activate && pip freeze > requirements.txt

