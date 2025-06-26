## 開催日

2025 年 6 月 21 日

## コンテストページ

[ユニークビジョンプログラミングコンテスト2025 夏（AtCoder Beginner Contest 411）](https://atcoder.jp/contests/abc411)

## [A - Required Length](https://atcoder.jp/contests/abc411/tasks/abc411_a)

Pythonでは文字列の長さを`len()`で取得できる。そのため単純に取得した文字列の長さと必要なパスワードの長さを比較する。

## [B - Distance Table](https://atcoder.jp/contests/abc411/tasks/abc411_b)

B問題なので、毎回スタート駅毎にループして駅間距離を加算する。

効率化するために、最初の駅からの距離を計算しておいて、次からは最初の駅とスタート駅の距離を引き算することも考えた。しかし足し算か引き算かの違いだけなので効率化できないと判断した。

## [C - Black Intervals](https://atcoder.jp/contests/abc411/tasks/abc411_c)

フリップ操作をして、その結果から連続する島の数を数えるのでは制限時間を超過することが目に見える。

先日覚えたimos法を使うのかと思ったが、フィリップする場所の前後を見ることで直接島の数を推定できることに気がついた。

- 白から黒に変わる場合
  - 両側が黒の場合は、島をつなぐので島の数が減る。
  - 両側が白の場合は、新しい島を作るので島の数が増える。
  - 隣が白と黒の場合は、島が大きくなるので島の数は変わらない。

- 黒から白に変わる場合
  - 両側が黒の場合は、島を切断するので島の数が増える。
  - 両側が白の場合は、島が消えるので島の数が減る。
  - 隣が白と黒の場合は、島が小さくなるだけなので島の数は変わらない。

## [D - Conflict 2](https://atcoder.jp/contests/abc411/tasks/abc411_d)

## [E - E [max]](https://atcoder.jp/contests/abc411/tasks/abc411_e)

## [F - Contraction](https://atcoder.jp/contests/abc411/tasks/abc411_f)

## [G - Count Cycles](https://atcoder.jp/contests/abc411/tasks/abc411_g)
