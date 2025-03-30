"""入力
3 4
"""

"""出力
Even
"""

a, b = map(int, input().split())

# 2進数で表すと、奇数は最下位のbitが1になる。
# 優先順位に自信がないので、順番を強制する。
result = "Even" if ((a * b) & 0x1) == 0 else "Odd"

print(result)
