# ISM3232 Midterm: Harvest Table Catering

- **Name:** Madison Guss
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program calculates catering event costs and generates a report for Harvest Table Catering. It applies business rules for discounts, service fees, manager sign-off, and second-chef requirements.

## Business Rules

1. Food cost is the price per guest multiplied by the number of guests.
2. Events with fewer than 25 guests receive no discount. Events with 25–99 guests receive a 5% discount. Events with 100 or more guests receive a 12% discount if registered as a nonprofit and a 5% discount otherwise.
3. A $75 service fee is added when the discounted food cost is $500 or less.
4. Manager sign-off is required when the event total exceeds $2,500.
5. A second chef is required for events with more than 80 guests or a total of at least $3,000.

## How to Run

Activate the virtual environment, install the dependencies, and run the program:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## How to Test

Run the unit tests:

```bash
pytest -v
```

Check code style and formatting:

```bash
ruff check .
ruff format --check .
```

The test suite contains 23 tests.

## Files in This Repository

- `business_rules.py` — Business rule constants and calculation functions.
- `main.py` — Sample catering events and the event report.
- `commands.md` — Terminal commands and their outputs.
- `README.md` — Project documentation.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Files and folders excluded from Git.
- `tests/__init__.py` — Test package initialization.
- `tests/test_business_rules.py` — Unit tests for the business rules.

## AI Use Statement

There was no AI used for this exam.
