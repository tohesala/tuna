import platform
import sys

from invoke import Context, task


@task
def check_portaudio(ctx: Context):
    # On Linux, PortAudio needs to be separately installed, so verify that
    if not ctx.run("python -c 'import sounddevice'", hide=True, warn=True).ok:
        print("PortAudio not installed")
        if platform.system() == "Linux":
            print("Please install PortAudio using the following command:")
            print("sudo apt-get install portaudio19-dev")
        else:
            print("Please run 'poetry install' first")
        sys.exit(1)


@task(check_portaudio)
def start(ctx: Context):
    ctx.run("python tuna/app.py", pty=True)


@task(check_portaudio)
def test_all(ctx: Context):
    ctx.run("pytest", pty=True)


@task(check_portaudio)
def test_unit(ctx: Context):
    ctx.run("pytest tests/unit", pty=True)


@task(check_portaudio)
def test_perf(ctx: Context):
    ctx.run("pytest tests/perf", pty=True)


@task(check_portaudio)
def coverage(ctx: Context, json=False):
    ctx.run("coverage run")
    if json:
        ctx.run("coverage json")
    else:
        ctx.run("coverage report")
