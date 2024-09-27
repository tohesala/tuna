from tuna.fft import fft
from tuna.filtering import hamming_window
from tuna.types import RealSequence
from tuna.utils import argmax


def detect_pitch(signal: RealSequence, sample_rate: int) -> float:
    """
    Detects the pitch of a signal using the simple method of finding the peak in
    the magnitude spectrum. This will basically only work reliably for signals
    with no noise and no harmonics.

    Args:
        signal: The input signal as a sequence of discrete real valued samples.
        sample_rate: The sample rate of the signal.

    Returns:
        The detected pitch in Hz.
    """
    N = len(signal)
    signal = [s * w for s, w in zip(signal, hamming_window(N))]
    spectrum = fft(signal)
    mag = [abs(x) for x in spectrum]
    resolution = sample_rate / N
    # The spectrum of a real valued signal is symmetric so we only need to look
    # at the first half.
    peak = argmax(mag[:N//2])
    return peak * resolution
