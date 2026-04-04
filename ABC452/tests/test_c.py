# -*- coding: utf-8 -*-
"""
C - C - Fishbones
https://atcoder.jp/contests/abc452/tasks/abc452_c
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "C.py"


CASES = [
    pytest.param("5\n5 3\n5 2\n4 1\n5 1\n3 2\n8\nretro\nchris\nitchy\ntuna\ncrab\nrock\ncod\nash", "Yes\nYes\nNo\nNo\nNo\nNo\nNo\nNo", id="sample1"),
    pytest.param("5\n5 1\n5 2\n5 3\n5 4\n5 5\n8\nretro\nchris\nitchy\ntuna\ncrab\nrock\ncod\nash", "Yes\nYes\nYes\nNo\nNo\nNo\nNo\nNo", id="sample2"),
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
