.PHONY: install test lint format check-format check-imports ci-check clean

# Install dependencies
install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install black

# Run tests with coverage
test:
	pytest --cov=src --cov-report=term-missing --cov-fail-under=100

# Run pylint
lint:
	pylint src/ tests/ --fail-under=8.0

# Format code with black and isort
format:
	black src/ tests/
	isort src/ tests/

# Check code formatting (dry run)
check-format:
	black --check --diff src/ tests/

# Check import sorting (dry run)
check-imports:
	isort --check-only --diff src/ tests/

# Run all CI checks locally (same as GitHub Actions)
ci-check: check-imports check-format lint test
	@echo "✅ All CI checks passed!"

# Clean up generated files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage coverage.xml .pytest_cache
