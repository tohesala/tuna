import struct
import unittest
from unittest.mock import Mock, patch

import sounddevice as sd

from tuna.tuner import Time, Tuner


class TunerTests(unittest.TestCase):
    def test_process_audio_frame_valid(self):
        """
        When the frame is valid, but the samples have too low amplitude, there
        should be no pitch detected.
        """

        pitch_callback = Mock()
        tuner = Tuner(pitch_callback)
        indata = struct.pack('h' * 4, 0, 0, 0, 0)
        time = Time(0, 0, 0)
        status = sd.CallbackFlags()

        tuner.process_audio_frame(indata, 4, time, status)

        pitch_callback.assert_called_once_with(None)

    def test_process_audio_frame_with_errors(self):
        """
        When the audio frame is invalid, the error callback should be called.
        """

        pitch_callback = Mock()
        err_callback = Mock()
        tuner = Tuner(pitch_callback, err_callback)
        indata = struct.pack('h' * 4, 0, 0, 0, 0)
        time = Time(0, 0, 0)
        status = sd.CallbackFlags(1)

        tuner.process_audio_frame(indata, 4, time, status)

        err_callback.assert_called_once_with(status)

    @patch('tuna.tuner.detect_pitch', return_value=440)
    @patch('tuna.tuner.freq_to_note', return_value=('A4', 0))
    def test_process_audio_frame_with_pitch(self, mock_freq_to_note, mock_detect_pitch):
        """
        When the audio is valid and the amplitudes are high enough, the
        pitch_callback should get called with the detected pitch.
        """

        pitch_callback = Mock()
        tuner = Tuner(pitch_callback, frame_rate=4096)
        indata = struct.pack('h' * 4, 1000, 1000, 1000, 1000)
        time = Time(0, 0, 0)
        status = sd.CallbackFlags()

        tuner.process_audio_frame(indata, 4, time, status)

        mock_detect_pitch.assert_called_once_with(
            [1000, 1000, 1000, 1000], 4096)
        mock_freq_to_note.assert_called_once_with(440)
        pitch_callback.assert_called_once_with(('A4', 0))
