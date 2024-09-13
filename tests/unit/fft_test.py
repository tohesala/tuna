import unittest
import tuna.fft as fft


class TestFFT(unittest.TestCase):
    def assertListsAlmostEqual(self, a, b, places=7):
        self.assertEqual(len(a), len(b))
        for i in range(len(a)):
            try:
                self.assertAlmostEqual(a[i], b[i], places=places)
            except AssertionError as e:
                raise AssertionError(f"Lists differ at index {i}: {e}")

    def test_fft_constant_signal(self):
        # For a constant signal t the FFT should be a spike of Size(t) at zero
        # frequency
        self.assertEqual(fft.fft([1, 1, 1, 1]), [
            4+0j, 0+0j, 0+0j, 0+0j])

    def test_fft_sine_wave(self):
        # For a sine wave the FFT should be a spike of Size(t) at the frequency
        # of the sine wave
        self.assertListsAlmostEqual(
            fft.fft([0, 1, 0, -1]), [0+0j, 0-2j, 0+0j, 0+2j])

    def test_fft_cosine_wave(self):
        # For a cosine wave the FFT should be a spike of Size(t) at the frequency
        # of the cosine wave
        self.assertListsAlmostEqual(
            fft.fft([1, 0, -1, 0]), [0+0j, 2+0j, 0+0j, 2+0j])
