"""TEST_DATA
7 3
<expected> 400

1000000 2
<expected> inf

999999999 1
<expected> 1000000000

998244353 99
<expected> inf

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
