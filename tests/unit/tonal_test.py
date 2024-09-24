from tests.base import TestBase
from tuna.tonal import freq_to_note


class FreqToNoteTest(TestBase):
    def test_exact(self):
        self.assertEqual(freq_to_note(440.0), ('A4', 0.0))

    def test_sharp(self):
        self.assertEqual(freq_to_note(446.12), ('A4', 6.12))

    def test_flat(self):
        self.assertEqual(freq_to_note(433.87), ('A4', -6.13))

    def test_right_in_between(self):
        self.assertEqual(freq_to_note(190.0)[0], 'F#3')
        self.assertEqual(freq_to_note(190.5)[0], 'F#3')
        self.assertEqual(freq_to_note(191.0)[0], 'G3')
