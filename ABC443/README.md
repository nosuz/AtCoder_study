## 開催日

2026-01-31

## コンテストページ

[Denso Create Programming Contest 2026（AtCoder Beginner Contest 443）](https://atcoder.jp/contests/abc443)

## [A - Append s](https://atcoder.jp/contests/abc443/tasks/abc443_a)

文字列の結合。

- Java

## [B - Setsubun](https://atcoder.jp/contests/abc443/tasks/abc443_b)

B問題なので、条件に一致するまで実際に豆を食べてみる。

しかし、式を立てて二次方程式を解くことでO(1)で答えを求められる。

条件を満たす年を $Y (Y \gt 0)$ とする。

$$
\begin{aligned}
N + \sum_{i=1}^Y i + NY \ge K \\
N + \frac{(1 + Y) Y}{2} + NY \ge K \\
\frac{1}{2}Y^2 + (\frac{1}{2}+N)Y + (N-K) \ge 0
\end{aligned}
$$

この $Y$ の二次方程式を解いて得られる値が、豆を $K$ 食べる時。

- Java

## [C - Chokutter Addiction](https://atcoder.jp/contests/abc443/tasks/abc443_c)

次に開く時間（それまでは閉じている）を更新しながら、青木くんが後ろを通る時間をスキャンする。

- Java

## [D - Pawn Line](https://atcoder.jp/contests/abc443/tasks/abc443_d)

2つのアルゴリズム `D.java`と`D2.java`。

`D.java`は、一番下の駒から左右に広げていゆく。1ヶ所に集中して伸ばすと、より低い駒が見つかった時に再配置が必要になる。そこで1段だけ伸ばして隣に移る。

格段にある駒の位置を記録したListオプジェクトをそのまま使うと、オブジェクトサイズが大きくなってLTEになる。それに無駄なループが多い。

`D2.java`は、仮想的な駒を配置する[解説](https://atcoder.jp/contests/abc443/editorial/15179)を実装したもの。

1. 局所的最小値から $ \left| R[i] - R[i+1] \right| = 1 $ となる場所に線を引く。
    1. 局所的最小値から右に向かって上の条件を満たす場所に線を引く。
    2. 同様に左に向かって局所的最小値から線を引く。
2. 先の小さい方が、最終的な駒の位置となる。
3. 実際の駒と目的の場所との差を累積する。

- Java

## [E - Climbing Silver](https://atcoder.jp/contests/abc443/tasks/abc443_e)

## [F - Non-Increasing Number](https://atcoder.jp/contests/abc443/tasks/abc443_f)
