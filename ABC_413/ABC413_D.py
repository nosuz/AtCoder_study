#!/usr/bin/python3

# python3 validate.py sample.py

# D - Make Geometric Sequence
# https://atcoder.jp/contests/abc413/tasks/abc413_d

"""TEST_DATA
3
5
1 8 2 4 16
5
-16 24 54 81 -36
7
90000 8100 -27000 729 -300000 -2430 1000000
<expected> Yes No Yes

3
5
1 -1 1 1 -1
4
1 -2 1 -2
4
1 2 1 2
<expected> Yes No No

2
2
1 3
2
-1 3
<expected> Yes Yes

"""

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))

    # Always Yes if the size of array is 2.
    # https://atcoder.jp/contests/abc413/submissions/67411289
    if len(a) == 2:
        print("Yes")
        continue

    a_set = set(a)
    match len(a_set):
        case 1:
            # ratio 1
            print("Yes")
            continue
        case 2:
            # ratio -1
            # count + and -
            delta = sum(a)
            if (sum(a_set) == 0) and ((delta == 0) or (delta in a_set)):
                print("Yes")
            else:
                print("No")
            continue

    b = sorted(a, key=abs)
    # print(b)
    # A_i / A_{i-1} = A_{i+1} / A_i
    # (a_i)^2 = A_{i-1} * A_{i+1}
    for i in range(1, len(b) - 1):
        if (b[i] * b[i]) != (b[i - 1] * b[i + 1]):
            print("No")
            break
    else:
        print("Yes")
