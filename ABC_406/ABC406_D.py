#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
3 4 5
1 2
1 3
3 4
3 1
2 2
5
1 1
1 2
2 2
2 4
1 2
<expected> 2 1 0 1 0

1 2 1
1 2
7
2 1
2 1
2 1
2 1
2 1
2 1
2 1
<expected> 0 0 0 0 0 0 0

4 4 16
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
7
2 1
1 1
2 2
1 2
2 3
1 3
2 4
<expected> 4 3 3 2 2 1 1


"""

h, w, n = map(int, input().split())

garbage_row = [set() for _ in range(h)]
garbage_column = [set() for _ in range(w)]

# x = h
# y = w
for _ in range(n):
    x, y = map(int, input().split())
    # fit for array
    x -= 1
    y -= 1
    # print(x, y)
    garbage_row[x].add(y)
    garbage_column[y].add(x)
# print(garbage_row, garbage_column)


q = int(input())

query = set()
for _ in range(q):
    c, xy = map(int, input().split())
    xy -= 1  # fit for array

    if (c, xy) in query:
        # skip the same query
        print(0)
    elif c == 1:
        # print(c, "x", xy)
        garbage = garbage_row[xy]
        print(len(garbage))

        # clean garbage
        # garbage_row[xy] = set() # no need to clear by remembering queries
        # avoid scan all
        for i in garbage:
            garbage_column[i].discard(xy)
    else:
        # print(c, "y", xy)
        garbage = garbage_column[xy]
        print(len(garbage))

        # clean garbage
        # garbage_column[xy] = set() # no need to clear by remembering queries
        # avoid scan all
        for i in garbage:
            garbage_row[i].discard(xy)

    query.add((c, xy))
