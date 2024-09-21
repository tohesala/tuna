from tests.base import TestBase
from tuna.pitch_detection import detect_pitch_simple
from hypothesis import given, strategies as st


def make_sine_wave(f, sample_rate=4096):
    from math import sin, pi
    return [sin(2 * pi * f * t / sample_rate) for t in range(sample_rate)]


class SimplePitchDetectionTests(TestBase):
    def test_pitch_of_sine_wave_foo(self):
        # Below, the four samples represent a single full period of a sine wave.
        # If we say that the signal came with a sample rate of 4, then it means
        # the period is exactly 1 second -> the frequency of the sine wave is
        # 1Hz.
        signal = [0, 1, 0, -1]
        sample_rate = 4
        self.assertEqual(detect_pitch_simple(signal, sample_rate), 1)

        # With a sample rate of 8, the period of the same sampled wave
        # becomes 0.5 seconds so the frequency should be 2Hz.
        sample_rate = 8
        self.assertEqual(detect_pitch_simple(signal, sample_rate), 2)

    @given(st.integers(min_value=1, max_value=2000))
    def test_pitch_of_sine_wave_hypothesis(self, f):
        signal = make_sine_wave(f, 4096)
        predicted = detect_pitch_simple(signal, 4096)
        print(f"expected: {f}, predicted: {predicted}")
        self.assertAlmostEqual(predicted, f)
