.PHONY: format lint tests all

# Format code using black and isort
format:
	black .
	isort .

# Lint code with pylint (checks both src and test directories)
lint:
	pylint src test

# Run tests using pytest
tests:
	pytest

# Run all tasks: format, lint, and test
all: format lint test
