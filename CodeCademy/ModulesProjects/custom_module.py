"""Utility functions for the Time Travelers Toolkit.

This module provides a single helper to build a user-facing time travel message.
"""

from decimal import Decimal
from typing import Union


def generate_time_travel_message(year: int, destination: str, cost: Union[Decimal, float, int]) -> str:
    """Return a formatted time-travel message including the cost.

    The cost is formatted to two decimal places.
    """

    try:
        # Use Decimal for consistent formatting if possible
        cost_decimal = Decimal(cost)
    except Exception:
        # Fallback: convert to string if Decimal conversion fails
        return f"Pack your bags! You're traveling to {destination} in the year {year}. The cost of this trip will be ${cost}."

    return (
        f"Pack your bags! You're traveling to {destination} in the year {year}. "
        f"The cost of this trip will be ${cost_decimal:.2f}."
    )
