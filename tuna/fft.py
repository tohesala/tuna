"""
This module contains functions for taking the Discrete Fourier Transform of a
signal, and its inverse. The algorithm is basically the one suggested by Cooley
and Tukey in 1965, as discussed in Introduction to Algorithms (CLRS).
"""

from cmath import exp, pi

from tuna.types import ComplexSequence, RealSequence
from tuna.utils import is_power_of_two


def fft(x: RealSequence) -> ComplexSequence:
    """
    Implements the Fast Fourier Transform (FFT) algorithm. The algorithm follows
    the variant of Cooley-Tukey that is discussed in Introduction to Algorithms
    by CLRS.

    [Cooley-Tukey FFT algorithm
    (Wikipedia)](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)

    Args:
        x: The input signal as a sequnce of discrete real valued samples. The
        list needs to be non empty and have a size that is a power of two.

    Returns:
        The complex-valued spectrum of the input signal.
    """
    N = len(x)

    if N == 0:
        raise ValueError("Input sequence must not be empty.")
    if not is_power_of_two(len(x)):
        raise ValueError("Input length must be a power of two.")

    if N == 1:
        return x
    X = [0] * N
    even = fft(x[::2])
    odd = fft(x[1::2])
    for k in range(N // 2):
        twiddle_factor = exp(-2j * pi * k / N)
        X[k] = even[k] + twiddle_factor * odd[k]
        X[k + N // 2] = even[k] - twiddle_factor * odd[k]
    return X


def ifft(X: ComplexSequence) -> ComplexSequence:
    """
    Implements the Inverse Fast Fourier Transform (IFFT) algorithm. The
    algorithm is basically the same as the FFT algorithm, but with the twiddle
    factors negated.

    Args:
        X: The complex-valued spectrum of a signal. The list needs to be non
        empty and have a size that is a power of two.

    Returns:
        The inverse fourier signal (complex valued).
    """
    N = len(X)

    if N == 0:
        raise ValueError("Input sequence must not be empty.")
    if not is_power_of_two(N):
        raise ValueError("Input length must be a power of two.")

    def _ifft(X):
        n = len(X)
        if n == 1:
            return X
        even = _ifft(X[::2])
        odd = _ifft(X[1::2])
        x = [0] * n
        for k in range(n // 2):
            twiddle_factor = exp(2j * pi * k / n)
            x[k] = even[k] + twiddle_factor * odd[k]
            x[k + n // 2] = even[k] - twiddle_factor * odd[k]
        return x

    return [x / N for x in _ifft(X)]
