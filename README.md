# Tuna - A digital guitar tuner

[![codecov](https://codecov.io/github/tohesala/tuna/graph/badge.svg?token=74VQQ80RMX)](https://codecov.io/github/tohesala/tuna)

This project is a simple digital guitar tuner that can be used to tune a guitar
(and possibly other instruments) using a computer. The tuner is implemented in
Python and uses Fast Fourier Transform (FFT) to analyze the sound input from a
microphone.

## Running the application

The project uses poetry for dependency management. To run the project, make sure you have python3 and poetry installed. Then install the dependencies with `poetry install`, and run the application with the following command:

```bash
poetry run python tuna/app.py
```
