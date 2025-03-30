"""入力
1
2 3
test
"""

"""出力
6 test
"""

a = int(input())

b, c = map(int, input().split())

str = input()

print(f"{a + b + c} {str}")
