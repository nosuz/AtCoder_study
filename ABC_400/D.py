"""TEST_DATA
10 10
..........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
.##.#.#.#.
###.#.#.#.
###.#.#.#.
#.....#...
1 1 7 1
<expected> 1

2 2
.#
#.
1 1 2 2
<expected> 1

1 3
.#.
1 1 1 3
<expected> 1

20 20
####################
##...##....###...###
#.....#.....#.....##
#..#..#..#..#..#..##
#..#..#....##..#####
#.....#.....#..#####
#.....#..#..#..#..##
#..#..#.....#.....##
#..#..#....###...###
####################
####################
##..#..##...###...##
##..#..#.....#.....#
##..#..#..#..#..#..#
##..#..#..#..#..#..#
##.....#..#..#..#..#
###....#..#..#..#..#
#####..#.....#.....#
#####..##...###...##
####################
3 3 18 18
<expected> 3
"""

h, w = map(int, input().split())

map_data = list()
visited = list()

for _ in range(h):
    row = input()
    map_data.append([row[i] for i in range(w)])
    visited.append([False] * w)  # visited.append([False for _ in range(w)])
a, b, c, d = [int(v) for v in input().split()]
trow, tcol, frow, fcol = a - 1, b - 1, c - 1, d - 1  # adjust for 0-start

# use Set instead of List because same points may be pushed for multiple times.
next_stack = set()
stack = set()
next_stack.add((trow, tcol))

step = 0
while len(next_stack) > 0:
    step += 1
    stack = next_stack
    next_stack = set()
    kicked = set()
    while len(stack) > 0:
        row, col = stack.pop()
        if visited[row][col]:
            continue

        visited[row][col] = True
        map_data[row][col] = str(step)  # for debug

        if row == frow and col == fcol:
            # arrived at the fish market
            break

        for delta in [(-1, 0), (0, -1), (1, 0), (0,  1),]:
            y = row + delta[0]
            x = col + delta[1]
            if (w > x >= 0 and h > y >= 0) and not visited[y][x]:
                if map_data[y][x] == '#':
                    # visit at the next round
                    next_stack.add((y, x))
                    kicked.add((y, x))

                    # kick one more wall on the same direction
                    _y = y + delta[0]
                    _x = x + delta[1]
                    if (w > _x >= 0 and h > _y >= 0) and map_data[_y][_x] == '#':
                        # omit adding on the next_stack because the second kicked wall should visited through the first one
                        kicked.add((_y, _x))
                else:
                    stack.add((y, x))

    # remove broken walls
    for pos in kicked:
        row, col = pos
        map_data[row][col] = str(step)

    # for i, row in enumerate(map_data):
    #     print("".join(row))
    #     # print(visited[i])
    # print("-----")

    if visited[frow][fcol]:
        break

print(step - 1)
