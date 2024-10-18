"""
This module contains functions for taking the Discrete Fourier Transform of a
signal, and its inverse. The algorithm is basically the one suggested by Cooley
and Tukey in 1965, as discussed in Introduction to Algorithms (CLRS).
"""

from cmath import exp, pi

from tuna.utils import is_power_of_two


def fft(x: list[int | float]) -> list[complex]:
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
    n = len(x)
    if not is_power_of_two(len(x)):
        raise ValueError("Input length must be a power of two.")
    if n == 1:
        return x
    dft = [0] * n
    even = fft(x[::2])
    odd = fft(x[1::2])
    for k in range(n // 2):
        twiddle_factor = exp(-2j * pi * k / n)
        dft[k] = even[k] + twiddle_factor * odd[k]
        dft[k + n // 2] = even[k] - twiddle_factor * odd[k]
    return dft


def ifft(dft: list[complex]) -> list[complex]:
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
    if not is_power_of_two(len(dft)):
        raise ValueError("Input length must be a power of two.")

    def _ifft(dft):
        n = len(dft)
        if n == 1:
            return dft
        even = _ifft(dft[::2])
        odd = _ifft(dft[1::2])
        x = [0] * n
        for k in range(n // 2):
            twiddle_factor = exp(2j * pi * k / n)
            x[k] = even[k] + twiddle_factor * odd[k]
            x[k + n // 2] = even[k] - twiddle_factor * odd[k]
        return x

    return [x / len(dft) for x in _ifft(dft)]
