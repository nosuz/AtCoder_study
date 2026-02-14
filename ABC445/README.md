## 開催日

2026-02-14

## コンテストページ

[AtCoder Beginner Contest 445](https://atcoder.jp/contests/abc445)

## [A - Strong Word](https://atcoder.jp/contests/abc445/tasks/abc445_a)

文字列を配列として扱って、最初と最後を取り出す。

- Python

## [B - Center Alignment](https://atcoder.jp/contests/abc445/tasks/abc445_b)

指定した長さの文字列を `*` を使って作成する。整数になることが分かっていても、整数型の割り算でないと文字列を作る `*` に使えない。

- Python

## [C - Sugoroku Destination](https://atcoder.jp/contests/abc445/tasks/abc445_c)

$10^{100}$ は、場所の数 $N$ よりも十分に大きい。そのため、同じ場所でグルグルにたどり着く場合は、どこからはじめてもその場所にたどり着く。

複数の場所をめぐるループになる可能性がある。しかし問題の解説からは、その可能性が排除されているように思える。実際複数の場所をめぐるループがない前提のコードで正解になった。問題文からは、なぜ複数の場所をめぐるループの可能性を排除できるのか読み取れなかった。

制約を読むと $i \le A_i \le N$ となっている。複数の場所をめぐるループは、自分より小さい場所に飛ぶ場所があるはず。しかしこの制約で、同じ場所にとどまるか、先に進むしか無いことが分かる。

- Python

## [D - Reconstruct Chocolate](https://atcoder.jp/contests/abc445/tasks/abc445_d)

## [E - Many LCMs](https://atcoder.jp/contests/abc445/tasks/abc445_e)

## [F - Exactly K Steps 2](https://atcoder.jp/contests/abc445/tasks/abc445_f)
