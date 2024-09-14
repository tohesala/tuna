"""
Miscellaneous utility functions.
"""


def is_power_of_two(n: int) -> bool:
    """
    Check if a number is a power of two.

    Args:
        n: The number to check.

    Returns:
        True if n is a power of two, False otherwise.
    """
    # any power of two will have exactly one bit set in its binary
    # representation
    return n.is_integer() and int(n) & (int(n) - 1) == 0
