# Tuna - A digital guitar tuner

![CI status](https://github.com/tohesala/tuna/actions/workflows/checks.yml/badge.svg)
[![codecov](https://codecov.io/github/tohesala/tuna/graph/badge.svg?token=74VQQ80RMX)](https://codecov.io/github/tohesala/tuna)

This project is a digital guitar tuner implemented in Python. It's basically a
toy project to learn more about signal processing in general and pitch detection
in particular. Basically, it's a simple command line application that begins
listening to microphone input as soon as it's started, read the input in frames
(of about 250ms) and then outputs the estimated pitch of the input. The pitch is
output in scientific pitch notation (eg. `A4` for the A above middle C), with
the distance to this nearest note also output in Hz.

The tuner is implemented in Python and uses Fast Fourier Transform (FFT) to
analyze the sound input. Do note that the pitch detection algorithm is rather
simple, so especially octave errors are expected. The note base should however
generally be quite correct, given a clean enough input signal.

## Installation

The project requires at least Python 3.10, so make sure you have it installed.
Poetry is also required, so make sure to install it first. You can find
instructions for this in the [Poetry
documentation](https://python-poetry.org/docs/#installation).

After the previous prerequisites are met, you can install the project dependencies with:

```bash
poetry install
```

> [!IMPORTANT]
> This project relies on the [sounddevice](https://python-sounddevice.readthedocs.io/en/0.5.1/)
> library, which itself is a wrapper on [PortAudio](https://www.portaudio.com/). This
> means that you need to have PortAudio installed on your system. On Linux, this
> is not done automatically. The way to install it depends on the distribution.
> On Ubuntu you can install it with `sudo apt-get install portaudio19-dev`. Also note that on
> some systems you might not even have [pulseaudio](https://www.freedesktop.org/wiki/Software/PulseAudio/)
> installed. In this case, you also need to install that. On Ubuntu you can install it with
> `sudo apt-get install pulseaudio`.

## Usage

After installation you can start the application with:

```bash
poetry run inv start
```

You should now start seeing the periodically detected pitch in your terminal.
You can stop the application with `Ctrl+C`.

> [!NOTE]
> Without options, the application will select the microphone based on system defaults.

## Configuration options

There are some configuration options available:

- `--select-input`: Enables selecting the input device when launching the app.
- `--noise-threshold`: Enables setting the noise gate threshold value. Unfortunately, currently the configuration of this is essentially a matter of trial and error.

For help, see `poetry run inv start -h`.
