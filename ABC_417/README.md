## 開催日

2025 年 8 月 2 日

## コンテストページ

[AtCoder Beginner Contest 417](https://atcoder.jp/contests/abc417)

## [A - A Substring](https://atcoder.jp/contests/abc417/tasks/abc417_a)

文字列の範囲指定を使用する。

## [B - Search and Delete](https://atcoder.jp/contests/abc417/tasks/abc417_b)

N * M が最大10^4なので、実際に配列を操作する。

配列から指定位置の値を削除するには、`pop()`を使用する。

## [C - Distance Indicators](https://atcoder.jp/contests/abc417/tasks/abc417_c)

j - i = Ai + Aj のまま候補を探すと二重ループになる。そこで、j - Aj = Ai + i と変換して、それぞれを計算して、同じ値を探す。この時、Aiとiが1以上なので、j - Ajが0以下は無視して良い。i = j は、j - iが0となり、Ai + Ajが必ず正の整数と矛盾するので考慮する必要はない。

## [D - Takahashi's Expectation](https://atcoder.jp/contests/abc417/tasks/abc417_d)

## [E - A Path in A Dictionary](https://atcoder.jp/contests/abc417/tasks/abc417_e)

## [F - Random Gathering](https://atcoder.jp/contests/abc417/tasks/abc417_f)

## [G - Binary Cat](https://atcoder.jp/contests/abc417/tasks/abc417_g)
