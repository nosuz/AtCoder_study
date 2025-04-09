"""TEST_DATA
20
<expected> 5

400
<expected> 24

1234567890
<expected> 42413

"""
import math

n = int(input())

count = math.isqrt(n//2) + math.isqrt(n) // 2

print(count)
