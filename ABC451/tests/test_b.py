# -*- coding: utf-8 -*-
"""
B - B - Personnel Change
https://atcoder.jp/contests/abc451/tasks/abc451_b
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "B.py"


CASES = [
    pytest.param("5 4\n1 2\n2 1\n3 1\n2 2\n2 4", "1\n-1\n-1\n1", id="sample1"),
    pytest.param("10 5\n3 2\n3 4\n1 2\n2 2\n4 4\n3 1\n3 4\n4 2\n3 3\n3 2", "0\n4\n-5\n1\n0", id="sample2"),
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
