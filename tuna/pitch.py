from tuna.fft import fft
from tuna.filtering import hamming_window
from tuna.utils import argmax


def detect_pitch(signal: list[int | float], sample_rate: int) -> float:
    """
    Detects the pitch of a signal using the simple method of finding the peak in
    the magnitude spectrum. This will basically only work reliably for signals
    with no noise and no harmonics.

    Args:
        signal: The input signal as a list of discrete real valued samples.
        sample_rate: The sample rate of the signal.

    Returns:
        The detected pitch in Hz.
    """
    n = len(signal)
    signal = [s * w for s, w in zip(signal, hamming_window(n))]
    spectrum = fft(signal)
    mag = [abs(x) for x in spectrum]
    resolution = sample_rate / n
    # The spectrum of a real valued signal is symmetric so we only need to look
    # at the first half.
    peak = argmax(mag[:n//2])
    return peak * resolution
