import unittest

from tests.base import TestBase
from tuna.pitch_detection import detect_pitch


class PitchDetectionTests(TestBase):
    def test_pitch_of_sine_wave(self):
        # Below, the four samples represent a single full period of a sine wave.
        # If we say that the signal came with a sample rate of 4, then it means
        # the period is exactly 1 second -> the frequency of the sine wave is
        # 1Hz.
        signal = [0, 1, 0, -1]
        sample_rate = 4
        self.assertEqual(detect_pitch(signal, sample_rate), 1)
