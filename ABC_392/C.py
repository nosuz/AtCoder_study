"""TEST_DATA
4
4 3 2 1
2 3 1 4
<expected> 3 4 1 2

10
2 6 4 3 7 8 9 10 1 5
1 4 8 2 10 5 7 3 9 6
<expected> 4 8 6 5 3 10 9 2 1 7

"""

n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

# lookup table to find whose looking
wearing2looking = [0] * n

for i in range(n):
    # substitute 1 to index lists
    wearing2looking[q[i] - 1] = p[i] - 1

# wearing2looking is same as sorted by the wearing number
# print(wearing2looking)

# wearing = [q[i] for i in wearing2looking]
# # use map to convert int to string
# print(" ".join(map(str, wearing)))

# convert int to string before concatenate
wearing = [str(q[i]) for i in wearing2looking]
print(" ".join(wearing))
