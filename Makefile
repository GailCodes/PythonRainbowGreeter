# Define the virtual environment directory
VENV_DIR = venv

# Define the requirements file
REQUIREMENTS = requirements.txt

# Create virtual environment
$(VENV_DIR)/bin/activate: $(REQUIREMENTS)
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Installing dependencies from $(REQUIREMENTS)..."
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Install dependencies (if the virtual environment exists)
install: $(VENV_DIR)/bin/activate
	@echo "Installing dependencies in the virtual environment..."
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Remove the virtual environment (useful for cleanups)
clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)

# Run Python scripts within the virtual environment
run:
	@echo "Running the Python script in the virtual environment..."
	$(VENV_DIR)/bin/python3 term_greeter.py


# Update the requirements.txt with currently installed packages in the virtual environment
update-reqs:
	@echo "Updating requirements.txt with installed packages..."
	$(VENV_DIR)/bin/pip freeze > $(REQUIREMENTS)
