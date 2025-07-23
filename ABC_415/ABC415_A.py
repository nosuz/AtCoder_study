#!/usr/bin/python3

# python3 validate.py sample.py

# A - Unsupported Type
# https://atcoder.jp/contests/abc415/tasks/abc415_a

"""TEST_DATA
5
3 1 4 1 5
4
<expected> Yes

4
100 100 100 100
100
<expected> Yes

6
2 3 5 7 11 13
1
<expected> No


"""

N = int(input())
A = list(map(int, input().split()))
X = int(input())
# also can handle as strings
# A = input().split()
# X = input()

if X in A:
    print("Yes")
else:
    print("No")
