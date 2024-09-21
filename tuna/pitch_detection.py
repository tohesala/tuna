
from math import log2, ulp
from tuna.fft import fft, ifft
from tuna.typing import RealSequence
from tuna.utils import argmax

# The smallest possible difference between two floating point numbers. This is
# used to avoid taking the log of zero.
EPS = ulp(1.0)


def detect_pitch_simple(signal: RealSequence, sample_rate: int) -> float:
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
    spectrum = fft(signal)[:N//2]
    mag = [abs(x) for x in spectrum]
    resolution = sample_rate / N
    peak = argmax(mag)
    return peak * resolution


def detect_pitch_cepstral(signal: RealSequence, sample_rate: int) -> float:
    """
    Detects the pitch of a signal using cepstral analysis.

    Args:
        signal: The input signal as a sequence of discrete real valued samples.
        sample_rate: The sample rate of the signal.

    Returns:
        The detected pitch in Hz.
    """
    spectrum = fft(signal)
    log_spectrum = [log2(abs(f + EPS)) for f in spectrum]
    cepstrum = ifft(log_spectrum)
    # The peak of the cepstrum (which is a time domain sequence) corresponds to
    # the period of the fundamental frequency, i.e. the pitch.
    return sample_rate * argmax(cepstrum) / len(signal)
