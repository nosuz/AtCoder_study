#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
tak??a?h?
nashi
<expected> Yes

??e??e
snuke
<expected> No

????
aoki
<expected> Yes

"""

"""TEST_DATA
input
<expected> output
"""

t = input()
u = input()

for i in range(len(t) - len(u) + 1):
    for j in range(len(u)):
        # print(f"{i}, {j}")
        # print(f"{t[i + j]} == {u[j]}")
        if t[i + j] == u[j]:
            pass
        elif t[i + j] == '?':
            pass
        else:
            break
    else:
        print("Yes")
        exit()
print("No")
