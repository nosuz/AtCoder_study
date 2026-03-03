#!/usr/bin/python3

# B - Most Frequent Substrings
# https://atcoder.jp/contests/abc428/tasks/abc428_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
9 3
ovowowovo
<expected> 2
ovo owo

9 1
ovowowovo
<expected> 5
o

35 3
thequickbrownfoxjumpsoverthelazydog
<expected> 2
the

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

N, K = map(int, input().split())
S = input()

word = dict()
for i in range(N-K+1):
    debug(S[i:i+K])
    if not S[i:i+K] in word:
        word[S[i:i+K]] = 0
    word[S[i:i+K]] += 1

max_count = max(word.values())
ans = []
for k, v in word.items():
    if v == max_count:
        ans.append(k)

print(max_count)
print(*sorted(ans))
