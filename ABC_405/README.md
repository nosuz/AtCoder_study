## 開催日

2025 年 5 月 10 日

## コンテストページ

[AtCoder Beginner Contest 405（Promotion of AtCoder Career Design DAY）](https://atcoder.jp/contests/abc405)

## A - Is it rated?

単純に条件分岐

## B - Not All

条件を満たさなくなるまで後ろから削る。これを逆に考えて、前から見ていって条件を満たした所まで削れば良い。

条件を満たしたかは、条件に必要な要素を除いていって必要な要素がなくなったことで判断できる。

## C - Sum of Product

二重ループを無くすパターン。

順番に掛け算をして加算するのは、加算をしておいた結果に掛け算をするのと同じ。このときの加算も i を進める毎に事前計算の合計から引き算しても良いし、後ろから足し算をしていっても良い。

全体の合計から引いていくほうが単純かな。

さらにスマートな[@ila*o*](https://x.com/ila_o_/status/1921204887305564572)の解法。

## D - Escape Route

非常口を目指すのではなく、非常口から一歩ずつ戻っていくイメージ。

## E - Fruit Lineup

## F - Chord Crossing

## G - Range Shuffle Query
