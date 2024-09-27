
from math import cos, pi
from tuna.types import RealSequence


def hamming_window(n: int) -> RealSequence:
    """
    Creates a Hamming window.

    Args:
        n: The size of the window.

    Returns:
        A list of n Hamming window coefficients.
    """
    return [0.54 - 0.46 * cos(2 * pi * i / (n - 1)) for i in range(n)]
