# -*- coding: utf-8 -*-
"""
D - D - Integer-duplicated Path
https://atcoder.jp/contests/abc448/tasks/abc448_d
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "D.py"


CASES = [
    pytest.param("5\n1 3 2 1 2\n1 2\n1 3\n3 4\n3 5", "No\nNo\nNo\nYes\nYes", id="sample1"),
    pytest.param("2\n1000000000 1000000000\n2 1", "No\nYes", id="sample2"),
    pytest.param("10\n10 7 3 9 1 3 8 5 7 10\n3 6\n8 6\n6 1\n9 7\n7 10\n5 4\n4 2\n10 2\n1 9", "No\nYes\nYes\nYes\nYes\nNo\nNo\nNo\nNo\nYes", id="sample3"),
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
