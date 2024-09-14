from hypothesis import given, strategies as st
from tests.base import TestBase
from tuna.fft import fft
from tuna.dft import naive_dft
from tuna.utils import is_power_of_two


class TestFFT(TestBase):
    def test_raises_on_empty_list(self):
        self.assertRaises(ValueError, fft, [])

    @given(st.lists(st.integers(), min_size=1).filter(lambda x: not is_power_of_two(len(x))))
    def test_raises_on_lists_with_unsuitable_size(self, signal):
        self.assertRaises(ValueError, fft, signal)

    @given(st.lists(st.integers(min_value=-1e6, max_value=1e6), min_size=1).filter(lambda x: is_power_of_two(len(x))))
    def test_fft_should_equal_dft(self, signal):
        self.assertListsAlmostEqual(fft(signal), naive_dft(signal), places=5)


# class TestInverseFFT(TestBase):
#     def test_inverse_of_fft_constant_signal(self):
#         self.assertEqual(fft.ifft([4, 0, 0, 0]), [1, 1, 1, 1])

#     def test_inverse_of_fft_sine_wave(self):
#         self.assertEqual(fft.ifft([0, -2j, 0, 2j]), [0, 1, 0, -1])

#     def test_inverse_of_fft_cosine_wave(self):
#         self.assertEqual(fft.ifft([0, 2, 0, 2]), [1, 0, -1, 0])
