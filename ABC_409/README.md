## 開催日

2025 年 6 月 7 日

## コンテストページ

[AtCoder Beginner Contest 409](https://atcoder.jp/contests/abc409)

## [A - Conflict](https://atcoder.jp/contests/abc409/tasks/abc409_a)

TとAのペアを作成して、両方が`o`になる場合を探す。Pythonの`zip()`を使ったが、単純に$0 \cdots N$番目の文字同士を比較しても良かった。

## [B - Citation](https://atcoder.jp/contests/abc409/tasks/abc409_b)

問題文の意図を十二分に理解する必要がある。

- **条件を満たす$0 \ldots 100$のxを答えるのであって、与えられた数列の中で条件を満たす最大の数ではない。**
- 与えられる数列に非常に大きな数が含まれるが、数列の項目数としては最大100に制限されている。

素直に$0 \ldots 100$を順番に試して行って、条件を満たす最大（条件を満たさない一つ前）を探す。組み合わせは$100 \times 100$でしかない。

## [C - Equilateral Triangle](https://atcoder.jp/contests/abc409/tasks/abc409_c)

- 最初の頂点はいつも0。
- Lが3の倍数以外では、正三角形ができない。
- 正三角形の頂点は、0から$\frac{L}{3}-1$を必ず頂点とする。
- 辺の長さは、$\frac{L}{3}$なので、その間隔で頂点を探す。

## [D - String Rotation](https://atcoder.jp/contests/abc409/tasks/abc409_d)

## [E - Pair Annihilation](https://atcoder.jp/contests/abc409/tasks/abc409_e)

## [F - Connecting Points](https://atcoder.jp/contests/abc409/tasks/abc409_f)

## [G - Accumulation of Wealth](https://atcoder.jp/contests/abc409/tasks/abc409_g)
