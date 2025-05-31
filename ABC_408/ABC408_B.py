#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
4
3 1 4 1
<expected> 3 1 3 4

3
7 7 7
<expected> 1 7

8
19 5 5 19 5 19 4 19
<expected> 3 4 5 19


"""

n = int(input())
a = set(map(int, input().split()))

sorted_a = sorted(a)
print(len(sorted_a))
print(" ".join(map(str, sorted_a)))
