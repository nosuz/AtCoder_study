## 開催日

2025-12-06

## コンテストページ

[AtCoder Beginner Contest 435](https://atcoder.jp/contests/abc435)

## [A - Triangular Number](https://atcoder.jp/contests/abc435/tasks/abc435_a)

ループと加算。

## [B - No-Divisible Range](https://atcoder.jp/contests/abc435/tasks/abc435_b)

累積和と余り計算。

## [C - Domino](https://atcoder.jp/contests/abc435/tasks/abc435_c)

最大値の更新。

## [D - Reachability Query 2](https://atcoder.jp/contests/abc435/tasks/abc435_d)

逆向きに幅優先探索(BFS)をして、黒い頂点に到達可能な頂点を探す。この時、新しく黒い頂点が加わる度にBFSを行うのではなく、これまでに到達可能とされた頂点に達したらそこで探索を打ち切る。visited情報を共有するイメージ。逆向きの有向グラフなので、既存の到達可能頂点に達したということは、ぶつかった頂点からBFS開始頂点に到達できることを意味する。

一度黒くなった頂点が白に戻らないことが重要。

計算量は1回のBFSとほぼ同じO(Q+M+N)。

- Python

## [E - Cover query](https://atcoder.jp/contests/abc435/tasks/abc435_e)

## [F - Cat exercise](https://atcoder.jp/contests/abc435/tasks/abc435_f)
