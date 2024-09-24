from hypothesis import given
from hypothesis import strategies as st

from tests.base import TestBase
from tuna.tonal import NOTES, freq_to_note, note_to_freq


class FreqToNoteTests(TestBase):
    def test_exact(self):
        self.assertEqual(freq_to_note(440.0), ('A4', 0.0))

    def test_sharp(self):
        self.assertEqual(freq_to_note(446.12), ('A4', 6.12))

    def test_flat(self):
        self.assertEqual(freq_to_note(433.87), ('A4', -6.13))

    def test_guitar_notes(self):
        self.assertEqual(freq_to_note(82.41), ('E2', 0.0))
        self.assertEqual(freq_to_note(110.0), ('A2', 0.0))
        self.assertEqual(freq_to_note(146.83), ('D3', 0.0))
        self.assertEqual(freq_to_note(196.0), ('G3', 0.0))
        self.assertEqual(freq_to_note(246.94), ('B3', 0.0))
        self.assertEqual(freq_to_note(329.63), ('E4', 0.0))

    def test_right_in_between(self):
        self.assertEqual(freq_to_note(190.0)[0], 'F#3')
        self.assertEqual(freq_to_note(190.5)[0], 'F#3')
        self.assertEqual(freq_to_note(191.0)[0], 'G3')


class NoteConversionHypotheses(TestBase):
    @given(st.sampled_from(NOTES))
    def test_note_id_hypothesis(self, note):
        self.assertEqual(freq_to_note(note_to_freq(note)), (note, 0.0))

    @given(st.floats(min_value=0.0, max_value=20000.0))
    def test_freq_id_hypothesis(self, freq):
        self.assertAlmostEqual(note_to_freq(
            *freq_to_note(freq)), freq, places=2)
