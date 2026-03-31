# -*- coding: utf-8 -*-
"""
A - A - Streamer Takahashi
https://atcoder.jp/contests/abc414/tasks/abc414_a
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "A.py"


CASES = [
    pytest.param("5 19 22\n17 23\n20 23\n19 22\n0 23\n12 20", "3", id="sample1"),
    pytest.param("3 12 13\n0 1\n0 1\n0 1", "0", id="sample2"),
    pytest.param("10 8 14\n5 20\n14 21\n9 21\n5 23\n8 10\n0 14\n3 8\n2 6\n0 16\n5 20", "5", id="sample3"),
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
