# -*- coding: utf-8 -*-
"""
D - D - Goin' to the Zoo
https://atcoder.jp/contests/abc404/tasks/abc404_d
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "D.py"


CASES = [
    pytest.param("4 3\n1000 300 700 200\n3 1 3 4\n3 1 2 4\n2 1 3", "1800", id="sample1"),
    pytest.param("7 6\n500 500 500 500 500 500 1000\n3 1 2 7\n3 2 3 7\n3 3 4 7\n3 4 5 7\n3 5 6 7\n3 6 1 7", "2000", id="sample2"),
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
