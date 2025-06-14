#!/usr/bin/python3

# python3 validate.py sample.py

# C - Rotatable Array
# https://atcoder.jp/contests/abc410/tasks/abc410_c

"""TEST_DATA
5 5
2 3
1 2 1000000
3 4
2 2
2 3
<expected> 3 1 1000000

1000000 2
1 1000000 999999
3 1000000000
<expected>


"""

n, q = map(int, input().split())

a = [i + 1 for i in range(n)]

head = 0
for _ in range(q):
    q = list(map(int, input().split()))

    match q[0]:
        case 1:
            p = (head + q[1] - 1) % n
            x = q[2]
            a[p] = x
        case 2:
            p = (head + q[1] - 1) % n
            print(a[p])
        case 3:
            k = q[1]
            # head = (head + k) % n
            # max(head) = 3*10^14 < 2^64
            head += k
