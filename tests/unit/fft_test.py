from hypothesis import given, strategies as st
from tests.base import TestBase
from tuna.fft import fft, ifft
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


class TestInverseFFT(TestBase):
    def test_raises_on_empty_list(self):
        self.assertRaises(ValueError, ifft, [])

    @given(st.lists(st.complex_numbers(), min_size=1).filter(lambda x: not is_power_of_two(len(x))))
    def test_raises_on_lists_with_unsuitable_size(self, spectrum):
        self.assertRaises(ValueError, ifft, spectrum)

    @given(st.lists(st.integers(min_value=-1e6, max_value=1e6), min_size=1).filter(lambda x: is_power_of_two(len(x))))
    def test_inverse_fft_should_return_original_signal(self, signal):
        self.assertListsAlmostEqual(ifft(fft(signal)), signal)
