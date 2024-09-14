from hypothesis import given, strategies as st
from tests.base import TestBase
from tuna.fft import fft
from tuna.dft import naive_dft


class TestFFT(TestBase):
    @given(signal=st.lists(st.integers(min_value=-1e6, max_value=1e6), min_size=1))
    def test_fft_should_equal_dft(self, signal):
        self.assertListsAlmostEqual(fft(signal), naive_dft(signal))


# class TestInverseFFT(TestBase):
#     def test_inverse_of_fft_constant_signal(self):
#         self.assertEqual(fft.ifft([4, 0, 0, 0]), [1, 1, 1, 1])

#     def test_inverse_of_fft_sine_wave(self):
#         self.assertEqual(fft.ifft([0, -2j, 0, 2j]), [0, 1, 0, -1])

#     def test_inverse_of_fft_cosine_wave(self):
#         self.assertEqual(fft.ifft([0, 2, 0, 2]), [1, 0, -1, 0])
