"""TEST_DATA
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

n = input()
s = input()
t = input()

# sとtのペアを作成する。
# x = [(a, b) for a, b in zip(s, t)]
y = [True if a != b else False for a, b in zip(s, t)]

# 合計で1の数を数え上げる。
print(sum(y))
