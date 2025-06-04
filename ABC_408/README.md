## 開催日

2025 年 5 月 31 日

## コンテストページ

[AtCoder Beginner Contest 408](https://atcoder.jp/contests/abc408)

## [A - Timeout](https://atcoder.jp/contests/abc408/tasks/abc408_a)

時間の数列が与えられるので、前の時間を覚えておいて順番に差を計算していく問題。

## [B - Compression](https://atcoder.jp/contests/abc408/tasks/abc408_b)

与えられた数列を小さい順に並べる問題。ただし重複は除くので、`Set型`に入れて重複を消したあとで`List型`に戻してソートする。

`sort()`と`sorted()`の差異に注意する。

## [C - Not All Covered](https://atcoder.jp/contests/abc408/tasks/abc408_c)

配列を作って、一番オーバーラップが小さい数を探す問題。ナイーブに配列を更新すると制限時間を超えるので、[いもす法(imos 法)](https://imoz.jp/algorithms/imos_method.html)というアルゴリズムを使うらしい。入退場者数をカウントして、滞在者数を数える方法のこと。

- 1 番の壁は、0 から 1 の柱という意味。そのため 1 番から 2 番の壁を守るということは、柱 0 から柱 2 を守るということ。
- 最後の柱で壁が終わるので、最後の柱から右を示す最後の数は除く。

## D - Flip to Gather

## E - Minimum OR Path

## F - Athletic

## G - A/B < p/q < C/D
