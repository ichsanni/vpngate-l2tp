import subprocess


def _run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def run(cmd):
    command = _run(cmd)
    if command.returncode != 0:
        raise RuntimeError(command.stderr)