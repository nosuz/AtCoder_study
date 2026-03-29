# -*- coding: utf-8 -*-
"""
C - C - Understory
https://atcoder.jp/contests/abc451/tasks/abc451_c
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "C.py"


CASES = [
    pytest.param("5\n1 5\n1 7\n1 8\n2 7\n1 3", "1\n2\n3\n1\n2", id="sample1"),
    pytest.param("12\n2 256601193\n1 85138616\n1 202564041\n2 276477192\n1 55551662\n1 170271057\n2 754166580\n1 854388209\n1 772036624\n2 651124113\n1 301137866\n2 290875185", "0\n1\n2\n0\n1\n2\n0\n1\n2\n2\n3\n3", id="sample2"),
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
