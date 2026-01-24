# -*- coding: utf-8 -*-
"""
C - C - Peer Review
https://atcoder.jp/contests/abc442/tasks/abc442_c
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "C.py"


CASES = [
    pytest.param("6 5\n1 2\n1 4\n2 3\n5 3\n3 1", "0 1 0 4 4 10", id="sample1"),
    pytest.param("7 3\n1 2\n3 4\n5 6", "10 10 10 10 10 10 20", id="sample2"),
    pytest.param("6 9\n3 6\n2 5\n2 3\n4 3\n1 5\n6 2\n3 1\n5 3\n2 4", "1 0 0 1 0 1", id="sample3"),
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
