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

4 6
1 2
2 3
1 4
1 3
2 4
3 4
# 3

5 8
1 2
2 3
1 3
1 4
3 4
3 5
4 5
2 5
# 4

"""

n, m = map(int, input().split())
# n: number of nodes
# m: number of path
# [set()] * (n + 1) not work. all items share one Set.
nodes = [set() for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    if not v in nodes[u]:
        nodes[u].add(v)
        if not u in nodes[v]:
            nodes[v].add(u)
# print(tree)

loop = 0
for i in range(len(nodes)):
    if len(nodes[i]) == 0:
        continue

    # follow paths and stack branches with cutting traces.
    stack = [i]
    while len(stack) > 0:
        this_node = stack[-1]
        visited[this_node] = True

        if len(nodes[this_node]) == 0:
            # reached the terminal
            stack.pop()
        else:
            next_node = nodes[this_node].pop()

            if visited[next_node]:
                loop += 1

            nodes[next_node].remove(this_node)
            if len(nodes[next_node]) > 0:
                stack.append(next_node)

print(loop)
