from cmath import exp, pi
from typing import Sequence


def naive_dft(x: Sequence[int | float]) -> Sequence[complex]:
    """
    Implements the Discrete Fourier Transform (DFT) directly using the
    definition. This is useful for testing, as the algorithm is much simpler to
    understand, and FFT should return the exact same output. This also enables
    verifying the performance characteristics of the fft implementation, as it
    should be much faster for large inputs (O(n lg n) vs O(n^2)).

    [Discrete Fourier Transform
    (Wikipedia)](https://en.wikipedia.org/wiki/Discrete_Fourier_transform#Definition)

    Args:
        x: The input signal as a sequnce of discrete samples.

    Returns:
        The complex-valued spectrum of the input signal.
    """
    N = len(x)
    if N == 1:
        return x
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * exp(-2j * pi * k * n / N)
    return X
