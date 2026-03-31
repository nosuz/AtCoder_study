# -*- coding: utf-8 -*-
"""
B - B - String Too Long
https://atcoder.jp/contests/abc414/tasks/abc414_b
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "B.py"


CASES = [
    pytest.param("8\nm 1\ni 1\ns 2\ni 1\ns 2\ni 1\np 2\ni 1", "mississippi", id="sample1"),
    pytest.param("7\na 1000000000000000000\nt 1000000000000000000\nc 1000000000000000000\no 1000000000000000000\nd 1000000000000000000\ne 1000000000000000000\nr 1000000000000000000", "Too Long", id="sample2"),
    pytest.param("1\na 100", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", id="sample3"),
    pytest.param("6\ng 4\nj 1\nm 4\ne 4\nd 3\ni 4", "ggggjmmmmeeeedddiiii", id="sample4"),
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
