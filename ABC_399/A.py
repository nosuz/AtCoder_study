import io
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()  # .env
except ModuleNotFoundError:
    pass  # ignore no dotenv error

TEST_DATA = """
6
abcarc
agcahc

7
atcoder
contest

8
chokudai
chokudai

10
vexknuampx
vzxikuamlx

"""

if os.getenv("LOCAL_DEBUG"):
    # trim \n
    sys.stdin = io.StringIO(TEST_DATA[1:].replace('\n\n', '\n'))


def code():
    n = input()
    s = input()
    t = input()

    # sとtのペアを作成する。
    # x = [(a, b) for a, b in zip(s, t)]
    y = [True if a != b else False for a, b in zip(s, t)]

    # 合計で1の数を数え上げる。
    print(sum(y))


if os.getenv("LOCAL_DEBUG"):
    while True:
        try:
            code()
        except EOFError:
            break
else:
    code()
