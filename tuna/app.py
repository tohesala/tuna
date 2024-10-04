"""
A simple CLI application wrapper around the Tuner.
"""

from tuna.tuner import Tuner

CLEAR = "\r\033[K"
FRAME_RATE = 1024


def main():
    def out_replace(msg):
        """
        Output the message to the console. Replaces the previous message.
        """
        print(CLEAR + msg, end="")

    def output_pitch(pitch=None):
        if not pitch:
            return out_replace("No pitch detected")
        out_replace(f"Detected pitch: {pitch[0]} ({pitch[1]:.2f}Hz)")

    tuner = Tuner(frame_rate=FRAME_RATE, pitch_callback=output_pitch)
    try:
        print("Listening to the microphone...")
        print("Press Ctrl+C to exit.")
        tuner.start()
    except KeyboardInterrupt:
        tuner.stop()
        print("")
        print("Goodbye!")


if __name__ == "__main__":
    main()
