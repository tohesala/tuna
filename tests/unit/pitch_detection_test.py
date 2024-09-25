from hypothesis import given
from hypothesis import strategies as st

from tests.base import TestBase
from tuna.pitch_detection import detect_pitch_simple
from tuna.wavegen import make_sine_wave


class SimplePitchDetectionTests(TestBase):
    def test_pitch_of_sine_wave(self):
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
