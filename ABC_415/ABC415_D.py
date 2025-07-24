#!/usr/bin/python3

# python3 validate.py sample.py

# D - Get Many Stickers
# https://atcoder.jp/contests/abc415/tasks/abc415_d

"""TEST_DATA
5 3
5 1
4 3
3 1
<expected> 3

3 3
5 1
5 1
4 2
<expected> 0

415 8
327 299
413 396
99 67
108 51
195 98
262 180
250 175
234 187
<expected> 11


"""

# DEBUG = True


def debug(*args):
    if globals().get("DEBUG", False):
        print(*args)


N, M = map(int, input().split())

# key: delta, value: consumed bottles
rules = {}
for _ in range(M):
    A, B = map(int, input().split())
    delta = A - B
    if delta in rules:
        if rules[delta] > A:
            # update new consumed
            rules[delta] = A
    else:
        rules[delta] = A

debug(rules)
rules = list(rules.items())
# sort by お得順 (減少が少ない)
rules.sort(key=lambda x: x[0])
debug(rules)

current_bottles = N
step = 0
for rule in rules:
    delta = rule[0]
    consume = rule[1]
    if current_bottles >= consume:
        # if available, repeat it
        available = (current_bottles - consume) // delta + 1
        step += available
        current_bottles = current_bottles - delta * available
        debug(f"available: {available}, remain: {current_bottles}")
print(step)
