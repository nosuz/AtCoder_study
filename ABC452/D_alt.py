#!/usr/bin/python3

# D - No-Subsequence Substring
# https://atcoder.jp/contests/abc452/tasks/abc452_d

S = input().strip()
T = input().strip()

n = len(S)

# 英子文字を前提に 26 個用意
# next_pos[i][c] = S[i:] の中で文字 c が最初に現れる位置
# 存在しなければ n
next_pos = [[n] * 26 for _ in range(n + 1)]

# 末尾から構築
for i in range(n - 1, -1, -1):
    next_pos[i] = next_pos[i + 1][:]
    idx = ord(S[i]) - ord("a")
    next_pos[i][idx] = i

ans = 0

for start in range(n):
    pos = start
    matched = True

    for ch in T:
        idx = ord(ch) - ord("a")
        p = next_pos[pos][idx]
        if p == n:
            matched = False
            break
        pos = p + 1

    if matched:
        # T を部分列として含む最短の部分文字列は S[start : pos]
        # 含まないのは長さ 1 ～ (pos-start-1) の分なので pos-start 個
        ans += pos - start - 1
    else:
        # start から始まる全部の部分文字列が条件を満たす
        ans += n - start

print(ans)
