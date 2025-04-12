"""TEST_DATA
10 3
3 9 2
<expected> 7 1 4 5 6 7 8 10

6 6
1 3 5 2 4 6
<expected> 0

9 1
9
<expected> 8 1 2 3 4 5 6 7 8

"""

n, m = map(int, input().split())

# use set instead of list
a = set(map(int, input().split()))

all = set(range(1, n + 1))
# substitute a from all
sub = all.difference(a)

print(len(sub))
if len(sub) == 0:
    print()
else:
    sub_str = [str(i) for i in sub]
    # if sub isn't sorted.
    # sub_str = [str(i) for i in sorted(sub)]
    print(" ".join(sub_str))
