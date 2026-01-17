# -*- coding: utf-8 -*-
"""
B - B - Two Languages
https://atcoder.jp/contests/abc441/tasks/abc441_b
"""

import subprocess
import sys
from pathlib import Path

import pytest


def strip_last_newline(s: str) -> str:
    return s[:-1] if s.endswith("\n") else s


SCRIPT = Path(__file__).resolve().parents[1] / "B.py"


CASES = [
    pytest.param("6 5\nahikst\naikot\n5\nasahi\nokita\nkiai\nhash\nit", "Takahashi\nAoki\nUnknown\nTakahashi\nUnknown", id="sample1"),
    pytest.param("7 6\nahiknst\nahikos\n5\nkioki\nohiki\ntashi\nnishi\nkashi", "Aoki\nAoki\nTakahashi\nTakahashi\nUnknown", id="sample2"),
    pytest.param("13 11\ndefghiqsvwxyz\nacejmoqrtwx\n15\nqhsqzhd\njcareec\nwwqxqew\nwxqxwex\njxxrtwa\ntrtqjxe\nsqyggse\nxxqwxew\nxewwxxw\nwwqxwex\nxqqxqwq\nqxxexxe\nteqeroc\neeeqqee\nvxdevyy", "Takahashi\nAoki\nUnknown\nUnknown\nAoki\nAoki\nTakahashi\nUnknown\nUnknown\nUnknown\nUnknown\nUnknown\nAoki\nUnknown\nTakahashi", id="sample3"),
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
