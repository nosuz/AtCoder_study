#!/usr/bin/python3

# python3 validate.py sample.py

# C - Large Queue
# https://atcoder.jp/contests/abc413/tasks/abc413_c

"""TEST_DATA
5
1 2 3
1 4 5
2 3
1 6 2
2 5
<expected> 11 19

10
1 75 22
1 81 72
1 2 97
1 84 82
1 2 32
1 39 57
2 45
1 40 16
2 32
2 42
<expected> 990 804 3024

10
1 160449218 954291757
2 17217760
1 353195922 501899080
1 350034067 910748511
1 824284691 470338674
2 180999835
1 131381221 677959980
1 346948152 208032501
1 893229302 506147731
2 298309896
<expected> 16430766442004320 155640513381884866 149721462357295680

3
1 2 3
1 4 5
2 6
<expected> 26

5
1 2 3
1 4 5
2 2
2 2
2 2
<expected> 6 10 10

"""

Q = int(input())

que = []
index = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    match q[0]:
        case 1:
            que.append({"num": q[1], "val": q[2]})
        case 2:
            size = q[1]
            length = 0
            sum = 0
            # print(f"size: {size}")
            for i in range(index, len(que)):
                length += que[i]["num"]
                sum += que[i]["val"] * que[i]["num"]

                if length == size:
                    print(sum)
                    length = 0
                    sum = 0
                    index = i + 1
                    break
                elif length > size:
                    over = length - size
                    sum -= que[i]["val"] * over
                    print(sum)

                    que[i]["num"] = over
                    index = i
                    break
