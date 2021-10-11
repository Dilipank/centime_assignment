# Setup
Ensure python3 and pipenv are installed.
Clone this repository.
Navigate to the cloned folder.

# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install

# Run tests via pytest
pytest --html=report.html

# HTML report
A html file with the name provided while running the test will be created with the test details.
