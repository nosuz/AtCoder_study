#!/usr/bin/python3

# python3 validate.py sample.py

# C - Mixture
# https://atcoder.jp/contests/abc415/tasks/abc415_c

"""TEST_DATA
5
3
0010000
3
0010110
1
1
2
100
4
001110010101110
<expected> Yes No No Yes Yes

1
4
001110010101110
<expected> Yes

2
1
0
1
1
<expected> Yes No

"""

# DEBUG = True


def debug(*args):
    if globals().get("DEBUG", False):
        print(*args)


T = int(input())

for _ in range(T):
    N = int(input())
    S = list(input())

    ALL_MIXED = 2**N - 1
    if S[ALL_MIXED - 1] == "1":
        print("No")
        continue

    solutions = set([2**i for i in range(N)])

    state = solutions
    while len(state) > 0:
        debug("---")
        debug(*state)
        if ALL_MIXED in state:
            # already checked safe
            print("Yes")
            break

        next_state = set()
        for s in state:
            # check the state is safe
            if S[s - 1] != "1":
                # add solutions
                for t in solutions:
                    # 1 + 1 should 1 => use bit OR
                    u = s | t
                    if u != s:
                        # added new solution
                        next_state.add(u)
        state = next_state
        debug(">>>")
        debug(*next_state)
    else:
        print("No")
