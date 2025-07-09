## 開催日

2025 年 7 月 5 日

## コンテストページ

[デンソークリエイトプログラミングコンテスト2025（AtCoder Beginner Contest 413）](https://atcoder.jp/contests/abc413)

## [A - Content Too Large](https://atcoder.jp/contests/abc413/tasks/abc413_a)

itemの大きさの合計がかばんの大きさ以下であるか確認する。

## [B - cat 2](https://atcoder.jp/contests/abc413/tasks/abc413_b)

難しく考えずに全ての組み合わせを作成して、その種類を数え上げる。

## [C - Large Queue](https://atcoder.jp/contests/abc413/tasks/abc413_c)

実際に配列を操作すると制限時間を超過する。ポインターを使ってどこまで削除したかを管理する。itemの途中までを削除する場合が有ることに注意する。

## [D - Make Geometric Sequence](https://atcoder.jp/contests/abc413/tasks/abc413_d)

等比数列は、同じ割合で増減するので、隣との比はどこでも一定。ただし割り算を使うと誤差が出るので、式を変形して掛け算のみとする。

$$
\frac{A_i}{A_{i-1}} = \frac{A_{i+1}}{A_i}
$$
$$
(A_i)^2 = {A_{i-1}} A_{i+1}
$$

- 比が負の場合、正と負が交互に現れることがるので絶対値でsortする。
- 全てが同じ値または絶対値が同じ場合が有ることに注意。
- 数列の数が2の場合も有ることに注意。

## [E - Reverse 2^i](https://atcoder.jp/contests/abc413/tasks/abc413_e)

## [F - No Passage](https://atcoder.jp/contests/abc413/tasks/abc413_f)

## [G - Big Banned Grid](https://atcoder.jp/contests/abc413/tasks/abc413_g)
