"""入力
101
"""

"""出力
2
"""

str = input()

# 問題からリストのサイズを3に固定
# 1になっている数を数える代わりに加算する。
bin = [int(str[i]) for i in range(3)]

print(sum(bin))
