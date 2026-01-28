# -*- coding: utf-8 -*-
"""
C - C - Reindeer and Sleigh 2
https://atcoder.jp/contests/abc437/tasks/abc437_c
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "C.py"


CASES = [
    pytest.param("3\n3\n3 1\n4 1\n5 9\n5\n1000000000 1\n1000000000 1\n1000000000 1\n1000000000 1\n1000000000 1\n10\n133180711 458704923\n531424946 225863856\n141986070 637075158\n500770732 289806469\n502866767 408857335\n559714289 569084545\n287444582 992432993\n559747907 753133304\n432846188 949871298\n727072164 756020367", "2\n0\n6", id="sample1"),
]


@pytest.mark.parametrize("inp, expected", CASES)
def test_main(inp: str, expected: str):
    # stdin は末尾改行がある方が自然なので、無ければ付ける
    if not inp.endswith("\n"):
        inp = inp + "\n"

    p = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=inp,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert p.returncode == 0, f"returncode={p.returncode}\nSTDERR:\n{p.stderr}"

    got = strip_last_newline(p.stdout)
    exp = strip_last_newline(expected)

    assert got == exp, (
        "\n--- got ---\n" + got + "\n"
        + "--- expected ---\n" + exp + "\n"
        + "--- raw stdout ---\n" + p.stdout + "\n"
        + "--- stderr ---\n" + p.stderr + "\n"
    )
