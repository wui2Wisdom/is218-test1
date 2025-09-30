# Python Calculator - TinyTools Inc.

A professional Python calculator module implementing four basic operations with full test coverage.

## Features

- Addition
- Subtraction  
- Multiplication
- Division (with proper error handling for division by zero)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest -q
   ```

3. Check coverage:
   ```bash
   coverage run -m pytest
   coverage report
   ```

4. Run linting:
   ```bash
   pylint --errors-only src
   ```

## Usage

```python
from calculator import Calculator

calc = Calculator()
result = calc.add(2, 3)  # Returns 5
```