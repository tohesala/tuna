import random
import timeit
import unittest
from statistics import mean

from tuna.dft import naive_dft
from tuna.fft import fft


class FFTPerformanceTests(unittest.TestCase):
    def test_fft_performance_short(self):
        minmax = 1000
        signal = [random.uniform(-minmax, minmax) for _ in range(32)]

        # Time multiple executions of the FFT and DFT
        rounds = 100
        fft_avg_rt = mean(
            timeit.repeat(lambda: fft(signal), number=rounds))
        dft_avg_rt = mean(
            timeit.repeat(lambda: naive_dft(signal), number=rounds))

        # The FFT should on average be faster than DFT, even for shorter signals
        self.assertLess(fft_avg_rt, dft_avg_rt)

    def test_fft_performance_long(self):
        minmax = 1000
        signal = [random.uniform(-minmax, minmax) for _ in range(1024)]

        # Time multiple executions of the FFT and DFT. Note the signal is larger
        # so we can't run as many rounds if we want this to ever finish.
        rounds = 10
        fft_avg_rt = mean(
            timeit.repeat(lambda: fft(signal), number=rounds))
        dft_avg_rt = mean(
            timeit.repeat(lambda: naive_dft(signal), number=rounds))

        # With n=1024 the FFT should already be a 100 times faster than the
        # naive DFT. But let's take it safe and assert its 50 times faster
        self.assertLess(fft_avg_rt * 50, dft_avg_rt)
