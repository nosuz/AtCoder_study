#!/usr/bin/python3

# C - Palindromic in Both Bases
# https://atcoder.jp/contests/abc414/tasks/abc414_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
8
1000
<expected> 2155

8
999999999999
<expected> 914703021014

6
999999999999
<expected> 283958331810

3
1
<expected> 1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


def PalindCheck(x):
    x_str = str(x)
    digit = len(x_str)
    # 1桁はOK
    if digit == 1:
        return True

    for i in range(digit // 2):
        # debug(f"{x_str[i]}:{x_str[digit - 1 - i]}")
        if x_str[i] != x_str[-i - 1]:
            break
    else:
        # no break or 回文
        return True
    return False


def EvenDigit(x):
    digit = len(x) // 2
    for i in num:
        xix = x[:digit] + i * 2 + x[digit:]
        # xixの回文確認は不要
        j = int(xix, A)
        if j > N:
            break
        if PalindCheck(j):
            debug(f"xix:{xix}=>{j}")
            palindrome.append(j)
        # もう1桁増やす
        InsertDigit(xix)
        # もう2桁増やす
        EvenDigit(xix)


def InsertDigit(x):
    digit = len(x) // 2
    for i in num:
        xix = x[:digit] + i + x[digit:]
        # xixの回文確認は不要
        j = int(xix, A)
        if j > N:
            break
        if PalindCheck(j):
            # debug(f"xix:{xix}=>{j}")
            palindrome.append(j)


A = int(input())
N = int(input())

num = [str(i) for i in range(A)]

palindrome = []
# 1桁
for i in num:
    # 10進数をA進数に変えるより、A進数を10進数に変えるほうが簡単
    j = int(i, A)
    if j > N:
        break
    if PalindCheck(j):
        palindrome.append(j)

# 偶数
# 先頭には0を置かない
for i in num[1:]:
    # 2桁
    ii = i * 2
    j = int(ii, A)
    if j > N:
        break
    if PalindCheck(j):
        debug(f"ii:{ii}=>{j}")
        palindrome.append(j)
    # もう1桁増やす
    InsertDigit(ii)
    # もう2桁増やす
    EvenDigit(ii)

# print(sorted(palindrome))
print(sum(palindrome))
