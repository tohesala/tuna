import struct
import threading
from dataclasses import dataclass
from statistics import mean

import sounddevice as sd

from tuna.filtering import noise_gate
from tuna.pitch import detect_pitch
from tuna.tonal import freq_to_note


@dataclass
class Time:
    """
    A dataclass to type the time argument of the sounddevice audio stream
    callback.
    """
    # pylint: disable=invalid-name
    currentTime: float
    inputBufferAdcTime: float
    outputBufferDacTime: float


CLEAR = "\r\033[K"


class Tuner:
    """
    Class ecapsulating the tuner functionality.
    """

    def __init__(self, pitch_callback, err_callback=None, frame_rate=1024):
        self.frame_rate = frame_rate
        self.pitch_callback = pitch_callback
        self.finished = None
        self.err_callback = err_callback

    # pylint: disable=unused-argument
    def process_audio_frame(self, indata: bytes, frames: int, time: Time, status: sd.CallbackFlags):
        """
        Process audio frame. Calls the `pitch_callback` function with the detected pitch.
        """
        if status and self.err_callback:
            self.err_callback(status)
        n = len(indata)
        audio = list(struct.unpack('h' * (n // 2), indata))
        audio = noise_gate(audio)
        if mean([abs(s) for s in audio]) < 25:
            return self.pitch_callback(None)
        pitch = detect_pitch(audio, self.frame_rate)
        self.pitch_callback(freq_to_note(pitch))

    def start(self, ready_callback):  # pragma: no cover
        """
        Starts the tuner, i.e. begins listening to the microphone and processing
        the data in each frame.
        """
        self.finished = threading.Event()
        with sd.RawInputStream(
                callback=self.process_audio_frame,
                channels=1,
                dtype='int16',
                samplerate=self.frame_rate, blocksize=self.frame_rate//4,
                finished_callback=self.finished.set):
            ready_callback()
            self.finished.wait()

    def stop(self):  # pragma: no cover
        """
        Stops the tuner.
        """
        self.finished.set()
