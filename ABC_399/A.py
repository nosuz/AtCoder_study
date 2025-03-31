"""入力
6
abcarc
agcahc
"""

"""出力
2
"""

n = input()
s = input()
t = input()

# sとtのペアを作成する。
# x = [(a, b) for a, b in zip(s, t)]
y = [True if a != b else False for a, b in zip(s, t)]

# 合計で1の数を数え上げる。
print(sum(y))
