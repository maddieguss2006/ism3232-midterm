import pytest

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def test_calculate_food_cost():
    assert calculate_food_cost(20.0, 10) == 200.0


def test_calculate_food_cost_with_zero_guests():
    assert calculate_food_cost(20.0, 0) == 0.0


def test_no_discount_below_25_guests():
    assert get_event_discount(24) == 0.0


def test_discount_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_standard_discount_below_100_guests():
    assert get_event_discount(99) == 0.05


def test_standard_discount_at_100_guests():
    assert get_event_discount(100) == 0.05


def test_nonprofit_discount_at_100_guests():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_nonprofit_discount_below_100_guests():
    assert get_event_discount(99, nonprofit=True) == 0.05


def test_event_total_with_service_fee():
    assert calculate_event_total(10.0, 10) == 175.0


def test_event_total_without_service_fee():
    assert calculate_event_total(20.0, 30) == 570.0


def test_service_fee_applies_at_500():
    assert calculate_event_total(25.0, 20) == 575.0


def test_service_fee_boundary():
    assert calculate_event_total(25.05, 20) == pytest.approx(501.0)


def test_signoff_not_needed_at_2500():
    assert needs_signoff(2500.0) is False


def test_signoff_needed_above_2500():
    assert needs_signoff(2500.01) is True


def test_second_chef_not_needed_at_80_guests():
    assert needs_second_chef(80, 1000.0) is False


def test_second_chef_needed_above_80_guests():
    assert needs_second_chef(81, 1000.0) is True


def test_second_chef_needed_at_3000_total():
    assert needs_second_chef(50, 3000.0) is True


def test_second_chef_not_needed_below_3000_total():
    assert needs_second_chef(50, 2999.99) is False


def test_total_booked():
    events = [
        {"guest_price": 10.0, "guests": 10, "nonprofit": False},
        {"guest_price": 20.0, "guests": 10, "nonprofit": False},
    ]
    assert total_booked(events) == 450.0


def test_total_booked_empty_list():
    assert total_booked([]) == 0.0


def test_largest_event():
    events = [
        {
            "client": "Small Event",
            "guest_price": 10.0,
            "guests": 10,
            "nonprofit": False,
        },
        {
            "client": "Large Event",
            "guest_price": 30.0,
            "guests": 100,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Large Event"


def test_largest_event_empty_list():
    assert largest_event([]) == ""


def test_format_event_line():
    result = format_event_line("Finch Law", 435.0, False, False)
    assert result == ("Finch Law: $435.00 | sign-off: no | second chef: no")
def test_largest_event_returns_first_on_tie():
    """Return the first client when event totals are equal."""
    events = [
        {
            "client": "First Client",
            "guest_price": 20.0,
            "guests": 30,
            "nonprofit": False,
        },
        {
            "client": "Second Client",
            "guest_price": 20.0,
            "guests": 30,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "First Client"
