## 開催日

2025 年 6 月 14 日

## コンテストページ

[CodeQUEEN 2025 予選 (AtCoder Beginner Contest 410)](https://atcoder.jp/contests/abc410)

## [A - G1](https://atcoder.jp/contests/abc410/tasks/abc410_a)

単純に\(K\)以上の\(A_i\)の数を数えた。

出場可能かの配列に変換して、出場可能な数を数えても良かった。

## [B - Reverse Proxy](https://atcoder.jp/contests/abc410/tasks/abc410_b)

\(0\)の場合は、B問題なので深く考えずに頭らかループして最小の箱を探す。

最小の箱を探す時に、1つだけではなく見つけた他の候補を記憶しておけば、2個めの\(0\)の場合に再度のスキャンが不要になる。しかし実際に`ABC410_B_alt.py`を書いて試してみたが、使用メモリ量は減っているが、計算時間自体は箱の数が最大でも100のため差が見られない。。

## [C - Rotatable Array](https://atcoder.jp/contests/abc410/tasks/abc410_c)

実際に配列を組み替えていると二重ループになり時間制限を満たせない。リングバッファーのようにローテートした結果先頭となる位置を覚えておく。

先頭となる位置の値は、\(\max K \times \max Q = 3 \times 10^{14}\)となり\(2^{64}\)よりも小さいので\(3\)の操作毎に\(\mod K\)する必要はない。

## [D - XOR Shortest Walk](https://atcoder.jp/contests/abc410/tasks/abc410_d)

[解説](https://atcoder.jp/contests/abc410/editorial/13208)にある頂点倍化ってなんですか？

## [E - Battles in a Row](https://atcoder.jp/contests/abc410/tasks/abc410_e)

## [F - Balanced Rectangles](https://atcoder.jp/contests/abc410/tasks/abc410_f)

## [G - Longest Chord Chain](https://atcoder.jp/contests/abc410/tasks/abc410_g)
