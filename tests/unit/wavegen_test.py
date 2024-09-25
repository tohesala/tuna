from hypothesis import given
from hypothesis import strategies as st

from tests.base import TestBase
from tuna.wavegen import make_sine_wave, make_square_wave


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
        # a sine wave, that has an integer frequency, and its reverse should be
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


class MakeSquareWaveTests(TestBase):
    def test_1hz_sampled_at_4hz(self):
        self.assertListsAlmostEqual(make_square_wave(1, 4), [1, 1, -1, -1])

    def test_1hz_sampled_at_8hz(self):
        self.assertListsAlmostEqual(
            make_square_wave(1, 8),
            [1, 1, 1, 1, -1, -1, -1, -1])

    def test_4hz_sampled_at_16hz(self):
        self.assertListsAlmostEqual(
            make_square_wave(4, 16),
            [1, 1, -1, -1] * 4)

    def test_21hz_sampled_at_16hz(self):
        self.assertListsAlmostEqual(
            make_square_wave(4, 16),
            [1, 1, -1, -1] * 4)

    def test_square_wave_symmetry(self):
        # a square wave, whose frequency is a rational multiple of the sample
        # rate, should be symmetric around 0
        wave = make_square_wave(256, 4096)
        expected = [-x for x in wave[::-1]]
        self.assertListsAlmostEqual(wave, expected, places=2)

    @given(st.integers(min_value=1, max_value=2000))
    def test_square_wave_sum_hypothesis(self, f):
        wave = make_square_wave(f, 4096)
        self.assertAlmostEqual(sum(wave), 0)
