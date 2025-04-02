"""TEST_DATA
4 4
1 2
1 3
2 4
3 4

5 0

10 10
7 9
4 6
6 10
2 5
5 6
5 9
6 8
4 8
1 5
1 4

5 1
1 2

6 6
1 2
2 3
1 3
4 5
4 6
5 6

"""


def follow(step, stem, leaf):
    used_tree[leaf] = step
    loop = 0

    for next in tree[leaf]:
        if next != stem:
            if used_tree[next] == 0:
                # not visited
                if step < 1500:
                    loop += follow(step + 1, leaf, next)
            else:
                # looping
                if used_tree[next] < step:
                    loop += 1
                else:
                    # already counted
                    pass

    return loop


n, m = map(int, input().split())
# n: number of nodes
# m: number of path
# [set()] * (n + 1) not work. all items share one Set.
tree = [set() for _ in range(n + 1)]
used_tree = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    if not v in tree[u]:
        tree[u].add(v)
        if not u in tree[v]:
            tree[v].add(u)
# print(tree)

loop = 0
step = 1
for i in range(n + 1):
    if used_tree[i] == 0:
        # 0 is not visited
        used_tree[i] = step
        for next in tree[i]:
            if (i != next) and (used_tree[next] == 0):
                # print(i, next)
                loop += follow(step + 1, i, next)
print(loop)
