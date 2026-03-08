# -*- coding: utf-8 -*-
"""
B - B - Pepper Addiction
https://atcoder.jp/contests/abc448/tasks/abc448_b
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "B.py"


CASES = [
    pytest.param("7 5\n4 4 8 3 7\n1 2\n2 3\n5 2\n4 10\n2 3\n5 4\n2 3", "15", id="sample1"),
    pytest.param("1 1\n1\n1 1", "1", id="sample2"),
    pytest.param("15 10\n7 94 100 82 63 81 75 2 76 73\n10 44\n5 77\n10 47\n7 32\n2 82\n5 90\n3 37\n6 70\n6 28\n3 25\n2 26\n10 56\n1 69\n5 46\n7 26", "438", id="sample3"),
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
