from tests.base import TestBase
from tuna.filtering import hamming_window, noise_gate


class HammingWindowTests(TestBase):
    def test_len(self):
        self.assertEqual(len(hamming_window(128)), 128)

    def test_first(self):
        self.assertAlmostEqual(hamming_window(128)[0], 0.08)

    def test_mid_is_one(self):
        self.assertAlmostEqual(hamming_window(128)[128//2], 1, places=3)

    def test_symmetry(self):
        window = hamming_window(128)
        self.assertListsAlmostEqual(window, window[::-1])

    def test_first_half_should_be_increasing(self):
        n = 128
        window = hamming_window(n)
        # if the window is in ascending sorted order, it is increasing
        self.assertEqual(window[:n//2], sorted(window[:n//2]))


class NoiseGateTests(TestBase):
    def test_noise_gate_zeroes_below_threshold(self):
        signal = [0, 1, 2, 3, 4, 5]
        self.assertEqual(noise_gate(signal, 3), [0, 0, 0, 3, 4, 5])

    def test_noise_gate_no_change_above_threshold(self):
        signal = [0, 1, 2, 3, 4, 5]
        self.assertEqual(noise_gate(signal, 0), signal)
