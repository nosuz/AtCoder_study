## 開催日

2026-03-07

## コンテストページ

[AtCoder Beginner Contest 448](https://atcoder.jp/contests/abc448)

## [A - chmin](https://atcoder.jp/contests/abc448/tasks/abc448_a)

ループと比較。

- Python

## [B - Pepper Addiction](https://atcoder.jp/contests/abc448/tasks/abc448_b)

リストの更新。

- Python

## [C - Except and Min](https://atcoder.jp/contests/abc448/tasks/abc448_c)

$K \le 5$ という条件に気がつくかが大切。

計算量は、 $A$ のソートの部分が大きい。

- Python

## [D - Integer-duplicated Path](https://atcoder.jp/contests/abc448/tasks/abc448_d)

深さ優先探索。

これまでの値を `set()` で持ち回ると、node毎にコピーが必要になってしまう。そこで、これまでの値をカウントして、node間で共有する。

この場合、戻ってきた時にカウントを引き算する必要がある。再帰で処理するのが一般的と思うが、nodeの探索から戻ったことを示すマーカーをスタックに積むことで再帰でなくともカウントを引き算する。

`D_alt.py` に再帰を使った方法も実装してみた。この場合は、 `RecursionError` に注意が必要。

- Python

## [E - Simple Division](https://atcoder.jp/contests/abc448/tasks/abc448_e)

## [F - Authentic Traveling Salesman Problem](https://atcoder.jp/contests/abc448/tasks/abc448_f)
