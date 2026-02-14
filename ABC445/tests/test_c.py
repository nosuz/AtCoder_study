# -*- coding: utf-8 -*-
"""
C - C - Sugoroku Destination
https://atcoder.jp/contests/abc445/tasks/abc445_c
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "C.py"


CASES = [
    pytest.param("7\n2 4 7 5 5 6 7", "5 5 7 5 5 6 7", id="sample1"),
    pytest.param("5\n1 2 3 4 5", "1 2 3 4 5", id="sample2"),
    pytest.param("15\n11 3 10 7 15 10 10 11 11 13 11 12 14 14 15", "11 14 14 14 15 14 14 11 11 14 11 12 14 14 15", id="sample3"),
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
