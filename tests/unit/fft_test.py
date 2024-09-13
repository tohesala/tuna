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

    def test_fft_more_complex_wave(self):
        wave = [5, 1, 7, 9, 1, 7, 7, 2, 7, 9, 5, 5, 6, 2, 1, 0]
        # The asserted output was calculated directly with the DFT definition:
        # https://en.wikipedia.org/wiki/Discrete_Fourier_transform#Definition
        expected = [(74+0j),
                    (-14.449905882224153-6.675669447903423j),
                    (-2.7781745930520163-13.19238815542512j),
                    (-2.0745276663934296-1.6694261631388503j),
                    (-1.000000000000009-2.999999999999999j),
                    (3.731381915885777+19.644282335845922j),
                    (12.778174593052015-5.192388155425119j),
                    (4.793051632731775-5.361960948918666j),
                    (4-9.066100197509943e-15j),
                    (4.79305163273175+5.361960948918657j),
                    (12.778174593051999+5.192388155425099j),
                    (3.731381915885874-19.64428233584591j),
                    (-1.0000000000000546+2.9999999999999876j),
                    (-2.074527666393384+1.6694261631388267j),
                    (-2.7781745930520176+13.192388155425117j),
                    (-14.449905882224062+6.6756694479033j)]
        self.assertListsAlmostEqual(fft.fft(wave), expected, places=3)
