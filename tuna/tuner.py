import struct
import threading
from dataclasses import dataclass

import sounddevice as sd

from tuna.filtering import noise_gate
from tuna.pitch import detect_pitch
from tuna.tonal import freq_to_note

DEFAULT_FRAME_RATE = 1024
DEFAULT_NOISE_THRESHOLD = 50


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


class Tuner:
    """
    Class ecapsulating the tuner functionality.
    """

    def __init__(self,
                 pitch_callback,
                 frame_rate=DEFAULT_FRAME_RATE,
                 noise_threshold=DEFAULT_NOISE_THRESHOLD,
                 err_callback=None,
                 input_device=None):
        """
        Initializes a new Tuner instance.

        Args:
            frame_rate: The frame rate of the audio stream.
            noise_threshold: The noise threshold.
            pitch_callback: A function to call with the detected pitch.
            err_callback: A function to call with the error status.
            input_device: The input device to use.

        Returns:
            A new Tuner instance.
        """
        self.frame_rate = frame_rate
        self.noise_threshold = noise_threshold
        self.pitch_callback = pitch_callback
        self.err_callback = err_callback
        self.input_device = input_device
        self.finished = None

    # pylint: disable=unused-argument
    def process_audio_frame(self, indata: bytes, frames: int, time: Time, status: sd.CallbackFlags):
        """
        Process audio frame. Calls the `pitch_callback` function with the detected pitch.
        """
        if status and self.err_callback:
            self.err_callback(status)
        n = len(indata)
        audio = list(struct.unpack('h' * (n // 2), indata))
        audio = noise_gate(audio, self.noise_threshold)
        null_samples = sum([1 for s in audio if s == 0])
        if null_samples / n > 0.2:
            self.pitch_callback(None)
        else:
            pitch = detect_pitch(audio, self.frame_rate)
            self.pitch_callback(freq_to_note(pitch))

    def start(self, ready_callback):  # pragma: no cover
        """
        Starts the tuner, i.e. begins listening to the microphone and processing
        the data in each frame.
        """
        self.finished = threading.Event()
        with sd.RawInputStream(
                device=self.input_device,
                callback=self.process_audio_frame,
                channels=1,
                dtype='int16',
                samplerate=self.frame_rate,
                blocksize=self.frame_rate//4,
                finished_callback=self.finished.set):
            ready_callback()
            self.finished.wait()

    def stop(self):  # pragma: no cover
        """
        Stops the tuner.
        """
        self.finished.set()

    @staticmethod
    def list_inputs():  # pragma: no cover
        """
        List available input devices.
        """
        devices = {i: d['name'] for i, d in enumerate(
            sd.query_devices()) if d['max_input_channels'] > 0}
        return devices, sd.default.device[0]
