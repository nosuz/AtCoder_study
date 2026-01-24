# -*- coding: utf-8 -*-
"""
D - D - Swap and Range Sum
https://atcoder.jp/contests/abc442/tasks/abc442_d
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "D.py"


CASES = [
    pytest.param("4 4\n2 7 1 8\n1 2\n2 1 2\n1 1\n2 2 4", "3\n17", id="sample1"),
    pytest.param("8 10\n22 75 26 45 72 81 47 29\n2 2 7\n2 6 8\n2 4 4\n1 2\n2 1 3\n1 1\n2 2 4\n1 2\n1 4\n2 1 1", "346\n157\n45\n123\n142\n26", id="sample2"),
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
