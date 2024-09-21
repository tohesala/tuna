"""
A simple CLI application wrapper around the tuna pitch detection functions.
"""

from statistics import mean
import struct
import sys
from tuna.pitch_detection import detect_pitch_simple
from sounddevice import RawInputStream, sleep

CLEAR = "\r\033[K"
Fs = 1024


def noise_gate(signal, thresh=50):
    return [0 if abs(x) < thresh else x for x in signal]


def process_audio(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    N = len(indata)
    audio = list(struct.unpack('h' * (N // 2), indata))
    audio = noise_gate(audio)
    if mean([abs(s) for s in audio]) < 25:
        return print(CLEAR + "No pitch detected", end="")
    pitch = detect_pitch_simple(audio, Fs)
    print(CLEAR + f"Detected pitch: {pitch:.2f} Hz", end="")


def main():
    try:
        with RawInputStream(callback=process_audio, channels=1, dtype='int16', samplerate=Fs, blocksize=Fs//4) as stream:
            print("Listening to the microphone...")
            print("Press Ctrl+C to exit.")
            while True:
                sleep(1000)
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
