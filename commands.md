# Terminal Record: Harvest Table Catering

## 1. Building the project

The project was created in the `ism3232-midterm` directory. A Python virtual environment was created and activated, dependencies were installed, and Git was initialized and connected to the GitHub repository.

```bash
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
git init
git remote add origin https://github.com/maddieguss2006/ism3232-midterm.git
```

The project files were created and edited using Nano. The dependencies were recorded in `requirements.txt`, and `.gitignore` was configured to exclude the virtual environment, Python cache files, and pytest cache.

## 2. The virtual environment

Command:

```bash
which python3
```

Output:

```text
/home/madisonguss2006/ism3232-midterm/.venv/bin/python3
```

This confirms that Python is running from the project's virtual environment.

## 3. The project structure

Command:

```bash
tree -L 2
```

Output:

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The project contains the main program, business rules, documentation, dependencies, and unit tests. Python cache directories are generated automatically when Python runs.

## 4. Every function and test

Commands:

```bash
rg -n 'def ' business_rules.py tests/test_business_rules.py
pytest -v
```

Function and test output:

```text
tests/test_business_rules.py
15:def test_calculate_food_cost():
19:def test_calculate_food_cost_with_zero_guests():
23:def test_no_discount_below_25_guests():
27:def test_discount_at_25_guests():
31:def test_standard_discount_below_100_guests():
35:def test_standard_discount_at_100_guests():
39:def test_nonprofit_discount_at_100_guests():
43:def test_nonprofit_discount_below_100_guests():
47:def test_event_total_with_service_fee():
51:def test_event_total_without_service_fee():
55:def test_service_fee_applies_at_500():
59:def test_service_fee_boundary():
63:def test_signoff_not_needed_at_2500():
67:def test_signoff_needed_above_2500():
71:def test_second_chef_not_needed_at_80_guests():
75:def test_second_chef_needed_above_80_guests():
79:def test_second_chef_needed_at_3000_total():
83:def test_second_chef_not_needed_below_3000_total():
87:def test_total_booked():
95:def test_total_booked_empty_list():
99:def test_largest_event():
117:def test_largest_event_empty_list():
121:def test_format_event_line():

business_rules.py
13:def calculate_food_cost(guest_price: float, guests: int) -> float:
18:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
29:def calculate_event_total(
43:def needs_signoff(total: float) -> bool:
48:def needs_second_chef(guests: int, total: float) -> bool:
53:def total_booked(events: list) -> float:
65:def largest_event(events: list) -> str:
83:def format_event_line(
```

Test results:

```text
========================== test session starts ==========================
platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.7.0
collected 23 items

23 passed in 0.05s
```

All 23 tests passed. The tests cover food costs, discount boundaries, service fees, sign-off requirements, second-chef requirements, totals, the largest event, and report formatting.

## 5. Which files print

Command:

```bash
rg -l 'print' --glob '*.py' .
```

Output:

```text
./main.py
```

Only `main.py` contains a print statement. It displays the catering event report. The functions in `business_rules.py` return calculated values instead of printing them.

## 6. The commit history

Command:

```bash
git log --format="%h %ad %s" --date=local
```

Output:

```text
0dd1321 Sun Oct 25 20:38:55 2026 Document project in README
d81140a Sun Oct 25 20:34:23 2026 Build catering event report
676aa09 Sun Oct 25 20:34:08 2026 Add business rule unit tests
e6b23e6 Sun Oct 25 20:33:56 2026 Implement catering business rules
a9b23a1 Sun Oct 25 20:33:40 2026 Set up project configuration and dependencies
```

The output shows five commits at the time this command was run. The README has its own separate commit, and the terminal record is maintained in a separate file.
