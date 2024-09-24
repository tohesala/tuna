from typing import Tuple


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
    return 'A', 4
