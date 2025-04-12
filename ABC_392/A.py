"""TEST_DATA
3 15 5
<expected> Yes

5 3 2
<expected> No

3 3 9
<expected> Yes
"""

a = list(map(int, input().split()))

if (a[0] * a[1] == a[2]) or (a[1] * a[2] == a[0]) or (a[0] * a[2] == a[1]):
    print("Yes")
else:
    print("No")
