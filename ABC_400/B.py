"""TEST_DATA
7 3
# 400

1000000 2
# inf

999999999 1
# 1000000000

998244353 99
# inf

"""

n, m = map(int, input().split())

total = 0
for i in range(m + 1):
    total += n ** i
    if total > 1_000_000_000:
        print("inf")
        break
else:
    print(total)
