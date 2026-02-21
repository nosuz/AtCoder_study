# -*- coding: utf-8 -*-
"""
B - B - Greedy Draft
https://atcoder.jp/contests/abc446/tasks/abc446_b
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "B.py"


CASES = [
    pytest.param("4 5\n3\n3 1 2\n3\n3 2 1\n2\n2 3\n4\n2 5 3 1", "3\n2\n0\n5", id="sample1"),
    pytest.param("6 5\n1\n3\n2\n3 5\n5\n5 3 1 4 2\n5\n5 1 3 4 2\n5\n3 4 1 5 2\n5\n5 1 3 2 4", "3\n5\n1\n4\n2\n0", id="sample2"),
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
