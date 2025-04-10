"""
A simple CLI application wrapper around the Tuner.
"""

import sys

from tuna.tuner import DEFAULT_FRAME_RATE, DEFAULT_NOISE_THRESHOLD, Tuner

CLEAR = "\r\033[K"


def select_input():
    """
    Runs the user through input device configuration.
    """
    devices, default = Tuner.list_inputs()
    print("Available input devices:")
    for did in devices:
        print(f"  - {devices[did]} ({did})")
    try:
        device = int(
            input(f"Select input device: ({default})\n").strip() or default)
        if device not in devices:
            raise ValueError("Invalid input device")
        return device
    except ValueError:
        print("The input needs to be an integer")
        sys.exit(1)
    except KeyboardInterrupt:
        print("")
        print("Cancelled")
        sys.exit(1)


def read_noise_threshold():
    """
    Reads the noise threshold from the arguments.
    """
    try:
        return float(sys.argv[sys.argv.index('-n') + 1])
    except ValueError:
        print("Invalid noise threshold")
        sys.exit(1)


def print_replace(msg):
    """
    Output the message to the console. Replaces the previous message.
    """
    print(CLEAR + msg, end="")


def print_pitch(pitch=None):
    if not pitch:
        print_replace("No pitch detected")
    else:
        print_replace(f"Detected pitch: {pitch[0]} ({pitch[1]:+.2f}Hz)")


def print_error(status):
    print(f"\nError: {status}", file=sys.stderr)


def print_ready():
    print("Listening to the microphone...")
    print("Press Ctrl+C to exit.")


def main():
    device = None
    noise_threshold = DEFAULT_NOISE_THRESHOLD

    if '-s' in sys.argv or '--select-input' in sys.argv:
        device = select_input()

    if '-n' in sys.argv or '--noise-threshold' in sys.argv:
        noise_threshold = read_noise_threshold()

    tuner = Tuner(frame_rate=DEFAULT_FRAME_RATE,
                  noise_threshold=noise_threshold,
                  pitch_callback=print_pitch,
                  err_callback=print_error,
                  input_device=device)

    try:
        tuner.start(ready_callback=print_ready)
    except KeyboardInterrupt:
        tuner.stop()
        print("")
        print("Goodbye!")


if __name__ == "__main__":
    main()
