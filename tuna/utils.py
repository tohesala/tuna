"""
Miscellaneous utility functions.
"""


from typing import Sequence


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
    return int(n) & (int(n) - 1) == 0


def argmax(t: Sequence[int | float]) -> int:
    """
    Return the index of the maximum element in a sequence.

    Args:
        t: The sequence to search.

    Returns:
        The index of the maximum element in the sequence.
    """
    if len(t) == 0:
        raise ValueError("Can not find the argmax of an empty sequence.")
    return max(enumerate(t), key=lambda x: x[1])[0]
