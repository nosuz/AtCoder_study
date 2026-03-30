## 開催日

2026-03-28

## コンテストページ

[AtCoder Beginner Contest 451](https://atcoder.jp/contests/abc451)

## [A - illegal](https://atcoder.jp/contests/abc451/tasks/abc451_a)

文字列の長さと倍数チェック。

- Python

## [B - Personnel Change](https://atcoder.jp/contests/abc451/tasks/abc451_b)

部門ごとに人数を集計して前後比較。

`zip`の使いどころだけど、コンテスト内ではインデックスを使った。

- Python

## [C - Understory](https://atcoder.jp/contests/abc451/tasks/abc451_c)

二分探索で木の高さ順リストを作成しておくのは良いアイデア。ただし、リストに挿入する計算量は$O(N)$なので、トータルでの計算量が$O(N^2)$になってしまう。

そこで優先度付きキュー（ヒープキュー）'heapq'を使用する。これは、挿入に必要な計算量は$O(\log N)$で、最小値を取り出す計算量が$O(1)$ですむ。また、キューに使用するリストの左端は常に最小の値が入っている。

- Python

## [D - Concat Power of 2](https://atcoder.jp/contests/abc451/tasks/abc451_d)

$2^n \le 10^9$となる数は、$\log_2{10^9} = \frac{\log10^9}{\log{2}} \approx 29.9 \lt 30$と少ない。

これを組み合わせて、9桁以下の全ての組み合わせを作成する。組み合わせの作成には、`deque`を使う方法と幅優先探索を使う方法が考えられる。

- Python


## [E - Tree Distance](https://atcoder.jp/contests/abc451/tasks/abc451_e)

## [F - Make Bipartite 3](https://atcoder.jp/contests/abc451/tasks/abc451_f)
