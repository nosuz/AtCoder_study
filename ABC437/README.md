## 開催日

2025-12-20

## コンテストページ

[UNIQUE VISION Programming Contest 2025 Christmas (AtCoder Beginner Contest 437)](https://atcoder.jp/contests/abc437)

## [A - Feet](https://atcoder.jp/contests/abc437/tasks/abc437_a)

掛け算。

## [B - Tombola](https://atcoder.jp/contests/abc437/tasks/abc437_b)

数え上げ。

事前にHashを作っておくと速くなりそうだけど、B問題なのでOK。

## [C - Reindeer and Sleigh 2](https://atcoder.jp/contests/abc437/tasks/abc437_c)

そりを引くトナカイの数を$n$とすると、

$$
\sum_{i=0}^n P \ge \sum_{i=n+1}^N W
$$

ここで$\sum_{i=n+1}^N W$は、全体の重さからそりを引くトナカイの重さを引いたものになる。

$$
\sum_{i=n+1}^N W = \sum_{i=0}^N W - \sum_{i=0}^n W
$$

これを最初の式に代入すると

$$
\sum_{i=0}^n P \ge \sum_{i=0}^N W - \sum_{i=0}^n W \\
\sum_{i=0}^n P + \sum_{i=0}^n W \ge \sum_{i=0}^N W
$$

よって、できるだけ$P+W$が大きい方からそりを引かせて次の式を満たすようにする。なお、全体の重さ$\sum_{i=0}^N W$は定数。

$$
\sum_{i=0}^n (P + W) \ge \sum_{i=0}^N W
$$

- Python

## [D - Sum of Differences](https://atcoder.jp/contests/abc437/tasks/abc437_d)

同じ数字を圧縮した上で、前後からの累積和。

intのオーバーフローに注意。

## [E - Sort Arrays](https://atcoder.jp/contests/abc437/tasks/abc437_e)

## [F - Manhattan Christmas Tree 2](https://atcoder.jp/contests/abc437/tasks/abc437_f)
