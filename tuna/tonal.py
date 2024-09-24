from typing import Tuple

OCTAVES = 10
NOTE_BASES = "C C# D D# E F F# G G# A A# B".split()
NOTES = [f"{note}{octave}" for octave in range(OCTAVES) for note in NOTE_BASES]
A4 = 440
# The formula for note frequencies is from https://en.wikipedia.org/wiki/Scientific_pitch_notation
NOTE_FREQS = {note: round(A4 * 2**((12+m-69)/12), 2)
              for m, note in enumerate(NOTES)}


def freq_to_note(freq: float) -> Tuple[str, float]:
    """
    Convert a frequency to a note name in the scientific pitch notation.

    Args:
        freq: The frequency to convert.

    Returns:
        A tuple containing the note name (with octave), as well as the signed
        distance. A negative distance implies the note is flat, i.e. the
        frequency is below the note. Similarly, a positive distance implies the
        note is sharp.
    """
    nearest = min(NOTES, key=lambda n: abs(NOTE_FREQS[n] - freq))
    distance = freq - NOTE_FREQS[nearest]
    return nearest, round(distance, 2)


def note_to_freq(note: str, distance: float = 0.0) -> float:
    """
    Convert a note name and distance to a frequency.

    Args:
        note: The note name in the scientific pitch notation.
        distance: The signed distance from the note.

    Returns:
        The frequency of the note.
    """
    return NOTE_FREQS[note] + distance
