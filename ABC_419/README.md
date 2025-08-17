## 開催日

2025 年 8 月 16 日

## コンテストページ

[AtCoder Beginner Contest 419](https://atcoder.jp/contests/abc419)

## [A - AtCoder Language](https://atcoder.jp/contests/abc419/tasks/abc419_a)

部分一致ではなく単純に指定のキーワードかだけを判定すれば良い。

## [B - Get Min](https://atcoder.jp/contests/abc419/tasks/abc419_b)

Qが100以下なので、単純に配列に値を入れて管理する。

## [C - King's Summit](https://atcoder.jp/contests/abc419/tasks/abc419_c)

最終的に集合するのに最適の場所を考えて、現在地との距離を計算する。

- 斜め方向に移動できるので、縦と横への移動を独立に考えられる。
- 全員の中間地点に集まるのが最適。この時の中間は、平均ではなく最も離れた縦間の中間と最も離れた横間の中間になる。

## [D - Substr Swap](https://atcoder.jp/contests/abc419/tasks/abc419_d)

実際に文字列を操作したら制限時間を超えることは自明。flipする場所を記録して、最終的にどうなるかを頭から見ていくimos法を使用する。

場所の記録は、その文字の場所では無いことに注意する。その文字の場所ではなく、文字間の場所を示している。

## [E - Subarray Sum Divisibility](https://atcoder.jp/contests/abc419/tasks/abc419_e)

## [F - All Included](https://atcoder.jp/contests/abc419/tasks/abc419_f)

## [G - Count Simple Paths 2](https://atcoder.jp/contests/abc419/tasks/abc419_g)
