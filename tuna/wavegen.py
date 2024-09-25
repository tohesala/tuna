from math import floor, pi, sin

from tuna.types import RealSequence


def make_sine_wave(frequency, sample_rate=4096, duration=1) -> RealSequence:
    """
    Generate a sine wave of a given frequency.

    Args:
        frequency: The frequency of the sine wave in Hz.
        sample_rate: The sample rate of the signal.
        duration: The duration of the signal in seconds.

    Returns:
        The sine wave as a sequence of real valued samples.
    """
    t = [i / sample_rate for i in range(int(sample_rate * duration))]
    return [sin(2 * pi * frequency * ti) for ti in t]


def make_square_wave(frequency, sample_rate=4096, duration=1) -> RealSequence:
    """
    Generate a square wave of a given frequency.

    Args:
        frequency: The frequency of the square wave in Hz.
        sample_rate: The sample rate of the signal.
        duration: The duration of the signal in seconds.

    Returns:
        The square wave as a sequence of real valued samples.
    """
    t = [i / sample_rate for i in range(int(sample_rate * duration))]
    return [(-1)**floor(2*frequency*ti) for ti in t]
