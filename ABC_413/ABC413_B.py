#!/usr/bin/python3

# python3 validate.py sample.py

# B - cat 2
# https://atcoder.jp/contests/abc413/tasks/abc413_b

"""TEST_DATA
4
at
atco
coder
der
<expected> 11

5
a
aa
aaa
aaaa
aaaaa
<expected> 7

10
armiearggc
ukupaunpiy
cogzmjmiob
rtwbvmtruq
qapfzsitbl
vhkihnipny
ybonzypnsn
esxvgoudra
usngxmaqpt
yfseonwhgp
<expected> 90


"""

n = int(input())

s = []
for _ in range(n):
    s.append(input())

concat = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        concat.add(s[i] + s[j])

print(len(concat))
