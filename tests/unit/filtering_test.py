from tests.base import TestBase
from tuna.filtering import hamming_window


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
