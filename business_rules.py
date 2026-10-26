# Business rule constants
NO_DISCOUNT_GUEST_LIMIT = 25
LARGE_EVENT_GUEST_LIMIT = 100
STANDARD_DISCOUNT_RATE = 0.05
NONPROFIT_DISCOUNT_RATE = 0.12
SERVICE_FEE_LIMIT = 500.00
SERVICE_FEE = 75.00
MANAGER_SIGNOFF_LIMIT = 2500.00
SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Calculate the food cost before discounts."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate for an event."""
    if guests < NO_DISCOUNT_GUEST_LIMIT:
        return 0.0
    if guests >= LARGE_EVENT_GUEST_LIMIT:
        if nonprofit:
            return NONPROFIT_DISCOUNT_RATE
        return STANDARD_DISCOUNT_RATE
    return STANDARD_DISCOUNT_RATE


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Calculate the final cost of an event."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)

    if discounted_cost <= SERVICE_FEE_LIMIT:
        discounted_cost += SERVICE_FEE

    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Check whether an event needs manager sign-off."""
    return total > MANAGER_SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Check whether an event needs a second chef."""
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def total_booked(events: list) -> float:
    """Calculate the total cost of all booked events."""
    total = 0.0
    for event in events:
        total += calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
    return total


def largest_event(events: list) -> str:
    """Return the client with the largest event total."""
    largest_client = ""
    largest_total = -1.0

    for event in events:
        event_total = calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
        if event_total > largest_total:
            largest_total = event_total
            largest_client = event["client"]

    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Format one event as a line in the report."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )
