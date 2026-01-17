# -*- coding: utf-8 -*-
"""
D - D - Paid Walk
https://atcoder.jp/contests/abc441/tasks/abc441_d
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "D.py"


CASES = [
    pytest.param("5 8 3 80 100\n1 2 20\n1 3 70\n2 1 30\n2 5 10\n3 2 10\n3 4 30\n3 5 20\n5 1 70", "1 5", id="sample1"),
    pytest.param("10 1 1 1 100\n2 3 1", "\n", id="sample2"),
    pytest.param("2 5 3 1 100\n1 1 1\n2 2 100\n1 2 1\n1 2 1\n1 2 100", "1 2", id="sample3"),
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
