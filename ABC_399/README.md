## 開催日

2025 年 3 月 29 日

## コンテストページ

[AtCoder Beginner Contest 399](https://atcoder.jp/contests/abc399)

## C - Make it Forest

グラフを森（ループがない状態）にするには、ループの数を数えれば良いと考えていた。しかし、三角錐（4 面体）を考えれば面の数（ループの数）≠ 答えではない。

そこで、単純に path をたどって、次の node が visited の場合には、ループになっていて森にするにはそこを切ればよいとしてカウントすることにした。

また、path をたどるために再帰を当初使ったが、RE (Runtime Error)となった。これは、文法的な間違いの可能性もあるが、再帰の回数を制限したら WA (Wrong Answer)になったので Memory size limit を超えたためのエラーだと推定した。そこで再帰を止めて、経路を覚えておいてループするようにした。
