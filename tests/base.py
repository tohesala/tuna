import unittest

# pylint: disable=invalid-name, consider-using-enumerate


class TestBase(unittest.TestCase):
    def assertListsAlmostEqual(self, a, b, places=7):
        self.assertEqual(len(a), len(b))
        for i in range(len(a)):
            try:
                self.assertAlmostEqual(a[i], b[i], places=places)
            except AssertionError as e:
                raise AssertionError(f"Lists differ at index {i}: {e}") from e
