#!/usr/bin/python3

# python3 validate.py sample.py

# C - Black Intervals
# https://atcoder.jp/contests/abc411/tasks/abc411_c

"""TEST_DATA
5 7
2 3 3 5 1 5 2
<expected> 1 1 1 2 2 1 1

1 2
1 1
<expected> 1 0

3 3
1 3 2
<expected> 1 2 1


"""

n, q = map(int, input().split())
A = list(map(int, input().split()))

box = [False] * n

count = 0
if n == 1:
    face = False
    for _ in A:
        face = not face
        if face:
            print(1)
        else:
            print(0)
else:
    for a in A:
        i = a - 1
        face = not box[i]
        box[i] = face

        if face:
            if i == 0:
                if box[i + 1]:
                    pass
                else:
                    count += 1
            elif i == (n - 1):
                if box[i - 1]:
                    pass
                else:
                    count += 1
            else:
                if box[i - 1] and box[i + 1]:
                    count -= 1
                elif not box[i - 1] and box[i + 1]:
                    pass
                elif box[i - 1] and not box[i + 1]:
                    pass
                elif not box[i - 1] and not box[i + 1]:
                    count += 1
        else:
            if i == 0:
                if box[i + 1]:
                    pass
                else:
                    count -= 1
            elif i == (n - 1):
                if box[i - 1]:
                    pass
                else:
                    count -= 1
            else:
                if box[i - 1] and box[i + 1]:
                    count += 1
                elif not box[i - 1] and box[i + 1]:
                    pass
                elif box[i - 1] and not box[i + 1]:
                    pass
                elif not box[i - 1] and not box[i + 1]:
                    count -= 1

        print(count)
