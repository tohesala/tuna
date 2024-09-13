from cmath import exp, pi

from tuna.typing import NumericSequence


def naive_dft(x: NumericSequence) -> NumericSequence:
    """
    Implements the Discrete Fourier Transform (DFT) using the direct definition.
    This is useful when generating test cases, as well as for testing the
    performance of the fft implementation later on (it should be much better for
    large inputs).

    [Discrete Fourier Transform
    (Wikipedia)](https://en.wikipedia.org/wiki/Discrete_Fourier_transform#Definition)

    Args:
        x: The input signal as a sequnce of discrete samples.

    Returns:
        The complex-valued spectrum of the input signal.
    """
    n = len(x)
    if n == 1:
        return x
    X = [0] * n
    for k in range(n):
        X[k] = sum(x[n] * exp(-2j * pi * k * n / n) for n in range(n))
    return X
