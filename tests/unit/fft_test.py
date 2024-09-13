import unittest
import tuna.fft as fft

class TestFFT(unittest.TestCase):
    def test_fft(self):
        self.assertEqual(fft.fft([1,1,1,1]), [4+0j, 0+0j, 0+0j, 0+0j])
