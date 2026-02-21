import os
import socket
import subprocess
import sys
import time

import pytest


def _wait_for_port(host: str, port: int, timeout_seconds: float = 5.0) -> None:
    """Wait until a TCP port is accepting connections."""
    start = time.time()
    while time.time() - start < timeout_seconds:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return
        except OSError:
            time.sleep(0.1)
    raise RuntimeError(f"Server did not start on http://{host}:{port} within {timeout_seconds}s")


@pytest.fixture(scope="session")
def demo_server_url():
    """
    Starts a local HTTP server for ui/demo_app and returns the base URL.
    Automatically stops the server after the test session.
    """
    host = "127.0.0.1"
    port = 8000

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    demo_app_dir = os.path.join(project_root, "ui", "demo_app")

    # Start: python -m http.server 8000 --bind 127.0.0.1  (in ui/demo_app)
    cmd = [sys.executable, "-m", "http.server", str(port), "--bind", host]

    proc = subprocess.Popen(
        cmd,
        cwd=demo_app_dir,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
    )

    try:
        _wait_for_port(host, port, timeout_seconds=5.0)
        yield f"http://{host}:{port}"
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()