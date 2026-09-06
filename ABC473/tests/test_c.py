# -*- coding: utf-8 -*-
"""
C - C - Change Schools
https://atcoder.jp/contests/abc473/tasks/abc473_c
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "C.py"


CASES = [
    pytest.param("8 5\n3 3 5 5 4 4 3 2", "3", id="sample1"),
    pytest.param("6 1\n1 1 1 1 1 1", "1", id="sample2"),
    pytest.param("14 8\n6 1 5 3 8 4 3 4 3 5 1 2 5 1", "4", id="sample3"),
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
