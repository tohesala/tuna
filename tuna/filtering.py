
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


def noise_gate(signal, thresh=50):
    """
    Apply a noise gate to the signal. Samples with magnitude below the threshold
    are set to zero.

    Args:
        signal: The input signal.
        thresh: The threshold value.

    Returns:
        The signal with the noise gate applied.
    """
    return [0 if abs(x) < thresh else x for x in signal]
