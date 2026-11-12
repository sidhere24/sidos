#!/usr/bin/env python3
"""SiD OS VM smoke-test harness (Windows/macOS/Linux with qemu-system-x86_64).

Boots a qcow2/raw image headless, captures screenshots via QMP screendump,
and logs the serial console. Designed for CI-free local verification.

Usage:
  python scripts/vm_gui_test.py --disk sidos-test.qcow2 --out shots/ [--count 6] [--interval 15]

Requires: qemu-system-x86_64 on PATH (or --qemu /path/to/qemu), Python >= 3.8.
Screenshots are PPM (P6) — convert to PNG with Pillow if installed: pip install pillow
"""
import argparse
import json
import re
import socket
import subprocess
import sys
import threading
import time


def qmp_send(sock, obj):
    sock.sendall((json.dumps(obj) + "\n").encode())


class QMP:
    def __init__(self, host, port):
        self.sock = socket.create_connection((host, port), timeout=30)
        self.buf = b""
        self.lock = threading.Lock()
        self.resp = []
        self.greeting = self._read_line()
        if b"QMP" not in self.greeting:
            raise RuntimeError(f"unexpected greeting: {self.greeting}")
        qmp_send(self.sock, {"execute": "qmp_capabilities"})
        self._read_line()

    def _read_line(self):
        while b"\n" not in self.buf:
            chunk = self.sock.recv(65536)
            if not chunk:
                raise ConnectionError("closed")
            self.buf += chunk
        line, self.buf = self.buf.split(b"\n", 1)
        return line

    def cmd(self, execute, arguments=None, timeout=30):
        with self.lock:
            payload = {"execute": execute}
            if arguments:
                payload["arguments"] = arguments
            qmp_send(self.sock, payload)
            deadline = time.time() + timeout
            while time.time() < deadline:
                line = self._read_line()
                try:
                    msg = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if "return" in msg or "error" in msg:
                    return msg

    def close(self):
        self.sock.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--disk", required=True)
    ap.add_argument("--out", default="shots")
    ap.add_argument("--count", type=int, default=6)
    ap.add_argument("--interval", type=float, default=15.0)
    ap.add_argument("--memory", default="4096")
    ap.add_argument("--smp", default="2")
    ap.add_argument("--qemu", default="qemu-system-x86_64")
    ap.add_argument("--qmp-port", type=int, default=4444)
    ap.add_argument("--accel", default="whpx,tcg")
    ap.add_argument("--machine", default="q35", help="QEMU machine type (default q35; i440FX panics with Fedora kernels)")
    args = ap.parse_args()

    import os
    os.makedirs(args.out, exist_ok=True)

    cmd = [
        args.qemu, "-name", "sidos-test",
        "-m", args.memory, "-smp", args.smp,
        "-accel", args.accel,
        "-drive", f"file={args.disk},format=qcow2",
        "-display", "none",
        "-machine", args.machine,
        "-qmp", f"tcp:127.0.0.1:{args.qmp_port},server,nowait",
        "-serial", f"file:{args.out}/serial.log",
        "-netdev", "user,id=n0",
        "-device", "virtio-net-pci,netdev=n0",
    ]
    print("launching:", " ".join(cmd))
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(2)

    shots = []
    try:
        if proc.poll() is not None:
            raise RuntimeError(f"QEMU exited immediately with code {proc.returncode}")

        try:
            from PIL import Image
        except ImportError:
            Image = None

        def to_png(ppm):
            if Image is None:
                return
            png = ppm[:-4] + ".png"
            Image.open(ppm).save(png)
            return png

        time.sleep(10)  # BIOS + grub
        qmp = QMP("127.0.0.1", args.qmp_port)
        for i in range(args.count):
            fname = f"{args.out}/shot-{i:02d}.ppm"
            qmp.cmd("screendump", {"filename": fname, "format": "ppm"})
            png = to_png(fname)
            shots.append(png or fname)
            time.sleep(args.interval)
        # ask for graceful shutdown
        qmp.cmd("system_powerdown")
        qmp.close()
    except Exception as e:
        print("error:", e)
        proc.terminate()
        proc.wait()
        sys.exit(1)

    try:
        proc.wait(timeout=300)
    except subprocess.TimeoutExpired:
        print("note: guest did not power off within 5 min of ACPI powerdown; screenshots captured anyway.")
        proc.terminate()
        proc.wait(timeout=60)
    print("screenshots:", shots)
    print(f"serial log: {args.out}/serial.log")


if __name__ == "__main__":
    main()
