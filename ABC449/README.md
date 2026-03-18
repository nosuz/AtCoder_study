## 開催日

2026-03-14

## コンテストページ

[AtCoder Beginner Contest 449](https://atcoder.jp/contests/abc449)

## [A - π](https://atcoder.jp/contests/abc449/tasks/abc449_a)

Pythonで `PI` は、`math.pi`。直径から半径を計算するときに、答えが実数になるようにする。

円の面積は $ \pi r^2$。

- Python

## [B - Deconstruct Chocolate](https://atcoder.jp/contests/abc449/tasks/abc449_b)

食べた部分を更新する。

- Python

## [C - Comfortable Distance](https://atcoder.jp/contests/abc449/tasks/abc449_c)

条件を満たす範囲にある文字と数を数えておく。そして、 $i$ が右に移動するのに合わせて、条件範囲から左端を除いて、右端を追加する。

計算量は $O(N)$

- Python

## [D - Make Target 2](https://atcoder.jp/contests/abc449/tasks/abc449_d)

各rowまたはcolumnに注目して黒になる場所を考える。そこからパターンを見つけて各rowまたはcolumnに含まれる黒の数を$O(1)$で計算する。

rowとcolumnの数は、それぞれ最大$2 \times 10^6$なので、ループしても制限時間内に収まると判断した。しかし`CPython`では間に合わず、`PyPy`で間に合わせた。

全体の計算量は、$O(N)$

$L = R$ の可能性に注意する。

- Python

## [E - A += v](https://atcoder.jp/contests/abc449/tasks/abc449_e)

## [F - Grid Clipping](https://atcoder.jp/contests/abc449/tasks/abc449_f)
