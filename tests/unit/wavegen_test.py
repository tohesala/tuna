from hypothesis import given
from hypothesis import strategies as st

from tests.base import TestBase
from tuna.wavegen import make_sine_wave


class MakeSineWaveTests(TestBase):
    def test_1hz_sampled_at_4hz(self):
        self.assertListsAlmostEqual(
            make_sine_wave(1, 4),
            [0, 1, 0, -1])

    def test_1hz_sampled_at_8hz(self):
        self.assertListsAlmostEqual(
            make_sine_wave(1, 8),
            [0, 0.71, 1, 0.71, 0, -0.71, -1, -0.71],
            places=2)

    def test_2hz_sampled_at_4hz(self):
        self.assertListsAlmostEqual(
            make_sine_wave(2, 4),
            [0, 0, 0, 0])

    def test_2hz_sampled_at_8hz(self):
        self.assertListsAlmostEqual(
            make_sine_wave(2, 8),
            [0, 1, 0, -1, 0, 1, 0, -1])

    def test_2hz_sampled_at_32hz(self):
        wave = make_sine_wave(2, 32)
        expected = [0.0, 0.383, 0.707, 0.924,
                    1.0, 0.924, 0.707, 0.383,
                    0.0, -0.383, -0.707, -0.924,
                    -1.0, -0.924, -0.707, -0.383,
                    -0.0, 0.383, 0.707, 0.924,
                    1.0, 0.924, 0.707, 0.383,
                    0.0, -0.383, -0.707, -0.924,
                    -1.0, -0.924, -0.707, -0.383]
        self.assertListsAlmostEqual(wave, expected, places=2)

    @given(st.integers(min_value=1, max_value=2000))
    def test_sine_wave_symmetry_hypothesis(self, f):
        # a wave, that has an integer frequency, and its reverse should be
        # symmetric around 0
        wave = make_sine_wave(f, 4096)
        expected = [-x for x in wave[::-1]]
        self.assertListsAlmostEqual(wave[1:], expected[:-1], places=2)

    @given(st.integers(min_value=1, max_value=2000))
    def test_sine_wave_sum_hypothesis(self, f):
        # the sum of the sample magnitudes should be 0 for a sine wave that has
        # an integer frequency
        wave = make_sine_wave(f, 4096)
        self.assertAlmostEqual(sum(wave), 0)
