from hypothesis import given, strategies as st
from tests.base import TestBase
from tuna.utils import is_power_of_two


class IsPowerOfTwoTests(TestBase):
    POWERS_OF_TWO_32 = set(2**i for i in range(32))

    def test_32bit_powers_of_two_pass(self):
        for n in self.POWERS_OF_TWO_32:
            self.assertTrue(is_power_of_two(n))

    @given(st.integers(min_value=1, max_value=2**31) | st.floats(min_value=1, max_value=2**31))
    def test_32bit_non_powers_of_two_fail(self, n):
        if n not in self.POWERS_OF_TWO_32:
            self.assertFalse(is_power_of_two(n))
